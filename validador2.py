import re
import tkinter as tk
from tkinter import ttk, messagebox, END

regex = r"^(?=.*[A-Z])(?=.*[!@#$%&.*]).{8,}$"

root = tk.Tk()
root.title("Validador de contraseñas")
root.geometry("600x400")
root.resizable(False, False)

icono = tk.PhotoImage(file="logo.png")
root.iconphoto(True, icono)

# Fondo principal
root.configure(bg="#EAF0F6")

# Marco principal
frame = tk.Frame(root, bg="white", bd=2, relief="groove")
frame.place(x=60, y=40, width=480, height=310)

titulo = tk.Label(
    frame,
    text="Valida que tan segura es tu contraseña"
)
titulo.config(
    bg="white",
    fg="#1F3C88",
    font=("Segoe UI", 16, "bold")
)
titulo.place(x=45, y=30)

subtitulo = tk.Label(
    frame,
    text="Ingresa una contraseña para analizar su seguridad",
    bg="white",
    fg="gray",
    font=("Segoe UI", 10)
)
subtitulo.place(x=95, y=70)

contraseña = tk.Entry(
    frame,
    bg="#F8F9FA",
    font=("Arial", 11),
    relief="solid",
    bd=1,
    justify="center"
)
contraseña.place(x=115, y=125, width=250, height=32)

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
        contraseña.delete(0, END)
        return bool(re.match(regex, password))

boton_verificador = tk.Button(
    frame,
    text="Verificar",
    command=lambda: messagebox.showinfo(
        "Resultado",
        "Tu contraseña es segura" if validar(contraseña.get())
        else "Contraseña insegura. Debe contener al menos: \n"
             "1. 8 caracteres\n"
             "2. Una mayuscula\n"
             "3. Un digito\n"
             "4. Un simbolo\n"
             "\nSigue el ejemplo: Hola123@"
    )
)
boton_verificador.config(
    fg="white",
    bg="#1F6FEB",
    activebackground="#174EA6",
    activeforeground="white",
    font=("Arial", 12, "bold"),
    relief="flat",
    cursor="hand2"
)
boton_verificador.place(x=180, y=190, width=120, height=38)

footer = tk.Label(
    frame,
    text="Protege tus cuentas con contraseñas seguras",
    bg="white",
    fg="gray",
    font=("Segoe UI", 9, "italic")
)
footer.place(x=115, y=255)

root.mainloop()