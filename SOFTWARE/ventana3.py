#!/bin/usr/python
# -*- coding: utf-8 -*-
from tkinter import *
import sqlite3
from tkinter import messagebox
import sqlite3 as db
from time import sleep
import os
import sys
sleep(0)
import winsound
#Venatan 3
ventana3=Tk()
ventana3.geometry("1350x700+0+0")
ventana3.title("Sistema de votación de Bogotá")
lblBienvenida=Label(text="Seleccione el candidato de su preferencia",font=("Times New Roman",30)).place(x=350,y=20)
lblTXT=Label(text="Recuerde que solo podra elegir un candidato.\n Por favor este seguro de su voto,\n Una vez seleccione VOTAR NO PODRA RETROCEDER.",font=("Arial",20)).place(x=320,y=120)
ventana3.resizable(width=False, height=False)
#Imagenbogota
imagenb=PhotoImage(file="bogota.gif")
lblImagen=Label(ventana3,image=imagenb).place(x=8,y=15)
#imagenregistraduria
imagenr=PhotoImage(file="logo.png")
lblImagen=Label(ventana3,image=imagenr).place(x=1050,y=28)

#FUNCION VOTO1
def vot1callback():
    winsound.PlaySound("gr.wav", winsound.SND_FILENAME)
    os.system("python votoc1.py")
    messagebox.showinfo(title = "Sistema de votación de Bogotá",
                       message = "Su voto ha sido registrado")
    ventana3.destroy()
    os.system("python Inicio.py")
#FUNCION VOTO2
def vot2callback():
    winsound.PlaySound("gr.wav", winsound.SND_FILENAME)
    os.system("python votoc2.py")
    messagebox.showinfo(title = "Sistema de votación de Bogotá",
                       message = "Su voto ha sido registrado")
    
    ventana3.destroy()
    os.system("python Inicio.py")
#FUNCION VOTO3
def vot3callback():
    winsound.PlaySound("gr.wav", winsound.SND_FILENAME)
    os.system("python votoc3.py")
    messagebox.showinfo(title = "Sistema de votación de Bogotá",
                       message = "Su voto ha sido registrado")
    ventana3.destroy()
    os.system("python Inicio.py")
#FUNCION VOTO4
def vot4callback():
    winsound.PlaySound("gr.wav", winsound.SND_FILENAME)
    os.system("python votoc4.py")
    messagebox.showinfo(title = "Sistema de votación de Bogotá",
                       message = "Su voto ha sido registrado")
    ventana3.destroy()
    os.system("python Inicio.py")
#FUNCION VOTO5
def vot5callback():
    winsound.PlaySound("gr.wav", winsound.SND_FILENAME)
    os.system("python votoc5.py")
    messagebox.showinfo(title = "Sistema de votación de Bogotá",
                       message = "Su voto ha sido registrado")
    ventana3.destroy()
    os.system("python Inicio.py")
    #FUNCION VOTO5
def vot6callback():
    winsound.PlaySound("gr.wav", winsound.SND_FILENAME)
    os.system("python votoc6.py")
    messagebox.showinfo(title = "Sistema de votación de Bogotá",
                       message = "Su voto ha sido registrado")
    ventana3.destroy()
    os.system("python Inicio.py")
#ImagenCand1
imagen1=PhotoImage(file="clara.png")
lblImagen=Label(ventana3,image=imagen1).place(x=30,y=250)
lblClara=Label(text="Clara López",font=("Times New Roman",20)).place(x=55,y=450)
btnVC=Button(ventana3,text="VOTAR",command=vot1callback, bd=10, bg="sky blue",font=("Times new Roman",18),width=10).place(x=53,y=530)
#ImagenCand2
imagen2=PhotoImage(file="pardo.png")
lblImagen=Label(ventana3,image=imagen2).place(x=250,y=250)
lblrafa=Label(text="Rafael Pardo",font=("Times New Roman",20)).place(x=280,y=450)
btnVR=Button(ventana3,text="VOTAR",command=vot2callback, bd=10,bg="sky blue",font=("Times new Roman",18),width=10).place(x=280,y=530)
#ImagenCand3
imagen3=PhotoImage(file="santos.png")
lblImagen=Label(ventana3,image=imagen3).place(x=475,y=250)
lblfran=Label(text="Francisco Santos",font=("Times New Roman",20)).place(x=490,y=450)
btnVF=Button(ventana3,text="VOTAR",command=vot3callback, bd=10,bg="sky blue",font=("Times new Roman",18),width=10).place(x=505,y=530)
#ImagenCand4
imagen4=PhotoImage(file="Enrique.png")
lblImagen=Label(ventana3,image=imagen4).place(x=698,y=250)
lblfran=Label(text="Enrique Peñalosa",font=("Times New Roman",20)).place(x=700,y=450)
btnVE=Button(ventana3,text="VOTAR",command=vot4callback, bd=10,bg="sky blue",font=("Times new Roman",18),width=10).place(x=720,y=530)
#ImagenCand5
imagen5=PhotoImage(file="mercedes.png")
lblImagen=Label(ventana3,image=imagen5).place(x=906,y=250)
lblfran=Label(text="Mercedes Maldonado",font=("Times New Roman",20)).place(x=900,y=450)
btnVM=Button(ventana3,text="VOTAR",command=vot5callback, bd=10,bg="sky blue",font=("Times new Roman",18),width=10).place(x=923,y=530)
#ImagenBLANCO
imagen6=PhotoImage(file="blanco.png")
lblImagen=Label(ventana3,image=imagen6).place(x=1130,y=250)
lblblan=Label(text="Voto en Blanco",font=("Times New Roman",20)).place(x=1150,y=450)
btnVM=Button(ventana3,text="VOTAR",command=vot6callback, bd=10,bg="sky blue",font=("Times new Roman",18),width=10).place(x=1150,y=530)



ventana3.mainloop()
