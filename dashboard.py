import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


@st.cache
def load_data(url):
    try:
        data = pd.read_csv(url)
        return data
    except Exception as e:
        st.error(f"Terjadi kesalahan saat memuat data: {e}")
        return None

def create_visualization(data_2011, data_2012):
    if data_2011 is not None and data_2012 is not None:
        st.subheader('Visualisasi Data')
        st.subheader('Tren Peminjaman Sepeda (2011 vs 2012)')

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

def main():
    st.title('Dashboard Bike Sharing')

    df_day = load_data('https://github.com/YaserAp/uasAnalisisData/blob/main/day.csv')
    df_hour = load_data('https://github.com/YaserAp/uasAnalisisData/blob/main/hour.csv')

    create_visualization(data_2011, data_2012)

if __name__ == "__main__":
    main()
