
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
    initial_sidebar_state="collapsed"
)


st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

    html, body, [class*="st-"] {
        font-family: 'Inter', sans-serif;
        color: #333; /* Warna teks umum */
    }

    .stApp {
        background-color: #f8f8f8; /* Latar belakang aplikasi */
        padding: 20px; /* Padding keseluruhan */
    }

    /* Header */
    .header-section {
        padding: 20px 0;
        text-align: center;
        background-color: #F4F8D3;
        border-bottom: 1px solid #eee;
        margin-bottom: 30px;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }
    .header-section h1 {
        color: #5F6F65;
        font-weight: 700;
        margin: 0;
    }

    /* Hero Section */
    .hero-section {
        background: linear-gradient(to right, #CAE8BD, #B0DB9C); /* Gradien biru */
        color: white;
        padding: 60px 30px;
        text-align: center;
        border-radius: 10px;
        margin-bottom: 40px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    
    .hero-section h2 {
        font-size: 2.8em;
        font-weight: 700;
        margin-bottom: 15px;
        line-height: 1.2;
        color: white; /* Pastikan judul di hero putih */
    }
    
    .hero-section h3 {
        font-size: 28px;
        font-weight: 750;
        margin-bottom: 15px;
        line-height: 1.2;
        color: #5F6F65;
    }

    
    .hero-section p {
        font-size: 1.1em;
        margin-bottom: 20px;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
    }

    /* General Card/Container Style */
    .app-card {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        margin-bottom: 30px;
    }
    .app-card h3, .app-card h4 {
        color: #2193b0; 
        font-weight: 600;
        margin-bottom: 20px;
    }

    /* Input Fields */
    .stNumberInput label, .stTextInput label, .stTextArea label {
        font-weight: 600;
        color: #555;
        margin-bottom: 5px;
        display: block;
    }
    .stNumberInput input, .stTextInput input, .stTextArea textarea {
        border-radius: 5px;
        border: 1px solid #ddd;
        padding: 8px 12px;
        width: 100%;
        box-sizing: border-box;
    }
    .stNumberInput input:focus, .stTextInput input:focus, .stTextArea textarea:focus {
        border-color: #2193b0;
        box-shadow: 0 0 0 0.1rem rgba(33, 147, 176, 0.25);
        outline: none;
    }

    /* Buttons  */
    .stButton > button {
        background-color: #BAD8B6;
        color: white;
        border: none;
        padding: 10px 25px;
        border-radius: 5px;
        font-size: 1.0em;
        cursor: pointer;
        transition: background-color 0.3s ease, box-shadow 0.3s ease;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .stButton > button:hover {
        background-color: #E1EACD;
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }
    /* Style for the "Add Row" and "Remove Row" buttons */
    .stButton > button[data-testid="stFormSubmitButton"] { /* Target specific buttons if needed */
        background-color: #28a745; /* Green for add */
    }
    .stButton > button[data-testid="stFormSubmitButton"]:hover {
        background-color: #218838;
    }
    .stButton > button[data-testid="stFormSubmitButton"] + div .stButton > button { /* Target remove button */
        background-color: #dc3545; /* Red for remove */
    }
    .stButton > button[data-testid="stFormSubmitButton"] + div .stButton > button:hover {
        background-color: #c82333;
    }
        
    
    /* Data Editor */
    .stDataFrame {
        border-radius: 8px;
        overflow: hidden; /* Ensures rounded corners apply */
        border: 1px solid #ddd;
    }
    .stDataFrame .data-grid {
        border-radius: 8px;
    }

    /* Warna untuk kolom input seperti NST, U95, K */
    input[type="number"] {
        background-color: #393E46 !important;
        color: #FDFAF6 !important;
        border: 2px solid #819A91 !important;
        border-radius: 6px;
        padding: 8px;
    }

    /* Warna untuk teks label input */
    label {
        color: #FDFAF6 !important;
    }

    /* Warna header tabel Data Editor */
    .st-emotion-cache-13k62yr {
        background-color: #393E46 !important;
        color: #FDFAF6 !important;
        border: 2px solid #819A91 !important;
    }

    /* Warna sel data editor */
    [data-testid="stDataFrame"] input {
        background-color: #393E46 !important;
        color: #FDFAF6 !important;
        border: 2px solid #819A91 !important;
        border-radius: 6px !important;
        padding: 6px;
    }
    
    

       
    /* Specific styling for table headers */
    .stDataFrame .data-grid-header {
        background-color: #f0f0f0;
        color: #333;
        font-weight: 600;
    }

    /* Info/Warning/Error messages */
    .stAlert {
        border-radius: 8px;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    .stAlert.info {
        background-color: #e0f7fa;
        color: #00796b;
        border-left: 5px solid #00bcd4;
    }
    .stAlert.warning {
        background-color: #fff3e0;
        color: #e65100;
        border-left: 5px solid #ff9800;
    }
    .stAlert.error {
        background-color: #ffebee;
        color: #c62828;
        border-left: 5px solid #ef5350;
    }

    /* Divider */
    .stDivider {
        margin: 40px 0;
        border-top: 1px solid #eee;
    }

    /* Footer */
    .footer-section {
        text-align: center;
        padding: 30px 0;
        margin-top: 50px;
        border-top: 1px solid #eee;
        color: #777;
        font-size: 0.9em;
    }

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

# --- Header ---
st.markdown('<div class="header-section"><h1>Aplikasi Kalibrasi Volume Labu Takar</h1></div>', unsafe_allow_html=True)

# --- Hero Section (Deskripsi Aplikasi) ---
st.markdown("""
    <div class="hero-section">
        <h2>Hitung Volume Sebenarnya dan Ketidakpastian Labu Takar Anda</h2>
        <p>Alat komprehensif ini membantu Anda melakukan perhitungan kalibrasi volume labu takar secara akurat, termasuk analisis ketidakpastian sesuai standar metrologi.</p>
    </div>
""", unsafe_allow_html=True)


# --- SESSION STATE ---
if "show_sidebar" not in st.session_state:
    st.session_state.show_sidebar = False
if "menu_selected" not in st.session_state:
    st.session_state.menu_selected = "🏠 Home"

# --- SEMBUNYIKAN SIDEBAR DI AWAL ---
if not st.session_state.show_sidebar:
    st.markdown("""
        <style>
        [data-testid="stSidebar"] {
            display: none;
        }
        </style>
    """, unsafe_allow_html=True)

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

    # FIX: Suntikkan CSS agar sidebar selalu tampil di mobile
    st.markdown("""
        <style>
        [data-testid="stSidebar"] {
            display: block !important;
        }
        </style>
    """, unsafe_allow_html=True)

    # FIX: Suntikkan JS agar sidebar langsung muncul
    st.components.v1.html("""
        <script>
        const sidebar = parent.document.querySelector('[data-testid="stSidebar"]');
        if(sidebar){ sidebar.style.display = "block"; }
        </script>
    """, height=0)

# --- TOMBOL UNTUK MEMUNCULKAN SIDEBAR ---
selected = st.session_state.menu_selected
if selected == "🏠 Home":
    st.markdown("<h1 style='text-align:center; font-size: 3rem;'>🧪 Techmicals</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center; color:#3f3d56;'>Teman Asik Kimia-mu – Seru, Modern, dan Mudah!</h3>", unsafe_allow_html=True)
    st.write("""
        <p style='text-align:center;'>Selamat datang di <b>Techmicals</b>, aplikasi all-in-one untuk semua kebutuhan kimia kamu.  
        🚀 Hitung reaksi, mol, konsentrasi, hingga regresi linier dengan mudah.</p>
    """, unsafe_allow_html=True)


