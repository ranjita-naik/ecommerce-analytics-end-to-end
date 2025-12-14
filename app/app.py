import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

import streamlit as st

st.set_page_config(
    page_title="E-Commerce Analytics Demo",
    layout="wide"
)

st.title("📊 E-Commerce Analytics — End-to-End Demo")

st.markdown("""
This dashboard demonstrates a **production-style analytics workflow**:
- Python-based ETL
- SQL materialization (SQLite)
- KPI computation using SQL
- Executive-ready visualization

Designed to mirror real client engagements.
""")

