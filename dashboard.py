import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache
def load_data(url):
    try:
        data = pd.read_csv(url)
        return data, None
    except Exception as e:
        return None, e

def main():
    df_day, error_day = load_data('https://raw.githubusercontent.com/YaserAp/uasAnalisisData/main/day.csv')
    df_hour, error_hour = load_data('https://raw.githubusercontent.com/YaserAp/uasAnalisisData/main/hour.csv')

    if df_day is not None and df_hour is not None:
        data_2011 = df_hour[df_hour['yr'] == 0]
        data_2012 = df_hour[df_hour['yr'] == 1]

        create_visualization(data_2011, data_2012)
    else:
        if error_day:
            st.error(f"Terjadi kesalahan saat memuat data day.csv: {error_day}")
        if error_hour:
            st.error(f"Terjadi kesalahan saat memuat data hour.csv: {error_hour}")

def create_visualization(data_2011, data_2012):
    peminjaman_2011 = data_2011.groupby(data_2011['dteday'].dt.month)['cnt'].sum()
    peminjaman_2012 = data_2012.groupby(data_2012['dteday'].dt.month)['cnt'].sum()

    plt.figure(figsize=(10, 6))
    sns.lineplot(data=peminjaman_2011, label='2011', marker='o')
    sns.lineplot(data=peminjaman_2012, label='2012', marker='o')
    plt.title('Tren Peminjaman Sepeda (2011 vs 2012)')
    plt.xlabel('Bulan')
    plt.ylabel('Total Peminjaman Sepeda')
    plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    plt.legend()
    st.pyplot()

if __name__ == "__main__":
    main()
