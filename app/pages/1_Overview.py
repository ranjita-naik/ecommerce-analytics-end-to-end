import sys
from pathlib import Path

# Determine repo root
ROOT = Path(__file__).resolve().parents[2]

# Clean incorrect sys.path entries inserted by Streamlit
BAD_PATHS = ["app", "app/app.py"]
sys.path = [p for p in sys.path if p not in BAD_PATHS]

# Add repo root to sys.path (must be first)
sys.path.insert(0, str(ROOT))

# Now imports work
from app.utils.sql_reader import run_query
import streamlit as st

st.header("📈 Business Overview")

with open("sql/kpis.sql") as f:
    kpi_df = run_query(f.read())

kpis = kpi_df.iloc[0]

c1, c2, c3, c4, c5 = st.columns(5)

c1.metric("Orders", int(kpis.total_orders))
c2.metric("Revenue", f"${kpis.total_revenue:,.0f}")
c3.metric("AOV", f"${kpis.avg_order_value:.2f}")
c4.metric("Avg Review", round(kpis.avg_review_score, 2))
c5.metric("On-Time %", f"{kpis.on_time_delivery_rate * 100:.1f}%")

