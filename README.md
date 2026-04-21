# QuantumAI-IntradayRiskDemo

![Python](https://img.shields.io/badge/python-3.8%2B-blue?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)
![Domain](https://img.shields.io/badge/domain-quantitative%20finance-informational?style=flat-square)

> Intraday risk modelling combining LSTM-based volatility prediction with quantum-inspired portfolio optimisation. A demonstration of production-grade ML thinking applied to high-frequency financial risk.

---

## Overview

Intraday risk management is a latency-constrained, explainability-constrained, and regulatory-constrained problem. A model that produces the right answer at the wrong time, or cannot explain why it moved a risk limit, is not production-ready.

This repository demonstrates an end-to-end intraday risk pipeline:

1. **Live data ingestion** — real-time market data via Bloomberg API (mock fallback included)
2. **Volatility prediction** — LSTM model trained on historical price data
3. **Quantum optimisation** — QUBO-formulated risk sensitivity adjustment via D-Wave annealer
4. **Integrated workflow** — all three stages composing into actionable intraday portfolio decisions

The design reflects the constraints of quantitative finance ML: correctness guarantees, model risk management requirements, and the expectation that every output can be audited and explained.

---

## Architecture

```
data_ingestion.py          →  Bloomberg API / mock CSV
       ↓
lstm_prediction.py         →  LSTM volatility forecast (PyTorch)
       ↓
quantum_optimization.py    →  QUBO risk sensitivity solver (D-Wave / SimulatedAnnealing)
       ↓
integrated_solution.py     →  Combined pipeline: data → forecast → optimise → output
       ↓
demo_notebook.ipynb        →  End-to-end walkthrough with visualisations
```

---

## Quick Start

**Without Bloomberg API (mock data — works out of the box):**

```bash
git clone https://github.com/mukund1985/QuantumAI-IntradayRiskDemo.git
cd QuantumAI-IntradayRiskDemo

conda create -n quantum_ai python=3.8
conda activate quantum_ai

pip install -r requirements.txt
jupyter notebook demo_notebook.ipynb
```

The notebook uses pre-generated data from `data/pre_generated_data.csv` by default. No Bloomberg credentials required.

**With Bloomberg API (live data):**

```bash
pip install blpapi
# Ensure Bloomberg Terminal is running and logged in (Windows)
# Or use Bloomberg Anywhere (macOS)
```

Set `USE_LIVE_DATA = True` in the notebook or pass `--live` to the integrated script.

---

## Repository Structure

```
QuantumAI-IntradayRiskDemo/
├── demo_notebook.ipynb           # Full end-to-end walkthrough
├── requirements.txt
├── scripts/
│   ├── data_ingestion.py         # Bloomberg API + mock data fallback
│   ├── lstm_prediction.py        # LSTM volatility model (train + infer)
│   ├── quantum_optimization.py   # QUBO formulation + D-Wave / SA solver
│   └── integrated_solution.py    # Orchestrates full pipeline
├── tests/
│   ├── test_data_ingestion.py
│   ├── test_lstm_prediction.py
│   ├── test_quantum_optimization.py
│   └── test_integrated_solution.py
├── data/
│   └── pre_generated_data.csv    # Mock market data for offline runs
└── images/
    ├── architecture_diagram.png
    └── example_visual.png
```

---

## Pipeline Components

### Data Ingestion
Fetches OHLCV market data via Bloomberg `blpapi`. Falls back to `pre_generated_data.csv` for environments without Bloomberg access. Output: timestamped price and volume series normalised for model input.

### LSTM Volatility Prediction
Sequence-to-one LSTM trained on rolling intraday windows. Predicts next-period volatility. Key design choice: the model outputs a calibrated confidence interval alongside the point forecast — a requirement in any production MRM (Model Risk Management) context.

### Quantum Optimisation
Formulates the portfolio risk sensitivity adjustment as a Quadratic Unconstrained Binary Optimisation (QUBO) problem. Solves using D-Wave’s quantum annealer when available, or simulated annealing as a classical fallback. Output: binary allocation adjustments that minimise projected risk exposure.

### Integrated Workflow
The `integrated_solution.py` script chains all three stages. Designed for intraday batch runs (e.g. every 15 minutes during market hours), with structured output logs for downstream consumption by risk reporting systems.

---

## Running Tests

```bash
pytest tests/ -v
```

---

## Context

This project was built to demonstrate the application of quantum-classical hybrid optimisation to a real financial risk management problem. The constraints that shaped the design — latency, explainability, auditability, regulatory compliance — are the same constraints I work with building production ML systems at scale.

---

## License

MIT
