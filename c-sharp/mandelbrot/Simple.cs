using System;

class Program
{
    static void Main()
    {
        var startTime = DateTime.Now;

        Index();

        var endTime = DateTime.Now;
        var duration = endTime - startTime;
        Console.WriteLine("Execution time: " + duration.TotalMilliseconds + "ms");
    }

    static void Index()
    {
        for (int y = -39; y < 39; y++)
        {
            Console.WriteLine();

            for (int x = -39; x < 39; x++)
            {
                int i = Mandelbrot(x / 40.0, y / 40.0);

                if (i == 0)
                {
                    Console.Write("*");
                }
                else
                {
                    Console.Write(" ");
                }
            }
        }

        Console.WriteLine();
    }

    static int Mandelbrot(double x, double y)
    {
        double cr = y - 0.5;
        double ci = x;
        double zi = 0.0;
        double zr = 0.0;
        int i = 0;

        while (true)
        {
            i++;

            double temp = zr * zi;

            double zr2 = zr * zr;
            double zi2 = zi * zi;

            zr = zr2 - zi2 + cr;
            zi = temp + temp + ci;

            if (zi2 + zr2 > 16)
            {
                return i;
            }

            if (i > 5000)
            {
                return 0;
            }
        }
    }
}
