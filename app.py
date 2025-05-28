
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load datasets
daily_df = pd.read_csv('daily_counts_for_dashboard.csv')
monthly_df = pd.read_csv('monthly_series_for_dashboard.csv', parse_dates=True, index_col=0)
heatmap_2024 = pd.read_csv('heatmap_2024.csv', index_col=0)
heatmap_2025 = pd.read_csv('heatmap_2025.csv', index_col=0)

# Title
st.title("Dashboard Interaktif Kedatangan Pasien IGD - RS Tipe B Medan")

# Filter Tahun
year_option = st.selectbox("Pilih Tahun", sorted(daily_df['Year'].unique()))
filtered_daily = daily_df[daily_df['Year'] == year_option]

# Heatmap Hari vs Jam
st.subheader(f"Heatmap Kedatangan IGD Tahun {year_option}")
fig_hm, ax_hm = plt.subplots(figsize=(12, 5))
hm_data = heatmap_2024 if year_option == 2024 else heatmap_2025
sns.heatmap(hm_data, cmap='YlOrRd', annot=True, fmt='d', ax=ax_hm)
st.pyplot(fig_hm)

# Tren Bulanan
st.subheader("Tren Bulanan Kedatangan Pasien IGD")
fig_month, ax_month = plt.subplots(figsize=(12, 4))
monthly_df.plot(ax=ax_month, legend=False)
ax_month.set_title("Jumlah Pasien IGD per Bulan")
ax_month.set_ylabel("Jumlah Pasien")
st.pyplot(fig_month)

# Distribusi Harian
st.subheader("Distribusi Jumlah Pasien Harian")
fig_day, ax_day = plt.subplots(figsize=(12, 4))
sns.boxplot(data=filtered_daily['Arrivals'], ax=ax_day)
ax_day.set_title("Boxplot Jumlah Pasien Harian")
st.pyplot(fig_day)

st.markdown("Dibuat oleh: Data Analysis & Report AI 🌍")
