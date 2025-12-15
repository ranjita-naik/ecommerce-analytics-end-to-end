import streamlit as st
import plotly.express as px
from app.utils.sql_reader import run_query

st.header("🧑‍🤝‍🧑 Customer 360 Insights")

# ---- Load SQL Queries ----
with open("sql/customers_overview.sql") as f:
    df_overview = run_query(f.read())

st.subheader("Customer Distribution by State")

fig = px.bar(
    df_overview,
    x="state",
    y="customers",
    title="Number of Customers by State",
)
st.plotly_chart(fig, use_container_width=True)


st.subheader("Revenue Contribution by State")

with open("sql/customers_revenue_by_state.sql") as f:
    df_rev = run_query(f.read())

fig2 = px.bar(
    df_rev.head(10),
    x="state",
    y="total_revenue",
    title="Top 10 States by Customer Revenue",
)
st.plotly_chart(fig2, use_container_width=True)



st.subheader("Customer Segmentation (Frequency vs Revenue)")

with open("sql/customers_segmentation.sql") as f:
    df_seg = run_query(f.read())

# Clean numeric columns
df_seg["order_count"] = pd.to_numeric(df_seg["order_count"], errors="coerce")
df_seg["total_revenue"] = pd.to_numeric(df_seg["total_revenue"], errors="coerce")

# Remove rows that would break Plotly
df_seg = df_seg.dropna(subset=["order_count", "total_revenue", "state"])

# Safe fill for hover data
df_seg["avg_review"] = df_seg["avg_review"].fillna(0)

# Build figure with safe columns only
fig3 = px.scatter(
    df_seg,
    x="order_count",
    y="total_revenue",
    color="state",
    size="total_revenue",
    hover_data=["customer_unique_id", "order_count", "total_revenue", "avg_review"],
    title="Customer Segmentation: Frequency vs Revenue"
)

st.plotly_chart(fig3, use_container_width=True)

st.subheader("Customer Summary Metrics")

summary = {
    "Total Customers": df_overview["customers"].sum(),
    "Top Revenue State": df_rev.iloc[0]["state"],
    "Top Revenue Value": df_rev.iloc[0]["total_revenue"],
    "Average Orders per Customer": round(df_seg["order_count"].mean(), 2),
    "Average Customer Revenue": round(df_seg["total_revenue"].mean(), 2)
}

st.table(pd.DataFrame(summary, index=[0]))

