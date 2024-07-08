#Betanzos Reyes Gustavo Noel
#Tarea Monos que escriben
import random
import string

def calificacion(cadena, objetivo):
    return sum(1 for a, b in zip(cadena, objetivo) if a == b)

objetivo = "PRUEBA DE ALGORITMOS DAWKINS"
caracteres = string.ascii_uppercase + " "
probabilidad = 0.05

# Generamos la población inicial
optimo = ''.join(random.choice(caracteres) for _ in range(len(objetivo)))
calificacion_optimo = calificacion(optimo, objetivo)

# Iteraciones
iteraciones = 0

# Mientras no encontremos al optimo
while calificacion_optimo != len(objetivo):

    iteraciones += 1

    # Mutamos la población actual
    poblacion = [''.join(random.choice(caracteres) if random.random() < probabilidad else c for c in optimo) for _ in range(100)]

    # Actualizamos las calificaciones
    calificaciones = [calificacion(x, objetivo) for x in poblacion]

    # Obtenemos al mejor individuo
    mejor_individuo, mejor_calificacion = max(zip(poblacion, calificaciones), key=lambda x: x[1])

    # Mostramos la evolución del mejor individuo
    print(mejor_individuo)

    # Actualizamos el optimo
    if mejor_calificacion > calificacion_optimo:
        optimo = mejor_individuo
        calificacion_optimo = mejor_calificacion

print('Númeor total de iteraciones realizadas: {}'.format(iteraciones))
