"""
Ejercicio No. 2 - Análisis de Complejidad Algorítmica
Implementación de función con break en bucle anidado
"""

import time
import matplotlib.pyplot as plt
import pandas as pd

def function_ejercicio2(n):
    """
    Implementación del algoritmo del ejercicio 2
    void function (int n) {
        if (n <= 1) return;
        int i, j;
        for (i = 1; i <= n; i++) {
            for (j = 1; j <= n; j++) {
                printf ("Sequence\n");
                break;
            }
        }
    }
    """
    if n <= 1:
        return 0
    
    counter = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # Simulamos el printf("Sequence\n")
            counter += 1
            break  # El break hace que solo se ejecute una vez por cada i
    return counter

def analizar_complejidad_ejercicio2():
    """
    Análisis de complejidad del Ejercicio 2:
    
    Bucle externo (i): va de 1 a n → O(n)
    Bucle interno (j): va de 1 a n, pero tiene break → O(1)
    
    El break hace que el bucle interno solo se ejecute una vez por cada iteración
    del bucle externo, por lo que la complejidad es O(n) × O(1) = O(n)
    
    Complejidad total: O(n)
    """
    print("=== ANÁLISIS DE COMPLEJIDAD - EJERCICIO 2 ===")
    print("Bucle externo (i): va de 1 a n → O(n)")
    print("Bucle interno (j): va de 1 a n, pero tiene break → O(1)")
    print("El break hace que el bucle interno solo se ejecute una vez por cada i")
    print("Complejidad total: O(n) × O(1) = O(n)")
    print()

def medir_tiempos_ejercicio2():
    """
    Mide los tiempos de ejecución para diferentes valores de n
    """
    print("=== MEDICIÓN DE TIEMPOS - EJERCICIO 2 ===")
    
    # Valores de n a probar
    valores_n = [1, 10, 100, 1000, 10000, 100000, 1000000]
    tiempos = []
    contadores = []
    
    for n in valores_n:
        print(f"Probando con n = {n}...")
        inicio = time.time()
        counter = function_ejercicio2(n)
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
    plt.plot(valores_n, tiempos, 'ro-', linewidth=2, markersize=8)
    plt.xlabel('Tamaño de entrada (n)')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Ejercicio 2: Tiempo vs Tamaño de entrada\nComplejidad: O(n)')
    plt.xscale('log')
    plt.yscale('log')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('ejercicio2_grafica.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    return df

def ejecutar_ejercicio2():
    """
    Función principal para ejecutar el ejercicio 2
    """
    print("EJERCICIO 2 - ANÁLISIS DE COMPLEJIDAD ALGORÍTMICA")
    print("=" * 60)
    
    # Análisis de complejidad
    analizar_complejidad_ejercicio2()
    
    # Medición de tiempos
    resultados = medir_tiempos_ejercicio2()
    
    return resultados

if __name__ == "__main__":
    ejecutar_ejercicio2()
