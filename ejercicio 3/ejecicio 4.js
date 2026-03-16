public class Bus {
    private int capacidad;
    private int pasajeros;
    private double precio;
    private double totalRecaudado;
    public Bus(int capacidad) {
        this.capacidad = capacidad;
        this.pasajeros = 0;
        this.precio = 1.50;
        this.totalRecaudado = 0;
    }
    public int getCapacidad() {
        return capacidad;
    }
    public int getPasajeros() {
        return pasajeros;
    }
    public double getPrecio() {
        return precio;
    }
    public double getTotalRecaudado() {
        return totalRecaudado;
    }
    public void subir(int cantidad) {
        if (cantidad <= 0) {
            System.out.println("La cantidad debe ser positiva");
            return;
        }
        if (pasajeros + cantidad <= capacidad) {
            pasajeros += cantidad;
            System.out.println("✓ Subieron " + cantidad + " pasajeros. Total: " + pasajeros);
        } else {
            int disponibles = capacidad - pasajeros;
            System.out.println("✗ Solo pueden subir " + disponibles + " pasajeros");
            if (disponibles > 0) {
                pasajeros = capacidad;
                System.out.println("  Subieron " + disponibles + " pasajeros. Bus lleno");
            }
        }
    }
    public double cobrar() {
        if (pasajeros > 0) {
            double cobro = pasajeros * precio;
            totalRecaudado += cobro;
            System.out.println("💰 Cobro total: Bs. " + String.format("%.2f", cobro));
            System.out.println("   Total recaudado: Bs. " + String.format("%.2f", totalRecaudado));
            return cobro;
        } else {
            System.out.println("No hay pasajeros para cobrar");
            return 0;
        }
    }
    public int asientosLibres() {
        int libres = capacidad - pasajeros;
        System.out.println("💺 Asientos libres: " + libres + " de " + capacidad);
        return libres;
    }
    public void mostrarEstado() {
        System.out.println("\n" + "=".repeat(30));
        System.out.println("ESTADO DEL BUS");
        System.out.println("=".repeat(30));
        System.out.println("Capacidad: " + capacidad);
        System.out.println("Pasajeros: " + pasajeros);
        System.out.println("Asientos libres: " + (capacidad - pasajeros));
        System.out.println("Total recaudado: Bs. " + String.format("%.2f", totalRecaudado));
        System.out.println("=".repeat(30) + "\n");
    }
    public static void main(String[] args) {
        Bus miBus = new Bus(20);
        System.out.println("=== SIMULADOR DE BUS ===\n");
        miBus.subir(15);
        miBus.cobrar();
        miBus.asientosLibres();
        miBus.subir(10); 
        miBus.cobrar();
        miBus.asientosLibres();
        miBus.mostrarEstado();
    }
}