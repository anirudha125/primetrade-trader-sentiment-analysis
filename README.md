# Trader Performance vs Market Sentiment
Primetrade.ai – Data Science Internship Assignment

---

## Objective

This project analyzes how Bitcoin market sentiment (Fear vs Greed) relates to trader behavior and performance on Hyperliquid.

The goal is to determine:

- Whether profitability differs across sentiment regimes
- Whether trader behavior changes under different regimes
- Whether certain trader segments respond differently
- Whether sentiment can be used predictively

---

## Project Structure

```
primetrade-assignment/
├─ data/                      # Raw datasets
├─ notebooks/
│  └─ prime_trade_assignment.ipynb
├─ results/                   # Generated charts and tables
├─ streamlit_app.py           # Interactive dashboard (bonus)
├─ requirements.txt
├─ README.md
└─ summary.md                 # 1-page findings and recommendations
```


---

## Methodology Overview

1. Data Preparation
   - Standardized timestamps and aligned data at daily level
   - Filtered only realized trades (Closed PnL ≠ 0)
   - Computed daily trader metrics:
     - Daily PnL
     - Trade frequency
     - Win rate
     - Average trade size
   - Merged market sentiment (Fear/Greed) at daily level

2. Statistical Analysis
   - Compared PnL distributions using Mann-Whitney U test
   - Segmented traders by risk profile (trade size quantiles)
   - Evaluated risk-adjusted performance (mean / standard deviation)

3. Bonus Modeling
   - Implemented logistic regression
   - Corrected for temporal leakage by shifting target to next-day profitability
   - Evaluated predictive power using ROC-AUC

---

## Key Findings (Summary)

- No statistically significant difference in overall mean PnL between Fear and Greed regimes.
- High-risk traders significantly outperform during Fear regimes (p < 0.05).
- Risk-adjusted returns are higher during Fear.
- Predictive modeling shows limited next-day forecasting power (ROC-AUC ≈ 0.57).
- Sentiment acts more as a risk-management overlay rather than a direct return predictor.

See `summary.md` for full detailed write-up.

---

## Setup Instructions

1. Clone the repository:

   git clone <repo_link>
   cd primetrade-assignment

2. Install dependencies:

   pip install -r requirements.txt

---

## How to Run

### Run Notebook

Open:

notebooks/prime_trade_assignment.ipynb

Run all cells from top to bottom.

All output charts and tables will be saved in the `results/` folder.

---

### Run Streamlit Dashboard (Optional)

From project root directory:

python -m streamlit run streamlit_app.py

Then open:

http://localhost:8501

---

## Output

The following artifacts are generated:

- fig_pnl_by_sentiment.png
- fig_segment_analysis.png
- pnl_summary_by_sentiment.csv
- segment_analysis.csv
- behavior_summary.csv

All results are stored in the `results/` directory.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Seaborn / Matplotlib
- SciPy (Statistical Testing)
- Scikit-learn (Logistic Regression)
- Streamlit (Dashboard)

---

## Conclusion

While overall trader profitability does not significantly differ across sentiment regimes, segment-level analysis reveals that high-risk traders significantly benefit during Fear environments.

The most actionable insight is regime-aware capital allocation across trader risk profiles rather than direct return prediction.

---
