# Práctica de Hormiga de Langton

## Desarrollador
- Betanzos Reyes Gustavo Noel

## Descripción
En esta práctica se implementa la Hormiga de Langton, un autómata celular sobre un grid bidimensional. La hormiga sigue una serie de reglas simples que generan patrones complejos a partir de movimientos y cambios de color de las celdas del grid.

## Funcionalidad
El programa define una clase `HormigaDeLangton` que simula el comportamiento de la hormiga en un grid de tamaño definido. La hormiga se mueve y gira dependiendo del color de la celda en la que se encuentra, cambiando el color de la celda y avanzando a la siguiente posición. El programa permite al usuario definir el número de pasos a simular a través de una interfaz gráfica creada con Tkinter.

## Uso
1. Ejecutar el script `HormigaLangton.py`.
2. Ingresar el número de pasos en la ventana emergente.
3. El algoritmo ejecutará la simulación y mostrará el grid resultante después del número de pasos especificado.