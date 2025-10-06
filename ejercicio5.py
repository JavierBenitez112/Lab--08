"""
Ejercicio No. 5 - Verificación de Enunciados de Notación Big-Oh
Análisis de enunciados sobre complejidad algorítmica
"""

import time
import matplotlib.pyplot as plt
import pandas as pd

def analizar_enunciado_a():
    """
    Enunciado a) Si f(n) = Θ(g(n)) y g(n) = Θ(h(n)), entonces h(n) = Θ(f(n)).
    """
    print("=== ENUNCIADO A ===")
    print("Si f(n) = Θ(g(n)) y g(n) = Θ(h(n)), entonces h(n) = Θ(f(n)).")
    print()
    
    print("ANÁLISIS:")
    print("Si f(n) = Θ(g(n)), entonces existen constantes c₁, c₂, n₀ tales que:")
    print("c₁·g(n) ≤ f(n) ≤ c₂·g(n) para todo n ≥ n₀")
    print()
    print("Si g(n) = Θ(h(n)), entonces existen constantes c₃, c₄, n₁ tales que:")
    print("c₃·h(n) ≤ g(n) ≤ c₄·h(n) para todo n ≥ n₁")
    print()
    print("Combinando ambas desigualdades:")
    print("c₁·c₃·h(n) ≤ f(n) ≤ c₂·c₄·h(n)")
    print()
    print("Esto significa que f(n) = Θ(h(n))")
    print("Por transitividad de Θ, también tenemos h(n) = Θ(f(n))")
    print()
    print("RESPUESTA: VERDADERO")
    print("JUSTIFICACIÓN: La relación Θ es transitiva y simétrica.")
    print()

def analizar_enunciado_b():
    """
    Enunciado b) Si f(n) = O(g(n)) y g(n) = O(h(n)), entonces h(n) = Ω(f(n)).
    """
    print("=== ENUNCIADO B ===")
    print("Si f(n) = O(g(n)) y g(n) = O(h(n)), entonces h(n) = Ω(f(n)).")
    print()
    
    print("ANÁLISIS:")
    print("Si f(n) = O(g(n)), entonces existe una constante c₁ tal que:")
    print("f(n) ≤ c₁·g(n) para todo n suficientemente grande")
    print()
    print("Si g(n) = O(h(n)), entonces existe una constante c₂ tal que:")
    print("g(n) ≤ c₂·h(n) para todo n suficientemente grande")
    print()
    print("Combinando ambas desigualdades:")
    print("f(n) ≤ c₁·g(n) ≤ c₁·c₂·h(n)")
    print("Por lo tanto: f(n) ≤ c₁·c₂·h(n)")
    print()
    print("Esto significa que h(n) ≥ (1/(c₁·c₂))·f(n)")
    print("Por definición, h(n) = Ω(f(n))")
    print()
    print("RESPUESTA: VERDADERO")
    print("JUSTIFICACIÓN: La relación O es transitiva, y si f(n) = O(h(n)), entonces h(n) = Ω(f(n)).")
    print()

