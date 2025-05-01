class MetodosOrdenamiento:
    def sort_by_bubble(self, arreglo):
        arreglo = arreglo.copy()
        n = len(arreglo)
        for i in range (n):
            for j in range (i + 1, n):
                if arreglo [i] > arreglo [j]:
                    ##aux = arreglo [i]
                    ##arreglo [i] = arreglo [j]
                    ##arreglo [j] = aux 
                    ##Solo en Python
                    arreglo [i], arreglo [j] = arreglo [j], arreglo [i]
        return arreglo
    
    def sort_by_selection(self, array):
        array = array.copy()
        n = len(array)
        for i in range(n - 1):
            min_index = i
            for j in range(n):
                if array[min_index] < array[j]:
                    min_index = j
            if min_index != i:
                aux = array[min_index]
                array[min_index] = array[i]
                array[i] = aux
        return array

        