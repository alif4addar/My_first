
import streamlit as st
import pandas as pd
import numpy as np
import math
import statistics

st.set_page_config(page_title="Aplikasi Kalibrasi Volume", layout="wide")

st.set_page_config(
    page_title="Aplikasi Kalibrasi Volume",
    page_icon="📖",
    layout="wide",     
)

# Inisialisasi session_state
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "username" not in st.session_state:
    st.session_state.username = None
if "data" not in st.session_state:
    st.session_state.data = None

# Login Page
if not st.session_state.authenticated:
    if st.button("Login"):
        st.session_state.authenticated = True
        st.success("Login successful!")
        st.rerun()
    st.stop()

# Sidebar Navigation
page = st.sidebar(
    "🏠 Home", "📋 Cara Penggunaan Web Aplikasi",
    "📑 Syarat Yang Harus Dipenuhi",
    "🧮 Perhitungan", "end Page"
)
