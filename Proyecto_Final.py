import tkinter as tk

def datos_usuario():
    # Obtenemos los valores de los campos
    dni = dni_entry.get()
    nombres = nombres_entry.get()
    apellidos = apellidos_entry.get()
    direccion = direccion_entry.get()
    telefono = telefono_entry.get()
    pedido = pedido_entry.get("1.0", tk.END)

  # Imprimimos los valores por consola
    print("El dni es:", dni)
    print("El nombre es:", nombres)
    print("El apellido es:", apellidos)
    print("La dirrecion es :", direccion)
    print("El teléfono es:", telefono)
    print("El Pedido que hizo es:", pedido)

    # Limpiamos los campos
    dni_entry.delete(0, tk.END)
    nombres_entry.delete(0, tk.END)
    apellidos_entry.delete(0, tk.END)
    direccion_entry.delete(0, tk.END)
    telefono_entry.delete(0, tk.END)
    pedido_entry.delete("1.0", tk.END)

    # Creamos la ventana principal
root = tk.Tk()
root.title("Ferreteria El tornillo feliz")

# Creamos los campos de entrada
dni_label = tk.Label(root, text="DNI:")
dni_entry = tk.Entry(root)
nombres_label = tk.Label(root, text="Nombres:")
nombres_entry = tk.Entry(root)
apellidos_label = tk.Label(root, text="Apellidos:")
apellidos_entry = tk.Entry(root)
direccion_label = tk.Label(root, text="Dirección:")
direccion_entry = tk.Entry(root)
telefono_label = tk.Label(root, text="Teléfono:")
telefono_entry = tk.Entry(root)
pedido_label = tk.Label(root, text="Pedido:")
pedido_entry = tk.Text(root, height=5, width=30)