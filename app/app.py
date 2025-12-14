
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

