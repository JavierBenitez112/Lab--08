"""
Laboratorio 8 - Análisis de Complejidad Algorítmica
Archivo principal que ejecuta todos los ejercicios automáticamente con límite de tiempo
"""

import sys
import os
import time
import threading
import pandas as pd
from datetime import datetime
import matplotlib
matplotlib.use('Agg')  # Usar backend sin interfaz gráfica para evitar problemas

# Importar todos los módulos de ejercicios
from ejercicio1 import ejecutar_ejercicio1
from ejercicio2 import ejecutar_ejercicio2
from ejercicio3 import ejecutar_ejercicio3
from ejercicio4 import ejecutar_ejercicio4
from ejercicio5 import ejecutar_ejercicio5

class TimeoutException(Exception):
    """Excepción para manejar timeouts"""
    pass

def ejecutar_con_timeout(funcion, nombre, limite_tiempo=40):
    """
    Ejecuta una función con un límite de tiempo (compatible con Windows)
    """
    resultado_contenedor = {'completado': False, 'resultado': None, 'error': None}
    
    def wrapper():
        try:
            resultado_contenedor['resultado'] = funcion()
            resultado_contenedor['completado'] = True
        except Exception as e:
            resultado_contenedor['error'] = str(e)
    
    inicio = time.time()
    hilo = threading.Thread(target=wrapper, daemon=True)
    hilo.start()
    hilo.join(timeout=limite_tiempo)
    fin = time.time()
    tiempo_ejecucion = fin - inicio
    
    if hilo.is_alive():
        # El hilo todavía está ejecutándose, excedió el tiempo límite
        return {
            'estado': 'Timeout',
            'tiempo': tiempo_ejecucion,
            'resultado': None,
            'error': f'Excedió el límite de {limite_tiempo} segundos'
        }
    elif resultado_contenedor['error']:
        # Hubo un error durante la ejecución
        return {
            'estado': 'Error',
            'tiempo': tiempo_ejecucion,
            'resultado': None,
            'error': resultado_contenedor['error']
        }
    else:
        # Se completó exitosamente
        return {
            'estado': 'Completado',
            'tiempo': tiempo_ejecucion,
            'resultado': resultado_contenedor['resultado'],
            'error': None
        }

def ejecutar_todos_los_ejercicios():
    """
    Ejecuta todos los ejercicios en secuencia automáticamente con límite de tiempo
    """
    print("=" * 100)
    print("LABORATORIO 8 - ANÁLISIS DE COMPLEJIDAD ALGORÍTMICA")
    print("EJECUTANDO TODOS LOS EJERCICIOS CON LIMITE DE 40 SEGUNDOS")
    print("=" * 100)
    print()
    
    ejercicios = [
        ("Ejercicio 1", ejecutar_ejercicio1, "O(n² log n)"),
        ("Ejercicio 2", ejecutar_ejercicio2, "O(n)"),
        ("Ejercicio 3", ejecutar_ejercicio3, "O(n²)"),
        ("Ejercicio 4", ejecutar_ejercicio4, "Busqueda Lineal"),
        ("Ejercicio 5", ejecutar_ejercicio5, "Verificacion Big-Oh")
    ]
    
    # Lista para almacenar resultados
    resultados = []
    inicio_total = time.time()
    
    print(f"{'Ejercicio':<15} {'Complejidad':<20} {'Estado':<12} {'Tiempo (s)':<12} {'Error':<30}")
    print("-" * 100)
    
    for i, (nombre, funcion, complejidad) in enumerate(ejercicios, 1):
        print(f"{nombre:<15} {complejidad:<20} {'Ejecutando...':<12} {'':<12} {'':<30}", end='\r')
        
        resultado = ejecutar_con_timeout(funcion, nombre, 40)
        
        # Actualizar la línea con el resultado
        tiempo_str = f"{resultado['tiempo']:.2f}" if resultado['tiempo'] > 0 else "0.00"
        error_str = resultado['error'][:28] + "..." if resultado['error'] and len(resultado['error']) > 30 else resultado['error'] or ""
        
        print(f"{nombre:<15} {complejidad:<20} {resultado['estado']:<12} {tiempo_str:<12} {error_str:<30}")
        
        # Guardar resultado
        resultados.append({
            'Ejercicio': nombre,
            'Complejidad': complejidad,
            'Estado': resultado['estado'],
            'Tiempo (segundos)': resultado['tiempo'],
            'Error': resultado['error'] or 'N/A'
        })
        
        # Pausa breve entre ejercicios
        if i < len(ejercicios):
            time.sleep(0.5)
    
    fin_total = time.time()
    tiempo_total = fin_total - inicio_total
    
    # Crear DataFrame y mostrar tabla completa
    df = pd.DataFrame(resultados)
    
    print("\n" + "=" * 100)
    print("TABLA COMPLETA DE RESULTADOS")
    print("=" * 100)
    print(df.to_string(index=False))
    
    # Estadísticas adicionales
    completados = len([r for r in resultados if r['Estado'] == 'Completado'])
    timeouts = len([r for r in resultados if r['Estado'] == 'Timeout'])
    errores = len([r for r in resultados if r['Estado'] == 'Error'])
    
    print(f"\nESTADISTICAS:")
    print(f"   Ejercicios completados: {completados}/{len(ejercicios)}")
    print(f"   Ejercicios con timeout: {timeouts}/{len(ejercicios)}")
    print(f"   Ejercicios con error: {errores}/{len(ejercicios)}")
    print(f"   Tiempo total de ejecucion: {tiempo_total:.2f} segundos")
    
    # Guardar resultados en CSV
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    archivo_csv = f"resultados_lab8_{timestamp}.csv"
    df.to_csv(archivo_csv, index=False)
    print(f"   Resultados guardados en: {archivo_csv}")
    
    print("\n" + "=" * 100)
    print("EJECUCION COMPLETADA")
    print("Las graficas de los ejercicios 1, 2 y 3 han sido guardadas en archivos PNG")
    print("=" * 100)
    
    return df

def main():
    """
    Funcion principal del programa
    """
    try:
        resultados = ejecutar_todos_los_ejercicios()
        return resultados
    except KeyboardInterrupt:
        print("\n\nPrograma interrumpido por el usuario.")
    except Exception as e:
        print(f"\nError inesperado: {str(e)}")

if __name__ == "__main__":
    main()
