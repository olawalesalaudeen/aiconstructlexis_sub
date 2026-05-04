import ast
import json
import re

# Quote bare keys at start-of-dict or after a comma, but only if not already quoted.
# Examples: { Title: ... , Another-Key: ... }  ->  { "Title": ... , "Another-Key": ... }
_KEY_RE = re.compile(
    r'(?P<prefix>\{|,)\s*(?P<key>(?!")(?:[A-Za-z0-9 _\-\./]+?))\s*:'
)


def clean_to_dict(data):
    """
    Recursively walk a dict/list/str and convert any dict-like strings into real dicts.
    - Keeps apostrophes in words (e.g., paper's)
    - Handles \" and \' gracefully
    - Quotes bare keys
    """
    if isinstance(data, dict):
        return {k: clean_to_dict(v) for k, v in data.items()}

    if isinstance(data, list):
        return [clean_to_dict(v) for v in data]

    if isinstance(data, str):
        s = clean_messy_string(data)
        s_stripped = s.strip()
        if (s_stripped.startswith("{") and s_stripped.endswith("}")) or (
            s_stripped.startswith("[") and s_stripped.endswith("]")
        ):
            # 1) Try Python literal (handles single quotes, None/True/False, etc.)
            try:
                return ast.literal_eval(s)
            except Exception:
                pass
            # 2) Try JSON (works after we normalize double quotes)
            try:
                return json.loads(s)
            except Exception:
                # leave as cleaned string if still not parseable
                return s
        return s

    return data


def clean_messy_string(messy: str) -> str:
    """
    Clean a messy dict/list-like string so ast/json can parse it.
    - Trims one pair of outer quotes if present
    - Unescapes \" -> ", and collapses \\'
    - Adds quotes around bare keys
    - Converts single-quoted string *delimiters* to double quotes while
      preserving apostrophes inside words (paper's, O'Neil).
    Returns a STRING (not a dict).
    """
    s = messy.strip()

    # 1) Trim one layer of full-string quotes (common when a dict is embedded in JSON as a string)
    if (len(s) >= 2) and ((s[0] == s[-1]) and s[0] in ("'", '"')):
        s = s[1:-1]

    # 2) Conservative unescape for common cases only
    #    Do NOT blanket replace backslashes (to preserve \n, \t, etc.)
    s = s.replace(r"\"", '"')  # \" -> "
    s = s.replace(r"\\'", r"\'")  # \\'=> \'

    # 3) Quote bare keys (that aren't already quoted)
    s = _KEY_RE.sub(lambda m: f'{m.group("prefix")} "{m.group("key")}":', s)

    # 4) First attempt: Python literal eval (often succeeds already)
    try:
        obj = ast.literal_eval(s)
        # Return as JSON string so caller can json.loads or display cleanly without escapes
        return json.dumps(obj, ensure_ascii=False)
    except Exception:
        pass

    # 5) If that failed, convert string delimiters:
    #    Turn single-quoted strings into double-quoted strings, but keep apostrophes inside words.
    out = []
    in_single = False
    in_double = False
    i = 0
    while i < len(s):
        ch = s[i]

        if ch == "'" and not in_double:
            # Apostrophe in a word? (prev and next alnum)
            prev = s[i - 1] if i > 0 else ""
            nxt = s[i + 1] if i + 1 < len(s) else ""
            if prev.isalnum() and nxt.isalnum():
                out.append("'")  # keep apostrophe
            else:
                # Toggle single-quoted string -> use double quotes as delimiters
                in_single = not in_single
                out.append('"')
        elif ch == '"' and not in_single:
            # Toggle double-quoted string if not escaped
            if i > 0 and s[i - 1] == "\\":
                out.append(ch)
            else:
                in_double = not in_double
                out.append(ch)
        else:
            out.append(ch)
        i += 1

    s2 = "".join(out)

    # 6) After delimiter conversion, any lingering \' should become plain '
    s2 = s2.replace(r"\'", "'")

    # 7) Ensure keys are quoted (again, in case earlier edits exposed new bare keys)
    s2 = _KEY_RE.sub(lambda m: f'{m.group("prefix")} "{m.group("key")}":', s2)

    return s2
