using System;
using System.Collections.Generic;

namespace Collatz
{
    public sealed class MaxSequence
    {
        private const int NUMBER = 500000;

        public static int collatz(int x)
        {
            var len = 0;

            while (x > 1)
            {
                if (x % 2 == 0)
                {
                    x = x / 2;
                }
                else
                {
                    x = 3 * x + 1;
                }

                len++;
            }

            return len;
        }

        public static KeyValuePair<int, int> findMaxCollatz(int to)
        {
            var result = new KeyValuePair<int, int>(1, 1);

            for (var number = 1; number <= to; number++)
            {
                int len = collatz(number);

                if (len > result.Value)
                {
                    result = new KeyValuePair<int, int>(number, len);
                }
            }

            return result;
        }

        public static void Main(string[] args)
        {
            long start = DateTime.Now.Ticks / TimeSpan.TicksPerMillisecond;

            Console.WriteLine(findMaxCollatz(NUMBER));

            long end = DateTime.Now.Ticks / TimeSpan.TicksPerMillisecond;
            long duration = end - start;

            Console.WriteLine("Execution time: " + duration + "ms");
        }
    }
}
