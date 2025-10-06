"""
Ejercicio No. 3 - Análisis de Complejidad Algorítmica
Implementación de función con bucles con incrementos especiales
"""

import time
import matplotlib.pyplot as plt
import pandas as pd

def function_ejercicio3(n):
    """
    Implementación del algoritmo del ejercicio 3
    void function (int n) {
        int i, j;
        for (i=1; i<=n/3; i++) {
            for (j=1; j<=n; j+=4) {
                printf("Sequence\n");
            }
        }
    }
    """
    counter = 0
    for i in range(1, n//3 + 1):
        for j in range(1, n + 1, 4):  # j se incrementa de 4 en 4
            # Simulamos el printf("Sequence\n")
            counter += 1
    return counter

def analizar_complejidad_ejercicio3():
    """
    Análisis de complejidad del Ejercicio 3:
    
    Bucle externo (i): va de 1 a n/3 → O(n/3) = O(n)
    Bucle interno (j): va de 1 a n con incremento de 4 → O(n/4) = O(n)
    
    El bucle interno se ejecuta n/4 veces aproximadamente (ya que j se incrementa de 4 en 4)
    
    Complejidad total: O(n) × O(n) = O(n²)
    """
    print("=== ANÁLISIS DE COMPLEJIDAD - EJERCICIO 3 ===")
    print("Bucle externo (i): va de 1 a n/3 → O(n/3) = O(n)")
    print("Bucle interno (j): va de 1 a n con incremento de 4 → O(n/4) = O(n)")
    print("El bucle interno se ejecuta aproximadamente n/4 veces")
    print("Complejidad total: O(n) × O(n) = O(n²)")
    print()

def medir_tiempos_ejercicio3():
    """
    Mide los tiempos de ejecución para diferentes valores de n
    """
    print("=== MEDICIÓN DE TIEMPOS - EJERCICIO 3 ===")
    
    # Valores de n a probar
    valores_n = [1, 10, 100, 1000, 10000, 100000, 1000000]
    tiempos = []
    contadores = []
    
    for n in valores_n:
        print(f"Probando con n = {n}...")
        inicio = time.time()
        counter = function_ejercicio3(n)
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
    plt.plot(valores_n, tiempos, 'go-', linewidth=2, markersize=8)
    plt.xlabel('Tamaño de entrada (n)')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Ejercicio 3: Tiempo vs Tamaño de entrada\nComplejidad: O(n²)')
    plt.xscale('log')
    plt.yscale('log')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('ejercicio3_grafica.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    return df

def ejecutar_ejercicio3():
    """
    Función principal para ejecutar el ejercicio 3
    """
    print("EJERCICIO 3 - ANÁLISIS DE COMPLEJIDAD ALGORÍTMICA")
    print("=" * 60)
    
    # Análisis de complejidad
    analizar_complejidad_ejercicio3()
    
    # Medición de tiempos
    resultados = medir_tiempos_ejercicio3()
    
    return resultados

if __name__ == "__main__":
    ejecutar_ejercicio3()
