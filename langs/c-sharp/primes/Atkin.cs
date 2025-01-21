using System;
using System.Collections;
using System.Collections.Generic;

namespace Primes
{
    public sealed class Atkin
    {
        private const int UPPER_BOUND = 5000000;
        private const int PREFIX = 32338;

        private sealed class Node
        {
            public Dictionary<char, Node> children = new Dictionary<char, Node>();
            public bool terminal = false;
        }

        private sealed class Sieve
        {
            private readonly int limit;
            private readonly BitArray prime;

            public Sieve(int limit)
            {
                this.limit = limit;
                this.prime = new BitArray(limit + 1, false);
            }

            public IEnumerable<int> ToList()
            {
                var result = new List<int> { 2, 3 };
                for (int p = 5; p <= this.limit; p++)
                {
                    if (this.prime.Get(p))
                    {
                        result.Add(p);
                    }
                }
                return result;
            }

            public Sieve OmitSquares()
            {
                for (int r = 5; r * r < this.limit; r++)
                {
                    if (this.prime.Get(r))
                    {
                        for (int i = r * r; i < this.limit; i += r * r)
                        {
                            this.prime.Set(i, false);
                        }
                    }
                }
                return this;
            }

            public void Step1(int x, int y)
            {
                int n = (4 * x * x) + (y * y);
                if (n <= this.limit && (n % 12 == 1 || n % 12 == 5))
                {
                    this.prime.Set(n, !this.prime.Get(n));
                }
            }

            public void Step2(int x, int y)
            {
                int n = (3 * x * x) + (y * y);
                if (n <= this.limit && n % 12 == 7)
                {
                    this.prime.Set(n, !this.prime.Get(n));
                }
            }

            public void Step3(int x, int y)
            {
                int n = (3 * x * x) - (y * y);
                if (x > y && n <= this.limit && n % 12 == 11)
                {
                    this.prime.Set(n, !this.prime.Get(n));
                }
            }

            public void LoopY(int x)
            {
                for (int y = 1; y * y < limit; y++)
                {
                    Step1(x, y);
                    Step2(x, y);
                    Step3(x, y);
                }
            }

            public void LoopX()
            {
                for (int x = 1; x * x < limit; x++)
                {
                    LoopY(x);
                }
            }

            public Sieve Calc()
            {
                LoopX();
                return OmitSquares();
            }
        }

        private static Node GenerateTree(IEnumerable<int> l)
        {
            var root = new Node();
            foreach (var el in l)
            {
                var head = root;
                foreach (var ch in el.ToString())
                {
                    if (!head.children.ContainsKey(ch))
                    {
                        head.children[ch] = new Node();
                    }
                    head = head.children[ch];
                }
                head.terminal = true;
            }
            return root;
        }

        private static IEnumerable<int> Find(int upperBound, int prefix)
        {
            var sieve = new Sieve(upperBound).Calc();
            var primes = sieve.ToList();
            var strPrefix = prefix.ToString();
            var head = GenerateTree(primes);

            foreach (var ch in strPrefix)
            {
                if (head.children.ContainsKey(ch))
                {
                    head = head.children[ch];
                }
                else
                {
                    return null;
                }
            }

            var queue = new Queue<KeyValuePair<Node, string>>();
            queue.Enqueue(new KeyValuePair<Node, string>(head, strPrefix));

            var result = new List<int>();

            while (queue.Count > 0)
            {
                var queueTop = queue.Dequeue();
                var top = queueTop.Key;
                var currentPrefix = queueTop.Value;
                if (top.terminal)
                {
                    if (int.TryParse(currentPrefix, out int prime))
                    {
                        result.Add(prime);
                    }
                }
                foreach (var entry in top.children)
                {
                    queue.Enqueue(new KeyValuePair<Node, string>(entry.Value, currentPrefix + entry.Key));
                }
            }
            return result;
        }

        public static void Main(string[] args)
        {
            var start = DateTime.Now;

            Console.WriteLine(string.Join(", ", Find(UPPER_BOUND, PREFIX)));

            var end = DateTime.Now;
            var duration = end - start;

            Console.WriteLine("Execution time: " + duration.TotalMilliseconds + "ms");
        }
    }
}
