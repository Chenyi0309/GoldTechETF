# GoldTechETF — A Rules-Based Tech–Gold Rotation Strategy

Actively managed ETF concept that rotates between **U.S. large-cap technology stocks** (growth sleeve) and **gold (GLD)** as a defensive sleeve. Allocation is driven by **weekly momentum** within tech and **trend/volatility filters** for gold. All results are reported **net of transaction costs and fees**.

> **Disclaimer:** Academic project for MSDS-451. Not investment advice.

---

## Quick Links

- **Final Report (PDF):** [`report/GoldTechETF_Report.pdf`](report/GoldTechETF_Report.pdf)  
- **Slides (PDF):** see [`presentation/`](presentation/)  
- **Recording:** [`presentation/recording_link.txt`](presentation/recording_link.txt)  
- **One-click Repro:** [`RUNME.md`](RUNME.md)  
- **MC Pipeline Notebook:** [`Week10/00_pipeline.ipynb`](Week10/00_pipeline.ipynb)  
- **Monte Carlo Outputs:** [`Week10/mc/out/`](Week10/mc/out/)  
  - Summary table: [`summary.csv`](Week10/mc/out/summary.csv)  
  - Logs: [`logs.txt`](Week10/mc/out/logs.txt)  
  - Figures: [`equity_curves.png`](Week10/mc/out/equity_curves.png), [`cagr_dist.png`](Week10/mc/out/cagr_dist.png), [`risk_return.png`](Week10/mc/out/risk_return.png)

---

## Strategy at a Glance

- **Universe & Initial Holdings:** liquid **large-cap U.S. tech** (proxied by **QQQ** top constituents), **equal-weight** within the sleeve.  
- **Signals:**  
  - **Tech sleeve:** weekly **1-week momentum rank**; equal-weight top names.  
  - **Defense sleeve:** allocate to **GLD** when **GLD > 200-day SMA** **and** **VIX > 20**.  
- **Rebalance & Constraints:** **weekly**; **10% position cap** per name; **cash allowed** when defense is active.  
- **Benchmark:** **SPY**.  
- **Net performance:** includes **transaction costs**, **annual management fees**, and **performance fees**.  
  - Sensitivity ranges used in tests: costs **10–50 bps** per trade, management fee **1–4%**, performance fee **5–25%** on alpha vs. SPY.

---

## Why Tech + Gold?

- **Tech** compounds innovation-driven growth but is cyclically volatile.  
- **Gold** historically diversifies during equity stress and inflation/vol shocks.  
- A **transparent, rules-based** rotation can improve **risk-adjusted** outcomes versus buy-and-hold, provided it’s validated across many plausible market paths.

---

## Data & Model Design

- **Historical prices:** Yahoo Finance via `yfinance` (or local CSV).  
- **Return metric:** daily log returns; weekly rebalancing.  
- **Backtest window:** recent history demo (e.g., 2020–2024) plus **Monte Carlo** stress tests calibrated to longer-run stats.  
- **Monte Carlo engines:**
  1. **Parametric (Gaussian)** using daily means/covariances saved in `Week10/mc/params.json`.  
  2. **Block bootstrap** from `Week10/mc/hist_returns.csv` to preserve serial dependence/regime clustering.  

See **`RUNME.md`** for the exact two-step pipeline.

---

## Reproducibility & Artifacts

- **Inputs (generated in Step 1):**  
  - `Week10/mc/params.json` — daily mean/covariance, ticker order, start prices  
  - `Week10/mc/hist_returns.csv` — historical log-return panel for block bootstrap
- **Outputs (from Step 2):**  
  - `Week10/mc/out/summary.csv` — per-run **net** metrics (CAGR, vol, Sharpe, maxDD, alpha/beta, turnover)  
  - `Week10/mc/out/logs.txt` — batch log with seeds and grids  
  - Figures: `equity_curves.png`, `cagr_dist.png`, `risk_return.png`

> To reproduce locally or in Colab, follow **`RUNME.md`** (install → run `00_pipeline.ipynb` → inspect `mc/out/`).

---

## Repository Layout
```
GoldTechETF/
├─ Checkpoint_A/ 
├─ Checkpoint_B/ 
├─ Checkpoint_C/ 
├─ Week10/
│ ├─ 00_pipeline.ipynb # End-to-end MC pipeline (params + MC runs + figures)
│ └─ mc/
│ ├─ params.json # generated in step 1 
│ ├─ hist_returns.csv # generated in step 1
│ └─ out/
│ ├─ summary.csv
│ ├─ logs.txt
│ ├─ equity_curves.png
│ ├─ cagr_dist.png
│ └─ risk_return.png
├─ presentation/
│ ├─ slides.pdf 
│ └─ recording_link.txt
├─ report/
│ └─ GoldTechETF_Report.pdf # Final Week 10 paper (prospectus + evaluation)
├─ data/ # optional local data
├─ references/ # citations/literature
├─ RUNME.md
├─ requirements.txt
├─ LICENSE
└─ README.md # this file
```
---

## Selected Results (net of fees)

- **Equity-curve samples:** diversified outcomes across cost/fee grids and seeds (see `equity_curves.png`).  
- **Return distribution:** overlapping **CAGR** histograms across rule variants (momentum vs. SMA-VIX) indicate robust convergence (see `cagr_dist.png`).  
- **Risk–return profile:** cloud of **CAGR vs. annualized vol** summarises trade-offs and alpha–beta behavior relative to SPY (see `risk_return.png`).  
- **Fee sensitivity (from `summary.csv`):** median **net** CAGR **declines roughly linearly** as management fee rises **1%→4%**; **performance fees 5%→25%** mainly **truncate the right tail** with modest impact on the median.

---

## GenAI Tools

This repository was drafted with assistance from a large-language-model assistant for:
- code scaffolding and docstrings,
- pipeline orchestration and README/RUNME wording,
- slide and report phrasing (final editing by the author).

All code and results were **run and verified** locally/Colab. Conversation logs available upon request.

---

## License

MIT License (see `LICENSE`).  
© 2025 for academic use in MSDS-451.


