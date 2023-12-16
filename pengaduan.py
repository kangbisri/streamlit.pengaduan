import mysql.connector
import streamlit as st
import crud
from PIL import Image
from streamlit_option_menu import option_menu
import pandas as pd
import datetime

st.set_page_config(
    page_title="WEBSITE INFORMASI & PENGADUAN TEKNIK INDUSTRI UTM",
    page_icon= "hmti.jpg",
    layout="wide"
)

with st.sidebar:
    menu = option_menu("LAYANAN KAMI", ["HOME", 'PENGADUAN', "CONTACT PERSON", "USER", "TENTANG KAMI"],
                           icons=['house', 'list', 'phone', 'person', 'person' ], menu_icon="cast", default_index=1)
if menu == "HOME":
# informasi data form
    st.success("MENU HOME")
    st.markdown("<h1 style='text-align: center; color: yellow;'>WEBSITE INFORMASI & PENGADUAN TEKNIK INDUSTRI UTM</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: blue ;'>Selamat Datang di Website Informasi & Pengaduan Teknik Industri UTM</h4>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center; color: white ;'>Sampaikan Saran dan Masukan Anda Untuk Perkembangan Teknik Industri UTM yang Lebih Baik</h6>", unsafe_allow_html=True)
    st.sidebar.title("Created By Kelompok 1")
    
    prodi, lab, mahasiswa = st.tabs(['INFORMASI PROGRAM STUDI', 'LABORATORIUM PENJURUSAN', 'DATA MAHASISWA'])
     #DESKRIPSI TEKS
    with prodi:
        st.success("Berikut Informasi Program Studi Teknik Industri UTM")
        with st.columns(8)[1]:
            st.image('ft.png', caption='Gedung Fakultas Teknik (RKB-F) merupakan salah satu gedung Universitas Trunojoyo Madura yang menunjang kegiatan perkuliahan program studi yang ada dalam Fakultas Teknik, termasuk Prodi Teknik Industri. Prodi Teknik Industri berdiri sejak tahun 2001 dan berhasil memperoleh Akreditasi B berdasarkan SK 1362/SK/BAN-PT/Akred/S/V/2019. Saat ini, Prodi Teknik Industri memiliki 21 Tenaga Pengajar dengan berbagai bidang peminatan seperti rantai pasok, optimasi, sistem, kualitas, ergonomi dan sistem produksi yang siap mencetak sarjana Teknik Industri yang profesional. Prodi Teknik industri mempersiapkan lulusan yang berkompeten untuk memanfaatkan sumber daya manusia, peralatan, material, informasi dan energi dengan mengikuti standar dan peraturan keselamatan untuk mencapai manfaat yang maksimal. Sehingga, lulusan prodi Teknik Industri mampu memperbaiki atau merancang proses produksi atau bisnis yang lebih efisien.',width=750)
            st.write("[Website Resmi>](http://industri.trunojoyo.ac.id/)")
    with lab:
        st.success("Berikut Informasi Laboratorium Penjurusan Program Studi Teknik Industri UTM")
        with st.columns(8)[1]:
            st.image("mi.jpeg", caption='Laboratorium Manajemen Industri adalah salah satu laboratorium yang dimiliki Program Studi Teknik Industri Fakultas Teknik, Universitas Trunojoyo Madura. Laboratorium Manajemen Industri adalah laboratorium yang bergerak dibidang minat manajemen industri. Dalam pembelajarannya, laboratorium ini berfokus pada beberapa mata kuliah yang berhubungan dengan Manajemen Industri', width=750 )
            st.write("[Website Resmi>](https://labmi.trunojoyo.ac.id/)")
            st.image('ergo.jpg', caption='Laboratorium Ergonomi & Perancangan Sistem Kerja merupakan salah satu laboratorium yang dimiliki Program Studi Teknik Industri Fakultas Teknik. Laboratorium ini mempunyai tujuan melakukan pendidikan, penelitian, dan pengabdian pada masyarakat terutama dalam bidang industri untuk menciptakan sIstem kerja yang sesuai dengan aspek-aspek ergonomi yaitu aman, nyaman, sehat, serta efisien dan efektif, Sehingga akan dapat meningkatkan produktifitas kerja. Selain itu juga laboratorium EPSK UTM juga bisa menjadi konsultan dalam bidang perancangan produk yang ergonomis.', width=750)
            st.write("[Website Resmi>](https://epsk-trunojoyo.blogspot.com/)")
            st.image('rspk.jpg', caption='Laboratorium Rekayasa Sistem dan Pengambilan Keputusan merupakan salah satu laboratorium yang dimiliki Program Studi Teknik Industri Fakultas Teknik yang memfasilitasi pengembangan kompetensi terkait rekayasa sistem dan pengambilan keputusan', width=750)
            st.write("[Instagram Resmi>](https://www.instagram.com/lab.rspk_utm/)")
            st.image('sisman.jpg', caption='Laboratorium Sistem Manufaktur merupakan salah satu laboratorium yang dimiliki Program Studi Teknik Industri Fakultas Teknik yang memfasilitasi pengembangan kompetensi terkait sistem manufaktur', width=750)
            st.write("[Website Resmi>](http://www.sisman-utm.com/)")
    
    with mahasiswa:
        st.success("Data Mahasiswa")
        st.markdown("<h6 style='text-align: center; color: yellow;'>Informasi Jumlah Mahasiswa Program Studi Teknik Industri UTM Tahun 2023 Berdasarkan Angkatan</h1>", unsafe_allow_html=True)
        df_data_mahasiswa =  pd.DataFrame(crud.getALLDatamahasiswa(), columns=['angkatan', 'jumlah'])
        st.table(df_data_mahasiswa)
        st.text("Tabel Informasi Jumlah Mahasiswa Teknik Industri UTM Tahun 2023 Berdasarkan Angkatan")    

    
