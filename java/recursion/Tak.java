package recursion;

public class Tak {

    public static void main(String[] args) {
        long startTimeMs = System.currentTimeMillis();

        System.out.println(tak(30, 22, 12));

        long endTimeMs = System.currentTimeMillis();
        long durationMs = endTimeMs - startTimeMs;

        System.out.println("Execution time: " + durationMs + "ms");
    }

    public static int tak(int x, int y, int z) {
        if (y < x) {
            return tak(tak(x - 1, y, z), tak(y - 1, z, x), tak(z - 1, x, y));
        } else {
            return z;
        }
    }
}
