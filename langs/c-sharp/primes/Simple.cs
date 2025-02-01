using System;

namespace Primes
{
    public sealed class Simple
    {
        private const int NUMBER = 1000000;

        public static int PrintPrimes(int count)
        {
            int lastPrime = 2;

            for (int i = 3; i <= count; i += 2)
            {
                bool isPrime = true;
                int limit = (int)Math.Sqrt(i);

                for (int j = 3; j <= limit; j += 2)
                {
                    if (i % j == 0)
                    {
                        isPrime = false;
                        break;
                    }
                }

                if (isPrime)
                {
                    lastPrime = i;
                }
            }

            return lastPrime;
        }

        public static void Main(string[] args)
        {
            DateTime start = DateTime.Now;

            long lastPrime = PrintPrimes(NUMBER);
            Console.WriteLine("Last prime: " + lastPrime);

            DateTime end = DateTime.Now;
            TimeSpan duration = end - start;

            Console.WriteLine("Execution time: " + duration.TotalMilliseconds + "ms");
        }
    }
}
