"""
Ejercicio No. 1 - Análisis de Complejidad Algorítmica
Implementación de función con 3 bucles anidados
"""

import time
import matplotlib.pyplot as plt
import pandas as pd

def function_ejercicio1(n):
    """
    Implementación del algoritmo del ejercicio 1
    void function (int n) {
        int i, j, k, counter = 0;
        for (i = n/2; i <= n; i++) {
            for (j = 1; j+n/2 <= n; j++) {
                for (k = 1; k <= n; k = k*2) {
                    counter++;
                }
            }
        }
    }
    """
    counter = 0
    for i in range(n//2, n + 1):
        for j in range(1, n - n//2 + 1):
            k = 1
            while k <= n:
                counter += 1
                k *= 2
    return counter

def analizar_complejidad_ejercicio1():
    """
    Análisis de complejidad del Ejercicio 1:
    
    Bucle externo (i): va de n/2 a n → O(n/2) = O(n)
    Bucle medio (j): va de 1 a n-n/2 → O(n/2) = O(n)  
    Bucle interno (k): va de 1 a n con k = k*2 → O(log n)
    
    Complejidad total: O(n) × O(n) × O(log n) = O(n² log n)
    """
    print("=== ANÁLISIS DE COMPLEJIDAD - EJERCICIO 1 ===")
    print("Bucle externo (i): va de n/2 a n → O(n/2) = O(n)")
    print("Bucle medio (j): va de 1 a n-n/2 → O(n/2) = O(n)")
    print("Bucle interno (k): va de 1 a n con k = k*2 → O(log n)")
    print("Complejidad total: O(n) × O(n) × O(log n) = O(n² log n)")
    print()

def medir_tiempos_ejercicio1():
    """
    Mide los tiempos de ejecución para diferentes valores de n
    """
    print("=== MEDICIÓN DE TIEMPOS - EJERCICIO 1 ===")
    
    # Valores de n a probar
    valores_n = [1, 10, 100, 1000, 10000, 100000, 1000000]
    tiempos = []
    contadores = []
    
    for n in valores_n:
        print(f"Probando con n = {n}...")
        inicio = time.time()
        counter = function_ejercicio1(n)
        fin = time.time()
        tiempo_ejecucion = fin - inicio
        
        tiempos.append(tiempo_ejecucion)
        contadores.append(counter)
        
        print(f"  Tiempo: {tiempo_ejecucion:.6f} segundos")
        print(f"  Counter: {counter}")
        print()
    
    # Crear tabla de resultados
    df = pd.DataFrame({
        'n': valores_n,
        'Tiempo (segundos)': tiempos,
        'Counter': contadores
    })
    
    print("=== TABLA DE RESULTADOS ===")
    print(df.to_string(index=False))
    print()
    
    # Crear gráfica
    plt.figure(figsize=(10, 6))
    plt.plot(valores_n, tiempos, 'bo-', linewidth=2, markersize=8)
    plt.xlabel('Tamaño de entrada (n)')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Ejercicio 1: Tiempo vs Tamaño de entrada\nComplejidad: O(n² log n)')
    plt.xscale('log')
    plt.yscale('log')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('ejercicio1_grafica.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    return df

def ejecutar_ejercicio1():
    """
    Función principal para ejecutar el ejercicio 1
    """
    print("EJERCICIO 1 - ANÁLISIS DE COMPLEJIDAD ALGORÍTMICA")
    print("=" * 60)
    
    # Análisis de complejidad
    analizar_complejidad_ejercicio1()
    
    # Medición de tiempos
    resultados = medir_tiempos_ejercicio1()
    
    return resultados

if __name__ == "__main__":
    ejecutar_ejercicio1()
