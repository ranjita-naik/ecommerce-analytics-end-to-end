import sys
from pathlib import Path

# Path to repo root: /mount/src/ecommerce-analytics-end-to-end
ROOT = Path(__file__).resolve().parents[2]

# Add repo root to sys.path so Python can find the 'app' package
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))


import os
import sys
from pathlib import Path

print("DEBUG: __file__ =", __file__)
print("DEBUG: cwd =", os.getcwd())
print("DEBUG: sys.path =", sys.path)
print("DEBUG: Contents of cwd =", os.listdir(os.getcwd()))
print("DEBUG: Parent 1 =", Path(__file__).resolve().parents[0])
print("DEBUG: Parent 2 =", Path(__file__).resolve().parents[1])
print("DEBUG: Parent 3 =", Path(__file__).resolve().parents[2])

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