def analizar_enunciado_c():
    """
    Enunciado c) f(n) = Θ(n!), donde f(n) está definido por el programa A(n)
    """
    print("=== ENUNCIADO C ===")
    print("f(n) = Θ(n!), donde f(n) está definido por el programa A(n):")
    print()
    print("def A(n):")
    print("    atupla = tuple(range(0, n))")
    print("    S = set()")
    print("    for i in range(0, n):")
    print("        for j in range (i + 1, n):")
    print("            S.add(atupla[i:j])")
    print()
    
    print("ANÁLISIS:")
    print("Analicemos el programa paso a paso:")
    print()
    print("1. atupla = tuple(range(0, n)) → O(n)")
    print("2. S = set() → O(1)")
    print("3. Bucle externo: for i in range(0, n) → O(n)")
    print("4. Bucle interno: for j in range(i + 1, n) → O(n-i)")
    print("5. S.add(atupla[i:j]) → O(j-i) para crear la tupla")
    print()
    print("El número total de operaciones es:")
    print("Σ(i=0 to n-1) Σ(j=i+1 to n-1) (j-i)")
    print()
    print("Para cada i, el bucle interno suma:")
    print("1 + 2 + 3 + ... + (n-1-i) = (n-1-i)(n-i)/2")
    print()
    print("Sumando sobre todos los i:")
    print("Σ(i=0 to n-1) (n-1-i)(n-i)/2")
    print()
    print("Esto es aproximadamente n³/6, que es O(n³)")
    print()
    print("Sin embargo, el enunciado dice que es Θ(n!)")
    print("n! crece mucho más rápido que n³")
    print("Por ejemplo: 10! = 3,628,800 vs 10³ = 1,000")
    print()
    print("RESPUESTA: FALSO")
    print("JUSTIFICACIÓN: El programa tiene complejidad O(n³), no Θ(n!).")
    print()

def demostrar_programa_a():
    """
    Demuestra el comportamiento del programa A(n) con diferentes valores
    """
    print("=== DEMOSTRACION DEL PROGRAMA A(n) ===")
    
    def A(n):
        atupla = tuple(range(0, n))
        S = set()
        operaciones = 0
        for i in range(0, n):
            for j in range(i + 1, n):
                S.add(atupla[i:j])
                operaciones += 1
        return len(S), operaciones
    
    print("Probando el programa A(n) con diferentes valores:")
    print()
    
    resultados = []
    
    # Crear tabla de resultados en tiempo real
    print(f"{'n':<5} {'Elementos S':<12} {'Operaciones':<12} {'Tiempo (s)':<12} {'n³':<8} {'n!':<10}")
    print("-" * 70)
    
    for n in [3, 4, 5, 6, 7, 8]:
        inicio = time.time()
        elementos_set, operaciones = A(n)
        fin = time.time()
        tiempo = fin - inicio
        
        n_factorial = 1
        for i in range(1, n + 1):
            n_factorial *= i
        
        resultados.append({
            'n': n,
            'Elementos en S': elementos_set,
            'Operaciones': operaciones,
            'Tiempo (s)': tiempo,
            'n³': n**3,
            'n!': n_factorial
        })
        
        print(f"{n:<5} {elementos_set:<12} {operaciones:<12} {tiempo:<12.6f} {n**3:<8} {n_factorial:<10}")
    
    # Crear tabla de resultados
    df = pd.DataFrame(resultados)
    print("\n=== TABLA DE RESULTADOS ===")
    print(df.to_string(index=False))
    print()
    
    # Crear grafica comparativa
    plt.figure(figsize=(12, 8))
    plt.plot(df['n'], df['Operaciones'], 'bo-', label='Operaciones reales', linewidth=2, markersize=8)
    plt.plot(df['n'], df['n³'], 'ro-', label='n³', linewidth=2, markersize=8)
    plt.plot(df['n'], df['n!'], 'go-', label='n!', linewidth=2, markersize=8)
    
    plt.xlabel('n')
    plt.ylabel('Numero de operaciones')
    plt.title('Comparacion: Operaciones reales vs n³ vs n!')
    plt.yscale('log')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('ejercicio5_grafica.png', dpi=300, bbox_inches='tight')
    plt.close()  # Cerrar la figura para liberar memoria
    
    return df

def ejecutar_ejercicio5():
    """
    Funcion principal para ejecutar el ejercicio 5
    """
    print("EJERCICIO 5 - VERIFICACION DE ENUNCIADOS DE NOTACION BIG-OH")
    print("=" * 70)
    
    # Analisis de cada enunciado
    analizar_enunciado_a()
    print()
    analizar_enunciado_b()
    print()
    analizar_enunciado_c()
    print()
    
    # Demostracion practica del programa A(n)
    resultados = demostrar_programa_a()
    
    return resultados

if __name__ == "__main__":
    ejecutar_ejercicio5()
