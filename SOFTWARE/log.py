#!/bin/usr/python
# -*- coding: utf-8 -*-
from tkinter import *
import sqlite3
from tkinter import messagebox
import os
import sys
from time import sleep
sleep(0)
     
#ventana log
log=Tk()
log.geometry("1350x700+0+0")
log.title("Sistema de votación de Bogotá")
lblBienvenida=Label(text="Inicie sesion para ver los resultados",
font=("Times New Roman",30)).place(x=300,y=20)
log.resizable(width=False, height=False)
#ImagenAdmin 
imagen1=PhotoImage(file="seguridad.gif")
lblImagen=Label(log,image=imagen1).place(x=500,y=100)
#Imagenbogota 
imagen2=PhotoImage(file="bogota.gif")
lblImagen=Label(log,image=imagen2).place(x=0,y=0)
#imagenregistraduria 
imagen3=PhotoImage(file="logo.png")
lblImagen=Label(log,image=imagen3).place(x=1050,y=28)
#CampoUser 
lblUser=Label(text="Ingrese su Usuario:",
                font=("Times New Roman",20)).place(x=290,y=400)
User=StringVar()
txtUser=Entry(log,textvariable=User,width=30).place(x=530,y=410)
#Campo Pass
lblPass=Label(text="Contrasena:",font=("Times New Roman",20)).place(x=290,y=450)
Pass=StringVar()
txtPass = Entry(log,textvariable=Pass,
                     show = "*",width=30).place(x=530,y=460)

#Conexion base de datos
def login():
 
 db = sqlite3.connect('urna.db')
 c = db.cursor()
 
 USER = User.get()
 PASS = Pass.get()
 
 c.execute('SELECT * FROM ADMIN WHERE USER = ? AND PASS = ?', (USER, PASS))
 
 if c.fetchall():
  os.system("python ventana4.py")
  log.destroy()
  
 else:
  messagebox.showerror(title = "Ingreso al sistema de resultados",
                       message = "Usuario o contraseña incorrecta.\n Intentelo nuevamente")
  
 c.close()
#Funcion cancelar
def cancallback():
    os.system("python Inicio.py")
    log.destroy()
#Funcion regresar
def volcallback():
    os.system("python ventana1.py")
    log.destroy()
#Boton de ingreso
Button (text = "Ingresar", bd=10, bg="sky blue", font=("Times new Roman",18), width=10,
        command = login).place(x=780,y=410)
#Boton Cancelar
Button (text = "Cancelar", bd=10, font=("Times new Roman",18), width=10, bg="red",
        command=cancallback).place(x=550,y=550)
#Boton Volver
Button (text = "Regresar", bd=10, font=("Times new Roman",18), width=10, bg="yellow",
        command=volcallback).place(x=180,y=550)

log.mainloop()
