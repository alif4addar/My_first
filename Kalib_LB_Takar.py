
import streamlit as st
import pandas as pd
import numpy as np
import math
import statistics

st.markdown("""
    <style>
    /* Paksa latar belakang utama aplikasi jadi putih */
    html, body, [class*="stApp"] {
        background-color: white !important;
        color: black !important;
    }

    /* Paksa latar belakang semua container jadi putih juga */
    .st-emotion-cache-1r6slb0 {
        background-color: white !important;
    }

    /* Warna header dan elemen lain juga bisa disesuaikan */
    .st-emotion-cache-13k62yr {
        background-color: white !important;
        color: black !important;
    }
    </style>
""", unsafe_allow_html=True)



st.set_page_config(page_title="Aplikasi Kalibrasi Volume", layout="wide")

st.set_page_config(
    page_title="Aplikasi Kalibrasi Volume",
    page_icon="📖",
    layout="wide", 
    initial_sidebar_state="collapsed"
)


# --- SESSION STATE ---
if "show_sidebar" not in st.session_state:
    st.session_state.show_sidebar = False
if "menu_selected" not in st.session_state:
    st.session_state.menu_selected = "🏠 Home"

# --- SIDEBAR MENU ---
if st.session_state.show_sidebar:
    with st.sidebar:
        menu = option_menu(
            menu_title="🌟 Kebutuhan Kimia",
            options=[
                "🏠 Home", "⚗ Reaksi Kimia", "🧪 Stoikiometri",
                "🧫 Konsentrasi Larutan", "💧 pH dan pOH",
                "🧬 Tabel Periodik", "🔄 Konversi Satuan",
                "📈 Regresi Linier", "📖 About"
            ],
            icons=[
                "house", "flask", "calculator",
                "droplet-half", "thermometer-half",
                "grid-3x3-gap-fill", "repeat",
                "graph-up", "info-circle"
            ],
            default_index=0
        )
        st.session_state.menu_selected = menu

selected = st.session_state.menu_selected  







