package primes;

public final class Simple {
    private static final int NUMBER = 1000000;

    public static int printPrimes(final int count) {
        int lastPrime = 2;

        for (var i = 3; i <= count; i += 2) {
            boolean isPrime = true;
            int limit = (int) Math.sqrt(i);

            for (var j = 3; j <= limit; j += 2) {
                if (i % j == 0) {
                    isPrime = false;
                    break;
                }
            }

            if (isPrime) {
                lastPrime = i;
            }
        }

        return lastPrime;
    }

    public static void main(String[] args) {
        long start = System.currentTimeMillis();

        long lastPrime = printPrimes(NUMBER);
        System.out.println("Last prime: " + lastPrime);

        long end = System.currentTimeMillis();
        long duration = end - start;

        System.out.println("Execution time: " + duration + "ms");
    }
}