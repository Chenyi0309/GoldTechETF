# GoldTechETF: A Thematic, Actively Managed ETF

This project is part of the Term Project for the MSiA program course taught by Professor Tom Miller (Revised July 16, 2025).  
The goal is to design an **actively managed exchange-traded fund (ETF)** that combines data science methods with investment philosophy, and is ultimately implementable through automated, algorithmic trading.

---

## Project Overview

**GoldTechETF** is an actively managed ETF designed to balance high-growth potential with risk protection by investing in two uncorrelated yet complementary asset classes:

1. **U.S. Technology Growth Stocks**  
   - Focused on high-momentum stocks from the NASDAQ 100
   - Represents the "growth engine" of the portfolio

2. **Gold Commodity ETF (e.g., GLD)**  
   - Functions as a macroeconomic hedge during periods of inflation or volatility
   - Offers a "defensive anchor" for the portfolio

This ETF is intended for **retail and institutional investors** seeking exposure to growth opportunities while maintaining downside protection through commodity diversification.

---

## Investment Thesis

The core thesis behind GoldTechETF is that:

- **Technology equities** continue to drive innovation and market returns in the U.S. economy.
- **Gold** retains its historical role as a safe-haven asset, especially during inflationary or uncertain economic conditions.
- The **alternating market cycles** between risk-on (tech) and risk-off (gold) make this dual-asset approach more robust than single-theme funds.
- Actively rebalancing between these components using transparent rules and market signals can enhance risk-adjusted returns.

---

## Research Focus

This project investigates and implements:

- **Momentum-based selection** of tech stocks using historical price changes (e.g., 10-day performance)
- **Technical signal tracking** (e.g., moving averages, RSI) to manage gold ETF exposure
- **Portfolio weighting schemes** (equal-weighted vs signal-based)
- **Rebalancing frequency** (weekly or monthly, rule-driven)
- **Automated implementation** using Python, yFinance, and backtesting frameworks

---

## Tools & Methodology

The following tools and methods will be used throughout the project:

- `Python` (Pandas, NumPy, yfinance, backtrader)
- Technical indicators (e.g., SMA, MACD, RSI)
- Financial data APIs (Yahoo Finance)
- Portfolio simulation & backtesting
- Git/GitHub for version control and project collaboration
- Markdown for documentation

---

## Repository Structure

GoldTechETF/
├── README.md ← Project overview and background (this file)
├── checkpoint_report.md ← Week 3 checkpoint research report (50 points)
├── /data/ ← Financial data (e.g., CSVs of GLD, NASDAQ stocks)
├── /notebooks/ ← Jupyter notebooks for strategy design and testing
└── /references/ ← Research articles, PDF papers, and citations

---

## 👤 Author

**Chenyi Zhao**  
MSDS Student @ Northwestern University   
Term Project, Summer 2025  

---

## 📚 References

This project is guided by key literature on ETFs, technical trading strategies, risk management, and automated investing. Full citations are included in the `checkpoint_report.md` and `references/` folder.

---

## 📝 License

This is an academic project developed for educational purposes. All code and content are freely available under the MIT License unless otherwise noted.

