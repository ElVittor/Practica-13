import random
import string
from tkinter import messagebox
class generador():
    def __init__(self,longitud,mayusculas,especiales,numeros,contraseña,seguridad):
        self.longitud=longitud
        self.mayusculas=mayusculas
        self.especiales=especiales
        self.numeros=numeros
        self.contraseña=contraseña
        self.seguridad=seguridad
        
    def generar(self):
        tamaño=int(self.longitud.get())
        mayus=self.mayusculas.get()
        especial = self.especiales.get()
        numer=self.numeros.get()
        caracteres = string.ascii_lowercase
        if mayus:
           caracteres += string.ascii_uppercase
        if especial:
            caracteres+=string.punctuation
        if numer:
            caracteres+=string.digits
        Password=''.join(random.choice(caracteres)for i in range(tamaño))
        self.contraseña.set(Password)
        messagebox.showinfo("Contraseña","La contraseña generada es: " + Password)
        
        score = 0
        if any(c.isupper() for c in Password):
            score += 1
        if any(c.islower() for c in Password):
            score += 1
        if any(c.isdigit() for c in Password):
            score += 1
        if any(c in string.punctuation for c in Password):
            score += 2
        if tamaño >= 12:
            score += 1
        if score == 1:
            SeguridadMostrar="Seguridad inexistente"
        elif score == 2:
            SeguridadMostrar="Seguridad minima"
        elif score == 3:
            SeguridadMostrar="Seguridad media"
        elif score == 4:
            SeguridadMostrar="Seguridad aceptable"
        elif score <= 5:
            SeguridadMostrar="Seguridad Máxima"
        self.seguridad.set(SeguridadMostrar)
    
    """
    #creamos una base de letras a usar
    minusculas="abcdefghijklmnñopqrstuvwxyz"
    mayus=minusculas.upper()
    numeros="0123456789"
    simbolos=",.-{}+¿'=!°|%&/()?¡*][_:<>"
    minimo=minusculas+mayus
    medio=minimo+numeros
    maximo=medio+simbolos
    #tamaño de la clave
    longitud=12

    #el generador usando rab¿ndom, primero los caracteres a usar y finalmente la longitud deseada
    muestra=random.sample(minusculas,longitud)
    password="".join(muestra)
    
"""