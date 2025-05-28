
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load datasets
daily_df = pd.read_csv('daily_counts_for_dashboard.csv')
monthly_df = pd.read_csv('monthly_series_for_dashboard.csv', parse_dates=True, index_col=0)
heatmap_2024 = pd.read_csv('heatmap_2024.csv', index_col=0)
heatmap_2025 = pd.read_csv('heatmap_2025.csv', index_col=0)

# Title and intro
st.title("Dashboard Interaktif Kedatangan Pasien IGD - RS Tipe B Medan")
st.markdown("""
Dashboard ini menyajikan analisis lengkap terhadap pola kedatangan pasien di IGD rumah sakit tipe B di Kota Medan, 
beserta rekomendasi strategis berdasarkan data aktual 2023–2025.
""")

# Tahun selector
year_option = st.selectbox("Pilih Tahun", sorted(daily_df['Year'].unique()))
filtered_daily = daily_df[daily_df['Year'] == year_option]

# Heatmap Hari vs Jam
st.subheader(f"📊 Heatmap Kedatangan IGD Tahun {year_option}")
fig_hm, ax_hm = plt.subplots(figsize=(12, 5))
hm_data = heatmap_2024 if year_option == 2024 else heatmap_2025
sns.heatmap(hm_data, cmap='YlOrRd', annot=True, fmt='d', ax=ax_hm)
st.pyplot(fig_hm)
st.markdown("""
**Analisis:** Terlihat bahwa jam 20:00–21:00 merupakan jam puncak di hampir setiap hari, 
dengan hari **Senin dan Sabtu** sebagai hari tersibuk.  
**Rekomendasi:** Tambah tenaga medis, fasilitas dan logistik pada malam hari terutama Senin–Sabtu.
""")

# Tren Bulanan
st.subheader("📈 Tren Bulanan Kedatangan Pasien IGD")
fig_month, ax_month = plt.subplots(figsize=(12, 4))
monthly_df.plot(ax=ax_month, legend=False)
ax_month.set_title("Jumlah Pasien IGD per Bulan")
ax_month.set_ylabel("Jumlah Pasien")
st.pyplot(fig_month)
st.markdown("""
**Analisis:** Jumlah pasien tertinggi terjadi pada bulan **Oktober dan September**.  
**Rekomendasi:** Prioritaskan persiapan logistik dan SDM pada bulan-bulan ini.
""")

# Distribusi Harian
st.subheader("📦 Boxplot Anomali Kedatangan Harian")
fig_day, ax_day = plt.subplots(figsize=(12, 4))
sns.boxplot(data=filtered_daily['Arrivals'], ax=ax_day)
ax_day.set_title("Boxplot Jumlah Pasien Harian")
st.pyplot(fig_day)
st.markdown("""
**Analisis:** Terdapat lonjakan jumlah pasien pada hari-hari tertentu (contoh: 21–22 Oktober).  
**Rekomendasi:** Lakukan investigasi penyebab lonjakan, seperti wabah lokal atau libur panjang.
""")

# Penutup
st.markdown("""
---

📌 **Dashboard ini mendukung pengambilan keputusan IGD berbasis data.**  
🧠 Rekomendasi strategis dapat digunakan untuk pengaturan shift, pengadaan alat medis, dan evaluasi kapasitas tahunan.
""")

st.markdown("Dibuat oleh: Data Analysis & Report AI 🌍")
