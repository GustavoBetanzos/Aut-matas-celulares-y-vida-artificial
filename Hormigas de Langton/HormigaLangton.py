#Betanzos Reyes Gustavo Noel
#Tarea Hormiga de Langton 
import tkinter as tk
from tkinter import simpledialog
import matplotlib.pyplot as plt
import numpy as np

# Definir la clase Hormiga
class HormigaDeLangton:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.grid = np.zeros((grid_size, grid_size), dtype=int)
        self.x = grid_size // 2
        self.y = grid_size // 2
        self.direccion = 0  # 0: arriba, 1: derecha, 2: abajo, 3: izquierda

    def mover(self):
        # Gira y cambia el color de la celda
        if self.grid[self.x, self.y] == 0:
            self.direccion = (self.direccion + 1) % 4  # Gira a la derecha
            self.grid[self.x, self.y] = 1  # Cambia el color de la celda a negro
        else:
            self.direccion = (self.direccion - 1) % 4  # Gira a la izquierda
            self.grid[self.x, self.y] = 0  # Cambia el color de la celda a blanco

        # Mover la hormiga a la siguiente celda
        if self.direccion == 0:
            self.x -= 1
        elif self.direccion == 1:
            self.y += 1
        elif self.direccion == 2:
            self.x += 1
        elif self.direccion == 3:
            self.y -= 1

        # Asegurarse de que la hormiga se quede dentro de los límites
        self.x %= self.grid_size
        self.y %= self.grid_size

    def ejecutar(self, pasos):
        for _ in range(pasos):
            self.mover()

# Función para iniciar la simulación
def iniciar_simulacion():
    # Crear una nueva ventana para la entrada del usuario
    input_window = tk.Toplevel(root)
    input_window.title("Input")

    # Configurar el tamaño de la ventana
    input_window.geometry("400x200")
    
    # Configurar la fuente para los textos y entradas
    font = ("Helvetica", 16)

    # Etiqueta y entrada para el número de pasos
    tk.Label(input_window, text="Número de pasos:", font=font).pack(pady=20)
    pasos_entry = tk.Entry(input_window, font=font)
    pasos_entry.pack(pady=10)

    # Función para obtener el valor ingresado y cerrar la ventana de entrada
    def obtener_pasos():
        pasos = int(pasos_entry.get())
        input_window.destroy()
        
        if pasos is not None:
            # Tamaño del grid
            grid_size = 101

            # Crear la hormiga y ejecutar los pasos
            hormiga = HormigaDeLangton(grid_size)
            hormiga.ejecutar(pasos)

            # Graficar el resultado
            plt.figure(figsize=(8, 8))
            plt.imshow(hormiga.grid, cmap='binary')
            plt.title(f'Hormiga de Langton después de {pasos} pasos', fontsize=16)
            plt.axis('off')
            plt.show()

    # Botón para confirmar la entrada
    tk.Button(input_window, text="Iniciar Simulación", font=font, command=obtener_pasos).pack(pady=20)

# Crear la ventana principal de Tkinter
root = tk.Tk()
root.withdraw()  # Esconder la ventana principal

# Ejecutar la función para iniciar la simulación
iniciar_simulacion()

# Ejecutar el loop de la ventana principal de Tkinter
root.mainloop()
