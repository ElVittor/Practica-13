from tkinter import messagebox
class logica:
    def __init__(self):
        self.__Usuario="Juan"
        self.__Password="1234"
    
    def Validar(self,correo,contra):
        if(correo=="" or contra ==""):
            messagebox.showwarning("Cuidado","Usuario y Constraseña deben contener algo")
        else:
            if(self.__Usuario == correo and self.__Password == contra):
                messagebox.showinfo("Exito","Bienvenido al sistema")
            else:
                messagebox.showerror("Error","Usuario y/o Constraseña incorrectos")
                