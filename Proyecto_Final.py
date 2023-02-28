import tkinter as tk

def datos_usuario():
    # Obtenemos los valores de los campos
    dni = dni_entry.get()
    nombres = nombres_entry.get()
    apellidos = apellidos_entry.get()
    direccion = direccion_entry.get()
    telefono = telefono_entry.get()
    pedido = pedido_entry.get("1.0", tk.END)

  