elif menu == "PENGADUAN":
    st.success("MENU PENGADUAN")
    st.markdown("<h2 style='text-align: center; color: yellow;'>MENU PENGADUAN</h2>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: blue ;'>Selamat Datang di Menu Pengaduan Teknik Industri UTM</h4>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center; color: white ;'>Sebelum melakukan pengaduan, Pastikan NIM anda telah terdaftar, Jika belum terdaftar, anda dapat melakukan pendaftaran pada menu user</h6>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center; color: white ;'>Silahkan isi data dibawah ini untuk melakukan pengaduan</h6>", unsafe_allow_html=True)
    st.sidebar.title("Created By Kelompok 1")
    
    objek_pengaduan = st.selectbox (
        "Pilih Objek Pengaduan",
        ("Dosen", "Fasilitas","Pelayanan")
    )

    if objek_pengaduan == "Dosen":
        tanggal = st.date_input("Tanggal Pengaduan")
        nim = st.text_input("Masukkan NIM Anda yang Telah Terdaftar Sebelumnya")
        jenis_pengaduan = st.text_input ("Informasikan Kategori Kasus, Contoh Kehadiran, Kedisiplinan, Metode Pembelajaran, Transparansi penilaian")
        matakuliah = st.text_input ("Informasikan Matakuliah, Contoh AEB, Mavek, Statistika, PEI, BASDAT, Pancasila, PPP, LEI")
        kelas = st.text_input ("Informasikan Kelas, Contoh A, B, C, D, E")
        keluhan = st.text_input("Deskripsikan Keluhan")
        if st.button ("Kirim"):
            if crud.insertDatapengaduan_dosen(tanggal, nim, jenis_pengaduan, matakuliah, kelas, keluhan) and (tanggal != '' and nim != '' and jenis_pengaduan != '' and matakuliah != '' and kelas != '' and keluhan != ''):
                st.success("Pengaduan Anda Telah Disampaikan")
                st.write("Terima Kasih telah memberikan masukan yang membangun untuk kemajuan Teknik Industri UTM")
            else:
                st.error("Gagal mengirim pengaduan, Pastikan anda sudah melakukan pendaftaran di menu user dan pastikan semua informasi pengaduan telah terisi dan sesuai")

    elif objek_pengaduan == "Fasilitas":
        tanggal = st.date_input("Tanggal Pengaduan")
        nim = st.text_input("Masukkan NIM Anda yang Telah Terdaftar Sebelumnya")
        letak = st.text_input("Informasikan Letak Objek yang diadukan, Contoh : Lantai 3 Barat, Ruang 201")
        objek_fasilitas = st.text_input (" Informasikan Objek Fasilitas, Contoh AC, Proyektor, Bangku, ATK, Kamar Mandi, Musholla")
        kondisi = st.text_input (" Informasikan Kondisi Fasilitas, Contoh Berfungsi Kurang Optimal, Rusak, Tidak Tersedia, Kotor, Air Mati")
        if st.button ("Kirim"):
            if crud.insertDatapengaduan_fasilitas(tanggal, nim, letak, objek_fasilitas, kondisi) and (tanggal != '' and nim != '' and letak != '' and objek_fasilitas != '' and kondisi != ''):
                st.success("Pengaduan Anda Telah Disampaikan")
                st.write("Terima Kasih telah memberikan masukan yang membangun untuk kemajuan Teknik Industri UTM")
            else:
                st.error("Gagal mengirim pengaduan, Pastikan anda sudah melakukan pendaftaran di menu user dan pastikan semua informasi pengaduan telah terisi dan sesuai")
              
    elif objek_pengaduan == "Pelayanan":
        tanggal = st.date_input("Tanggal Pengaduan")
        nim = st.text_input("Masukkan NIM Anda yang Telah Terdaftar Sebelumnya")
        objek_pengaduan = st.text_input ("Informasikan Kategori Kasus, Contoh Keramahan Pelayanan, Respon Pelayanan, Kecepatan Penanganan Pelayanan, Kedisiplinan")
        objek_pelayanan = st.text_input ("Informasikan Objek Pelayanan, Contoh Layanan Peminjaman Barang, Layanan Pengajuan Surat, Layanan Izin Penggunaan Ruangan")
        keluhan = st.text_input("Deskripsikan keluhan anda")
        if st.button ("Kirim"):
            if crud.insertDatapengaduan_pelayanan(tanggal, nim, objek_pengaduan, objek_pelayanan, keluhan) and (tanggal != '' and nim != '' and objek_pengaduan != '' and objek_pelayanan != '' and keluhan != ''):
                st.success("Pengaduan Anda Telah Disampaikan")
                st.write("Terima Kasih telah memberikan masukan yang membangun untuk kemajuan Teknik Industri UTM")
            else:
                st.error("Gagal mengirim pengaduan, Pastikan anda sudah melakukan pendaftaran di menu user dan pastikan semua informasi pengaduan telah terisi dan sesuai")
    
    
