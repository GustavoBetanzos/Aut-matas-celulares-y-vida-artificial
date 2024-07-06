#Betanzos Reyes Gustavo Noel
#Tarea Automatas1D 
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib.pyplot as plt

# Función para generar la regla de Wolfram
def generacion(numeroRegla):
    reglaBinaria = format(numeroRegla, '08b')
    regla = {tuple(map(int, format(i, '03b'))): int(reglaBinaria[7 - i]) for i in range(8)}
    return regla

# Función para evolucionar el autómata celular
def evolucion(numeroRegla, numeroGeneracion):
    regla = generacion(numeroRegla)
    ancho = numeroGeneracion * 2 + 1
    matriz = np.zeros((numeroGeneracion, ancho), dtype=bool)
    matriz[0, numeroGeneracion] = True

    for i in range(1, numeroGeneracion):
        for j in range(1, ancho - 1):
            izq, cent, der = matriz[i - 1, j - 1], matriz[i - 1, j], matriz[i - 1, j + 1]
            matriz[i, j] = regla[(izq, cent, der)]

    return matriz

# Función para imprimir la evolución en un gráfico
def imprimir(numeroRegla, numeroGeneracion):
    evo = evolucion(numeroRegla, numeroGeneracion)
    plt.imshow(evo, cmap='binary')
    plt.title(f'Regla {numeroRegla}')
    plt.axis('off')
    plt.show()

# Función para manejar el evento de clic en el botón "Generar"
def on_submit():
    numeroRegla = int(regla_entry.get())
    numeroGeneracion = int(generacion_entry.get())
    imprimir(numeroRegla, numeroGeneracion)

# Crear la ventana principal
root = tk.Tk()
root.title("Automata Celular")

# Configurar el tamaño de la ventana
root.geometry("600x400")

# Configurar el tamaño de la fuente
font_style = ("Arial", 16)

# Crear y posicionar los widgets
regla_label = ttk.Label(root, text="Regla de Wolfram (0-255):", font=font_style)
regla_label.pack()

regla_entry = ttk.Entry(root, font=font_style)
regla_entry.pack()

generacion_label = ttk.Label(root, text="Número de generaciones:", font=font_style)
generacion_label.pack()

generacion_entry = ttk.Entry(root, font=font_style)
generacion_entry.pack()

submit_button = ttk.Button(root, text="Generar", command=on_submit, style="TButton", width=20)
submit_button.pack(pady=10)

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()
