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

### Ejecutar todos los ejercicios automáticamente (con límite de 40 segundos por ejercicio):
```bash
python main.py
```

**Características de main.py:**
- ✅ Ejecuta los 5 ejercicios secuencialmente
- ✅ Límite de 40 segundos por ejercicio
- ✅ Si un ejercicio excede el tiempo, pasa al siguiente automáticamente
- ✅ Muestra resultados en formato de tabla
- ✅ Guarda resultados en archivo CSV
- ✅ Genera gráficas automáticamente

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
- ✅ Tablas de resultados en formato profesional
- ✅ **Límite de tiempo de 40 segundos por ejercicio**
- ✅ **Timeout automático** - pasa al siguiente ejercicio si excede el tiempo
- ✅ **Exportación a CSV** de todos los resultados
- ✅ **Estadísticas completas** de ejecución
- ✅ **Compatible con Windows** usando threading
- ✅ Documentación completa

## Salida del Programa

El programa muestra los resultados en formato de tabla:

```
====================================================================================================
LABORATORIO 8 - ANÁLISIS DE COMPLEJIDAD ALGORÍTMICA
EJECUTANDO TODOS LOS EJERCICIOS CON LÍMITE DE 40 SEGUNDOS
====================================================================================================

Ejercicio       Complejidad          Estado       Tiempo (s)   Error                         
----------------------------------------------------------------------------------------------------
Ejercicio 1     O(n² log n)         ✅ Completado 15.23        N/A                           
Ejercicio 2     O(n)                ✅ Completado 2.45         N/A                           
Ejercicio 3     O(n²)               ✅ Completado 8.67         N/A                           
Ejercicio 4     Búsqueda Lineal     ✅ Completado 3.12         N/A                           
Ejercicio 5     Verificación Big-Oh ✅ Completado 1.89         N/A                           

📊 TABLA COMPLETA DE RESULTADOS
     Ejercicio         Complejidad      Estado  Tiempo (segundos)  Error
0  Ejercicio 1       O(n² log n)  Completado             15.23    N/A
1  Ejercicio 2               O(n)  Completado              2.45    N/A
2  Ejercicio 3              O(n²)  Completado              8.67    N/A
3  Ejercicio 4  Búsqueda Lineal  Completado              3.12    N/A
4  Ejercicio 5  Verificación...  Completado              1.89    N/A

📈 ESTADÍSTICAS:
   ✅ Ejercicios completados: 5/5
   ⏰ Ejercicios con timeout: 0/5
   ❌ Ejercicios con error: 0/5
   ⏱️  Tiempo total de ejecución: 31.36 segundos
   💾 Resultados guardados en: resultados_lab8_20241006_143022.csv
```

## Gráficas Generadas

El programa genera las siguientes gráficas:
- `ejercicio1_grafica.png` - Tiempo vs tamaño de entrada (O(n² log n))
- `ejercicio2_grafica.png` - Tiempo vs tamaño de entrada (O(n))
- `ejercicio3_grafica.png` - Tiempo vs tamaño de entrada (O(n²))
- `ejercicio4_grafica.png` - Comparación de casos de búsqueda lineal
- `ejercicio5_grafica.png` - Comparación n³ vs n! vs operaciones reales

## Archivos Generados

- `resultados_lab8_AAAAMMDD_HHMMSS.csv` - Resultados exportados en formato CSV
- `*.png` - Gráficas de cada ejercicio

## Requisitos del Sistema

- Python 3.7+
- matplotlib
- pandas
- numpy

## Autor

Implementado para el Laboratorio 8 de Teoría de la Computación.
