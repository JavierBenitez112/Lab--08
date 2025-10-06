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
    Mide los tiempos de ejecucion para diferentes valores de n
    """
    print("=== MEDICION DE TIEMPOS - EJERCICIO 3 ===")
    
    # Valores de n a probar
    valores_n = [1, 10, 100, 1000, 10000, 100000, 1000000]
    tiempos = []
    contadores = []
    
    # Crear tabla de resultados en tiempo real
    print(f"{'n':<10} {'Tiempo (s)':<15} {'Counter':<15} {'Estado':<15}")
    print("-" * 60)
    
    for n in valores_n:
        inicio = time.time()
        counter = function_ejercicio3(n)
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
    plt.plot(valores_n, tiempos, 'go-', linewidth=2, markersize=8)
    plt.xlabel('Tamano de entrada (n)')
    plt.ylabel('Tiempo de ejecucion (segundos)')
    plt.title('Ejercicio 3: Tiempo vs Tamano de entrada\nComplejidad: O(n²)')
    plt.xscale('log')
    plt.yscale('log')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('ejercicio3_grafica.png', dpi=300, bbox_inches='tight')
    plt.close()  # Cerrar la figura para liberar memoria
    
    return df

def ejecutar_ejercicio3():
    """
    Funcion principal para ejecutar el ejercicio 3
    """
    print("EJERCICIO 3 - ANALISIS DE COMPLEJIDAD ALGORITMICA")
    print("=" * 60)
    
    # Analisis de complejidad
    analizar_complejidad_ejercicio3()
    
    # Medicion de tiempos
    resultados = medir_tiempos_ejercicio3()
    
    return resultados

if __name__ == "__main__":
    ejecutar_ejercicio3()
