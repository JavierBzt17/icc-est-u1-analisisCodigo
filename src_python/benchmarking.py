import random
import time
from metodos_ordenamiento import MetodosOrdenamiento 


class Benchmarking:
    def __init__(self):
        print("Bench inicializado.")
        self.mOrdenamiento = MetodosOrdenamiento()
        arreglo = self.build_Arreglo(50000)

        tarea = lambda: self.mOrdenamiento.Sort_By_Bubble(arreglo)
        tiempoMillis = self.contar_con_current_times_milles(tarea)
        tiempoNano = self.contar_con_nano_time(tarea)

        print(f"Tiempo en milisegundos: {tiempoMillis} ")
        print(f"Tiempo en nanosegundos: {tiempoNano} ")  




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