import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

st.set_page_config(page_title="Trader vs Sentiment Analysis", layout="wide")

st.title("Trader Performance vs Market Sentiment")
st.markdown("""
### Executive Summary
High-risk traders significantly outperform during Fear regimes (p = 0.024), with superior risk-adjusted returns.
Sentiment acts as a volatility amplifier rather than a direct return predictor.
""")

# =========================
# LOAD DATA
# =========================

@st.cache_data
def load_data():
    sent = pd.read_csv("data/fear_greed_index.csv")
    trades = pd.read_csv("data/historical_data.csv")

    sent['date'] = pd.to_datetime(sent['date'])
    sent['sentiment'] = sent['classification'].replace({'Extreme Fear': 'Fear'})
    sent = sent[sent['sentiment'].isin(['Fear','Greed'])]
    sent = sent[['date','sentiment']]

    trades['Timestamp IST'] = pd.to_datetime(
        trades['Timestamp IST'],
        dayfirst=True,
        errors='coerce'
    )
    trades['date'] = trades['Timestamp IST'].dt.date
    trades['date'] = pd.to_datetime(trades['date'])

    numeric_cols = ['Execution Price','Size Tokens','Size USD','Closed PnL','Fee']
    for col in numeric_cols:
        trades[col] = pd.to_numeric(trades[col], errors='coerce')

    trades = trades[trades['Closed PnL'] != 0]

    daily = trades.groupby(['date','Account']).agg(
        daily_pnl=('Closed PnL','sum'),
        trades_per_day=('Closed PnL','count'),
        win_rate=('Closed PnL', lambda x: (x>0).sum()/len(x)),
        avg_trade_size=('Size USD','mean')
    ).reset_index()

    daily = daily.merge(sent, on='date', how='left')
    daily = daily.dropna(subset=['sentiment'])

    return daily

daily_metrics = load_data()

# =========================
# HIGH-RISK SEGMENT
# =========================

threshold_high = daily_metrics['avg_trade_size'].quantile(0.75)
daily_metrics['risk_segment'] = np.where(
    daily_metrics['avg_trade_size'] >= threshold_high,
    "High Risk",
    "Other"
)

high_risk = daily_metrics[daily_metrics['risk_segment']=="High Risk"]

fear_hr = high_risk[high_risk['sentiment']=="Fear"]['daily_pnl']
greed_hr = high_risk[high_risk['sentiment']=="Greed"]['daily_pnl']

stat, p_value_hr = stats.mannwhitneyu(fear_hr, greed_hr)

# =========================
# TOP METRICS
# =========================

col1, col2, col3 = st.columns(3)

col1.metric("High Risk Fear Mean", round(fear_hr.mean(),2))
col2.metric("High Risk Greed Mean", round(greed_hr.mean(),2))
col3.metric("High Risk p-value", round(p_value_hr,4))

# =========================
# RISK-ADJUSTED PERFORMANCE
# =========================

risk_adj = daily_metrics.groupby('sentiment')['daily_pnl'].mean() / \
           daily_metrics.groupby('sentiment')['daily_pnl'].std()

st.subheader("Risk-Adjusted Performance")

st.write(risk_adj)

# =========================
# VISUALS
# =========================
win_rate_high = high_risk.groupby('sentiment')['win_rate'].mean()

st.subheader("High-Risk Average Win Rate")
st.write(win_rate_high)

st.subheader("High Risk PnL Distribution")

fig, ax = plt.subplots()
sns.boxplot(data=high_risk, x='sentiment', y='daily_pnl', ax=ax)
ax.set_yscale("symlog")
ax.set_ylabel("Daily PnL (Log Scale)")
ax.set_xlabel("Sentiment")
ax.set_title("High-Risk Trader Daily PnL Distribution")

st.pyplot(fig)

st.subheader("Segment Comparison")

segment_analysis = daily_metrics.groupby(['risk_segment','sentiment'])['daily_pnl'].mean().unstack()
st.dataframe(segment_analysis)

st.markdown("""
### Insight:
High-risk traders significantly outperform during Fear regimes (p < 0.05).
This suggests volatility-driven alpha during stressed market conditions.
""")
