## 3MLIDTS-CarlosSolar-05Python
### Formulario de registro
## almacenamiento en TXT con validación de entradas
import tkinter as tk
from tkinter import messagebox
import datetime
import re

### Definición de funciones
def limpiar_campos():
    tbNombre.delete(0, tk.END)
    tbApellidos.delete(0, tk.END)
    tbEdad.delete(0, tk.END)
    tbEstatura.delete(0, tk.END)
    tbTelefono.delete(0, tk.END)
    var_genero.set(0)

def borrar_fun():
    limpiar_campos()

### Funciones de validación
def es_entero_valido(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False

def es_decimal_valido(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

def es_telefono_valido(valor):
    return valor.isdigit() and len(valor) == 10

def es_texto_valido(valor):
    # letras, acentos, ñ y espacios
    return bool(re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$", valor))

def guardar_valores():
    # Obtener valores desde los entrys
    nombres = tbNombre.get().strip()
    apellidos = tbApellidos.get().strip()
    edad = tbEdad.get().strip()
    estatura = tbEstatura.get().strip()
    telefono = tbTelefono.get().strip()

    # Validación de campos vacíos
    if nombres == "" or apellidos == "" or edad == "" or estatura == "" or telefono == "":
        messagebox.showwarning("Datos incompletos", "Por favor completa todos los campos.")
        return

    # Validación de nombre y apellidos
    if not es_texto_valido(nombres):
        messagebox.showerror("Error Nombre", "El nombre solo debe contener letras.")
        return

    if not es_texto_valido(apellidos):
        messagebox.showerror("Error Apellidos", "Los apellidos solo deben contener letras.")
        return

    # Validación de edad
    if not es_entero_valido(edad) or int(edad) <= 0:
        messagebox.showerror("Error Edad", "La edad debe ser un número entero mayor a 0.")
        return

    # Validación de estatura
    if not es_decimal_valido(estatura) or float(estatura) <= 0:
        messagebox.showerror("Error Estatura", "La estatura debe ser un número mayor a 0.")
        return

    # Validación de teléfono
    if not es_telefono_valido(telefono):
        messagebox.showerror("Error Teléfono", "El teléfono debe tener exactamente 10 dígitos.")
        return

    # Validación de género
    genero = ""
    if var_genero.get() == 1:
        genero = "Hombre"
    elif var_genero.get() == 2:
        genero = "Mujer"
    else:
        messagebox.showwarning("Dato faltante", "Selecciona un género.")
        return

    fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    datos = ("Fecha: " + fecha_hora + "\n" +
             "Nombres: " + nombres + "\n" +
             "Apellidos: " + apellidos + "\n" +
             "Edad: " + edad + "\n" +
             "Estatura: " + estatura + "\n" +
             "Teléfono: " + telefono + "\n" +
             "Género: " + genero)

    # Guardar en TXT
    with open("datos.txt", "a", encoding="utf-8") as archivo:
        archivo.write(datos + "\n\n")

    messagebox.showinfo("Datos guardados", datos)

    # Limpiar después de guardar
    limpiar_campos()

##Creación de Ventana
ventana = tk.Tk()
ventana.geometry("520x500")
ventana.title("Formulario Vr.05")
var_genero = tk.IntVar()

## Etiquetas y campos de entrada
lbNombre = tk.Label(ventana, text="Nombres:")
lbNombre.pack()
tbNombre = tk.Entry(ventana)
tbNombre.pack()
lbApellidos = tk.Label(ventana, text="Apellidos:")
lbApellidos.pack()
tbApellidos = tk.Entry(ventana)
tbApellidos.pack()
lbTelefono = tk.Label(ventana, text="Teléfono (10 dígitos):")
lbTelefono.pack()
tbTelefono = tk.Entry(ventana)
tbTelefono.pack()
lbEdad = tk.Label(ventana, text="Edad:")
lbEdad.pack()
tbEdad = tk.Entry(ventana)
tbEdad.pack()
lbEstatura = tk.Label(ventana, text="Estatura (cm):")
lbEstatura.pack()
tbEstatura = tk.Entry(ventana)
tbEstatura.pack()
lbGenero = tk.Label(ventana, text="Género")
lbGenero.pack()
rbHombre = tk.Radiobutton(ventana, text="Hombre", variable=var_genero, value=1)
rbHombre.pack()
rbMujer = tk.Radiobutton(ventana, text="Mujer", variable=var_genero, value=2)
rbMujer.pack()

## Botones
btnBorrar = tk.Button(ventana, text="Borrar valores", command=borrar_fun)
btnBorrar.pack()
btnGuardar = tk.Button(ventana, text="Guardar", command=guardar_valores)
btnGuardar.pack()

ventana.mainloop()