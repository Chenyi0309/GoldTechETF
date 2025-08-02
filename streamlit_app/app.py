import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import date, timedelta

# ----------------------
# App title & description
# ----------------------
st.set_page_config(page_title="GoldTech ETF Strategy", layout="wide")
st.title("📈 GoldTech ETF: Interactive Strategy Explorer")
st.markdown("""
This Streamlit app demonstrates the **GoldTech ETF strategy**, dynamically allocating capital between top U.S. tech stocks and gold based on momentum and macro risk (VIX).
""")

# ----------------------
# Sidebar: Parameters
# ----------------------
st.sidebar.header("Configuration")
start_date = st.sidebar.date_input("Start Date", date(2020, 1, 1))
end_date = st.sidebar.date_input("End Date", date(2024, 1, 1))
rebalance_freq = st.sidebar.selectbox("Rebalancing Frequency", ["Weekly", "Monthly"])
momentum_window = st.sidebar.slider("Momentum Lookback (days)", 3, 30, 5)
top_n = st.sidebar.slider("Number of Top Tech Stocks", 1, 5, 3)
use_gold = st.sidebar.checkbox("Enable GLD Hedge via VIX", value=True)

# ----------------------
# Tickers and download
# ----------------------
tech_tickers = ["AAPL", "MSFT", "NVDA", "GOOGL", "AMZN"]
gold_ticker = "GLD"
vix_ticker = "^VIX"

all_tickers = tech_tickers + [gold_ticker, vix_ticker]
data = yf.download(all_tickers, start=start_date, end=end_date)['Adj Close']
data = data.dropna()

# Resample
freq = 'W-FRI' if rebalance_freq == "Weekly" else 'M'
data = data.resample(freq).last()
returns = data.pct_change().dropna()

# ----------------------
# Strategy Logic
# ----------------------
portfolio = pd.DataFrame(index=returns.index, columns=tech_tickers + [gold_ticker])

for date_idx in returns.index:
    past_returns = returns.loc[:date_idx].iloc[-momentum_window:][tech_tickers]
    mean_returns = past_returns.mean()
    top_stocks = mean_returns.sort_values(ascending=False).head(top_n).index.tolist()

    gold_signal = False
    if use_gold:
        if date_idx in data.index:
            sma_5 = data[gold_ticker].rolling(5).mean()
            gold_above_sma = data[gold_ticker][date_idx] > sma_5[date_idx]
            vix_value = data[vix_ticker][date_idx] if date_idx in data[vix_ticker] else 0
            gold_signal = gold_above_sma and (vix_value > 20)

    if gold_signal:
        gold_weight = 0.25
        tech_weight = 0.75 / top_n
        for ticker in tech_tickers:
            portfolio.loc[date_idx, ticker] = tech_weight if ticker in top_stocks else 0
        portfolio.loc[date_idx, gold_ticker] = gold_weight
    else:
        tech_weight = 1.0 / top_n
        for ticker in tech_tickers:
            portfolio.loc[date_idx, ticker] = tech_weight if ticker in top_stocks else 0
        portfolio.loc[date_idx, gold_ticker] = 0

portfolio = portfolio.fillna(0)
strategy_returns = (portfolio.shift(1) * returns[portfolio.columns]).sum(axis=1)
cumulative_returns = (1 + strategy_returns).cumprod()

# ----------------------
# Visualization
# ----------------------
st.subheader("📊 Cumulative Strategy Returns")
fig1, ax1 = plt.subplots(figsize=(10, 4))
ax1.plot(cumulative_returns, label="GoldTech Strategy", linewidth=2)
ax1.set_ylabel("Cumulative Return")
ax1.set_xlabel("Date")
ax1.grid(True)
ax1.legend()
st.pyplot(fig1)

# ----------------------
# Allocation Heatmap
# ----------------------
st.subheader("💼 Asset Allocation Over Time")
fig2, ax2 = plt.subplots(figsize=(10, 6))
im = ax2.imshow(portfolio.T.values, aspect='auto', cmap='viridis', interpolation='none')
ax2.set_yticks(np.arange(len(portfolio.columns)))
ax2.set_yticklabels(portfolio.columns)
ax2.set_xticks(np.arange(0, len(portfolio.index), max(1, len(portfolio) // 10)))
ax2.set_xticklabels(portfolio.index.date[::max(1, len(portfolio) // 10)], rotation=45)
ax2.set_xlabel("Date")
ax2.set_title("Normalized Portfolio Weights")
fig2.colorbar(im, ax=ax2, orientation='vertical')
st.pyplot(fig2)

# ----------------------
# Metrics
# ----------------------
st.subheader("📌 Strategy Performance Metrics")
ann_return = strategy_returns.mean() * 52 if rebalance_freq == "Weekly" else strategy_returns.mean() * 12
ann_vol = strategy_returns.std() * np.sqrt(52 if rebalance_freq == "Weekly" else 12)
sharpe = ann_return / ann_vol if ann_vol > 0 else 0

st.markdown(f"**Annualized Return:** {ann_return * 100:.2f}%")
st.markdown(f"**Annualized Volatility:** {ann_vol * 100:.2f}%")
st.markdown(f"**Sharpe Ratio:** {sharpe:.2f}")

# ----------------------
# Raw Data Option
# ----------------------
with st.expander("🔍 Show Raw Data"):
    st.dataframe(portfolio.round(2))
