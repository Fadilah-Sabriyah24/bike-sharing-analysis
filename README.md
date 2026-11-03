# Bike Sharing Analytics — Proyek Akhir Dicoding

Analisis deskriptif pola penyewaan sepeda periode **2011–2012** menggunakan dataset resmi Bike Sharing. Berisi notebook dan dashboard Streamlit yang menggunakan data bersih siap visualisasi.

## Struktur
- `data/day.csv`, `data/hour.csv`: dataset asli; `data/Readme.txt`: deskripsi kode kolom.
- `notebook.ipynb`: notebook lengkap, pertanyaan SMART, wrangling, EDA, visualisasi, dan rekomendasi.
- `dashboard/dashboard.py`: aplikasi Streamlit.
- `dashboard/daily_clean.csv`, `dashboard/hourly_clean.csv`: hasil transformasi notebook sebagai sumber dashboard.
- `dashboard/hourly_profile.csv`: ringkasan tambahan.
- `requirements.txt`: dependensi Python.
- `url.txt`: URL deploy (hanya setelah deploy berhasil).

## Cara menjalankan (dari folder submission)

```bash
python -m pip install -r requirements.txt
python -m streamlit run dashboard/dashboard.py
```

Akses alamat `http://localhost:8501` (atau alamat yang muncul di terminal). Untuk menjalankan ulang notebook, buka `notebook.ipynb` dalam Jupyter/Colab dan jalankan semua cell secara berurutan dari direktori submission. **Jalankan notebook sebelum mengirim submission** supaya output cell tersimpan.

## Pertanyaan bisnis
1. Pola jam puncak antara hari kerja dan non-kerja pada 2011–2012.
2. Perbandingan rata-rata penyewaan harian menurut musim dan cuaca pada 2011–2012.
3. Segmentasi hari berdasar tertil permintaan historis (binning, non-ML).

## Catatan metode
Dataset mentah tanpa missing value/duplikasi identik. Tanggal distandarkan menjadi datetime, kategori numerik ditransformasi menjadi label, outlier IQR diperiksa namun tidak dibuang sebab pola jam puncak adalah objek penelitian. Rata-rata adalah statistik deskriptif; tidak menunjukkan hubungan sebab-akibat. Dashboard menggunakan data hasil transformasi yang sama dengan notebook.

## Deploy Streamlit Community Cloud (opsional untuk skor lebih tinggi)
Unggah isi folder `submission` ke repositori GitHub, pilih entry point `dashboard/dashboard.py` di Streamlit Community Cloud, pastikan requirements dan dataset CSV dashboard ikut terunggah. Setelah situs benar-benar aktif, simpan URL lengkap pada `url.txt`.

## Checklist sebelum submit
- [ ] Ganti identitas dalam notebook.
- [ ] Jalankan semua cell notebook, simpan output dan pastikan tanpa error.
- [ ] Jalankan dashboard secara lokal.
- [ ] Pastikan semua berkas masuk ZIP.
- [ ] Jika deployment dilakukan, isi `url.txt` dengan tautan aktif.
