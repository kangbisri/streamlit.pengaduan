import mysql.connector
import streamlit as st

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="pengaduan"
    )
    cursor = mydb.cursor()
    mydb.commit()
except Exception as e:
   st.error("Gagal terhubung ke database")

