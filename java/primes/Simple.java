package primes;

public final class Simple {
    private static final int NUMBER = 100000;

    public static void printPrimes(final int count) {
        for (var i = 1; i <= count; i++) {
            if (i == 1 || i == 0) {
                continue;
            }

            boolean isPrime = true;

            for (var j = 2; j <= i / 2; ++j) {
                if (i % j == 0) {
                    isPrime = false;
                    break;
                }
            }

            if (isPrime) {
                System.out.println(i);
            }
        }
    }

    public static void main(String[] args) {
        printPrimes(NUMBER);
    }
}