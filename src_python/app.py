from benchmarking import Benchmarking
from metodos_ordenamiento import MetodosOrdenamiento
import matplotlib.pyplot as plt
import datetime as datetime 

fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if __name__ == "__main__":
    print ("Funciona")


    metodos  = MetodosOrdenamiento()
    benchmark = Benchmarking()

    tamaños = [500, 1000, 2000]
    resultados = []
    for tam in tamaños:
        arreglo_base = benchmark.build_Arreglo(tam)

        burbuja = metodos.sort_by_bubble(arreglo_base)
        seleccion = metodos.sort_by_selection(arreglo_base)

        dicc = {
            "Burbuja": metodos.sort_by_bubble,
            "Seleccion": metodos.sort_by_selection,
        }

        for nombre, metodo in dicc.items():
            tiempo = benchmark.medir_tiempo(metodo, arreglo_base)
            tuplaResultado = (tam, nombre, tiempo)
            resultados.append(tuplaResultado)

        for resultado in resultados:
            tam, nombre, tiempo = resultado
            print(f"Tamaño: {tam}, Método: {nombre}, Tiempo: {tiempo:.6f} segundos")

    tiempos_by_metodo = {
        "Burbuja" : [],
        "Seleccion" : [],
    }

    for tamaño, nombre, tiempo in resultados:  
        tiempos_by_metodo[nombre].append(tiempo)

    #Crear una grafica
    plt.figure(figsize=(10, 6))
    #graficar una linea de tiempo para cada metodo 
    # el x sean los tiempos obtenidos 
    # el y sean los tamaños de los arreglos
    for nombre, tiempos in tiempos_by_metodo.items():
        plt.plot(tamaños, tiempos, label=nombre, marker = 'o')

    plt.xlabel("Tamaño del arreglo")
    plt.ylabel("Tiempo (segundos)")
    plt.title(f"Comparacion de metodos\nJavier Barrezueta {fecha_hora}")
    plt.legend()
    plt.grid(True)
    plt.show()


