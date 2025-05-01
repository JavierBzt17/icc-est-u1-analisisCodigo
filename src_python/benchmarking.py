import random
import time
from metodos_ordenamiento import MetodosOrdenamiento 


class Benchmarking:
    def __init__(self):
        print("Bench inicializado.")

    def ejemplo(self):
        self.mOrdenamiento = MetodosOrdenamiento()
        arreglo = self.build_Arreglo(50000)

        tarea = lambda: self.mOrdenamiento.sort_by_bubble(arreglo)
        tiempoMillis = self.contar_con_current_times_milles(tarea)
        tiempoNano = self.contar_con_nano_time(tarea)
        medir_tiempo = self.medir_tiempo(tarea, arreglo)

        print(f"Tiempo en milisegundos: {tiempoMillis} ")
        print(f"Tiempo en nanosegundos: {tiempoNano} ")
        print(f"Tiempo en segundos: {medir_tiempo} ")


    def build_Arreglo(self, tamaño):
        array = []
        for i in range(tamaño):
            numero = random.randint(0, 99999)
            array.append(numero)
        return array
    

    # x = time.time()
    def contar_con_current_times_milles(self, tarea):
        inicio = time.time()
        tarea()
        fin = time.time()
        return fin - inicio 
    
    # x = time.time_ns()
    def contar_con_nano_time(self, tarea):
        inicio = time.time_ns()
        tarea()
        fin = time.time_ns()    
        return (fin - inicio)  / 1_000_000_000.0
    
    def medir_tiempo(self, tarea, array):
        inicio = time.perf_counter()
        tarea(array)
        fin = time.perf_counter()
        return fin - inicio
    

