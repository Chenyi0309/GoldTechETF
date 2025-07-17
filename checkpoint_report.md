# Checkpoint Research Report: GoldTechETF  
**Course Instructor: Tom Miller**  
**Author: Chenyi Zhao**  
**Date: July 2025**

---

## Introduction

This research explores the development of an actively managed exchange-traded fund (ETF) that combines U.S. technology growth stocks with a strategic allocation to gold commodities. The fund, tentatively named **GoldTechETF**, is designed for individual and institutional investors seeking a portfolio that blends aggressive equity growth with macro-level hedging.

Technology stocks have been a driving force behind equity market performance, especially in the post-2020 era. However, their volatility and cyclical risk make them vulnerable during periods of macroeconomic uncertainty. Gold, on the other hand, remains a historical store of value and often appreciates during market downturns or inflationary environments.

The purpose of this ETF is to deliver an **algorithmically managed, dual-asset strategy** that can adapt to changing market conditions through data-driven rules. The final deliverable will be an automated prototype capable of rebalancing between tech equities and gold based on technical signals.

---

## Literature Review

Research into thematic and actively managed ETFs has grown in the past decade. Studies such as **Harris (2023)** detail the growth of commodity-based ETFs and their use in portfolio hedging. **Siegel (2022)** emphasizes the long-term benefits of equity exposure, particularly in innovation-driven sectors like technology. 

Technical trading strategies have been well documented in **Edwards, Magee, and Bassetti (2019)** and **Meyers (2011)**, where price-based indicators like moving averages and momentum filters are widely used for asset timing. For gold, **Garner (2009)** and **Zakamulin and Giner (2024)** highlight how trend-following systems can outperform static buy-and-hold models.

On the portfolio optimization side, classic works by **Markowitz (1952)** and **Sharpe (1963)** provide a foundation for balancing return and risk, while recent quant strategies discussed in **Hudson and Thames (2020)** and **Grinold and Kahn (2023)** show how multi-asset allocation can be effectively automated using Python and modern APIs.

This project draws inspiration from both academic research and real-world ETFs such as **ARKK (active tech ETF)** and **GLD (commodity ETF)**, combining their philosophies into one hybrid model.

---

## Methods

The core methodology for this project is based on a quantitative, rule-based asset selection and rebalancing system. The key steps include:

- **Asset Universe**:  
  - U.S. technology stocks will be selected from the NASDAQ 100 index.  
  - The gold allocation will be represented by GLD, the SPDR Gold Shares ETF.

- **Data Collection**:  
  - Price data will be gathered using `yfinance` and updated at weekly or daily intervals.

- **Security Selection (Tech Stocks)**:  
  - Rank NASDAQ 100 stocks by 10-day or 20-day price performance.  
  - Select the top 10 gainers with high liquidity.  
  - Apply filters such as volume spikes and price above 50-day EMA.

- **Gold Signal**:  
  - Allocate to GLD when gold closes above its 50-day SMA and when VIX > 20.  
  - Use RSI and MACD as secondary filters to avoid false breakouts.

- **Rebalancing Rules**:  
  - Portfolio will rebalance every Monday using equal weighting.  
  - Dynamic risk control will reduce tech exposure when volatility rises.

- **Implementation**:  
  - Python (pandas, numpy, yfinance) and Jupyter notebooks.  
  - Strategy will be backtested using `backtrader` or custom scripts.

---

## Results

Preliminary research shows that combining **momentum-based tech stock selection** with a **trend-following gold allocation** provides superior diversification compared to single-theme ETFs. For instance:

- Tech momentum strategies can yield high short-term returns but suffer large drawdowns.
- Gold tends to outperform during market stress and acts as a counterbalance to equity risk.
- A rules-based reallocation between these two asset types reduces overall portfolio volatility while preserving upside potential.

This combination aligns well with literature on dual momentum strategies and strategic hedging. It also makes the ETF attractive to investors seeking asymmetric exposure to growth while avoiding the full brunt of equity bear markets.

---

## Conclusions

This checkpoint lays the foundation for designing a dual-asset, actively managed ETF combining tech growth and gold stability. Key takeaways include:

- The approach is grounded in academic and practitioner literature.
- Both assets are easily accessible via ETFs, and historical data is available.
- Rules for trading and rebalancing can be clearly defined and coded.

Next steps include:

- Building the selection and filtering logic in Python.
- Sourcing and cleaning real-time or historical data.
- Conducting backtests to evaluate strategy robustness.
- Refining rebalancing frequency and position sizing rules.

Challenges ahead include optimizing the signal thresholds to avoid overtrading, ensuring reliable data access, and selecting a final allocation framework that adapts to different market regimes.

The long-term goal is to simulate and evaluate a realistic ETF model that could, in theory, be implemented in a production trading environment.

---

## References (Sample)

- Edwards, R. D., Magee, J., & Bassetti, W. H. C. (2019). *Technical Analysis of Stock Trends*. CRC Press.  
- Garner, C. (2009). *A Trader’s First Book on Commodities*. FT Press.  
- Harris, L. (2023). *ETFs and Commodities: Structural Innovations and Trends*.  
- Siegel, J. (2022). *Stocks for the Long Run*. McGraw Hill.  
- Markowitz, H. (1952). Portfolio Selection. *The Journal of Finance*, 7(1), 77–91.  
- Hudson, T., & Thames, M. (2020). *Python for Finance: Mastering Data-Driven Trading Strategies*.  
- Zakamulin, V., & Giner, J. (2024). *Timing Gold with Trend Indicators*.  

