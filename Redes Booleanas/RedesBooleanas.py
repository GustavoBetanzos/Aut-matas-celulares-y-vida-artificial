#Betanzos Reyes Gustavo Noel
#Tarea Redes Booleanas
import tkinter as tk
from tkinter import ttk
import random

def ciclos():
    # Obtener el número de iteraciones y nodos desde las entradas de texto
    iteraciones = int(iteraciones_entry.get())
    numNodos = int(nodos_entry.get())
    
    # Definir la tabla de verdad
    tabla = {
        (0, 0, 0): 1,
        (0, 0, 1): 0,
        (0, 1, 0): 1,
        (0, 1, 1): 0,
        (1, 0, 0): 0,
        (1, 0, 1): 1,
        (1, 1, 0): 0,
        (1, 1, 1): 1
    }

    # Inicializar el texto con la tabla de verdad utilizada
    resultado_texto = f"La tabla de verdad utilizada es: {tabla}\n"

    # Realizar ciclos de cálculo
    for repetir in range(iteraciones):
        # Agregar el texto de la iteración actual
        resultado_texto += f"\nIteración número: {repetir + 1}\n"
        
        # Generar valores aleatorios para los nodos y conexiones
        nodos = [(n, random.choice([0, 1])) for n in range(numNodos)]
        conexiones = [(random.randint(0, numNodos-1), random.randint(0, numNodos-1), random.randint(0, numNodos-1)) for _ in range(numNodos)]
        valores_obtenidos = [(nodos[i][1], nodos[j][1], nodos[k][1]) for i, j, k in conexiones]

        # Mostrar valores de los nodos y conexiones
        for n in range(numNodos):
            resultado_texto += f"{nodos[n]} conectado a -> {conexiones[n]} valores -> {valores_obtenidos[n]} nuevo valor del nodo -> {tabla[valores_obtenidos[n]]}\n"

        # Actualizar los valores de los nodos según la tabla de verdad
        nodos = [(n, tabla[valores_obtenidos[n]]) for n in range(numNodos)]

    # Actualizar el contenido del widget Text
    resultado_text.config(state=tk.NORMAL)
    resultado_text.delete("1.0", tk.END)
    resultado_text.insert(tk.END, resultado_texto)
    resultado_text.config(state=tk.DISABLED)

# Crear la ventana
root = tk.Tk()
root.title("Calculadora de ciclos")
root.geometry("800x600")  # Ajustar el tamaño de la ventana

# Crear los elementos de la interfaz
tk.Label(root, text="Número de iteraciones:", font=("Arial", 14)).pack()
iteraciones_entry = tk.Entry(root, font=("Arial", 14))
iteraciones_entry.pack()

tk.Label(root, text="Número de nodos:", font=("Arial", 14)).pack()
nodos_entry = tk.Entry(root, font=("Arial", 14))
nodos_entry.pack()

calcular_button = tk.Button(root, text="Calcular", command=ciclos, font=("Arial", 14))
calcular_button.pack()

# Crear un widget Text con Scrollbar para mostrar el resultado
resultado_text = tk.Text(root, wrap=tk.WORD, width=100, height=30, font=("Arial", 12))
resultado_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20, pady=20)

scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=resultado_text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
resultado_text.config(yscrollcommand=scrollbar.set)

# Ejecutar la interfaz
root.mainloop()
