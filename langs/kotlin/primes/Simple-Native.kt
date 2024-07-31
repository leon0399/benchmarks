import kotlin.io.*
import kotlin.time.TimeSource
import platform.posix.*

private const val NUMBER = 1000000

fun printPrimes(count: Int): Int {
    var lastPrime = 2

    for (i in 3..count step 2) {
        var isPrime = true
        var limit = sqrt(i.toDouble()).toInt()

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

fun main(args: Array<String>) {
    val timeSource = TimeSource.Monotonic

    // current time in ms
    val start = timeSource.markNow()

    val lastPrime = printPrimes(NUMBER)
    println("Last prime: $lastPrime")

    val end = timeSource.markNow()
    val execTime = (end - start)
    // convert to ms

    println("Execution time: ${execTime.inWholeMilliseconds}ms")
}
