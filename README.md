# Laboratorio 8 - Análisis de Complejidad Algorítmica

Este proyecto contiene la implementación y análisis de complejidad de varios algoritmos en Python.

## Estructura del Proyecto

- `main.py` - Archivo principal que ejecuta todos los ejercicios
- `ejercicio1.py` - Función con 3 bucles anidados (O(n² log n))
- `ejercicio2.py` - Función con break en bucle anidado (O(n))
- `ejercicio3.py` - Función con incrementos especiales (O(n²))
- `ejercicio4.py` - Análisis de búsqueda lineal
- `ejercicio5.py` - Verificación de enunciados Big-Oh
- `requirements.txt` - Dependencias del proyecto

## Instalación

1. Instale las dependencias necesarias:
```bash
pip install -r requirements.txt
```

## Uso

### Ejecutar todos los ejercicios:
```bash
python main.py
```

### Ejecutar un ejercicio específico:
```bash
python ejercicio1.py
python ejercicio2.py
python ejercicio3.py
python ejercicio4.py
python ejercicio5.py
```

## Descripción de los Ejercicios

### Ejercicio 1 (25%)
- **Algoritmo**: Función con 3 bucles anidados
- **Complejidad**: O(n² log n)
- **Análisis**: 
  - Bucle externo: O(n)
  - Bucle medio: O(n)
  - Bucle interno: O(log n)

### Ejercicio 2 (25%)
- **Algoritmo**: Función con break en bucle anidado
- **Complejidad**: O(n)
- **Análisis**: El break hace que el bucle interno solo se ejecute una vez por iteración

### Ejercicio 3 (25%)
- **Algoritmo**: Función con incrementos especiales
- **Complejidad**: O(n²)
- **Análisis**: 
  - Bucle externo: O(n)
  - Bucle interno: O(n) (incremento de 4 en 4)

### Ejercicio 4 (10%)
- **Análisis**: Búsqueda lineal
- **Casos**:
  - Mejor caso: O(1)
  - Caso promedio: O(n)
  - Peor caso: O(n)

### Ejercicio 5 (15%)
- **Análisis**: Verificación de enunciados Big-Oh
- **Enunciados**:
  - a) Verdadero (transitividad de Θ)
  - b) Verdadero (transitividad de O)
  - c) Falso (complejidad O(n³), no Θ(n!))

## Características

- ✅ Análisis teórico detallado de complejidad
- ✅ Implementación práctica de cada algoritmo
- ✅ Medición de tiempos de ejecución
- ✅ Generación de gráficas comparativas
- ✅ Tablas de resultados
- ✅ Interfaz de menú interactiva
- ✅ Documentación completa

## Gráficas Generadas

El programa genera las siguientes gráficas:
- `ejercicio1_grafica.png` - Tiempo vs tamaño de entrada (O(n² log n))
- `ejercicio2_grafica.png` - Tiempo vs tamaño de entrada (O(n))
- `ejercicio3_grafica.png` - Tiempo vs tamaño de entrada (O(n²))
- `ejercicio4_grafica.png` - Comparación de casos de búsqueda lineal
- `ejercicio5_grafica.png` - Comparación n³ vs n! vs operaciones reales

## Requisitos del Sistema

- Python 3.7+
- matplotlib
- pandas
- numpy

## Autor

Implementado para el Laboratorio 8 de Teoría de la Computación.
