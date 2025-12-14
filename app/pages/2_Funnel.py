
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

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

