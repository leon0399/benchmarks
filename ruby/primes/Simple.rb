# frozen_string_literal: true

NUMBER = 100_000

def printPrimes(count)
  for i in 1..count
    if i == 0 || i == 1
      next
    end

    isPrime = true

    for j in 2..i/2
      if i % j == 0
        isPrime = false
        break
      end
    end

    if isPrime
      puts i
    end
  end
end

startTimeMs = Time.now.to_f * 1000

printPrimes(NUMBER)

endTimeMs = Time.now.to_f * 1000
durationMs = (endTimeMs - startTimeMs).to_i

puts "Execution time: #{durationMs}ms"