using System;
using System.Collections.Generic;

namespace Treap
{
    public sealed class Naive
    {
        // Nested SplitResult class
        public sealed class SplitResult
        {
            public Node lower;
            public Node equal;
            public Node greater;

            public SplitResult(Node lower, Node equal, Node greater)
            {
                this.lower = lower;
                this.equal = equal;
                this.greater = greater;
            }
        }

        // Nested NodePair class
        public sealed class NodePair
        {
            public Node first;
            public Node second;

            public NodePair(Node first, Node second)
            {
                this.first = first;
                this.second = second;
            }
        }

        // Nested Node class
        public sealed class Node
        {
            public static Random random = new Random();

            public int x;
            public int y;
            public Node left = null;
            public Node right = null;

            public Node(int x)
            {
                this.x = x;
                this.y = random.Next();
            }

            public static Node merge(Node lower, Node greater)
            {
                if (lower == null)
                    return greater;

                if (greater == null)
                    return lower;

                if (lower.y < greater.y)
                {
                    lower.right = merge(lower.right, greater);
                    return lower;
                }
                else
                {
                    greater.left = merge(lower, greater.left);
                    return greater;
                }
            }

            public static NodePair splitBinary(Node orig, int value)
            {
                if (orig == null)
                    return new NodePair(null, null);

                if (orig.x < value)
                {
                    NodePair splitPair = splitBinary(orig.right, value);
                    orig.right = splitPair.first;
                    return new NodePair(orig, splitPair.second);
                }
                else
                {
                    NodePair splitPair = splitBinary(orig.left, value);
                    orig.left = splitPair.second;
                    return new NodePair(splitPair.first, orig);
                }
            }

            public static Node merge(Node lower, Node equal, Node greater)
            {
                return merge(merge(lower, equal), greater);
            }

            public static SplitResult split(Node orig, int value)
            {
                NodePair lowerOther = splitBinary(orig, value);
                NodePair equalGreater = splitBinary(lowerOther.second, value + 1);
                return new SplitResult(lowerOther.first, equalGreater.first, equalGreater.second);
            }
        }

        // Nested Tree class
        public sealed class Tree
        {
            private Node mRoot = null;

            public bool hasValue(int x)
            {
                SplitResult splited = Node.split(mRoot, x);
                bool res = splited.equal != null;
                mRoot = Node.merge(splited.lower, splited.equal, splited.greater);
                return res;
            }

            public void insert(int x)
            {
                SplitResult splited = Node.split(mRoot, x);
                if (splited.equal == null)
                    splited.equal = new Node(x);
                mRoot = Node.merge(splited.lower, splited.equal, splited.greater);
            }

            public void erase(int x)
            {
                SplitResult splited = Node.split(mRoot, x);
                mRoot = Node.merge(splited.lower, splited.greater);
            }
        }

        public static void Main(string[] args)
        {
            long start = DateTime.Now.Ticks / TimeSpan.TicksPerMillisecond;

            Tree tree = new Tree();
            int cur = 5;
            int res = 0;

            for (int i = 1; i < 1000000; i++)
            {
                int a = i % 3;
                cur = (cur * 57 + 43) % 10007;
                if (a == 0)
                {
                    tree.insert(cur);
                }
                else if (a == 1)
                {
                    tree.erase(cur);
                }
                else if (a == 2)
                {
                    bool hasVal = tree.hasValue(cur);
                    if (hasVal)
                        res++;
                }
            }
            Console.WriteLine(res);

            long end = DateTime.Now.Ticks / TimeSpan.TicksPerMillisecond;
            long duration = end - start;

            Console.WriteLine("Execution time: " + duration + "ms");
        }
    }
}
