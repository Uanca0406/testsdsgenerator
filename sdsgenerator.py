import streamlit as st

# Judul aplikasi
st.title("SDS Generator")

# Input untuk informasi bahan kimia
st.header("Informasi Bahan Kimia")
chemical_name = st.text_input("Nama Bahan Kimia")
cas_number = st.text_input("Nomor CAS")
hazard_class = st.selectbox("Kelas Bahaya", ["Tidak Berbahaya", "Kelas 1", "Kelas 2", "Kelas 3"])
concentration = st.number_input("Konsentrasi (%)", min_value=0.0, max_value=100.0)

# Input untuk informasi penyimpanan
st.header("Informasi Penyimpanan")
storage_conditions = st.text_area("Kondisi Penyimpanan")

# Input untuk informasi penanganan
st.header("Informasi Penanganan")
handling_instructions = st.text_area("Instruksi Penanganan")

# Tombol untuk menghasilkan SDS
if st.button("Buat SDS"):
    if chemical_name and cas_number:
        sds_content = f"""
        # Safety Data Sheet (SDS)

        ## 1. Identifikasi Bahan Kimia
        - Nama Bahan Kimia: {chemical_name}
        - Nomor CAS: {cas_number}
        - Kelas Bahaya: {hazard_class}
        - Konsentrasi: {concentration}%

        ## 2. Informasi Penyimpanan
        {storage_conditions}

        ## 3. Informasi Penanganan
        {handling_instructions}
        """
        st.success("SDS berhasil dibuat!")
        st.text_area("SDS Anda:", value=sds_content, height=300)
    else:
        st.error("Silakan lengkapi semua informasi yang diperlukan.")

# Menjalankan aplikasi
if __name__ == "__main__":
    st.run()
