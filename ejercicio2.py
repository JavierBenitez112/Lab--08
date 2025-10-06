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
    Mide los tiempos de ejecucion para diferentes valores de n
    """
    print("=== MEDICION DE TIEMPOS - EJERCICIO 2 ===")
    
    # Valores de n a probar
    valores_n = [1, 10, 100, 1000, 10000, 100000, 1000000]
    tiempos = []
    contadores = []
    
    # Crear tabla de resultados en tiempo real
    print(f"{'n':<10} {'Tiempo (s)':<15} {'Counter':<15} {'Estado':<15}")
    print("-" * 60)
    
    for n in valores_n:
        inicio = time.time()
        counter = function_ejercicio2(n)
        fin = time.time()
        tiempo_ejecucion = fin - inicio
        
        tiempos.append(tiempo_ejecucion)
        contadores.append(counter)
        
        estado = "Completado" if tiempo_ejecucion < 40 else "Timeout"
        print(f"{n:<10} {tiempo_ejecucion:<15.6f} {counter:<15} {estado:<15}")
    
    # Crear tabla de resultados
    df = pd.DataFrame({
        'n': valores_n,
        'Tiempo (segundos)': tiempos,
        'Counter': contadores
    })
    
    print("\n=== TABLA DE RESULTADOS ===")
    print(df.to_string(index=False))
    print()
    
    # Crear grafica
    plt.figure(figsize=(10, 6))
    plt.plot(valores_n, tiempos, 'ro-', linewidth=2, markersize=8)
    plt.xlabel('Tamano de entrada (n)')
    plt.ylabel('Tiempo de ejecucion (segundos)')
    plt.title('Ejercicio 2: Tiempo vs Tamano de entrada\nComplejidad: O(n)')
    plt.xscale('log')
    plt.yscale('log')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('ejercicio2_grafica.png', dpi=300, bbox_inches='tight')
    plt.close()  # Cerrar la figura para liberar memoria
    
    return df

def ejecutar_ejercicio2():
    """
    Funcion principal para ejecutar el ejercicio 2
    """
    print("EJERCICIO 2 - ANALISIS DE COMPLEJIDAD ALGORITMICA")
    print("=" * 60)
    
    # Analisis de complejidad
    analizar_complejidad_ejercicio2()
    
    # Medicion de tiempos
    resultados = medir_tiempos_ejercicio2()
    
    return resultados

if __name__ == "__main__":
    ejecutar_ejercicio2()
