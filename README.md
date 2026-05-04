# AI Construct Lexis

Anonymous submission accompanying the NeurIPS 2026 Datasets & Benchmarks paper
*"AI Construct Lexis: TBD."* This repository contains the artifact (the
nomological network of constructs, behaviors, and measurement instruments
extracted from the AI evaluation literature), the interactive viewer, the
extraction/harmonization pipeline code, and the human validation data used to
assess artifact quality.

## Repository layout

```
.
├── index.html, view_network.html, network_graph.html  # interactive viewer
├── view_network.css, view_network_theme.css           # viewer styling
├── view_network_config.json                           # viewer settings
├── nomological_network_data/         # JSON consumed by the viewer
├── nomological_network_data_readable/# pretty-printed counterpart
├── lexis_artifact/
│   └── joint_v7_final.json           # the canonical Lexis (7-conference join)
├── network_data/                     # per-venue harmonized networks
├── code/                             # extraction & harmonization pipeline
│   ├── src/, utils/, scripts/        # Python source
│   ├── prompts/                      # extraction prompts (numbered 01..08)
│   ├── requirements.txt              # Python dependencies
│   ├── run_pipeline.sh, update_joint_network.sh
│   └── README.md                     # pipeline run instructions
├── validation/                       # expert validation data
│   ├── expert_reviews/               # extraction P/R workbooks (E1..E6)
│   ├── characterization_ratings/     # 5-point Likert ratings (E1..E6)
│   └── precision_recall_summary.csv
└── misc/                             # miscellaneous supporting files
```

## Viewing the network

Either open `index.html` directly in a browser (some browsers block local
fetches; if so use a local server) or run:

```bash
python -m http.server 8000
# then open http://localhost:8000/view_network.html
```

A live deployment of this viewer is available at the GitHub Pages URL listed
in the paper.

## Running the pipeline

See `code/README.md` for end-to-end pipeline instructions, including the
extraction prompts in `code/prompts/` and the harmonization scripts in
`code/scripts/`.

## Validation data

`validation/` contains the human review data used to compute the precision /
recall numbers and the characterization-rating agreement reported in §3.1
of the paper. Expert identities are anonymized as E1..E6.

## License

MIT (see `LICENSE`). Author attribution is omitted in this anonymous version
and will be added in the camera-ready release.
