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

Research into thematic and actively managed ETFs has expanded significantly in the past decade. Harris (2023) discusses the structural evolution of commodity-based ETFs, including how they are used as macroeconomic hedging tools. Siegel (2022) supports the long-term effectiveness of equity investment strategies, with particular emphasis on innovation-driven sectors such as technology. These insights support the hybrid design of GoldTechETF, which combines growth and defensive components in one strategy.

Technical trading strategies have long played a central role in quantitative finance. Edwards, Magee, and Bassetti (2019) provide a foundational treatment of price-based methods such as moving averages and momentum filters. For commodity investing, particularly in gold, Garner (2009) offers a practical perspective for new traders, while Zakamulin and Giner (2022) demonstrate the superiority of trend-following rules in gold-focused portfolios under regime-switching models.

From the portfolio optimization standpoint, Markowitz (1952) introduced Modern Portfolio Theory (MPT), which remains central to portfolio construction today. Sharpe (1964) added risk-adjusted return metrics that help evaluate asset efficiency. Building on these theories, Ma (2021) and Naik (2020) offer practical guidance on how to implement asset selection, diversification, and algorithmic trading logic using Python, including automation with financial APIs and machine learning models.

GoldTechETF draws inspiration from these academic frameworks as well as real-world ETF designs such as ARKK (an actively managed tech equity ETF) and GLD (a commodity ETF tracking gold). The proposed model leverages momentum-based equity screening and trend-informed commodity allocation to create a dynamic, rules-based, and implementable trading strategy.

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

## References

- Edwards, Robert D., John Magee, and W. H. C. Bassetti. 2019. *Technical Analysis of Stock Trends*. 11th ed. Boca Raton, FL: CRC Press.  
- Garner, Carley. 2009. *A Trader’s First Book on Commodities: An Introduction to the World’s Fastest-Growing Market*. Upper Saddle River, NJ: FT Press.  
- Harris, Larry. 2023. *ETFs and Commodities: Structural Innovations and Trends*. Report.  
- Siegel, Jeremy J. 2022. *Stocks for the Long Run*. 6th ed. New York: McGraw-Hill Education.  
- Markowitz, Harry. 1952. “Portfolio Selection.” *The Journal of Finance* 7 (1): 77–91. https://doi.org/10.2307/2975974.  
- Sharpe, William F. 1964. “Capital Asset Prices: A Theory of Market Equilibrium under Conditions of Risk.” *The Journal of Finance* 19 (3): 425–442.  
- Ma, Weiming. 2021. *Mastering Python for Finance*. 2nd ed. Birmingham, UK: Packt Publishing.  
- Naik, Krish. 2020. *Hands-On Python for Finance*. Birmingham, UK: Packt Publishing.  
- Zakamulin, Valeriy, and Javier Giner. 2022. “Optimal Trend Following Rules in Two-State Regime-Switching Models.” *Journal of Quantitative Finance* (preprint). https://allocatesmartly.com/zakamulins-optimal-trend-following.
