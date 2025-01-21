using System;

namespace Recursion
{
    public class Tak
    {
        public static void Main(string[] args)
        {
            long startTimeMs = DateTime.Now.Ticks / TimeSpan.TicksPerMillisecond;

            Console.WriteLine(tak(30, 22, 12));

            long endTimeMs = DateTime.Now.Ticks / TimeSpan.TicksPerMillisecond;
            long durationMs = endTimeMs - startTimeMs;

            Console.WriteLine("Execution time: " + durationMs + "ms");
        }

        public static int tak(int x, int y, int z)
        {
            if (y < x)
            {
                return tak(tak(x - 1, y, z), tak(y - 1, z, x), tak(z - 1, x, y));
            }
            else
            {
                return z;
            }
        }
    }
}
