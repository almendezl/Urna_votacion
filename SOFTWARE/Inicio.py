#!/bin/usr/python
# -*- coding: utf-8 -*-
from tkinter import *
import os
import sys
from time import sleep
sleep(0)
#Ventana 2
inicio=Tk()
inicio.geometry("1350x700+0+0")
inicio.title("Sistema de votación de Bogotá")
lbltitulo=Label(text="Bienvenido al sistema de votación de Bogotá",font=("Times New Roman",35)).place(x=250,y=0)
inicio.resizable(width=False, height=False)
#Llamar ventana 1
def v1callback():
     os.system('python ventana1.py')
     inicio.destroy()
#Imagenbogota ROOT
imagen2=PhotoImage(file="18.png")
lblImagen=Label(inicio,image=imagen2).place(x=30,y=45)
#imagenregistraduria ROOT
imagen3=PhotoImage(file="13.png")
lblImagen=Label(inicio,image=imagen3).place(x=1130,y=28)
#Imagen Bogota
imagenb=PhotoImage(file="bogo.gif")
lblImagenb=Label(inicio,image=imagenb).place(x=240,y=58)
#Imagen cedula
imagenc=PhotoImage(file="ced.gif")
lblImagenc=Label(inicio,image=imagenc).place(x=50,y=450)
#Botoncontinuar
btniniciar=Button(inicio,text="Iniciar el proceso de votación",command=v1callback,bg="sky blue",
                  bd=10,font=("Times new Roman",20),width=30).place(x=430,y=620)
#Nota
lblnota=Label(text="Estimado usuario recuerde tener a mano su Cedula de Ciudadania, leer \n y seguir atentamente las indicaciones para que el proceso sea exitoso.",
              font=("Arial",20)).place(x=340,y=450)

lblnota=Label(text="Agradecemos su colaboración",
              font=("Arial",20)).place(x=340,y=560)
def quit():
    inicio.destroy()
#Boton salir
Button (text = "Cancelar", bd=10, font=("Times new Roman",18), width=10, bg="red",
        command=quit).place(x=1060,y=620)

 
inicio.mainloop()
