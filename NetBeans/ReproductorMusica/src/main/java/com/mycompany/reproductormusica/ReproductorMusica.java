
package com.mycompany.reproductormusica;

public class ReproductorMusica {
    
    //ATRIBUTOS
    private String[] canciones;
    private int[] cancionesFavoritas;
    private boolean pausado;
    private int cancionReproduciendo;
    
    
    //CONSTRUCTOR
    public ReproductorMusica(String[] canciones) {
        //COMPLETE AQUÍ LA LÓGICA DEL CONSTRUCTOR SEGÚN EL ENUNCIADO
        this.canciones = canciones;
        cancionesFavoritas = new int [this.canciones.length];
        pausado = true; 
        cancionReproduciendo = 0; 
        
        for(int i = 0; i < cancionesFavoritas.length; i++){
            cancionesFavoritas[i] = -1;
            }
        }
    
    
    //MÉTODOS    
    public void proximaCancion(){
        //COMPLETE AQUÍ LA LÓGICA DE ESTE MÉTODO SEGÚN EL ENUNCIADO
        this.cancionReproduciendo = (cancionReproduciendo + 1) % canciones.length;
    }
    
    public void devolverCancion(){
        //COMPLETE AQUÍ LA LÓGICA DE ESTE MÉTODO SEGÚN EL ENUNCIADO
        this.cancionReproduciendo = (cancionReproduciendo + canciones.length - 1) % canciones.length;
    }
    
    public void cambiarEstadoReproduccion(){
        //COMPLETE AQUÍ LA LÓGICA DE ESTE MÉTODO SEGÚN EL ENUNCIADO
        if (pausado == true){
            pausado = false;
        } else {
            pausado = true;
        }
    }
    
    //NO SE DEBE PREOCUPAR POR DESARROLLAR ESTE MÉTODO. ¡NO ELIMINARLO NI MODIFICARLO!
    public void agregarCancionesFavoritas(){
        for(int i = 0; i < cancionesFavoritas.length; i++)
            /*En caso de que encuentre que cancionReproduciendo está en el banco de cancionesFavoritas
            no seguimos buscando espacio libre para agregarla, y salimos del método*/
            if(cancionesFavoritas[i] == cancionReproduciendo)
                return;
            //Pero si no la encontró, y además encuentra un espacio donde añadirlo, lo hace
            else if(cancionesFavoritas[i] == -1){
                cancionesFavoritas[i] = cancionReproduciendo;
                return;
            }                
    }

    public String[] getCanciones() {
        //COMPLETE AQUÍ EL GETTER CORRESPONDIENTE
        return canciones;
    }

    public void setCanciones(String[] canciones) {
        //COMPLETE AQUÍ EL SETTER CORRESPONDIENTE
        this.canciones = canciones;
    }

    public int[] getCancionesFavoritas() {
        //COMPLETE AQUÍ EL GETTER CORRESPONDIENTE
        return cancionesFavoritas;
    }

    public void setCancionesFavoritas(int[] cancionesFavoritas) {
        //COMPLETE AQUÍ EL SETTER CORRESPONDIENTE
        this.cancionesFavoritas = cancionesFavoritas;
    }

    public boolean isPausado() {
        //COMPLETE AQUÍ EL GETTER CORRESPONDIENTE
        return pausado;
    }

    public void setPausado(boolean pausado) {
        //COMPLETE AQUÍ EL SETTER CORRESPONDIENTE
        this.pausado = pausado;
    }

    public int getCancionReproduciendo() {
        //COMPLETE AQUÍ EL GETTER CORRESPONDIENTE
        return cancionReproduciendo;
    }

    public void setCancionReproduciendo(int cancionReproduciendo) {
        //COMPLETE AQUÍ EL SETTER CORRESPONDIENTE
        this.cancionReproduciendo = cancionReproduciendo;
    }
    
    
    public static void main (String args[]){
    
    String [] cancionesEscogidas = new String [] {
        "Mil horas",
        "Por ese hombre",
        "A esa",
        "Algo de mi",
        "Si me dejas ahora",
        "¿Quieres ser mi amante?",
        "Quel sorriso in volto",
        "Per una notte insieme",
        "Como un pintor",
        "Sencillamente",
        "Un segundo",
        "Enciéndeme",
        "Cuando me enamoro",
        "Tu eres mi tesoro",
        "Piccola anima",
        "Solo a ti pertenezco",
        "Todos por todos"
    };
    
    ReproductorMusica ventana1 =new ReproductorMusica(cancionesEscogidas);
        //Screenshot 2
        ventana1.devolverCancion();
        ventana1.devolverCancion();
        ventana1.devolverCancion();
        ventana1.devolverCancion();
        //Screenshot 3
        ventana1.agregarCancionesFavoritas();
        ventana1.proximaCancion();
        ventana1.agregarCancionesFavoritas();
        ventana1.devolverCancion();
        ventana1.agregarCancionesFavoritas();
        //Screenshot 4
        ventana1.cambiarEstadoReproduccion();
        ventana1.cambiarEstadoReproduccion();
        ventana1.cambiarEstadoReproduccion();
        ventana1.cambiarEstadoReproduccion();
        ventana1.cambiarEstadoReproduccion();
        
}
}