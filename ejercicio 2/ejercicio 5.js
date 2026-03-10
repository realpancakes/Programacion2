import java.util.ArrayList;
import java.util.List;
public class ServidorMinecraftCompleto {
    static class Jugador {
        private String nombre;
        private int diamantes;
        public Jugador(String nombre, int diamantes) {
            this.nombre = nombre;
            this.diamantes = diamantes;
        }
        public String getNombre() {
            return nombre;
        }
        public int getDiamantes() {
            return diamantes;
        }
        public int stacks() {
            return diamantes / 64;
        }
        public int diamantesRestantes() {
            return diamantes % 64;
        }
        @Override
        public String toString() {
            return String.format("%s: %d diamantes (%d stacks + %d)", 
                                nombre, diamantes, stacks(), diamantesRestantes());
        }
    }
    private List<Jugador> jugadores;
    private static final int MAX_JUGADORES = 10;
    public ServidorMinecraftCompleto() {
        this.jugadores = new ArrayList<>();
    }
    public void agregar(String nombre, int diamantes) {
        if (jugadores.size() < MAX_JUGADORES) {
            for (Jugador j : jugadores) {
                if (j.getNombre().equalsIgnoreCase(nombre)) {
                    System.out.println("✗ El jugador " + nombre + " ya existe");
                    return;
                }
            }
            jugadores.add(new Jugador(nombre, diamantes));
            System.out.println("✓ " + nombre + " agregado con " + diamantes + " diamantes");
        } else {
            System.out.println("✗ Servidor lleno");
        }
    }
    public void verificarStacks() {
        System.out.println("\n--- STACKS DE DIAMANTES ---");
        for (Jugador j : jugadores) {
            System.out.println("► " + j.getNombre() + ": " + j.stacks() + " stacks");
        }
    }
    public void maxDiamantes() {
        if (!jugadores.isEmpty()) {
            Jugador maxJ = jugadores.get(0);
            for (Jugador j : jugadores) {
                if (j.getDiamantes() > maxJ.getDiamantes()) {
                    maxJ = j;
                }
            }
            System.out.println("\n🏆 Más diamantes: " + maxJ.getNombre() + 
                             " (" + maxJ.getDiamantes() + ")");
        }
    }
    public void totalDiamantes() {
        int total = 0;
        for (Jugador j : jugadores) {
            total += j.getDiamantes();
        }
        System.out.println("💰 Total diamantes: " + total);
        System.out.println("   Equivalente a: " + (total/64) + " stacks + " + (total%64) + " diamantes");
    }
    public static void main(String[] args) {
        System.out.println("=== SERVIDOR MINECRAFT ===\n");
        ServidorMinecraftCompleto server = new ServidorMinecraftCompleto();
        server.agregar("Steve", 128);
        server.agregar("Alex", 65);
        server.agregar("Creeper", 192);
        server.verificarStacks();
        System.out.println("\n--- ESTADÍSTICAS ---");
        server.maxDiamantes();
        server.totalDiamantes();
    }
}