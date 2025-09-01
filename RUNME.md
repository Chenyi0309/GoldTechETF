# RUNME — Reproduce GoldTechETF Results

This document explains how to regenerate all figures and tables used in the final report and slides for the project “GoldTechETF: A Rules-Based Tech–Gold Rotation Strategy”.

All outputs will be written to:

```
Week10/mc/out/
├─ summary.csv          # per-iteration metrics (net of fees)
├─ logs.txt             # batch logs
├─ equity_curves.png    # Figure 1
├─ cagr_dist.png        # Figure 2
└─ risk_return.png      # Figure 3
```

If you keep the repository structure unchanged, running the two notebooks below will reproduce everything.

## 0) Prerequisites

- Python 3.9 or newer
- pip
- JupyterLab or VS Code (for the notebook route)
- Internet access if you want to fetch prices via yfinance

Create and activate a virtual environment, then install dependencies:

```
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
```

The file `requirements.txt` is at the repository root.

## 1) Jupyter or VS Code route

### Step 1 — Fit historical parameters

Open `Week10/mc/out/00_pipeline.ipynb` and run the section named “Fit Params”.
(Alternatively, open `fit_params.ipynb` if you prefer a smaller notebook.)

This creates:

- `Week10/mc/out/hist_returns.csv`  
  Daily log returns for block bootstrap.
- `Week10/mc/out/params.json` (or `params-*.json`)  
  Daily means, covariances, and start prices.

If you have a local prices CSV, point the notebook to `data/price_data.csv`.  
Otherwise it will fetch from Yahoo via `yfinance`.

### Step 2 — Run Monte Carlo experiments

Continue in `00_pipeline.ipynb` (MC section) **or** open `run_mc_experiments.ipynb` if present, and run all cells.

This creates:

- `Week10/mc/out/summary.csv`
- `Week10/mc/out/logs.txt`
- `Week10/mc/out/equity_curves.png`
- `Week10/mc/out/cagr_dist.png`
- `Week10/mc/out/risk_return.png`

## 2) Google Colab route (optional)

1. Open Colab and clone or mount the repository folder.
2. In the first cell of each notebook, install dependencies:

   ```
   !pip install -r /content/GoldTechETF/requirements.txt
   ```

3. Run `Week10/mc/out/00_pipeline.ipynb` (fit section) and then the MC section or `run_mc_experiments.ipynb`.
4. Outputs appear in `/content/GoldTechETF/Week10/mc/out/`.

## 3) Command-line automation with Papermill (optional)

```
pip install papermill

papermill "Week10/mc/out/fit_params.ipynb"           "Week10/mc/out/_fit_params_run.ipynb"           -p OUT_DIR "Week10/mc/out"

papermill "Week10/mc/out/run_mc_experiments.ipynb"           "Week10/mc/out/_mc_run.ipynb"           -p OUT_DIR "Week10/mc/out"           -p N_ITER 500           -p MODE "gaussian"
```

Outputs are identical to the interactive route and are written to `Week10/mc/out/`.

## 4) What each artifact is used for

- Figure 1: `Week10/mc/out/equity_curves.png`  
  Sample net equity curves versus SPY benchmark.

- Figure 2: `Week10/mc/out/cagr_dist.png`  
  Net CAGR distribution comparison across rule sets.

- Figure 3: `Week10/mc/out/risk_return.png`  
  Net risk–return scatter (annualized volatility vs net CAGR).

- Master table: `Week10/mc/out/summary.csv`  
  Per-run metrics: net CAGR, volatility, Sharpe, MaxDD, alpha/beta, turnover, and the fee and cost settings.

## 5) Fee-sensitivity mini table (optional)

After `summary.csv` is produced, run the snippet below in any notebook to create a compact table.

```
import pandas as pd

df = pd.read_csv("Week10/mc/out/summary.csv")

tbl_mgmt = (df.groupby("mgmt_fee")["CAGR_net"]
              .describe(percentiles=[0.25, 0.50, 0.75])[["25%", "50%", "75%"]]
              .rename(columns={"50%": "median"}))

tbl_perf = (df.groupby("perf_fee")["CAGR_net"]
              .describe(percentiles=[0.25, 0.50, 0.75])[["25%", "50%", "75%"]]
              .rename(columns={"50%": "median"}))

out = pd.concat({"mgmt_fee": tbl_mgmt, "perf_fee": tbl_perf}, axis=1)
out.to_csv("Week10/mc/out/fees_table.csv")
out.head()
```

This writes `fees_table.csv` next to the other outputs.

## 6) Troubleshooting

- If you reorganize folders, update `OUT_DIR`, `PARAMS_PATH`, and `HIST_PATH` in the notebooks.
- If `yfinance` is missing, run `pip install yfinance`.
- In Jupyter, if plots do not render inline, add:

  ```
  %matplotlib inline
  ```

- On macOS, if you see compiler tool warnings, install Xcode command line tools:

  ```
  xcode-select --install
  ```

## 7) Reproducibility and audit trail

- All numbers and figures in the report and slides are derived from `Week10/mc/out/summary.csv`.  
- Batch context is recorded in `Week10/mc/out/logs.txt`.  
- Parameter provenance is in `Week10/mc/out/params.json` (or `params-*.json`) and the bootstrap panel `Week10/mc/out/hist_returns.csv`.  
- Using the same random seeds and notebooks yields identical outputs in our test environment.

## 8) License

This is an academic project released under the MIT License unless otherwise noted.
