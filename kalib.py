import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import math
import statistics
from pathlib import Path

css_file = Path(__file__).parent / "gaya.css"
with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(
    page_title="Aplikasi Kalibrasi Volume",
    page_icon="📖",
    layout="centered",
)

if "rows" not in st.session_state:
    st.session_state.rows = 1
def add_row():
    st.session_state.rows += 1
def remove_row():
    if st.session_state.rows > 1:
        st.session_state.rows -= 1
def mulai():
    st.session_state.show_sidebar = True

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
    
# Sidebar Navigation
with st.sidebar:
    st.markdown("<h2 style='color:#030f00;'>Aplikasi Kalibrasi & Ketidakpastian</h2>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("<h3 style='color:#030f00;'>Menu</h3>", unsafe_allow_html=True)
    menu = option_menu(
        menu_title = None,
        options=[
                "🏠 Home", "📋 Cara Penggunaan Web Aplikasi", 
                "📑 Syarat Yang Harus Dipenuhi",
                "💾 Input Data", "📘 Penutup"],
        menu_icon="cast"    
    )
    st.session_state.menu_selected = menu
    
selected = st.session_state.menu_selected

if selected == "🏠 Home":
    st.markdown('<div class="header-section"><h1>Aplikasi Kalibrasi Volume Labu Takar</h1></div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="hero-section">
            <h2>Hitung Volume Sebenarnya dan Ketidakpastian Labu Takar Anda</h2>
            <p>Alat komprehensif ini membantu Anda melakukan perhitungan kalibrasi volume labu takar secara akurat, termasuk analisis ketidakpastian sesuai standar metrologi.</p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown('<div class="header-section"><h1>Aplikasi</h1></div>', unsafe_allow_html=True)
    st.divider()
    col_spasi, col_mulai, col_spasi_2 = st.columns([5, 4, 5])
    with col_mulai:
        if st.button("Mulai", key="start", on_click=mulai): 
            st.session_state.show_sidebar = True
            st.session_state.menu_selected = "📋 Cara Penggunaan Web Aplikasi"
    
elif selected == "📋 Cara Penggunaan Web Aplikasi":     
    st.markdown('<div class="header-section"><h2>Cara Penggunaan Web Aplikasi</h2></div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="hero-section">
            <p2>1. Pastikan sudah memenuhu semua syarat yang ditentukan.</p2>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("""
        <div class="hero-section">
            <p2>2. Pada saat akan memasukan data pengukuran, banyaknya kolom sesuaikan dengan banyaknya data.</p2>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("""
        <div class="hero-section">
            <p2>3. Sebelum menghitung nilai rata-rata  dari data pengukuran, semua kolom sudah terisi semua.</p2>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("""
        <div class="hero-section">
            <p2>4. Tombol untuk menghitung volume sebenarnya dan nilai ketidakpastian
                akan otomatis muncul setelah nilai rata-rata didapatkan.</p2>
        </div>
    """, unsafe_allow_html=True)

elif selected == "📑 Syarat Yang Harus Dipenuhi":
    st.markdown('<div class="header-section"><h2> Syarat Yang Harus Dipenuhi</h2></div>', unsafe_allow_html=True)
    cek1 = st.checkbox("✅ Pastikan Seluruh Alat Ukur Memiliki Sertifikat")
    cek2 = st.checkbox("✅ Pastikan Suhu, Tekanan Dan Kelembaban Ruangan Stabil")
    
    if cek1 and cek2:
        st.session_state.syarat = True
        st.success("✅ Semua syarat telah dipenuhi.")
    else:
        st.warning("⚠️ Harap centang semua syarat terlebih dahulu.")

elif selected == "💾 Input Data":
    if st.session_state.syarat:
        st.markdown('<div class="header-section"><h2>Input Data</h2></div>', unsafe_allow_html=True)
    
        # Input volume konvensional
        st.markdown("<h3 style='color:#5F6F65;'>1.Input Volume Labu Takar</h3>", unsafe_allow_html=True)
        v_konven = st.number_input("Masukkan Volume Konvensional (mL)", min_value=0.00, step=25.0,  format="%.2f")
        
        st.markdown('<div class="app-card">', unsafe_allow_html=True)
        st.markdown("<h3 style='color:#5F6F65;'>2. Input Ketelitian Alat</h3>", unsafe_allow_html=True)
        ketelitian_lb = st.number_input("Masukkan Ketelitian Labu Takar (mL)", min_value=0.00, step=0.0100, format="%.4f")
        
        # Template input tabel
        st.markdown('<div class="app-card">', unsafe_allow_html=True)
        st.markdown("<h3 style='color:#5F6F65;'>3. Input Data Pengukuran</h3>", unsafe_allow_html=True)
        cols = [
                "Bobot Kosong (g)",
                "Bobot Isi (g)",
                "Suhu Air (C)",
                "Suhu Udara (C)",
                "Tekanan Udara (mmHg)",
                "Kelembaban (%)"
        ]
            
         # jmlh baris
        col1, col2, col3 = st.columns([3, 6, 3])
        with col1:
            st.button(" + Tambah Baris", on_click=add_row)
        with col3:
            st.button(" - Hapus Baris", on_click=remove_row)
            
       
        def_data = [["" for _ in range(len(cols))] for _ in range(st.session_state.rows)] 
        df = st.data_editor(pd.DataFrame(def_data, columns=cols), use_container_width=True, num_rows="dynamic", key="data_input")
        
        if st.button("Hitung Rata-rata Data Pengukuran"):
            try:
                if df.isnull().values.any() or (df == "").values.any():
                    st.warning("⚠️ Semua sel harus diisi sebelum menghitung rata-rata.")
                else:
                        kosong = df["Bobot Kosong (g)"].astype(float).tolist()
                        isi = df["Bobot Isi (g)"].astype(float).tolist()
                        suhu_air = df["Suhu Air (C)"].astype(float).tolist()
                        suhu_udara = df["Suhu Udara (C)"].astype(float).tolist()
                        tekanan = df["Tekanan Udara (mmHg)"].astype(float).tolist()
                        kelembaban = df["Kelembaban (%)"].astype(float).tolist()
            
                        hasil = [b - a for a, b in zip(kosong, isi)]
            
                        rata = {
                            "Bobot Kosong (g)": sum(kosong)/len(kosong),
                            "Bobot Isi (g)": sum(isi)/len(isi),
                            "Bobot Isi (Hasil) (g)": sum(hasil)/len(hasil),
                            "Suhu Air (C)": sum(suhu_air)/len(suhu_air),
                            "Suhu Udara (C)": sum(suhu_udara)/len(suhu_udara),
                            "Tekanan Udara (mmHg)": sum(tekanan)/len(tekanan),
                            "Kelembaban (%)": sum(kelembaban)/len(kelembaban),
                            "U repeatability (g)": statistics.stdev(hasil) / math.sqrt(len(hasil))
                        }
            
                        st.session_state.rata_pengukuran = rata
            
                        st.subheader("Rata-rata Data Pengukuran")
                        for k, v in rata.items():
                            st.write(f"{k}: **{v:.4f}**")
            
            except Exception as e:
                st.error(f"Terjadi kesalahan saat menghitung rata-rata: {e}")
            
        # Input untuk ketidakpastian
        CC = ["Timbangan","Termometer Air","Termometer Udara","Barometer Udara","Hygrometer"]
        satuan = ["g", "C", "C", "mmHg", "%"]
        st.markdown('<div class="app-card">', unsafe_allow_html=True)
        st.markdown("<h3 style='color:#5F6F65;'>4. Input Data Alat Ukur</h3>", unsafe_allow_html=True)
        lop = st.number_input("Masukkan Nilai LOP Timbangan", value=0.0000, step=0.0001, format="%.4f")
        st.markdown("Masukkan nilai NST, U95, dan K untuk alat ukur:")
            
        col_nst, col_u95, col_k = st.columns(3)
        with col_nst:
                st.markdown("<h3 style='color:#5F6F65; font-size: 24px;'>NST</h3>", unsafe_allow_html=True)
                nst = [st.number_input(f" {label} ( {satuan[i]} )", value=0.0000, key=f"nst_{i}", step=0.0001, format="%.4f") for i, label in enumerate(CC)]
        with col_u95:
                st.markdown("<h3 style='color:#5F6F65; font-size: 24px;'>U95</h3>", unsafe_allow_html=True)
                u95 = [st.number_input(f" {label}", value=0.0000, key=f"u95_{i}", step=0.0010, format="%.4f") for i, label in enumerate(CC)]
        with col_k:
                st.markdown("<h3 style='color:#5F6F65; font-size: 24px;'>K</h3>", unsafe_allow_html=True)
                nilai_k = [st.number_input(f" {label}", value=2.0, key=f"kval_{i}", step=0.1000, format="%.4f") for i, label in enumerate(CC)]
                
        st.markdown('<div class="app-card">', unsafe_allow_html=True)
        st.markdown("<h3 style='color:#5F6F65;'>Perhitungan Ketidakpastian</h3>", unsafe_allow_html=True)   
           
            # Tombol ngitung ketidakpastian
        if "rata_pengukuran" in st.session_state:
                rata = st.session_state.rata_pengukuran
            
                st.divider()
                st.subheader("Perhitungan Volume dan Ketidakpastian")
            
                if st.button("Hitung Volume & Ketidakpastian"):
                    try:
                        T = rata["Suhu Air (C)"]
                        massa = rata["Bobot Isi (Hasil) (g)"]
                        suhu_udara = rata["Suhu Udara (C)"]
                        tekanan = rata["Tekanan Udara (mmHg)"]
                        kelembaban = rata["Kelembaban (%)"]
            
                        dens_air = 0.999974 - ((((T - 3.989)**2) * (T + 338.636)) / (563385.4 * (T + 72.45147)))
                        dens_udara = (((0.464554 * tekanan) - kelembaban*(0.00252*suhu_udara-0.020582)) / ((237.15+suhu_udara)*1000))
            
                        koef_muai = 0.00001
                        v_20 = massa * (1 - koef_muai * (T - 20)) / (dens_air - dens_udara)
                        koreksi = abs(v_20 - v_konven)
            
                    # Ketidakpastian massa air (U1)
                        k_neraca = (lop/(2*math.sqrt(3)))
                        k_ulangan = rata["U repeatability (g)"]
                        U1 = math.sqrt(k_neraca**2 + k_ulangan**2)
                        Cs1 = (1 - koef_muai * (T - 20)) / (dens_air - dens_udara)
            
                    #Ketidakpastian suhu air (U2)
                        U2 = u95[1] / nilai_k[1]
                        Cs2 = (massa * (-koef_muai)) / (dens_air - dens_udara)
            
                    #Ketidakpastian densitas air(U3)
                        Ut = U2
                        Ci = -((5.32*(10**-6) * T**2 + 1.20*(10**-4)*T + 2.82*(10**-5)) / ((T + 72.45147)**2))
                        U3 = math.sqrt((Ut * Ci)**2)
                        Cs3 = -massa * (1 - koef_muai*(T - 20)) / ((dens_air - dens_udara)**2)
            
                    #Ketidakpastian densitas udara(U4)
                        Uh = u95[4]/nilai_k[4]
                        Up = u95[3]/nilai_k[3]
                        Ut = u95[2]/nilai_k[2]
                        Ch = (0.020582 - 0.00252*suhu_udara) / ((237.15 + suhu_udara) * 1000)
                        Cp = (0.464554) / ((237.15 + suhu_udara) * 1000)
                        Ct = (-0.6182*kelembaban - 0.46554*tekanan) / (((237.15 + suhu_udara)**2) * 1000)
                        U4 = math.sqrt((Uh*Ch)**2 + (Up*Cp)**2 + (Ut*Ct)**2)
                        Cs4 = massa * (1 - koef_muai*(T - 20)) / ((dens_air - dens_udara)**2)
            
                    #Ketidakpastian KMV(U5)
                        U5 = (0.1 * koef_muai) / math.sqrt(3)
                        Cs5 = massa * (20 - T) / (dens_air - dens_udara)
            
                    #Ketidakpastian miniskus(U6)
                        U6 = ((5/100) * ketelitian_lb) / math.sqrt(3)
                        Cs6 = 1
    
                        st.session_state.ui = [U1, U2, U3, U4, U5, U6]
                        st.session_state.csi = [Cs1, Cs2, Cs3, Cs4, Cs5, Cs6]
                        
                    #Ketidakpastian gabungan(Ugab)
                        Ugab2 = ((U1*Cs1)**2 + (U2*Cs2)**2 + (U3*Cs3)**2 + (U4*Cs4)**2 + (U5*Cs5)**2 + (U6*Cs6)**2)
                        Ugab = math.sqrt((U1*Cs1)**2 + (U2*Cs2)**2 + (U3*Cs3)**2 + (U4*Cs4)**2 + (U5*Cs5)**2 + (U6*Cs6)**2)
                    
                    #Ketidakpastian Diperluas
                        U95_exp = Ugab * 2
    
                        st.subheader("Hasil Perhitungan")
                        st.write(f"Densitas Air: **{dens_air:.6f} g/mL**")
                        st.write(f"Densitas Udara: **{dens_udara:.6f} g/mL**")
                        st.write(f"Volume Sebenarnya (20°C): **{v_20:.6f} mL**")
                        st.write(f"Koreksi Volume Konvensional: **{koreksi:+.6f} mL**") 
                        
                        st.subheader("Ketidakpastian")
                        st.write(f"Ugab2 (Gabungan2): **{Ugab2:.6f} mL**")
                        st.write(f"Ugab (Gabungan): **{Ugab:.6f} mL**")
                        st.write(f"Ketidakpastian Diperluas (U95): **{U95_exp:.6f} mL**")
    
                        st.subheader("Ui")
                        st.write(f"U1 : **{U1:.11f}**")
                        st.write(f"U2 : **{U2:.11f}**")
                        st.write(f"U3 : **{U3:.11f}**")
                        st.write(f"U4 : **{U4:.11f}**")
                        st.write(f"U5 : **{U5:.11f}**")
                        st.write(f"U6 : **{U6:.11f}**")
                    
                        st.subheader("Csi")
                        st.write(f"Cs1 : **{Cs1:.11f}**")
                        st.write(f"Cs2 : **{Cs2:.11f}**")
                        st.write(f"Cs3 : **{Cs3:.11f}**")
                        st.write(f"Cs4 : **{Cs4:.11f}**")
                        st.write(f"Cs5 : **{Cs5:.11f}**")
                        st.write(f"Cs6 : **{Cs6:.11f}**")
                    
                        st.subheader("Ui x Csi")
                        st.write(f"U1 : **{(U1*Cs1):.11f}**")
                        st.write(f"U2 : **{(U2*Cs2):.11f}**")
                        st.write(f"U3 : **{(U3*Cs3):.11f}**")
                        st.write(f"U4 : **{(U4*Cs4):.11f}**")
                        st.write(f"U5 : **{(U5*Cs5):.11f}**")
                        st.write(f"U6 : **{(U6*Cs6):.11f}**")
                    
                        st.subheader("(Ui x Csi)^2")
                        st.write(f"U1 : **{(U1*Cs1)**2:.11f}**")
                        st.write(f"U2 : **{(U2*Cs2)**2:.11f}**")
                        st.write(f"U3 : **{(U3*Cs3)**2:.11f}**")
                        st.write(f"U4 : **{(U4*Cs4)**2:.11f}**")
                        st.write(f"U5 : **{(U5*Cs5)**2:.11f}**")
                        st.write(f"U6 : **{(U6*Cs6)**2:.11f}**")
    
                        nilai_maks = koreksi + U95_exp
                        st.subheader("Kesimpulan")
                        if koreksi < ketelitian_lb and nilai_maks < ketelitian_lb:
                            st.write("✅ labu Takar Dapat Digunakan")
                            st.write(f"Karena Nilai Koreksi ({koreksi:.4f}) Lebih Kecil Dari Ketelitian Labu Takar ({ketelitian_lb:.4f})")
                            st.write(f"Karena Nilai Maksimum(Nilai Koreksi + U95) ({koreksi:.4f}+{U95_exp:.4f} = {nilai_maks:.4f}) Lebih Kecil Dari Ketelitian Labu Takar ({ketelitian_lb:.4f})")
                        elif koreksi < ketelitian_lb and nilai_maks > ketelitian_lb:
                            st.write("labu Takar Tidak Dapat Digunakan")
                            st.write(f"Karena Nilai Koreksi ({koreksi:.4f}) Lebih Kecil Dari Ketelitian Labu Takar ({ketelitian_lb:.4f})")
                            st.write(f"Tetapi Nilai Maksimum(Nilai Koreksi + U95) ({koreksi:.4f}+{U95_exp:.4f} = {nilai_maks:.4f}) Lebih Besar Dari Ketelitian Labu Takar ({ketelitian_lb:.4f})")
                        elif koreksi > ketelitian_lb and nilai_maks < ketelitian_lb:
                            st.write("labu Takar Tidak Dapat Digunakan")
                            st.write(f"Karena Nilai Maksimum(Nilai Koreksi + U95) ({koreksi:.4f}+{U95_exp:.4f} = {nilai_maks:.4f}) Lebih Kecil Dari Ketelitian Labu Takar ({ketelitian_lb:.4f})")
                            st.write(f"Tetapi Nilai Koreksi ({koreksi:.4f}) Lebih Besar Dari Ketelitian Labu Takar ({ketelitian_lb:.4f})")
                        else:
                            st.write("labu Takar Tidak Dapat Digunakan")
                            st.write(f"Karena Nilai Koreksi ({koreksi:.4f}) Lebih Besar Dari Ketelitian Labu Takar ({ketelitian_lb:.4f})")
                            st.write(f"Dan Karena Nilai Maksimum(Nilai Koreksi + U95) ({koreksi:.4f}+{U95_exp:.4f} = {nilai_maks:.4f}) Lebih Besar Dari Ketelitian Labu Takar ({ketelitian_lb:.4f})")
                    except Exception as e:
                        st.error(f"Terjadi kesalahan saat perhitungan lanjutan: {e}")
    else:
        st.markdown("Harap Penuhi Semua Syarat")
elif selected == "📘 Penutup":
    st.markdown('<div class="header-section"><h1>Terimakasih</h1></div>', unsafe_allow_html=True)
           
            
            
        
       
