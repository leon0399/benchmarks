package io;

public final class NoLoad {
    private static final int NUMBER = 500000;

    public static void run(int times) {
        var x = 0;

        for(var i = 0; i <= times; i++) {
            x = i * i;
        }

        System.out.println(x);
    }

    public static void main(String[] args) {
        run(NUMBER);
    }
}