elif menu == "CONTACT PERSON":
    st.success("MENU CONTACT PERSON")
    st.markdown("<h2 style='text-align: center; color: yellow;'>CONTACT PERSON PELAYANAN</h2>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: blue ;'>Selamat Datang di Menu Contact Person Pelayanan</h4>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center; color: white ;'>Berikut Merupakan Data Informasi Contact Person Mengenai Pelayanan</h6>", unsafe_allow_html=True)
    st.sidebar.title("Created By Kelompok 1")
    df_contact_person =  pd.DataFrame(crud.getALLContactperson(), columns=['pelayanan', 'kontak'])
    st.table(df_contact_person)  

elif menu == 'USER':
    st.success("MENU USER")
    st.markdown("<h2 style='text-align: center; color: yellow;'>MENU USER</h2>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: blue ;'>Selamat Datang di Menu User</h4>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center; color: white ;'>Dalam menu ini anda dapat melakukan pendaftaran, perubahan (update) atau penghapusan (delete) akun dengan memilih sesuai fungsi yang diperlukan </h6>", unsafe_allow_html=True)
    st.sidebar.title("Created By Kelompok 1")
    fungsi = st.selectbox (
        "Silahkan Pilih Fungsi Pengelolaan Akun ",
        ("Daftar", "Ubah","Hapus")
    )
    if fungsi == "Daftar":
        st.text("Isi data dibawah ini secara lengkap dan sesuai untuk melakukan pendaftaran akun")
        nim = st.text_input("Masukkan NIM Anda")
        angkatan = st.text_input("Informasikan Angkatan Anda, Contoh 2019, 2020, 2021")
        nama = st.text_input("Masukkan Nama Lengkap Anda")
        email = st.text_input("Masukkan Email Resmi Anda")
        password = st.text_input("Masukkan Password Anda")
        if st.button("Daftar Akun"):
            if crud.insertDatauser(nim, angkatan, nama, email, password) and (nim != '' and angkatan != '' and nama != ''and email != ''and password != ''):
                st.success("Berhasil Melakukan Pendaftaran, Sekarang anda dapat melakukan pengaduan")
            else:
                st.error("Gagal Melakukan Pendaftaran")
                st.error("Pastikan semua informasi pendaftaran akun telah terisi dan sesuai serta pastikan NIM anda belum pernah didaftarkan, jika terjadi duplikasi data, anda dapat menghapus data pada fungsi Hapus")
            
    elif fungsi == "Ubah":
        st.text("Anda dapat mengubah salah satu atau keseluruhan informasi akun")
        nim = st.text_input("Masukkan NIM Anda")
        angkatan = st.text_input("Informasikan Angkatan Anda, Contoh 2019, 2020, 2021")
        nama = st.text_input("Masukkan Perubahan Nama Anda")
        email = st.text_input("Masukkan Perubahan Email Resmi Anda")
        password = st.text_input("Masukkan Perubahan Password Anda")
        if st.button("Perbarui Akun"):
            if crud.updateDatauser(angkatan, nama, email, password, nim) and (nim != '' and angkatan != '' and nama != ''and email != ''and password != ''):
                st.success("Berhasil Mengubah Data Akun")
            else:
                st.error("Gagal Mengubah Data AKun")
                st.error("Pastikan semua informasi perubahan akun telah terisi dan sesuai serta pastikan NIM dari akun yang anda ubah telah terdaftar")

    elif fungsi == "Hapus":
        st.text("Anda dapat menghapus akun berdasarkan NIM anda")
        nim = st.text_input("Masukkan NIM Anda")
        if st.button("Hapus Akun"):
            if crud.deleteDatauser(nim,):
                st.success("Berhasil Menghapus Data")
            else:
                st.error("Data Gagal Dihapus")
                st.error("Pastikan NIM akun yang akan dihapus telah sesuai")

elif menu == "TENTANG KAMI":
# informasi data form
    st.success("MENU TENTANG KAMI")
    st.markdown("<h1 style='text-align: center; color: yellow;'>INFORMASI TENTANG KAMI</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: blue ;'>Project Website ini Dibuat untuk Memenuhi Tugas Akhir Matakuliah Basis Data C</h4>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: white ;'>Dosen Pengampu : Bpk. Achmad Jauhari, S.T., M.Kom</h4>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center; color: white ;'>Dibuat oleh Kelompok 1 yang Beranggotakan Sebagai Berikut.</h6>", unsafe_allow_html=True)
    st.sidebar.title("Created By Kelompok 1")
    with st.columns(5)[2]:
        st.image("1.png", caption='MUCHAMMAD BISRI 220421100076', width=130)
        st.image('2.png', caption='M. ALDI ARMAN H. 220421100061', width=130)
        st.image('3.png', caption='RIFATUL AMALIYAH 220421100176', width=130)
        st.image('4.png', caption='NASHWA MAYUMI 22042110071', width=130)
        st.image('5.png', caption='DITA AMELIA 220421100165', width=130)


    
    





