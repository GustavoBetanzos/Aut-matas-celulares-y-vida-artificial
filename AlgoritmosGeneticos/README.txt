# Práctica de Algoritmos Genéticos

## Desarrollador
- Betanzos Reyes Gustavo Noel

## Descripción
En esta práctica se implementa un algoritmo genético para resolver el problema de la mochila. El objetivo es encontrar la combinación óptima de objetos que quepan en una mochila con un peso máximo dado.

## Funcionalidad
El programa genera una población inicial de individuos con cromosomas aleatorios que representan la selección de objetos (1 si se incluye, 0 si no). Luego, se evalúa la aptitud de cada individuo basándose en el peso total de los objetos seleccionados y se realiza la selección de padres mediante el método de la ruleta. Se aplican operadores de recombinación y mutación para crear una nueva generación de individuos. El proceso se repite hasta encontrar la solución óptima o alcanzar un número máximo de generaciones.

## Uso
1. Ejecutar el script `AlgoritmosGeneticos.py`.
2. Se mostrará el peso máximo de la mochila y la lista de objetos con sus respectivos pesos.
3. El algoritmo buscará la solución óptima, mostrando el progreso cada 50 generaciones.
4. Al finalizar, se mostrará la mejor combinación de objetos encontrada y su peso total.