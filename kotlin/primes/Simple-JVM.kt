object Simple {
    private const val NUMBER = 500000

    @JvmStatic
    fun printPrimes(count: Int): Int {
        var lastPrime = 2

        for (i in 3..count step 2) {
            var isPrime = true
            var limit = Math.sqrt(i.toDouble()).toInt()

            for (j in 3..limit step 2) {
                if (i % j == 0) {
                    isPrime = false
                    break
                }
            }

            if (isPrime) {
                lastPrime = i
            }
        }

        return lastPrime
    }

    @JvmStatic
    fun main(args: Array<String>) {
        val start = System.currentTimeMillis()

        val lastPrime = printPrimes(NUMBER)
        println("Last prime: $lastPrime")

        val end = System.currentTimeMillis()
        val duration = end - start

        println("Execution time: ${duration}ms")
    }
}
