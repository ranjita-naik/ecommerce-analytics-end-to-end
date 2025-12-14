import streamlit as st
import plotly.express as px
from app.utils.sql_reader import run_query

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

