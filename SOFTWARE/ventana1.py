#!/bin/usr/python
#! -*- coding: 850 -*-
from tkinter import *
import os
import sys
import sqlite3 as db
import tkinter.messagebox as mensaje
from tkinter import messagebox
from time import sleep
sleep(0)
#llamar ventana2 py
def v3callback():
     os.system("python ventana3.py")
     root.destroy()
#Llamar login estadisticas
def estcallback():
    os.system("python log.py")
    root.destroy()
#ventana principal ROOT
root=Tk()
root.geometry("1350x700+0+0")
root.title("Sistema de votaci¢n de Bogot ")
lbltitulo=Label(text="Verifique sus datos a continuaci¢n",font=("Times New Roman",35)).place(x=350,y=10)

root.resizable(width=False, height=False)
#ImagenAdmin ROOT
imagen1=PhotoImage(file="empresario.gif")
lblImagen=Label(root,image=imagen1).place(x=500,y=62)
#Imagenbogota ROOT
imagen2=PhotoImage(file="bogota.gif")
lblImagen=Label(root,image=imagen2).place(x=8,y=15)
#imagenregistraduria ROOT
imagen3=PhotoImage(file="logo.png")
lblImagen=Label(root,image=imagen3).place(x=1050,y=28)
#Info datos
def sqlite(var):
 conexion = db.connect("urna.db")
 cursor = conexion.cursor()
 f = cursor.execute("SELECT *FROM USUARIOS WHERE CEDULA = '%s'"%(var))
 
 fila = f.fetchone()

 if (fila != None):
  
  # widgets 
  contenedor2 = Label(root,font=("Times new Roman",18), text = " %s"%fila[2]).place(x=730,y=400)
  contenedor3 = Label(root,font=("Times new Roman",18), text = " %s"%fila[3]).place(x=730,y=440)
  contenedor4 = Label(root,font=("Times new Roman",18), text = " %s"%fila[4]).place(x=730,y=480)
  contenedor5 = Label(root,font=("Times new Roman",18), text = " %s"%fila[5]).place(x=730,y=520)
  contenedor6 = Label(root,font=("Times new Roman",18), text = " %s"%fila[7]).place(x=730,y=560)
  
 
 else:
  mensaje.showerror("Verificaci¢n de datos", "El n£mero de documento no se encuentra registrado en el sistema")
 
#Funcion consultar 
def consultar():
 valor = var1.get().capitalize()
 sqlite(valor)

# variables
var1 = StringVar()
Pass=0
# wigets
titulo = Label(root, text = " ", anchor="n", font="verdana 10 bold").place(x=600,y=490)
etiqueta = Label(root,font=("Times new Roman",20), text = "Ingrese su Cedula").place(x=310,y=325)
entrada = Entry(root, width = 30, textvariable = var1).place(x=540,y=335)
boton = Button(root,bd=10,bg="sky blue", text="Consultar",font=("Times new Roman",15), command=consultar).place(x=830,y=315)
#fUNCION Ingreso 
def login():
 
 log = db.connect("urna.db")
 c = log.cursor()
 
 USER = var1.get()
 PASS = Pass
 
 c.execute('SELECT * FROM USUARIOS WHERE CEDULA = ? AND VOT = ?', (USER, PASS))
 
 if c.fetchall():
  os.system("python ventana3.py")
  root.destroy()
  
 else:
  messagebox.showerror(title = "Ingreso al sistema de Votaci¢n",
                       message = "N£mero de cedula incorrecto.\n Intente nuevamente")
  
 c.close()
#Datos
#InfoPnombre
v2Pnombre=Label(text="Primer Nombre",font=("Times New Roman",20)).place(x=420,y=400)
#InfoSnombre
lblsnombre=Label(text="Segundo Nombre",font=("Times New Roman",20)).place(x=420,y=440)
#Infopapellido
lblpapellido=Label(text="Primer Apellido",font=("Times New Roman",20)).place(x=420,y=480)
#InfoSapellido
lblsapellido=Label(text="Segundo Apellido",font=("Times New Roman",20)).place(x=420,y=520)
#InfoFexpedicion
lblexpedicion=Label(text="Fecha de Expedici¢n",font=("Times New Roman",20)).place(x=420,y=560)

#Funcion Cancelar
def volcallback():
    os.system("python Inicio.py")
    root.destroy()

#Boton continuar ROOT
Boton = Button (text = "Continuar", bd=10, font=("Times new Roman",18), width=10, bg="green",
        command=login).place(x=1060,y=350)

#Boton Cancelar ROOT
Button (text = "Cancelar", bd=10, font=("Times new Roman",18), width=10, bg="red",
        command=volcallback).place(x=1060,y=530)
#Boton Ingreso a estadisticas
Button (text ="Resultados", bd=10, font=("Times new Roman",18),width=10, bg="silver",
        command=estcallback).place(x=100, y=530)
 


root.mainloop()
