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
    initial_sidebar_state="expanded",
)

if 'syarat' not in st.session_state:
    st.session_state.syarat = False
    
if 'ui' not in st.session_state:
    st.session_state.ui = [0]*6
if 'csi' not in st.session_state:
    st.session_state.csi = [0]*6
if 'ui_csi' not in st.session_state:
    st.session_state.ui_csi = [0]*6
if 'ui_csi2' not in st.session_state:
    st.session_state.ui_csi2 = [0]*6
if 'Ugab2' not in st.session_state:
    st.session_state.Ugab2 = 0    
if 'Ugab' not in st.session_state:
    st.session_state.Ugab = 0
if 'U95_exp' not in st.session_state:
    st.session_state.U95_exp = 0
    
if 'v_20' not in st.session_state:
    st.session_state.v_20 = 0
if 'koreksi' not in st.session_state:
    st.session_state.koreksi = 0

if 'dens_air' not in st.session_state:
    st.session_state.dens_air = 0
if 'dens_udara' not in st.session_state:
    st.session_state.dens_udara = 0

if 'v_konven' not in st.session_state:
    st.session_state.v_konven = 0.00
if 'ketelitian_lb' not in st.session_state:
    st.session_state.ketelitian_lb = 0.0000
    
if 'nst' not in st.session_state:
    st.session_state.nst = [0.0]*5
if 'u95' not in st.session_state:
    st.session_state.u95 = [0.0]*5

if "rows" not in st.session_state:
    st.session_state.rows = 1
def add_row():
    st.session_state.rows += 1
def remove_row():
    if st.session_state.rows > 1:
        st.session_state.rows -= 1
def mulai():
    st.session_state.show_sidebar = True
    st.session_state.u95 = [0.0]*5
    st.session_state.nst = [0.0]*5
    st.session_state.ui = [0]*6
    st.session_state.csi = [0]*6
    st.session_state.syarat = False
    st.session_state.v_konven = 0.00

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
                "💾 Input Data", "perhitungan", "📘 Penutup"],
        menu_icon="cast"    
    )
    st.session_state.menu_selected = menu
    
selected = st.session_state.menu_selected

