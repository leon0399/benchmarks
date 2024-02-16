package primes;

public final class Simple {
    private static final int NUMBER = 100000;

    public static int printPrimes(final int count) {
        int lastPrime = 2;

        for (var i = 2; i <= count; i++) {
            boolean isPrime = true;

            for (var j = 2; j <= i / 2; ++j) {
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