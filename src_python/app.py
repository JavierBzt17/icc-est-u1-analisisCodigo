from benchmarking import Benchmarking
from metodos_ordenamiento import MetodosOrdenamiento

if __name__ == "__main__":
    print ("Funciona")


    metodos  = MetodosOrdenamiento()
    benchmark = Benchmarking()
    tam = 10000
    arreglo_base = benchmark.build_Arreglo(tam)

    burbuja = metodos.sort_by_bubble(arreglo_base)
    seleccion = metodos.sort_by_selection(arreglo_base)

    dicc = {
        "Burbuja": metodos.sort_by_bubble,
        "Seleccion": metodos.sort_by_selection,
    }

    resultados = []
    for nombre, metodo in dicc.items():
        tiempo = benchmark.medir_tiempo(metodo, arreglo_base)
        tuplaResultado = (tam, nombre, tiempo)
        resultados.append(tuplaResultado)

    for resultado in resultados:
        tam, nombre, tiempo = resultado
        print(f"Tamaño: {tam}, Método: {nombre}, Tiempo: {tiempo:.6f} segundos")

