import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

@st.cache_data()
def load_data():
    url = 'https://github.com/YaserAp/uasAnalisisData/raw/main/day.csv'
    data = pd.read_csv(url)
    data['dteday'] = pd.to_datetime(data['dteday'])
    return data

def create_visualization(data):
    data_2011 = data[data['dteday'].dt.year == 2011]
    data_2012 = data[data['dteday'].dt.year == 2012]

    peminjaman_2011 = data_2011.groupby(data_2011['dteday'].dt.month)['cnt'].sum()
    peminjaman_2012 = data_2012.groupby(data_2012['dteday'].dt.month)['cnt'].sum()

    fig, ax = plt.subplots(figsize=(10, 6))  
    ax.plot(peminjaman_2011.index, peminjaman_2011.values, marker='o', label='2011')
    ax.plot(peminjaman_2012.index, peminjaman_2012.values, marker='o', label='2012')
    ax.set_title('Tren Peminjaman Sepeda per Bulan (2011 vs 2012)')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Total Peminjaman Sepeda')
    ax.set_xticks(range(1, 13))
    ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    ax.legend()

    st.pyplot(fig)

    with st.expander('Penjelasan Analisis Peminjaman:'):
        st.write('Setelah menganalisis data peminjaman sepeda untuk tahun 2011 dan 2012, kami menemukan bahwa terjadi peningkatan jumlah peminjaman sepeda dari tahun 2011 ke tahun 2012. Tahun 2011 mencapai puncak peminjaman sepeda pada bulan Juli, sementara tahun 2012 mencapai puncaknya pada bulan Juni. Pola umum menunjukkan bahwa peminjaman sepeda cenderung meningkat selama musim panas dan musim semi. Data ini dapat digunakan untuk perencanaan dan manajemen peminjaman sepeda di masa mendatang, dengan memperhitungkan pola musiman dan tren tahunan.')

def show_dashboard():
    
    with st.expander('Analisis Data'):
        st.write('Pilih tahun untuk analisis data:')
        if st.button('2011'):
            show_tabulation_2011()
        if st.button('2012'):
            show_tabulation_2012()

def show_tabulation_2011():
    st.header('Analisis Data Peminjaman 2011')
    data = [
        {'Bulan': 'Januari', 'Total Peminjaman': 328000},
        {'Bulan': 'Februari', 'Total Peminjaman': 414000},
        {'Bulan': 'Maret', 'Total Peminjaman': 507000},
        {'Bulan': 'April', 'Total Peminjaman': 566000},
        {'Bulan': 'Mei', 'Total Peminjaman': 691000},
        {'Bulan': 'Juni', 'Total Peminjaman': 726000},
        {'Bulan': 'Juli', 'Total Peminjaman': 731000},
        {'Bulan': 'Agustus', 'Total Peminjaman': 734000},
        {'Bulan': 'September', 'Total Peminjaman': 734000},
        {'Bulan': 'Oktober', 'Total Peminjaman': 719000},
        {'Bulan': 'November', 'Total Peminjaman': 618000},
        {'Bulan': 'Desember', 'Total Peminjaman': 168000}
    ]
    st.table(pd.DataFrame(data))

def show_tabulation_2012():
    st.header('Analisis Data Peminjaman 2012')
    data = [
        {'Bulan': 'Januari', 'Total Peminjaman': 38189},
        {'Bulan': 'Februari', 'Total Peminjaman': 48215},
        {'Bulan': 'Maret', 'Total Peminjaman': 64045},
        {'Bulan': 'April', 'Total Peminjaman': 94870},
        {'Bulan': 'Mei', 'Total Peminjaman': 135821},
        {'Bulan': 'Juni', 'Total Peminjaman': 143512},
        {'Bulan': 'Juli', 'Total Peminjaman': 141341},
        {'Bulan': 'Agustus', 'Total Peminjaman': 136691},
        {'Bulan': 'September', 'Total Peminjaman': 127418},
        {'Bulan': 'Oktober', 'Total Peminjaman': 123511},
        {'Bulan': 'November', 'Total Peminjaman': 102167},
        {'Bulan': 'Desember', 'Total Peminjaman': 87323}
    ]
    st.table(pd.DataFrame(data))

def main():
    st.title('Dashboard Analisis Bike Sharing')
    show_dashboard()
    data = load_data()
    create_visualization(data)

if __name__ == '__main__':
    main()
