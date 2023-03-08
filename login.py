from tkinter import *
from logica import *
import tkinter as tk

class login:
    def __init__(self):
        axc=logica()
        def ejecutaVal():
            axc.Validar(self.__var1.get(),self.__var2.get())
        self.__Ventana=Tk()
        self.__Ventana.title("Login")
        self.__Ventana.geometry("300x150")
        
        self.__section1=Frame(self.__Ventana)
        self.__section1.pack(expand=True,fill="both")
        
        self.__titulo=Label(self.__section1,text="Login",bg="black",fg="white",font=("Arial",12)).pack()
        
        self.__var1=tk.StringVar()
        self.__lblUsuario=Label(self.__section1,text="Usuario").pack()
        self.__txtUsusario=Entry(self.__section1,textvariable=self.__var1,takefocus=True).pack()
        
        self.__var2=tk.StringVar()
        self.__lblUsuario=Label(self.__section1,text="Contraseña").pack()
        self.__txtUsusario=Entry(self.__section1,show="**",textvariable=self.__var2).pack()
        
        self.__btnAceso=Button(self.__section1,text="Acceder",bg="green",command=ejecutaVal)
        self.__btnAceso.pack()
        
        self.__Ventana.mainloop()
        
    