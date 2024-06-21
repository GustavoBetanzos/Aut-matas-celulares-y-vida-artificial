#Betanzos Reyes Gustavo Noel
#Tarea Algoritmos Geneticos
import random

class Poblacion:
    class Individuo:
        def __init__(self, cromosoma) -> None:
            self.cromosoma = cromosoma
            self.aptitud = None
        
        def mutacion(self):
            probabilidad = 0.2
            # Recorremos el cromosoma del individuo
            for i in range(len(self.cromosoma)):
                # Valor random entre [0,1]
                if random.random() < probabilidad:
                    # Mutamos
                    self.cromosoma[i] = 1 - self.cromosoma[i]

    def __init__(self, p=50, objetos=None, m=50) -> None:
        if objetos is None:
            objetos = [random.randint(1, 20) for _ in range(20)]
        self.poblacion = [self.Individuo([random.randint(0, 1) for _ in range(len(objetos))]) for _ in range(m)]
        self.peso_maximo = p
        self.objetos = objetos
        self.optimo = None  # individuo optimo    

    def asignarAptitud(self):
        for i in self.poblacion:
            i.aptitud = self.fitness(i.cromosoma)
    
    def fitness(self, arr):
        peso = sum(self.objetos[i] for i in range(len(arr)) if arr[i] == 1)
        return abs(self.peso_maximo - peso)

    def elitismo(self):
        self.optimo = min(self.poblacion, key=lambda x: x.aptitud)
        return self.optimo

    def seleccioRuleta(self):
        sumatoria = sum(i.aptitud for i in self.poblacion)
        ran = random.random()
        acumulado = 0
        for individuo in self.poblacion:
            probabilidad = individuo.aptitud / sumatoria
            acumulado += probabilidad
            if ran < acumulado:
                return individuo

    def optimoEncontrado(self):
        return self.optimo is not None and self.optimo.aptitud == 0

def recombinacion(p1, p2):
    corte = random.randint(0, len(p1.cromosoma) - 2)
    hijo = Poblacion().Individuo(p1.cromosoma[0:corte + 1] + p2.cromosoma[corte + 1:])
    return hijo

if __name__ == "__main__":
    generaciones = 0
    poblacion = Poblacion()
    print(f"Peso maximo de la mochila: {poblacion.peso_maximo} ")
    print("Objetos y su peso: ")
    print(poblacion.objetos, "\n")
    poblacion.asignarAptitud()
    while generaciones < 1000 and not poblacion.optimoEncontrado():
        nuevaPoblacion = [poblacion.elitismo()]
        while len(nuevaPoblacion) < 50:
            individuo1 = poblacion.seleccioRuleta()
            individuo2 = poblacion.seleccioRuleta()
            hijo = recombinacion(individuo1, individuo2)
            hijo.mutacion()
            nuevaPoblacion.append(hijo)
        poblacion.poblacion = nuevaPoblacion
        poblacion.asignarAptitud()
        generaciones += 1
        if generaciones % 50 == 0:
            print(f"Mejor solucion en iteracion {generaciones} es: \n{poblacion.optimo.cromosoma} \nfitness: {poblacion.optimo.aptitud}")

    if poblacion.optimoEncontrado():
        print(f"Se encontro el optimo en la generacion {generaciones}:")
        print(f"{poblacion.optimo.cromosoma}\nfitness: {poblacion.optimo.aptitud}", '\n')

    print("Objetos y su peso:")
    peso_total_objetos = sum(poblacion.objetos[i] for i in range(len(poblacion.objetos)) if poblacion.optimo.cromosoma[i] == 1)
    for i, objeto in enumerate(poblacion.objetos):
        print(f"Objeto {i}, con peso: {objeto}, llevar en la mochila?: {'Si' if poblacion.optimo.cromosoma[i] == 1 else 'No'}")
    print(f"Peso total de los objetos llevados: {peso_total_objetos}")