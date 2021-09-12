package mandelbrot;

public final class Simple {
    public static final int SIZE = 40;

    public static void index() {
        for (var y = -39; y < 39; y++) {
            System.out.println();

            for (var x = -39; x < 39; x++) {
                int i = mandelbrot(
                    x / 40.0,
                    y / 40.0
                );

                if (i == 0) {
                    System.out.print("*");
                } else {
                    System.out.print(" ");
                }
            }
        }
    }

    public static int mandelbrot(double x, double y) {
        double cr = y - 0.5;
        double ci = x;
        double zi = 0.0;
        double zr = 0.0;
        int i = 0;

        while (true) {
            i++;

            double temp = zr * zi;

            double zr2 = zr * zr;
            double zi2 = zi * zi;

            zr = zr2 - zi2 + cr;
            zi = temp + temp + ci;

            if (zi2 + zr2 > 16) {
                return i;
            }

            if (i > 5000) {
                return 0;
            }
        }
    }

    public static void main(String[] args) {
        index();
    }
}