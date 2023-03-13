from tkinter import *

import tkinter as tk
from generador import *

ventana = tk.Tk()

ventana.title("Generador de contraseñas")

longitud=tk.Label(ventana,text="longitud del password: ")
longitud.pack()
longitudcontra=tk.StringVar(value=8)
longitud1=tk.Entry(ventana, textvariable=longitudcontra)
longitud1.pack()

mayus=tk.BooleanVar()
Mayusbtn=tk.Checkbutton(ventana,text="¿Incluir Mayusculas?",variable=mayus)
Mayusbtn.pack()

especiales=tk.BooleanVar()
btnespeciales=tk.Checkbutton(ventana,text="¿incluir caracteres especiales?",variable=especiales)
btnespeciales.pack()

numeros=tk.BooleanVar()
btnnumeros=tk.Checkbutton(ventana,text="¿Incluir números?")
btnnumeros.pack()

Contraseña=StringVar()
contragenerada=tk.Entry(ventana,textvariable=Contraseña)
contragenerada.pack()

seguridad = tk.IntVar()
seguridadetiq = tk.Label(ventana, text="Nivel de seguridad: ")
seguridadetiq.pack()
fortaleza = tk.Label(ventana, textvariable=seguridad)
fortaleza.pack()

generador = generador(longitud1, mayus, especiales, numeros,Contraseña, seguridad)
generar = tk.Button(ventana, text="Generar contraseña", command=generador.generar)
generar.pack()
ventana.mainloop()




