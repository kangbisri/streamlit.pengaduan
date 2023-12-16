import koneksidatabase as db
import mysql.connector
import streamlit as st

def getALLDatamahasiswa():
    sql = "SELECT * FROM data_mahasiswa"
    db.cursor.execute(sql)
    data  = db.cursor.fetchall()
    return data

def getALLContactperson():
    sql = "SELECT * FROM kontak_pelayanan"
    db.cursor.execute(sql)
    data  = db.cursor.fetchall()
    return data


def insertDatapengaduan_dosen(tanggal, nim, jenis_pengaduan, matakuliah, kelas, keluhan):
    try:
        
        sql = "INSERT INTO pengaduan_dosen (tanggal, nim, jenis_pengaduan, matakuliah, kelas, keluhan) VALUES (%s, %s, %s, %s, %s, %s)"
        value  = (tanggal, nim, jenis_pengaduan, matakuliah, kelas, keluhan)
        db.cursor.execute(sql, value)
        db.mydb.commit()
        return True
    except Exception as e:
        return False
    
def insertDatapengaduan_fasilitas(tanggal, nim, letak, objek_fasilitas, kondisi):
    try:
        
        sql = "INSERT INTO pengaduan_fasilitas (tanggal, nim, letak, objek_fasilitas, kondisi) VALUES (%s, %s, %s, %s, %s)"
        value  = (tanggal, nim, letak, objek_fasilitas, kondisi)
        db.cursor.execute(sql, value)
        db.mydb.commit()
        return True
    except Exception as e:
        return False
    
def insertDatapengaduan_pelayanan(tanggal, nim, objek_pengaduan, objek_pelayanan, keluhan):
    try:
        
        sql = "INSERT INTO pengaduan_pelayanan(tanggal, nim, objek_pengaduan, objek_pelayanan, keluhan) VALUES (%s, %s, %s, %s, %s)"
        value  = (tanggal, nim, objek_pengaduan, objek_pelayanan, keluhan)
        db.cursor.execute(sql, value)
        db.mydb.commit()
        return True
    except Exception as e:
        return False


def insertDatauser(nim, angkatan, nama, email, password):
    try:
        
        sql = "INSERT INTO user (nim, angkatan, nama, email, password) VALUES (%s, %s, %s, %s, %s)"
        value  = (nim, angkatan, nama, email, password)
        db.cursor.execute(sql, value)
        db.mydb.commit()
        return True
    except Exception as e:
        return False
    
def updateDatauser(angkatan, nama, email, password, nim):
    try:
        
        sql = "update user set angkatan=%s, nama=%s, email=%s, password=%s where nim=%s"
        value  = (angkatan, nama, email, password, nim)
        db.cursor.execute(sql, value)
        db.mydb.commit()
        return True
    except Exception as e:
        return False

def deleteDatauser(nim, ):
    try:
        
        sql = "delete from user where nim=%s"
        value  = (nim,)
        db.cursor.execute(sql, value)
        db.mydb.commit()
        return True
    except Exception as e:
        return False
    
   
