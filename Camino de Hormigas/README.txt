# Práctica de Camino de las Hormigas

## Desarrollador
- Betanzos Reyes Gustavo Noel

## Descripción
En esta práctica se implementa el algoritmo de optimización basado en colonia de hormigas (ACO, por sus siglas en inglés) para encontrar la ruta más corta en un grafo. El objetivo es simular el comportamiento de las hormigas al buscar caminos y depositar feromonas para guiar a otras hormigas hacia soluciones óptimas.

## Funcionalidad
El programa define una clase `Hormiga` que representa una hormiga individual. Cada hormiga sigue un camino desde un nodo inicial hasta un nodo final, eligiendo el siguiente nodo basándose en una probabilidad calculada a partir de la visibilidad y la cantidad de feromonas en cada arista. El programa ejecuta múltiples iteraciones del algoritmo, donde las hormigas depositan feromonas en las rutas que siguen, y se evapora una parte de las feromonas existentes. El proceso se repite hasta alcanzar un número máximo de iteraciones, registrando el mejor costo encontrado en cada iteración.

## Uso
1. Ejecutar el script `CaminoHormigas.py`.
2. Se mostrará la evolución del algoritmo a través de un gráfico que indica el mejor costo en cada generación.
3. Al finalizar, se imprimirá el mejor camino encontrado y su costo total.