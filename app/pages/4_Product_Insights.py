import streamlit as st
import plotly.express as px
from app.utils.sql_reader import run_query

st.header("📦 Product Insights")

st.subheader("Top Categories by Revenue")

with open("sql/products_top_categories.sql") as f:
    df_cat = run_query(f.read())

fig1 = px.bar(
    df_cat,
    x="category",
    y="total_revenue",
    title="Top 15 Categories by Revenue",
)
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Top Products by Revenue")

with open("sql/products_top_products.sql") as f:
    df_prod = run_query(f.read())

fig2 = px.bar(
    df_prod,
    x="product_id",
    y="total_revenue",
    color="category",
    title="Top 20 Products by Revenue",
)
st.plotly_chart(fig2, use_container_width=True)

st.subheader("Categories with Highest Delivery Delays")

with open("sql/products_delay_by_category.sql") as f:
    df_delay = run_query(f.read())

fig3 = px.bar(
    df_delay,
    x="category",
    y="avg_delay",
    title="Average Delivery Delay (Days) by Category",
    labels={"avg_delay": "Average Delay (Days)"},
)
st.plotly_chart(fig3, use_container_width=True)


st.subheader("Category Performance Summary")

with open("sql/products_performance.sql") as f:
    df_perf = run_query(f.read())

st.dataframe(df_perf, use_container_width=True)



