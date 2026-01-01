import streamlit as st
from patterns import (
    make_pyramid,
    make_segitiga_kiri,
    make_segitiga_kanan,
    make_belah_ketupat
)

st.title("Pattern Maker")

jenis = st.selectbox(
    "Pilih pola",
    (
        "Piramida",
        "Segitiga siku kiri",
        "Segitiga siku kanan",
        "Belah ketupat"
    )
)

tinggi = st.number_input(
    "Tinggi",
    min_value=1,
    max_value=50,
    step=1
)

if st.button("Generate"):
    if jenis == "Piramida":
        hasil = make_pyramid(tinggi)
    elif jenis == "Segitiga siku kiri":
        hasil = make_segitiga_kiri(tinggi)
    elif jenis == "Segitiga siku kanan":
        hasil = make_segitiga_kanan(tinggi)
    else:
        hasil = make_belah_ketupat(tinggi)

    st.code(hasil)
