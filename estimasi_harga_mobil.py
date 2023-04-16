import pickle
import streamlit as st

#pemanggilan model estimasi
model = pickle.load(open('estimasi_harga_mobil.sav','rb'))

#judul
st.title('Estimasi Harga Mobil Bekas Hyundai')

year = st.number_input('input Tahun Mobil')
mileage = st.number_input('input Km Mobil')
tax = st.number_input('Input Pajak Mobil')
mpg = st.number_input('Input Konsumsi BBM Mobil')
engineSize = st.number_input('Input engineSize')

#identifikasi modelnya
predict =''

#kondisi (if)kan ada tombolnya
if st.button('Estimasi Harga'):
    predict = model.predict(
        [[year,mileage,tax,mpg,engineSize]]
    )
#keterangan klo di klik tombol estimasi harga muncul keterangn...
st.write('Estimasi harga Mobil Berkas Dalam Pondn:',predict)
st.write('Estimasi harga mobil bekas dalam IDR(juta):',predict*19000)