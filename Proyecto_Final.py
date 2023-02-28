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

# Acomodamos los campos de entrada en la ventana
dni_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
dni_entry.grid(row=0, column=1, padx=5, pady=5)
nombres_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
nombres_entry.grid(row=1, column=1, padx=5, pady=5)
apellidos_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
apellidos_entry.grid(row=2, column=1, padx=5, pady=5)
direccion_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.E)
direccion_entry.grid(row=3, column=1, padx=5, pady=5)
telefono_label.grid(row=4, column=0, padx=5, pady=5, sticky=tk.E)
telefono_entry.grid(row=4, column=1, padx=5, pady=5)
pedido_label.grid(row=5, column=0, padx=5, pady=5, sticky=tk.E)
pedido_entry.grid(row=5, column=1, padx=5, pady=5)

# Creamos el botón de envío
submit_button = tk.Button(root, text="Enviar" , command=datos_usuario) # Aqui llamamos a la funcion del "def" que creamos con la variable (datos_usario)
submit_button.grid(row=6, column=1, padx=5, pady=5, sticky=tk.E)

# Creamos el botón de impresión
print_button = tk.Button(root, text="Imprimir")
print_button.grid(row=6, column=0, padx=5, pady=5, sticky=tk.W)

