# Práctica de Monos que Escriben

## Desarrollador
- Betanzos Reyes Gustavo Noel

## Descripción
Esta práctica implementa una simulación inspirada en el experimento mental conocido como "Monos que Escriben", utilizando un enfoque basado en algoritmos genéticos. El objetivo es aproximar una cadena objetivo específica mediante la generación y mutación de cadenas aleatorias hasta alcanzar la coincidencia exacta.

## Funcionalidad
El programa genera una población inicial de cadenas aleatorias y las evalúa en función de cuántos caracteres coinciden con la cadena objetivo. A través de iteraciones, las cadenas se mutan y se selecciona la mejor adaptación hasta que una de las cadenas coincide completamente con la cadena objetivo.

## Uso
1. Ejecutar el script `monos_que_escriben.py`.
2. El programa automáticamente generará la población inicial y comenzará a mutar las cadenas hasta encontrar una coincidencia exacta con la cadena objetivo.
3. El progreso del mejor individuo se mostrará en la consola a medida que el programa evoluciona.
4. Al finalizar, el programa mostrará el número total de iteraciones necesarias para alcanzar la coincidencia exacta.