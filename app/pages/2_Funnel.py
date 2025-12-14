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
import plotly.express as px

st.header("🧭 Order Funnel")

with open("sql/funnel.sql") as f:
    funnel_df = run_query(f.read())

fig = px.bar(
    funnel_df,
    x="order_status",
    y="orders",
    title="Order Status Funnel",
)

st.plotly_chart(fig, use_container_width=True)

