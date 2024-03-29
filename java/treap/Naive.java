package treap;

import java.util.*;
import java.lang.*;

public final class Naive {
    static final class SplitResult {
        SplitResult(Node lower, Node equal, Node greater) {
            this.lower = lower;
            this.equal = equal;
            this.greater = greater;
        }

        public Node lower;
        public Node equal;
        public Node greater;
    }

    static final class NodePair {
        NodePair(Node first, Node second) {
            this.first = first;
            this.second = second;
        }

        public Node first;
        public Node second;
    }

    static final class Node {
        public static Random random = new Random();

        Node(int x) {
            this.x = x;
        }

        int x;
        int y = random.nextInt();
        Node left = null;
        Node right = null;

        public static Node merge(Node lower, Node greater) {
            if (lower == null)
                return greater;

            if (greater == null)
                return lower;

            if (lower.y < greater.y) {
                lower.right = merge(lower.right, greater);
                return lower;
            } else {
                greater.left = merge(lower, greater.left);
                return greater;
            }
        }

        public static NodePair splitBinary(Node orig, int value) {
            if (orig == null)
                return new NodePair(null, null);

            if (orig.x < value) {
                NodePair splitPair = splitBinary(orig.right, value);
                orig.right = splitPair.first;
                return new NodePair(orig, splitPair.second);
            } else {
                NodePair splitPair = splitBinary(orig.left, value);
                orig.left = splitPair.second;
                return new NodePair(splitPair.first, orig);
            }
        }

        public static Node merge(Node lower, Node equal, Node greater) {
            return merge(merge(lower, equal), greater);
        }

        public static SplitResult split(Node orig, int value) {
            NodePair lowerOther = splitBinary(orig, value);
            NodePair equalGreater = splitBinary(lowerOther.second, value + 1);
            return new SplitResult(lowerOther.first, equalGreater.first, equalGreater.second);
        }
    }

    static final class Tree {
        public boolean hasValue(int x) {
            SplitResult splited = Node.split(mRoot, x);
            boolean res = splited.equal != null;
            mRoot = Node.merge(splited.lower, splited.equal, splited.greater);
            return res;
        }

        public void insert(int x) {
            SplitResult splited = Node.split(mRoot, x);
            if (splited.equal == null)
                splited.equal = new Node(x);
            mRoot = Node.merge(splited.lower, splited.equal, splited.greater);
        }

        public void erase(int x) {
            SplitResult splited = Node.split(mRoot, x);
            mRoot = Node.merge(splited.lower, splited.greater);
        }

        private Node mRoot = null;
    }

    public static void main(String[] args) {
        long start = System.currentTimeMillis();

        Tree tree = new Tree();
        int cur = 5;
        int res = 0;

        for (int i = 1; i < 1000000; i++) {
            int a = i % 3;
            cur = (cur * 57 + 43) % 10007;
            if (a == 0) {
                tree.insert(cur);
            } else if (a == 1) {
                tree.erase(cur);
            } else if (a == 2) {
                boolean hasVal = tree.hasValue(cur);
                if (hasVal)
                    res++;
            }
        }
        System.out.println(res);

        long end = System.currentTimeMillis();
        long duration = end - start;

        System.out.println("Execution time: " + duration + "ms");
    }
}