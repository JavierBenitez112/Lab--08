"""
Laboratorio 8 - Análisis de Complejidad Algorítmica
Archivo principal que ejecuta todos los ejercicios automáticamente
"""

import sys
import os
import time

# Importar todos los módulos de ejercicios
from ejercicio1 import ejecutar_ejercicio1
from ejercicio2 import ejecutar_ejercicio2
from ejercicio3 import ejecutar_ejercicio3
from ejercicio4 import ejecutar_ejercicio4
from ejercicio5 import ejecutar_ejercicio5

def ejecutar_todos_los_ejercicios():
    """
    Ejecuta todos los ejercicios en secuencia automáticamente
    """
    print("=" * 80)
    print("LABORATORIO 8 - ANÁLISIS DE COMPLEJIDAD ALGORÍTMICA")
    print("EJECUTANDO TODOS LOS EJERCICIOS AUTOMÁTICAMENTE")
    print("=" * 80)
    print()
    
    ejercicios = [
        ("Ejercicio 1", ejecutar_ejercicio1),
        ("Ejercicio 2", ejecutar_ejercicio2),
        ("Ejercicio 3", ejecutar_ejercicio3),
        ("Ejercicio 4", ejecutar_ejercicio4),
        ("Ejercicio 5", ejecutar_ejercicio5)
    ]
    
    inicio_total = time.time()
    
    for i, (nombre, funcion) in enumerate(ejercicios, 1):
        print(f"\n{'='*25} {nombre} {'='*25}")
        print(f"Progreso: {i}/{len(ejercicios)} ejercicios")
        print()
        
        try:
            inicio_ejercicio = time.time()
            funcion()
            fin_ejercicio = time.time()
            tiempo_ejercicio = fin_ejercicio - inicio_ejercicio
            
            print(f"\n✅ {nombre} completado exitosamente en {tiempo_ejercicio:.2f} segundos.")
            
        except Exception as e:
            print(f"\n❌ Error en {nombre}: {str(e)}")
        
        # Pausa breve entre ejercicios para mejor legibilidad
        if i < len(ejercicios):
            print("\n" + "-" * 60)
            time.sleep(1)  # Pausa de 1 segundo entre ejercicios
    
    fin_total = time.time()
    tiempo_total = fin_total - inicio_total
    
    print("\n" + "=" * 80)
    print("🎉 TODOS LOS EJERCICIOS COMPLETADOS")
    print(f"⏱️  Tiempo total de ejecución: {tiempo_total:.2f} segundos")
    print("📊 Las gráficas han sido guardadas en archivos PNG")
    print("=" * 80)

def main():
    """
    Función principal del programa
    """
    try:
        ejecutar_todos_los_ejercicios()
    except KeyboardInterrupt:
        print("\n\n⚠️  Programa interrumpido por el usuario.")
    except Exception as e:
        print(f"\n❌ Error inesperado: {str(e)}")

if __name__ == "__main__":
    main()
