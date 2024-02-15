import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data(allow_output_mutation=True)
def load_data(url):
    try:
        data = pd.read_csv(url)
        return data
    except Exception as e:
        st.error(f"Terjadi kesalahan saat memuat data: {e}")
        return None

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

def main():
    df_day = load_data('https://github.com/YaserAp/uasAnalisisData/blob/main/day.csv')
    df_hour = load_data('https://github.com/YaserAp/uasAnalisisData/blob/main/hour.csv')

    if df_day is not None and df_hour is not None:
        data_2011 = df_hour[df_hour['yr'] == 0]
        data_2012 = df_hour[df_hour['yr'] == 1]

        create_visualization(data_2011, data_2012)
    else:
        st.error("Gagal memuat data. Silakan periksa URL atau coba lagi nanti.")

if __name__ == "__main__":
    main()
