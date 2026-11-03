from pathlib import Path
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Bike Sharing | 2011–2012", layout="wide")
BASE=Path(__file__).resolve().parent
@st.cache_data
def load():
    daily=pd.read_csv(BASE/'daily_clean.csv',parse_dates=['date'])
    hourly=pd.read_csv(BASE/'hourly_clean.csv',parse_dates=['date'])
    return daily,hourly

daily,hourly=load()
st.title("Analisis Penyewaan Sepeda")
st.caption("Analisis deskriptif penyewaan sepeda historis, 2011–2012 | Data asli: Bike Sharing Dataset")
st.sidebar.header('Filter Data')
years=st.sidebar.multiselect('Tahun',sorted(daily.year.unique().tolist()),default=sorted(daily.year.unique().tolist()))
if not years:
    st.warning('Pilih minimal satu tahun untuk melihat hasil.');st.stop()
season_options=['Spring','Summer','Fall','Winter']
seasons=st.sidebar.multiselect('Musim',season_options,default=season_options)
if not seasons:
    st.warning('Pilih minimal satu musim.');st.stop()
d=daily[daily.year.isin(years)&daily.season_name.isin(seasons)].copy()
h=hourly[hourly.year.isin(years)&hourly.season_name.isin(seasons)].copy()
if d.empty or h.empty:st.info('Tidak ada data untuk filter ini.');st.stop()
c1,c2,c3=st.columns(3)
c1.metric('Total penyewaan harian (akumulasi)',f"{d.cnt.sum():,}")
c2.metric('Rata-rata penyewaan/hari',f"{d.cnt.mean():,.0f}")
c3.metric('Jumlah hari',f"{len(d):,}")
st.caption('Metrik mengikuti filter. Jumlah penyewaan merupakan agregasi harian, tidak dijumlahkan kembali dengan data per jam.')
t1,t2,t3=st.tabs(['Pola Jam','Musim & Cuaca','Tingkat Permintaan'])
with t1:
    st.subheader('Pertanyaan 1: jam puncak per jenis hari')
    prof=h.groupby(['day_type','hr'],as_index=False).cnt.mean()
    fig,ax=plt.subplots(figsize=(10,4.5))
    for name,grp in prof.groupby('day_type'):
        ax.plot(grp.hr,grp.cnt,marker='o',label=name)
    ax.set(title='Rata-rata penyewaan pada setiap jam',xlabel='Jam',ylabel='Rata-rata sewa/jam',xticks=range(0,24,2),ylim=(0,None))
    ax.legend();fig.tight_layout();st.pyplot(fig);plt.close(fig)
    st.dataframe(prof.pivot(index='hr',columns='day_type',values='cnt').round(1),use_container_width=True)
    st.info('Bandingkan jam puncak sebelum menyusun jadwal redistribusi armada. Penghitungan memakai rerata dari jam yang tercatat.')
with t2:
    st.subheader('Pertanyaan 2: musim dan kondisi cuaca')
    left,right=st.columns(2)
    for host,key,title in [(left,'season_name','Menurut musim'),(right,'weather_name','Menurut cuaca')]:
        profile=d.groupby(key,as_index=False).cnt.mean().sort_values('cnt',ascending=False)
        fig,ax=plt.subplots(figsize=(6,4))
        ax.bar(profile[key],profile.cnt,color='#497D91');ax.set(title=title,ylabel='Rata-rata sewa/hari',ylim=(0,None));ax.tick_params(axis='x',rotation=30);fig.tight_layout();host.pyplot(fig);plt.close(fig)
    st.info('Perbedaan rata-rata adalah asosiasi deskriptif, bukan bukti sebab-akibat.')
with t3:
    st.subheader('Pertanyaan 3: Pengelompokan Tingkat Penyewaan')
    # Batas ditentukan dari SEMUA data historis agar kategori tetap konsisten saat memfilter
    counts=d.demand_level.value_counts().reindex(['Low','Medium','High'],fill_value=0)
    fig,ax=plt.subplots(figsize=(8,4));ax.bar(counts.index,counts.values,color=['#749BB2','#E3B36D','#599776']);ax.set(ylabel='Jumlah hari',xlabel='Kategori',title='Distribusi level permintaan',ylim=(0,None));fig.tight_layout();st.pyplot(fig);plt.close(fig)
    q=daily.cnt.quantile([1/3,2/3]);st.caption(f'Batas tetap dari seluruh data 2011–2012: Low ≤ {q.iloc[0]:.1f}; Medium ≤ {q.iloc[1]:.1f}; High > {q.iloc[1]:.1f}.')
    st.info('Gunakan kategori untuk peninjauan historis, bukan model prediksi.')
st.divider()
st.markdown('**Rekomendasi operasional:** uji redistribusi sepeda pada jam puncak yang terlihat, lalu verifikasi dengan data ketersediaan armada. Pertimbangkan musim/cuaca ketika memantau kapasitas.')
st.caption('Sumber: Bike Sharing Dataset (UCI). Dataset historis 2011–2012. Dashboard untuk keperluan pembelajaran Dicoding.')