if selected == "🏠 Home":
    st.markdown('<div class="header-section"><h1>Aplikasi Kalibrasi Volume Labu Takar</h1></div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="hero-section">
            <h3>Latar Belakang Kalibrasi</h3>
            <p>Dalam dunia laboratorium, industri, dan pelayanan publik, alat ukur digunakan untuk menghasilkan data yang menjadi dasar dalam pengambilan keputusan teknis, ekonomi, maupun legal. Agar hasil pengukuran dapat diandalkan, akurat, dan dapat ditelusuri ke standar nasional atau internasional, maka kalibrasi harus dilakukan.</p>
            <p>ISO/IEC 17025:2017 sebagai standar internasional untuk laboratorium pengujian dan kalibrasi, mengatur bahwa semua alat ukur yang memengaruhi keabsahan hasil pengujian wajib dikalibrasi untuk menjamin validitas pengukuran.</p>
            <br>
            <h3>Apa Itu Kalibrasi?</h3>
            <p>Menurut VIM (International Vocabulary of Metrology) dan dirujuk dalam ISO/IEC 17025:</p>
            <p>Kalibrasi adalah: "Suatu rangkaian kegiatan yang menetapkan hubungan antara nilai yang ditunjukkan oleh alat ukur (atau sistem ukur), atau nilai yang diwakili oleh suatu bahan ukur, dengan nilai-nilai yang diketahui dari suatu standar acuan, dalam kondisi tertentu."</p>
            <p>Kalibrasi adalah proses membandingkan hasil pengukuran dari suatu alat ukur dengan standar acuan yang tertelusur (traceable) ke standar nasional atau internasional.</p>
            <p>Kalibrasi tidak hanya membandingkan nilai, tetapi juga melibatkan penentuan ketidakpastian pengukuran serta penyesuaian atau koreksi jika diperlukan.</p>
            <br>
            <h3>Mengapa Kalibrasi Harus Dilakukan?</h3>
            <ul>
                <li>Menjamin akurasi pengukuran.</li>
                <li>Menjamin Ketertelusuran ke Standar Internasional.</li>
                <li>Mendukung Keputusan Teknis dan Legal.</li>
                <li>Memastikan Kesesuaian Berkala.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
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
            <p2>1. Pastikan sudah memenuhi semua syarat yang ditentukan.</p2>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="hero-section">
            <p2>2. Pada saat akan memasukan data pengukuran, banyaknya kolom sesuaikan dengan banyaknya data.</p2>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("""
        <div class="hero-section">
            <p2>3. Sebelum menghitung nilai rata-rata dari data pengukuran,
                semua kolom sudah terisi semua.</p2>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("""
        <div class="hero-section">
            <p2>4. NST adalah nilai skala terkecil dari sebuah alat ukur,
                nilai U95 dan K didapatkan dari sertifikat alat ukur
                setelah diperoleh rata-rata hasil pengukuran.</p2>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("""
        <div class="hero-section">
            <p2>5. Tombol untuk menghitung volume sebenarnya dan nilai ketidakpastian
                akan otomatis muncul setelah nilai rata-rata didapatkan.</p2>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("""
        <div class="hero-section">
            <p2>6. Labu takar dinyatakan layak pakai apabila memenuhi syarat keberterimaan,
                yaitu nilai koreksi dan nilai maksimum yang didapatkan lebih kecil dari ketelitian labu takar.</p2>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("""
        <div class="hero-section">
            <p2>7. Nilai koreksi didapatkan dari selisih volume konvensional dan volume sebenarnya pada suhu 20°C.</p2>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("""
        <div class="hero-section">
            <p2>8. Nilai maksimum didapatkan dari jumlah nilai koreksi dan nilai U95.</p2>
        </div>
    """, unsafe_allow_html=True)

elif selected == "📑 Syarat Yang Harus Dipenuhi":
    st.markdown('<div class="header-section"><h2> Syarat Yang Harus Dipenuhi</h2></div>', unsafe_allow_html=True)
    cek1 = st.checkbox("✅ Pastikan Seluruh Alat Ukur Memiliki Sertifikat")
    cek2 = st.checkbox("✅ Pastikan Suhu, Tekanan Dan Kelembaban Ruangan Stabil Pada Saat Kalibrasi Berlangsung")
    
    if cek1 and cek2:
        st.session_state.syarat = True
        st.success("✅ Semua syarat telah dipenuhi.")
    else:
        st.warning("⚠️ Harap centang semua syarat terlebih dahulu.")

elif selected == "💾 Input Data":
    if st.session_state.syarat:
        st.markdown('<div class="header-section"><h2>Input Data</h2></div>', unsafe_allow_html=True)
    
        # Input volume konvensional
        st.markdown("<h3 style='color:#0a0000;'>1.Input Volume Labu Takar</h3>", unsafe_allow_html=True)
        st.session_state.v_konven = st.number_input("Masukkan Volume Konvensional (mL)", min_value=0.00, value=st.session_state.v_konven, step=25.0,  format="%.2f")
        
        st.markdown('<div class="app-card">', unsafe_allow_html=True)
        st.markdown("<h3 style='color:#0a0000;'>2. Input Ketelitian Alat</h3>", unsafe_allow_html=True)
        st.session_state.ketelitian_lb = st.number_input("Masukkan Ketelitian Labu Takar (mL)", min_value=0.00, value=st.session_state.ketelitian_lb, step=0.0100, format="%.4f")
        
        # Template input tabel
        st.markdown('<div class="app-card">', unsafe_allow_html=True)
        st.markdown("<h3 style='color:#0a0000;'>3. Input Data Pengukuran</h3>", unsafe_allow_html=True)
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
        st.markdown("<h3 style='color:#0a0000;'>4. Input Data Alat Ukur</h3>", unsafe_allow_html=True)
        lop = st.number_input("Masukkan Nilai LOP Timbangan", value=0.0000, step=0.0001, format="%.4f")
        st.markdown("<p2 style='color:#0a0000;'>Masukkan NST, nilai U95, dan K untuk alat ukur:</p2>",unsafe_allow_html=True)
            
        col_nst, col_u95, col_k = st.columns(3)
        with col_nst:
                st.markdown("<h3 style='color:#0a0000; font-size: 24px;'>NST</h3>", unsafe_allow_html=True)
                st.session_state.nst = [st.number_input(f" {label} ( {satuan[i]} )", value=st.session_state.nst[i], key=f"nst_{i}", step=0.0001, format="%.4f") for i, label in enumerate(CC)]
        with col_u95:
                st.markdown("<h3 style='color:#0a0000; font-size: 24px;'>U95</h3>", unsafe_allow_html=True)
                st.session_state.u95 = [st.number_input(f" {label}", value=st.session_state.u95[i], key=f"u95_{i}", step=0.0010, format="%.4f") for i, label in enumerate(CC)]
        with col_k:
                st.markdown("<h3 style='color:#0a0000; font-size: 24px;'>K</h3>", unsafe_allow_html=True)
                nilai_k = [st.number_input(f" {label}", value=2.0, key=f"kval_{i}", step=1.0000, format="%.4f") for i, label in enumerate(CC)]
                
        st.markdown('<div class="app-card">', unsafe_allow_html=True)  
           
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
            
                        st.session_state.dens_air = 0.999974 - ((((T - 3.989)**2) * (T + 338.636)) / (563385.4 * (T + 72.45147)))
                        st.session_state.dens_udara = (((0.464554 * tekanan) - kelembaban*(0.00252*suhu_udara-0.020582)) / ((237.15+suhu_udara)*1000))
            
                        koef_muai = 0.00001
                        st.session_state.v_20 = massa * (1 - koef_muai * (T - 20)) / (st.session_state.dens_air - st.session_state.dens_udara)
                        st.session_state. koreksi = abs(st.session_state.v_20 - st.session_state.v_konven)
            
                    # Ketidakpastian massa air (U1)
                        k_neraca = (lop/(2*math.sqrt(3)))
                        k_ulangan = rata["U repeatability (g)"]
                        U1 = math.sqrt(k_neraca**2 + k_ulangan**2)
                        Cs1 = (1 - koef_muai * (T - 20)) / (st.session_state.dens_air - st.session_state.dens_udara)
            
                    #Ketidakpastian suhu air (U2)
                        U2 = st.session_state.u95[1] / nilai_k[1]
                        Cs2 = (massa * (-koef_muai)) / (st.session_state.dens_air - st.session_state.dens_udara)
            
                    #Ketidakpastian densitas air(U3)
                        Ut = U2
                        Ci = -((5.32*(10**-6) * T**2 + 1.20*(10**-4)*T + 2.82*(10**-5)) / ((T + 72.45147)**2))
                        U3 = math.sqrt((Ut * Ci)**2)
                        Cs3 = -massa * (1 - koef_muai*(T - 20)) / ((st.session_state.dens_air - st.session_state.dens_udara)**2)
            
                    #Ketidakpastian densitas udara(U4)
                        Uh = st.session_state.u95[4]/nilai_k[4]
                        Up = st.session_state.u95[3]/nilai_k[3]
                        Ut = st.session_state.u95[2]/nilai_k[2]
                        Ch = (0.020582 - 0.00252*suhu_udara) / ((237.15 + suhu_udara) * 1000)
                        Cp = (0.464554) / ((237.15 + suhu_udara) * 1000)
                        Ct = (-0.6182*kelembaban - 0.46554*tekanan) / (((237.15 + suhu_udara)**2) * 1000)
                        U4 = math.sqrt((Uh*Ch)**2 + (Up*Cp)**2 + (Ut*Ct)**2)
                        Cs4 = massa * (1 - koef_muai*(T - 20)) / ((st.session_state.dens_air - st.session_state.dens_udara)**2)
            
                    #Ketidakpastian KMV(U5)
                        U5 = (0.1 * koef_muai) / math.sqrt(3)
                        Cs5 = massa * (20 - T) / (st.session_state.dens_air - st.session_state.dens_udara)
            
                    #Ketidakpastian miniskus(U6)
                        U6 = ((5/100) * st.session_state.ketelitian_lb) / math.sqrt(3)
                        Cs6 = 1
    
                        st.session_state.ui = [U1, U2, U3, U4, U5, U6]
                        st.session_state.csi = [Cs1, Cs2, Cs3, Cs4, Cs5, Cs6]
                        st.session_state.ui_csi = [U1*Cs1, U2*Cs2, U3*Cs3, U4*Cs4, U5*Cs5, U6*Cs6]
                        st.session_state.ui_csi2 = [(U1*Cs1)**2, (U2*Cs2)**2, (U3*Cs3)**2, (U4*Cs4)**2, (U5*Cs5)**2, (U6*Cs6)**2]
                        
                    #Ketidakpastian gabungan(Ugab)
                        st.session_state.Ugab2 = ((U1*Cs1)**2 + (U2*Cs2)**2 + (U3*Cs3)**2 + (U4*Cs4)**2 + (U5*Cs5)**2 + (U6*Cs6)**2)
                        st.session_state.Ugab = math.sqrt((U1*Cs1)**2 + (U2*Cs2)**2 + (U3*Cs3)**2 + (U4*Cs4)**2 + (U5*Cs5)**2 + (U6*Cs6)**2)
                    
                    #Ketidakpastian Diperluas
                        st.session_state.U95_exp = st.session_state.Ugab * 2
    
                        st.subheader("Hasil Perhitungan")
                        st.write(f"Densitas Air: **{st.session_state.dens_air:.6f} g/mL**")
                        st.write(f"Densitas Udara: **{st.session_state.dens_udara:.6f} g/mL**")
                        st.write(f"Volume Sebenarnya (20°C): **{st.session_state.v_20:.6f} mL**")
                        st.write(f"Koreksi Volume Konvensional: **{st.session_state.koreksi:.6f} mL**") 
                        
                        st.subheader("Ketidakpastian")
                        st.write(f"Ugab2 (Gabungan2): **{st.session_state.Ugab2:.6f} mL**")
                        st.write(f"Ugab (Gabungan): **{st.session_state.Ugab:.6f} mL**")
                        st.write(f"Ketidakpastian Diperluas (U95): **{st.session_state.U95_exp:.6f} mL**")

                        st.subheader("Kesimpulan")
                        nilai_maks = st.session_state.koreksi + st.session_state.U95_exp
                        if st.session_state.koreksi < st.session_state.ketelitian_lb and nilai_maks < st.session_state.ketelitian_lb:
                            st.write("✅ labu Takar Dapat Digunakan")
                            st.write(f"Karena Nilai Koreksi Dan Nilai Maksimum Lebih Kecil Dari Ketelitian Labu Takar")
                        
                        elif st.session_state.koreksi < st.session_state.ketelitian_lb and nilai_maks > st.session_state.ketelitian_lb:
                            st.write("❌ labu Takar Tidak Dapat Digunakan")
                            st.write(f"Karena Nilai Koreksi Lebih Kecil Dari Ketelitian Labu Takar")
                            st.write(f"Tetapi Nilai Maksimum Lebih Besar Dari Ketelitian Labu Takar")
                            
                        elif st.session_state.koreksi > st.session_state.ketelitian_lb and nilai_maks < st.session_state.ketelitian_lb:
                            st.write("❌ labu Takar Tidak Dapat Digunakan")
                            st.write(f"Karena Nilai Maksimum Lebih Kecil Dari Ketelitian Labu Takar")
                            st.write(f"Tetapi Nilai Koreksi Lebih Besar Dari Ketelitian Labu Takar")
                            
                        else:
                            st.write("❌ labu Takar Tidak Dapat Digunakan")
                            st.write(f"Karena Nilai Koreksi Dan Nilai Maksimum Lebih Besar Dari Ketelitian Labu Takar")
                                    
             
                    except Exception as e:
                        st.error(f"Terjadi kesalahan saat perhitungan lanjutan: {e}")
    else:
        st.warning("⚠️ Harap Penuhi Semua Syarat Terlebih Dahulu.")
elif selected == "perhitungan":
    st.markdown('<div class="header-section"><h2>Perhitungan</h2></div>', unsafe_allow_html=True)
    nilai_maks = st.session_state.koreksi + st.session_state.U95_exp
#baris ke-1
    col_U, col_kosongg = st.columns([4, 3])
    with col_U:
        st.subheader("Hasil Perhitungan")
        st.write(f"Ketelitian Labu Takar: **{st.session_state.ketelitian_lb:.4f} mL**")
        st.write(f"Densitas Air: **{st.session_state.dens_air:.6f} g/mL**")
        st.write(f"Densitas Udara: **{st.session_state.dens_udara:.6f} g/mL**")
        st.write(f"Volume Sebenarnya (20°C): **{st.session_state.v_20:.6f} mL**")
        st.write(f"Koreksi Volume Konvensional: **{st.session_state.koreksi:.6f} mL**") 
        
#baris ke-2
    col_ui, col_csi, col_ui_csi2 = st.columns([2, 2, 2])
    with col_ui:
        st.subheader("Ui")
        st.write(f"U1 : **{st.session_state.ui[0]:.11f}**")
        st.write(f"U2 : **{st.session_state.ui[1]:.11f}**")
        st.write(f"U3 : **{st.session_state.ui[2]:.11f}**")
        st.write(f"U4 : **{st.session_state.ui[3]:.11f}**")
        st.write(f"U5 : **{st.session_state.ui[4]:.11f}**")
        st.write(f"U6 : **{st.session_state.ui[5]:.11f}**")
     
    with col_csi:
        st.subheader("Csi")
        st.write(f"Cs1 : **{st.session_state.csi[0]:.11f}**")
        st.write(f"Cs2 : **{st.session_state.csi[1]:.11f}**")
        st.write(f"Cs3 : **{st.session_state.csi[2]:.11f}**")
        st.write(f"Cs4 : **{st.session_state.csi[3]:.11f}**")
        st.write(f"Cs5 : **{st.session_state.csi[4]:.11f}**")
        st.write(f"Cs6 : **{st.session_state.csi[5]:.11f}**")
    
    with col_ui_csi2:
        st.subheader("(Ui x Csi)²")
        st.write(f"(U1 x Cs1)² : **{st.session_state.ui_csi2[0]:.11f}**")
        st.write(f"(U2 x Cs2)² : **{st.session_state.ui_csi2[1]:.11f}**")
        st.write(f"(U3 x Cs3)² : **{st.session_state.ui_csi2[2]:.11f}**")
        st.write(f"(U4 x Cs4)² : **{st.session_state.ui_csi2[3]:.11f}**")
        st.write(f"(U5 x Cs5)² : **{st.session_state.ui_csi2[4]:.11f}**")
        st.write(f"(U6 x Cs6)² : **{st.session_state.ui_csi2[5]:.11f}**")
    
#baris ke-3
    col_ketidak, col_kesimpul = st.columns([3, 3])
    with col_ketidak:
        st.subheader("Ketidakpastian")
        st.write(f"Ketidakpastian Gabungan: **{st.session_state.Ugab:.6f} mL**")
        st.write(f"Ketidakpastian Diperluas: **{st.session_state.U95_exp:.6f} mL**")
        st.write(f"Nilai Maksimum: **{nilai_maks:.4f} mL**")
        
    with col_kesimpul:
        st.subheader("Kesimpulan")
        if st.session_state.koreksi < st.session_state.ketelitian_lb and nilai_maks < st.session_state.ketelitian_lb:
            st.write("✅ labu Takar Dapat Digunakan")
            st.write(f"Karena Nilai Koreksi Dan Nilai Maksimum Lebih Kecil Dari Ketelitian Labu Takar")
        
        elif st.session_state.koreksi < st.session_state.ketelitian_lb and nilai_maks > st.session_state.ketelitian_lb:
            st.write("❌ labu Takar Tidak Dapat Digunakan")
            st.write(f"Karena Nilai Koreksi Lebih Kecil Dari Ketelitian Labu Takar")
            st.write(f"Tetapi Nilai Maksimum Lebih Besar Dari Ketelitian Labu Takar")
            
        elif st.session_state.koreksi > st.session_state.ketelitian_lb and nilai_maks < st.session_state.ketelitian_lb:
            st.write("❌ labu Takar Tidak Dapat Digunakan")
            st.write(f"Karena Nilai Maksimum Lebih Kecil Dari Ketelitian Labu Takar")
            st.write(f"Tetapi Nilai Koreksi Lebih Besar Dari Ketelitian Labu Takar")
            
        else:
            st.write("❌ labu Takar Tidak Dapat Digunakan")
            st.write(f"Karena Nilai Koreksi Dan Nilai Maksimum Lebih Besar Dari Ketelitian Labu Takar")
                    
elif selected == "📘 Penutup":
    st.markdown('<div class="header-section"><h1>Terimakasih</h1></div>', unsafe_allow_html=True)
           
            
            
        
       
