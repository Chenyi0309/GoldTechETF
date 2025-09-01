#!/usr/bin/env python
# coding: utf-8

# In[9]:


# GoldTechETF Strategy Implementation (with VIX + Real Data + Signal Visuals + Enhancements)
# Actively managed ETF combining tech stocks and gold with momentum, trend, and macro filters

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import seaborn as sns

# ------------------------------
# 1. Load Real Historical Price Data
# ------------------------------
tech_tickers = ['AAPL', 'MSFT', 'NVDA', 'GOOGL', 'AMZN']
gold_ticker = 'GLD'
vix_ticker = '^VIX'
spy_ticker = 'SPY'  # benchmark

all_tickers = tech_tickers + [gold_ticker, vix_ticker, spy_ticker]

start_date = '2020-01-01'
end_date = '2024-01-01'

raw_data = yf.download(all_tickers, start=start_date, end=end_date)['Close'].dropna()
weekly_data = raw_data.resample('W-FRI').last().dropna()

# ------------------------------
# 2. Signal Construction
# ------------------------------
momentum = weekly_data[tech_tickers].pct_change()
top_tech_selection = momentum.apply(lambda row: row.nlargest(3).index.tolist(), axis=1)

# Gold signal: price > 5-week SMA
gold_sma = weekly_data[gold_ticker].rolling(window=5).mean()
gold_above_sma = weekly_data[gold_ticker] > gold_sma

# VIX filter: high fear if VIX > 20
vix_filter = weekly_data[vix_ticker] > 20

# Final signal: both true
final_gold_signal = gold_above_sma & vix_filter

# Optional: Dynamic gold weight scaling with VIX
vix_scaled = (weekly_data[vix_ticker] - 20).clip(lower=0) / 30  # normalized from VIX 20–50
vix_scaled = vix_scaled.clip(0, 1)
dynamic_gold_weight = final_gold_signal.astype(float) * vix_scaled

# ------------------------------
# 3. Portfolio Construction
# ------------------------------
portfolio_weights = pd.DataFrame(index=weekly_data.index, columns=weekly_data.columns).fillna(0)

for date in weekly_data.index:
    if date not in top_tech_selection.index:
        continue

    selected_techs = top_tech_selection.loc[date]
    gold_weight = dynamic_gold_weight.loc[date] if not pd.isna(dynamic_gold_weight.loc[date]) else 0
    tech_weight = (1 - gold_weight) / len(selected_techs)

    for tech in selected_techs:
        portfolio_weights.at[date, tech] = tech_weight

    if gold_weight > 0:
        portfolio_weights.at[date, gold_ticker] = gold_weight

# ------------------------------
# 4. Portfolio Return Calculation
# ------------------------------
weekly_returns = weekly_data.pct_change().shift(-1)
portfolio_returns = (portfolio_weights.shift().fillna(0) * weekly_returns).sum(axis=1)
cumulative_returns = (1 + portfolio_returns).cumprod()

benchmark_returns = weekly_returns[spy_ticker].dropna()
benchmark_cum = (1 + benchmark_returns).cumprod()

annualized_return = cumulative_returns.iloc[-1]**(1/4) - 1
annualized_volatility = portfolio_returns.std() * np.sqrt(52)
sharpe_ratio = annualized_return / annualized_volatility

# ------------------------------
# 5. Visualizations
# ------------------------------
plt.figure(figsize=(10, 5))
plt.plot(cumulative_returns, label='GoldTechETF')
plt.plot(benchmark_cum, label='SPY (Benchmark)', linestyle='--')
plt.title('Cumulative Portfolio Returns')
plt.xlabel('Date')
plt.ylabel('Portfolio Value')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 2))
plt.plot(final_gold_signal.index, final_gold_signal.astype(int), drawstyle='steps-post')
plt.title('Gold Allocation Signal (1 = Active)')
plt.yticks([0, 1])
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
sns.heatmap(portfolio_weights[tech_tickers].fillna(0).T, cmap='YlGnBu', cbar_kws={'label': 'Weight'})
plt.title('Tech Stock Weights Over Time')
plt.xlabel('Date')
plt.ylabel('Tech Stocks')
plt.tight_layout()
plt.show()

# ------------------------------
# 6. Output Summary
# ------------------------------
print("Annualized Return:", round(annualized_return * 100, 2), "%")
print("Annualized Volatility:", round(annualized_volatility * 100, 2), "%")
print("Sharpe Ratio:", round(sharpe_ratio, 2))

