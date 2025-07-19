
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
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
with st.sidebar:
    menu = option_menu(
        menu_title = "Kalibrasi & Ketidakpastian",
        options=[
                "🏠 Home", "📋 Cara Penggunaan Web Aplikasi", "📑 Syarat Yang Harus Dipenuhi",
                "🧮 Perhitungan", "end Page"
            ]
    )
    st.session_state.menu_selected = menu
selected = st.session_state.menu_selected
if selected == "🏠 Home":
    st.markdown("Aplikasi Kalibrasi Volume Labu Takar")
    st.markdown("<h1 style='text-align:center; font-size: 3rem;'>🤖 TECHMICALS 🤖</h1>", unsafe_allow_html=True)
 
    st.markdown('<div class="header-section"><h1>Aplikasi Kalibrasi Volume Labu Takar</h1></div>', unsafe_allow_html=True)






