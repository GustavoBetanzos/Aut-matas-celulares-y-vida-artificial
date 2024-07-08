#Betanzos Reyes Gustavo Noel
#Tarea L-Systems 

'''
Ejemplos de uso
Axioma=F
Reglas=
F->FF+[+F-F-F]-[-F+F+F]
Iteraciones=4
Angulo=25.7

Axioma=X
Reglas=
X->F-[[X]+X]+F[+FX]-X
F->FF
Iteraciones=5
Angulo=22.5
'''

import turtle
import tkinter as tk

REGLAS_SISTEMA_L = {}
COMANDOS_AVANZAR = {"F", "G", "R", "L"}

def derivacion(axioma, pasos):
    derivado = [axioma]
    for _ in range(pasos):
        siguiente_secuencia = [regla(char) for char in derivado[-1]]
        derivado.append(''.join(siguiente_secuencia))
    return derivado

def regla(secuencia):
    return REGLAS_SISTEMA_L.get(secuencia, secuencia)

def dibuja_sistema_l(tortuga, modelo, longitud_segmento, angulo):
    pila = []
    for comando in modelo:
        tortuga.pd()
        if comando in COMANDOS_AVANZAR:
            tortuga.forward(longitud_segmento)
        elif comando == "f":
            tortuga.pu()
            tortuga.forward(longitud_segmento)
        elif comando == "+":
            tortuga.right(angulo)
        elif comando == "-":
            tortuga.left(angulo)
        elif comando == "[":
            pila.append((tortuga.position(), tortuga.heading()))
        elif comando == "]":
            tortuga.pu()
            posicion, direccion = pila.pop()
            tortuga.goto(posicion)
            tortuga.setheading(direccion)

def configurar_tortuga(angulo_inicial):
    tortuga_recursiva = turtle.Turtle()
    tortuga_recursiva.screen.title("Derivación del Sistema L")
    tortuga_recursiva.speed(0)
    tortuga_recursiva.setheading(angulo_inicial)
    return tortuga_recursiva

def obtener_datos():
    axioma = axioma_entry.get()
    reglas = reglas_entry.get("1.0", tk.END).strip().splitlines()
    iteraciones = int(iteraciones_entry.get())
    angulo = float(angulo_entry.get())
    return axioma, reglas, iteraciones, angulo

def iniciar_dibujo():
    axioma, reglas, iteraciones, angulo = obtener_datos()
    for regla in reglas:
        clave, valor = regla.split("->")
        REGLAS_SISTEMA_L[clave] = valor
    modelo = derivacion(axioma, iteraciones)
    longitud_segmento = 5
    angulo_inicial = 90

    tortuga = configurar_tortuga(angulo_inicial)
    ventana_tortuga = turtle.Screen()
    ventana_tortuga.screensize(1500, 1500)
    dibuja_sistema_l(tortuga, modelo[-1], longitud_segmento, angulo)
    ventana_tortuga.exitonclick()

# Crear la ventana principal
root = tk.Tk()
root.title("Sistema L-System")

# Crear los campos de entrada
axioma_label = tk.Label(root, text="Axioma:")
axioma_label.pack()
axioma_entry = tk.Entry(root)
axioma_entry.pack()

reglas_label = tk.Label(root, text="Reglas (una por línea, formato X->F):")
reglas_label.pack()
reglas_entry = tk.Text(root, height=5, width=30)
reglas_entry.pack()

iteraciones_label = tk.Label(root, text="Iteraciones:")
iteraciones_label.pack()
iteraciones_entry = tk.Entry(root)
iteraciones_entry.pack()

angulo_label = tk.Label(root, text="Ángulo:")
angulo_label.pack()
angulo_entry = tk.Entry(root)
angulo_entry.pack()

# Botón para iniciar el dibujo
iniciar_button = tk.Button(root, text="Iniciar Dibujo", command=iniciar_dibujo)
iniciar_button.pack()

# Ejecutar la interfaz
root.mainloop()
