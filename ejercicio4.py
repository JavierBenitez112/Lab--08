"""
Ejercicio No. 4 - Análisis de Búsqueda Lineal
Análisis de mejor caso, caso promedio y peor caso
"""

import random
import time
import matplotlib.pyplot as plt
import pandas as pd

def busqueda_lineal(arr, target):
    """
    Implementación de búsqueda lineal
    Retorna el índice del elemento si se encuentra, -1 si no
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def analizar_casos_busqueda_lineal():
    """
    Análisis de los diferentes casos de búsqueda lineal
    """
    print("=== ANÁLISIS DE BÚSQUEDA LINEAL - EJERCICIO 4 ===")
    print()
    
    print("MEJOR CASO:")
    print("- Descripción: El elemento buscado está en la primera posición del arreglo")
    print("- Tiempo de ejecución: O(1)")
    print("- Justificación: Solo se necesita una comparación")
    print("- Ejemplo: Buscar el elemento 5 en [5, 1, 2, 3, 4]")
    print()
    
    print("CASO PROMEDIO:")
    print("- Descripción: El elemento buscado está en una posición aleatoria del arreglo")
    print("- Tiempo de ejecución: O(n/2) = O(n)")
    print("- Justificación: En promedio, se necesitan n/2 comparaciones")
    print("- Ejemplo: Buscar el elemento 3 en [1, 2, 3, 4, 5] (posición media)")
    print()
    
    print("PEOR CASO:")
    print("- Descripción: El elemento buscado está en la última posición o no existe")
    print("- Tiempo de ejecución: O(n)")
    print("- Justificación: Se necesitan n comparaciones en el peor escenario")
    print("- Ejemplo: Buscar el elemento 5 en [1, 2, 3, 4, 5] o buscar 6 en [1, 2, 3, 4, 5]")
    print()

def demostrar_casos_busqueda_lineal():
    """
    Demuestra los diferentes casos con ejemplos prácticos
    """
    print("=== DEMOSTRACIÓN PRÁCTICA ===")
    
    # Mejor caso
    print("MEJOR CASO:")
    arr_mejor = [5, 1, 2, 3, 4]
    target_mejor = 5
    inicio = time.time()
    resultado_mejor = busqueda_lineal(arr_mejor, target_mejor)
    fin = time.time()
    print(f"Arreglo: {arr_mejor}")
    print(f"Buscando: {target_mejor}")
    print(f"Resultado: Índice {resultado_mejor}")
    print(f"Tiempo: {fin - inicio:.8f} segundos")
    print(f"Comparaciones realizadas: 1")
    print()
    
    # Caso promedio
    print("CASO PROMEDIO:")
    arr_promedio = [1, 2, 3, 4, 5]
    target_promedio = 3
    inicio = time.time()
    resultado_promedio = busqueda_lineal(arr_promedio, target_promedio)
    fin = time.time()
    print(f"Arreglo: {arr_promedio}")
    print(f"Buscando: {target_promedio}")
    print(f"Resultado: Índice {resultado_promedio}")
    print(f"Tiempo: {fin - inicio:.8f} segundos")
    print(f"Comparaciones realizadas: 3")
    print()
    
    # Peor caso (elemento al final)
    print("PEOR CASO (elemento al final):")
    arr_peor = [1, 2, 3, 4, 5]
    target_peor = 5
    inicio = time.time()
    resultado_peor = busqueda_lineal(arr_peor, target_peor)
    fin = time.time()
    print(f"Arreglo: {arr_peor}")
    print(f"Buscando: {target_peor}")
    print(f"Resultado: Índice {resultado_peor}")
    print(f"Tiempo: {fin - inicio:.8f} segundos")
    print(f"Comparaciones realizadas: 5")
    print()
    
    # Peor caso (elemento no existe)
    print("PEOR CASO (elemento no existe):")
    arr_no_existe = [1, 2, 3, 4, 5]
    target_no_existe = 6
    inicio = time.time()
    resultado_no_existe = busqueda_lineal(arr_no_existe, target_no_existe)
    fin = time.time()
    print(f"Arreglo: {arr_no_existe}")
    print(f"Buscando: {target_no_existe}")
    print(f"Resultado: Índice {resultado_no_existe}")
    print(f"Tiempo: {fin - inicio:.8f} segundos")
    print(f"Comparaciones realizadas: 5")
    print()

def medir_tiempos_diferentes_casos():
    """
    Mide tiempos para diferentes tamaños de arreglo en cada caso
    """
    print("=== MEDICIÓN DE TIEMPOS PARA DIFERENTES CASOS ===")
    
    tamanos = [100, 1000, 10000, 100000]
    resultados = []
    
    for n in tamanos:
        print(f"Probando con n = {n}...")
        
        # Crear arreglo de tamaño n
        arr = list(range(1, n + 1))
        
        # Mejor caso: buscar el primer elemento
        inicio = time.time()
        busqueda_lineal(arr, 1)
        tiempo_mejor = time.time() - inicio
        
        # Caso promedio: buscar elemento en el medio
        inicio = time.time()
        busqueda_lineal(arr, n // 2)
        tiempo_promedio = time.time() - inicio
        
        # Peor caso: buscar el último elemento
        inicio = time.time()
        busqueda_lineal(arr, n)
        tiempo_peor = time.time() - inicio
        
        # Peor caso: buscar elemento que no existe
        inicio = time.time()
        busqueda_lineal(arr, n + 1)
        tiempo_no_existe = time.time() - inicio
        
        resultados.append({
            'n': n,
            'Mejor Caso': tiempo_mejor,
            'Caso Promedio': tiempo_promedio,
            'Peor Caso (final)': tiempo_peor,
            'Peor Caso (no existe)': tiempo_no_existe
        })
        
        print(f"  Mejor caso: {tiempo_mejor:.8f}s")
        print(f"  Caso promedio: {tiempo_promedio:.8f}s")
        print(f"  Peor caso (final): {tiempo_peor:.8f}s")
        print(f"  Peor caso (no existe): {tiempo_no_existe:.8f}s")
        print()
    
    # Crear tabla de resultados
    df = pd.DataFrame(resultados)
    print("=== TABLA DE RESULTADOS ===")
    print(df.to_string(index=False))
    print()
    
    # Crear gráfica
    plt.figure(figsize=(12, 8))
    plt.plot(tamanos, df['Mejor Caso'], 'go-', label='Mejor Caso O(1)', linewidth=2, markersize=8)
    plt.plot(tamanos, df['Caso Promedio'], 'bo-', label='Caso Promedio O(n)', linewidth=2, markersize=8)
    plt.plot(tamanos, df['Peor Caso (final)'], 'ro-', label='Peor Caso O(n)', linewidth=2, markersize=8)
    plt.plot(tamanos, df['Peor Caso (no existe)'], 'mo-', label='Peor Caso (no existe) O(n)', linewidth=2, markersize=8)
    
    plt.xlabel('Tamaño del arreglo (n)')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Búsqueda Lineal: Comparación de Casos')
    plt.xscale('log')
    plt.yscale('log')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('ejercicio4_grafica.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    return df

def ejecutar_ejercicio4():
    """
    Función principal para ejecutar el ejercicio 4
    """
    print("EJERCICIO 4 - ANÁLISIS DE BÚSQUEDA LINEAL")
    print("=" * 60)
    
    # Análisis teórico
    analizar_casos_busqueda_lineal()
    
    # Demostración práctica
    demostrar_casos_busqueda_lineal()
    
    # Medición de tiempos
    resultados = medir_tiempos_diferentes_casos()
    
    return resultados

if __name__ == "__main__":
    ejecutar_ejercicio4()
