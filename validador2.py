import re
import tkinter as tk
from tkinter import ttk, messagebox, END

regex = r"^(?=.*[A-Z])(?=.*[!@#$%&.*]).{8,}$"

root = tk.Tk()
root.title("Validador de contraseñas")
root.geometry("600x400")
icono = tk.PhotoImage(file = "logo.png")
root.iconphoto(True, icono)
root.configure(bg = "light grey")


titulo = tk.Label(root, text= "Valida que tan segura es tu contraseña")
titulo.config(bg= "light grey", font= ("Times New Roman", 16, "bold"))
titulo.place(x = 125, y = 60)

contraseña = tk.Entry(root, bg="white", font=("Arial",11))
contraseña.place(x=215, y=150)

contraseña.insert(0, "Introduce tu contraseña")
contraseña.config(fg="gray")

def entrar(event):
    if contraseña.get() == "Introduce tu contraseña":
        contraseña.delete(0, END)
        contraseña.config(fg="black")

def salir(event):
    if contraseña.get() == "":
        contraseña.insert(0, "Introduce tu contraseña")
        contraseña.config(fg="gray", show="")

contraseña.bind("<FocusIn>", entrar)
contraseña.bind("<FocusOut>", salir)

def validar(password):
    if contraseña.get() == "Introduce tu contraseña" or contraseña.get() == "":
        messagebox.showwarning("Advertencia", "Por favor, introduce una contraseña.")
        return False
    else:
        return bool(re.match(regex, password))

boton_verificador = tk.Button(root, text="Verificar", command=lambda: messagebox.showinfo("Resultado", "Contraseña segura" if validar(contraseña.get()) else "Contraseña insegura"))
boton_verificador.config(fg="white", bg="green", font=("Arial", 12))
boton_verificador.place(x = 260, y = 200)

root.mainloop()