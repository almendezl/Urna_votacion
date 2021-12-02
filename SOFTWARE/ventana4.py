#!/bin/usr/python
# -*- coding: utf-8 -*-
from tkinter import *
import sqlite3 as db
import os
import sys
import tkinter.messagebox as mensaje
from time import sleep
sleep(0)
ventana4=Tk()
ventana4.geometry("1350x700+0+0")
ventana4.title("Sistema de votación de Bogotá")
lblBienvenida=Label(text="Resultados de votación",font=("Times New Roman",30)).place(x=500,y=100)
ventana4.resizable(width=False, height=False)
#Imagenbogota
imagenb=PhotoImage(file="bogota.gif")
lblImagen=Label(ventana4,image=imagenb).place(x=8,y=15)
#ImagenOk
imagen12=PhotoImage(file="oki.png")
v2Imagen=Label(ventana4,image=imagen12).place(x=300,y=60)
#imagenregistraduria
imagenr=PhotoImage(file="logo.png")
lblImagen=Label(ventana4,image=imagenr).place(x=1050,y=28)
#ImagenCand1
imagen1=PhotoImage(file="clara.png")
lblImagen=Label(ventana4,image=imagen1).place(x=30,y=250)
#ImagenCand2
imagen2=PhotoImage(file="pardo.png")
lblImagen=Label(ventana4,image=imagen2).place(x=250,y=250)
#ImagenCand3
imagen3=PhotoImage(file="santos.png")
lblImagen=Label(ventana4,image=imagen3).place(x=475,y=250)
#ImagenCand4
imagen4=PhotoImage(file="Enrique.png")
lblImagen=Label(ventana4,image=imagen4).place(x=698,y=250)
#ImagenCand5
imagen5=PhotoImage(file="mercedes.png")
lblImagen=Label(ventana4,image=imagen5).place(x=906,y=250)
#ImagenBLANCO
imagen6=PhotoImage(file="blanco.png")
lblImagen=Label(ventana4,image=imagen6).place(x=1130,y=250)
#Funcion salir
def quit():
    ventana4.destroy()
#Info datos
def sqlite(var):
 conexion = db.connect("urna.db")
 cursor = conexion.cursor()
 f = cursor.execute("SELECT *FROM VOTOS WHERE ID = '%s'"%(var))
 fila = f.fetchone()
 
 if (fila != None):
  
  # widgets 
  contenedor1 = Label(ventana4,font=("Times new Roman",18), text = " %s"%fila[1]).place(x=100,y=460)
  contenedor2 = Label(ventana4,font=("Times new Roman",18), text = " %s"%fila[2]).place(x=330,y=460)
  contenedor3 = Label(ventana4,font=("Times new Roman",18), text = " %s"%fila[3]).place(x=550,y=460)
  contenedor4 = Label(ventana4,font=("Times new Roman",18), text = " %s"%fila[4]).place(x=750,y=460)
  contenedor5 = Label(ventana4,font=("Times new Roman",18), text = " %s"%fila[5]).place(x=1000,y=460)
  contenedor6 = Label(ventana4,font=("Times new Roman",18), text = " %s"%fila[6]).place(x=1220,y=460)
 
 else:
  mensaje.showerror("Verificación de datos", "Usted no se encuentra en el sistema")
 
 
def consultar():
 valor = var1
 sqlite(valor)


# variables

var1 = 1

# wigets
titulo = Label(ventana4, text = " ", anchor="n", font="verdana 10 bold").place(x=600,y=490)
boton = Button(ventana4,bd=10,bg="sky blue", text="Consultar",font=("Times new Roman",20), command=consultar).place(x=550,y=530)
#llamar ventanaINICIO py
def v1callback():
     os.system("python Inicio.py")
     ventana4.destroy()
#Datos
#Info1
v2Pnombre=Label(text="Clara López",font=("Times New Roman",20)).place(x=50,y=430)
#Info2
lblsnombre=Label(text="Rafael Pardo",font=("Times New Roman",20)).place(x=280,y=430)
#Info3
lblpapellido=Label(text="Francisco Santos",font=("Times New Roman",20)).place(x=470,y=430)
#Info4
lblsapellido=Label(text="Enrique Peñalosa",font=("Times New Roman",20)).place(x=680,y=430)
#Info5
lblexpedicion=Label(text="Mercedes Maldonado",font=("Times New Roman",20)).place(x=890,y=430)
#info6
lblblan=Label(text="Voto en Blanco",font=("Times New Roman",20)).place(x=1150,y=430)
#Boton salir
Button (text = "Salir", bd=10, font=("Times new Roman",18), width=10, bg="red",
        command=v1callback).place(x=1060,y=530)
ventana4.mainloop()
