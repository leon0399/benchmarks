package collatz;

import java.util.AbstractMap.SimpleEntry;
import java.util.ArrayList;
import java.util.Map;

public final class MaxSequence {
    private static final int NUMBER = 500000;

    public static final int collatz(int x) {
        var len = 0;

        while (x > 1) {
            if (x % 2 == 0) {
                x = x / 2;
            } else {
                x = 3 * x + 1;
            }

            len++;
        }

        return len;
    }

    public static final Map.Entry<Integer, Integer> findMaxCollatz(final int to) {
        Map.Entry<Integer, Integer> result = new SimpleEntry<Integer, Integer>(1, 1);

        for (var number = 1; number <= to; number++) {
            int len = collatz(number);

            if (len > result.getValue()) {
                result = new SimpleEntry<Integer, Integer>(number, len);
            }
        }

        return result;
    }

    public static void main(String[] args) {
        System.out.println(findMaxCollatz(NUMBER));
    }
}