import tkinter as tk
from tkinter import messagebox
import datetime
import re


### Definición de funciones
def limpiar_campos():
    for campo in (tbNombre, tbApellidos, tbTelefono, tbEdad, tbEstatura):
        campo.delete(0, tk.END)
        campo.config(bg="white")  # quita el verde/rojo
    var_genero.set(0)


def borrar_fun():
    limpiar_campos()


### Funciones de validación (retornan True/False)
def es_texto_valido(valor):
    # letras, acentos, ñ y espacios (y que no sea solo espacios)
    return valor.strip() != "" and re.fullmatch(r"[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\s]+", valor) is not None


def es_entero_valido(valor):
    # solo dígitos (no acepta signos ni espacios)
    return re.fullmatch(r"[0-9]+", valor) is not None


def es_decimal_valido(valor):
    # acepta 1.70 o 1,70
    return re.fullmatch(r"[0-9]+([.,][0-9]+)?", valor) is not None


def es_telefono_valido(valor):
    # exactamente 10 dígitos
    return re.fullmatch(r"[0-9]{10}", valor) is not None


# MEJORA IA: rangos realistas
def es_edad_valida(valor):
    return es_entero_valido(valor) and 1 <= int(valor) <= 120


def es_estatura_valida(valor):
    return es_decimal_valido(valor) and 0.5 <= float(valor.replace(",", ".")) <= 2.5


### Retroalimentación visual
def pintar_campo(entry, valido):
    if entry.get() == "":
        entry.config(bg="white")        # vacío: color normal
    elif valido:
        entry.config(bg="lightgreen")   # correcto
    else:
        entry.config(bg="lightpink")    # incorrecto


### Manejadores de eventos (se ejecutan al escribir)
def validar_nombre_evento(event):
    pintar_campo(tbNombre, es_texto_valido(tbNombre.get()))


def validar_apellidos_evento(event):
    pintar_campo(tbApellidos, es_texto_valido(tbApellidos.get()))


def validar_telefono_evento(event):
    pintar_campo(tbTelefono, es_telefono_valido(tbTelefono.get()))


def validar_edad_evento(event):
    pintar_campo(tbEdad, es_edad_valida(tbEdad.get()))


def validar_estatura_evento(event):
    pintar_campo(tbEstatura, es_estatura_valida(tbEstatura.get()))


### Guardar
def guardar_valores():
    # Obtener valores desde los entrys
    nombres = tbNombre.get().strip()
    apellidos = tbApellidos.get().strip()
    telefono = tbTelefono.get().strip()
    edad = tbEdad.get().strip()
    estatura = tbEstatura.get().strip()

    genero = ""
    if var_genero.get() == 1:
        genero = "Hombre"
    elif var_genero.get() == 2:
        genero = "Mujer"

    # MEJORA IA: se juntan TODOS los errores en un solo mensaje
    errores = ""

    if nombres == "":
        errores += "- Falta capturar los nombres.\n"
    elif not es_texto_valido(nombres):
        errores += "- Los nombres solo pueden contener letras.\n"

    if apellidos == "":
        errores += "- Falta capturar los apellidos.\n"
    elif not es_texto_valido(apellidos):
        errores += "- Los apellidos solo pueden contener letras.\n"

    if telefono == "":
        errores += "- Falta capturar el teléfono.\n"
    elif not es_telefono_valido(telefono):
        errores += "- El teléfono debe tener exactamente 10 dígitos.\n"

    if edad == "":
        errores += "- Falta capturar la edad.\n"
    elif not es_edad_valida(edad):
        errores += "- La edad debe ser un número entero entre 1 y 120.\n"

    if estatura == "":
        errores += "- Falta capturar la estatura.\n"
    elif not es_estatura_valida(estatura):
        errores += "- La estatura debe estar entre 0.50 y 2.50 m.\n"

    if genero == "":
        errores += "- Selecciona un género.\n"

    if errores != "":
        messagebox.showwarning("Errores de validación", "Corrige lo siguiente:\n\n" + errores)
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


##Creación de ventana
ventana = tk.Tk()
ventana.geometry("520x500")
ventana.title("Formulario Vr.05.1 (IA)")
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

lbEstatura = tk.Label(ventana, text="Estatura (m):")
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

## Eventos: validar mientras se escribe
tbNombre.bind("<KeyRelease>", validar_nombre_evento)
tbApellidos.bind("<KeyRelease>", validar_apellidos_evento)
tbTelefono.bind("<KeyRelease>", validar_telefono_evento)
tbEdad.bind("<KeyRelease>", validar_edad_evento)
tbEstatura.bind("<KeyRelease>", validar_estatura_evento)

ventana.mainloop()