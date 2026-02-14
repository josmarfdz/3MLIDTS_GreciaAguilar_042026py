import tkinter as tk
from tkinter import Radiobutton, Variable, font
from tkinter.tix import Form


ventana = tk.Tk()
ventana.configure(bg="dimgray")
ventana.geometry("350x500")
ventana.title("Actividad 04 - Formulario de Registro Vr 001")
rbSeleccioGenero = tk.StringVar(value="")

tk.Label(ventana, text="Nombre: ", font=("Arial", 14, "bold")).pack()
tbNombre = tk.Entry(ventana, width=35, justify="center")
tbNombre.pack()
tk.Label(ventana, text="Apellidos: ", font=("Arial", 14, "bold")).pack()
tbApellidos = tk.Entry(ventana, width=35, justify="center")
tbApellidos.pack()
tk.Label(ventana, text="Edad: ", font=("Arial", 14, "bold")).pack()
tbEdad = tk.Entry(ventana, width=35, justify="center")
tbEdad.pack()
tk.Label(ventana, text="Estatura: ", font=("Arial", 14, "bold")).pack()
tbEstatura = tk.Entry(ventana, width=35, justify="center")
tbEstatura.pack()
tk.Label(ventana, text="Telefono: ", font=("Arial", 14, "bold")).pack()
tbTelefono = tk.Entry(ventana, width=35, justify="center")
tbTelefono.pack()

generoBox = tk.LabelFrame(ventana, text = "Seleccione Genero")
generoBox.pack()
rbMasculino = tk.Radiobutton(generoBox, text = "Masculino", value="Masculino", variable=rbSeleccioGenero)
rbMasculino.grid(column=1, row=1)
rbFemenino = tk.Radiobutton(generoBox, text = "Femenino", value="Femenino", variable=rbSeleccioGenero)
rbFemenino.grid(column=2, row=1)
rbNoDefinido = tk.Radiobutton(generoBox, text = "NoDefinido", value="NoDefinido", variable=rbSeleccioGenero)
rbNoDefinido.grid(column=3, row=1)

ventana.mainloop()