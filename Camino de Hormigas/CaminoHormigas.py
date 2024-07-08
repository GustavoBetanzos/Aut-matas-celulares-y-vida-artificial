#Betanzos Reyes Gustavo Noel
#Tarea Camino de las hormigas
import numpy as np
import random
import matplotlib.pyplot as plt

# Datos
A = np.array([
    [0, 4, 3, np.inf, np.inf, np.inf, np.inf, np.inf],
    [4, 0, 2, 5, np.inf, np.inf, np.inf, np.inf],
    [3, 2, 0, 3, 6, np.inf, np.inf, np.inf],
    [np.inf, 5, 3, 0, 1, 5, np.inf, np.inf, ],
    [np.inf, np.inf, 6, 1, 0, np.inf, 5, np.inf],
    [np.inf, np.inf, np.inf, 5, np.inf, 0, 2, 7],
    [np.inf, np.inf, np.inf, np.inf, 5, 2, 0, 4],
    [np.inf, np.inf, np.inf, np.inf, np.inf, 7, 4, 0]
])
L = len(A)
V = np.zeros((L, L))

for i in range(L):
    for j in range(L):
        if A[i, j] != 0:
            V[i, j] = 1 / A[i, j]

tau_inicial = 0.1  # Feromona inicial
tau = tau_inicial * np.ones((L, L))  # vector de feromonas
ro = 0.1  # Factor de evaporacion
nh = 50  # Numero de hormigas en la colonia
N = 50  # Numero de iteraciones
pi = 0  # Punto inicial
pf = 7  # Punto final

mejora = []  # Lista que guarda el mejor costo en cada iteracion


class Hormiga(object):
    def __init__(self, pi, pf):
        self.pi = pi
        self.pf = pf
        self.Camino = [pi]

    def sig_nodo(self, n):
        P = V * tau
        P = P[n, :] / np.sum(P[n, :])
        indice = np.array(range(L))
        c = P > 0
        P = P[c]
        indice = indice[c]
        for i in range(1, len(P)):
            P[i] = P[i] + P[i - 1]
        u = random.random()

        if 0 <= u <= P[0]:
            y = indice[0]
        else:
            for i in range(1, len(P)):
                if P[i - 1] < u <= P[i]:
                    y = indice[i]
        self.Camino.append(y)

    def trayectoria(self):
        run = 0
        while run < L - 1:
            self.sig_nodo(self.Camino[-1])
            if self.Camino[-1] == self.pf:
                run = L
            run = run + 1

    def apor_fero(self, i, j, hormiga):
        C = self.Camino
        y = 0
        for t in range(len(C) - 1):
            if [i, j] == [C[t], C[t + 1]]:
                y = 1
                break
        return y

    def costo(self, hormiga):
        C = self.Camino
        if C[-1] != self.pf:
            y = np.inf
        else:
            y = 0
            for t in range(len(C) - 1):
                y = y + A[C[t], C[t + 1]]
        return y


def main():
    d = 0
    while d < N:
        Colonía = []
        for t in range(nh):
            hormiga = Hormiga(pi, pf)
            Colonía.append(hormiga)

        for hormiga in Colonía:
            hormiga.trayectoria()

        for hormiga in Colonía:
            hormiga.costo(hormiga)

        for i in range(L):
            for j in range(L):
                for hormiga in Colonía:
                    tau[i, j] = (1 - ro) * tau[i, j] + hormiga.apor_fero(i, j, hormiga) * 1 / (
                                hormiga.costo(hormiga) ** 4)

        M_C = []
        for hormiga in Colonía:
            M_C.append(hormiga.costo(hormiga))
        mejora.append(np.min(M_C))
        d = d + 1

    Costos = []
    for hormiga in Colonía:
        Costos.append(hormiga.costo(hormiga))

    indice = np.argsort(Costos)
    Mejor_Costo = Costos[indice[0]]
    Mejor_Camino = np.array(Colonía[indice[0]].Camino) + 1
    print("El mejor individuo es:" + str(Mejor_Camino) + ".")
    print("Su costo es: " + str(Mejor_Costo) + ".")
    mejora.append(Mejor_Costo)
    plt.plot(mejora)
    plt.title("Evolución del algoritmo", fontweight="bold", fontsize=14)
    plt.xlabel("Generación", fontweight="bold", fontsize=12)
    plt.ylabel("Mejor costo", fontweight="bold", fontsize=12)
    plt.xlim(0, N)
    plt.show()


if __name__ == '__main__':
    main()