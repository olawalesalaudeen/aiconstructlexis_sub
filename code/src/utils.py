def extract_text_from_pdf(pdf_path: str, max_pages: int = 0) -> str:
    """Extract text from a PDF file using PyMuPDF (fast), falling back to pdfminer.

    Args:
        pdf_path: Path to the PDF file.
        max_pages: If > 0, only extract from the first N pages.
    """
    import re as _re

    try:
        import pymupdf
        doc = pymupdf.open(str(pdf_path))
        try:
            n = min(max_pages, len(doc)) if max_pages > 0 else len(doc)
            text = "\n".join(doc[i].get_text() for i in range(n))
        finally:
            doc.close()
    except ImportError:
        try:
            from pdfminer.high_level import extract_text
            text = extract_text(pdf_path)
        except ImportError:
            raise ImportError(
                "PDF text extraction requires pymupdf or pdfminer.six. "
                "Install with: pip install pymupdf  OR  pip install pdfminer.six"
            )

    m = _re.search(r'\n\s*(References|REFERENCES|Bibliography)\s*\n', text)
    if m:
        text = text[:m.start()]
    return text
