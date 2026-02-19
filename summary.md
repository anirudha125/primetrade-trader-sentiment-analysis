# Trader Performance vs Market Sentiment  
Primetrade.ai – Data Science Assignment

---

## 1. Objective

This analysis investigates how Bitcoin market sentiment (Fear vs Greed) relates to trader behavior and performance on Hyperliquid.  

The goal is to determine:

- Whether profitability differs across sentiment regimes  
- Whether traders adjust behavior based on sentiment  
- Whether specific trader segments respond differently  
- Whether sentiment can be used predictively  

---

## 2. Methodology

### Data Sources

1. Bitcoin Fear & Greed Index (daily classification)
2. Historical Hyperliquid trade data

### Data Preparation

- Timestamps were standardized and aligned at the daily level.
- Only realized trades (Closed PnL ≠ 0) were used for performance evaluation.
- Extreme Fear was grouped with Fear.
- Trader-level daily metrics were computed:

  - Daily PnL  
  - Trade frequency  
  - Win rate  
  - Average trade size  

Sentiment was merged at a daily level to align performance with market regime.

Non-parametric statistical testing (Mann-Whitney U test) was used due to skewed PnL distributions.

---

## 3. Key Findings

### 3.1 Overall Profitability

A global comparison of daily PnL between Fear and Greed regimes showed:

- No statistically significant difference (p = 0.768)
- Similar distribution shape and heavy tails across regimes

This suggests sentiment alone does not determine average trader profitability.

---

### 3.2 Segment-Level Heterogeneity (Core Insight)

Traders were segmented based on average trade size (risk proxy):

- High Risk (top 25%)
- Medium
- Low Risk (bottom 25%)

High-risk traders exhibited:

- Mean PnL (Fear): ~15,104  
- Mean PnL (Greed): ~9,857  
- Mann-Whitney p-value: 0.024 (statistically significant)

This indicates that high-risk traders significantly outperform during Fear regimes.

---

### 3.3 Risk-Adjusted Performance

Risk-adjusted return (mean / standard deviation):

- Fear: 0.196  
- Greed: 0.130  

Even after accounting for volatility, Fear regimes produce superior risk-adjusted outcomes.

This suggests that Fear periods create volatility-driven opportunities that high-risk traders exploit effectively.

---

### 3.4 Behavioral Adaptation

Behavioral metrics (trade frequency, win rate, trade size) show variation across regimes, indicating that traders adjust exposure and activity levels depending on sentiment.

Sentiment appears to influence risk behavior more than baseline profitability.

---

## 4. Bonus: Predictive Modeling

A logistic regression model was implemented to test whether trader behavior and sentiment could predict profitability.

### Initial Model (Leakage Detected)

An initial model used same-day behavioral metrics to predict same-day profitability.  
This resulted in near-perfect performance (ROC-AUC ≈ 0.99), revealing data leakage.

Same-day win rate and trade metrics inherently contain information about daily PnL, inflating predictive accuracy.

### Corrected Model (Next-Day Prediction)

To remove leakage, the target variable was shifted to next-day profitability per account.

After correction:

- ROC-AUC ≈ 0.57  
- Performance only slightly above random  
- Strong class imbalance (majority profitable days)

### Interpretation

The limited predictive power suggests:

- Sentiment and simple behavioral features are weak short-term return predictors.
- Financial markets exhibit low signal-to-noise ratios.
- Sentiment functions better as a contextual risk-management overlay rather than a forecasting signal.

Segment-level structural insights were more informative than direct prediction.

---

## 5. Strategic Recommendations

### Strategy 1 — Volatility Allocation Strategy

During Fear regimes, selectively increase exposure to high-risk traders who statistically outperform in volatile environments.

This leverages volatility-driven alpha rather than relying on directional prediction.

---

### Strategy 2 — Regime-Aware Risk Management

During Greed regimes:

- Moderate allocation to high-risk strategies  
- Favor medium or lower-risk profiles  

Greed regimes appear to generate weaker volatility-driven edge.

---

## 6. Conclusion

Market sentiment alone does not significantly change average trader profitability.

However, sentiment interacts strongly with risk profile:

- High-risk traders benefit significantly during Fear regimes.
- Risk-adjusted performance improves under Fear.
- Predictive modeling confirms limited direct forecasting power.

The most actionable insight is regime-aware capital allocation across trader risk segments, rather than attempting direct PnL prediction.

---

End of Report
