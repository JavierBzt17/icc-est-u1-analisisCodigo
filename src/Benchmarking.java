import java.util.Random;

public class Benchmarking {
    private MetodosOrdenamiento metodosOrdenamiento;

    public Benchmarking(){
        //long inicioMillis = System.currentTimeMillis();
        //long inicioNano = System.nanoTime();

        //System.out.println(inicioMillis);
        //System.out.println(inicioNano);

        metodosOrdenamiento = new MetodosOrdenamiento();
        int[] arreglo = generarArregloAleatorio(1000000);
        Runnable tarea = () -> metodosOrdenamiento.burbujaTradicional(arreglo);

        double tiempoConNanoTime = medirConNanoTime(tarea);
        System.out.println("Tiempo con nanoTime: " + tiempoConNanoTime + " segundos");
        double tiempoConCurrentTime = medirConCurrentTime(tarea);
        System.out.println("Tiempo con currentTime: " + tiempoConCurrentTime + " segundos");

    }
    private int [] generarArregloAleatorio(int tamaño) {
        int[] arreglo = new int[tamaño];
        Random random = new Random();
        for (int i = 0; i < tamaño; i++) {
            arreglo[i] = random.nextInt(100_000); 
        }
        return arreglo;

    }

    public double medirConNanoTime(Runnable tarea){
        long inicio = System.nanoTime();
        tarea.run();
        long fin = System.nanoTime();
        return (fin - inicio) / 1_000_000_000.0;
    }

    public double medirConCurrentTime(Runnable tarea){
        long inicio = System.currentTimeMillis();
        tarea.run();
        long fin = System.currentTimeMillis();
        return (fin - inicio) / 1000.0; 
    }
}
