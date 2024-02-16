# frozen_string_literal: true

NUMBER = 100_000

def getLastPrime(count)
  lastPrime = 2

  for i in 2..count
    isPrime = true

    for j in 2..i/2
      if i % j == 0
        isPrime = false
        break
      end
    end

    if isPrime
      lastPrime = i
    end
  end

  lastPrime
end

startTimeMs = Time.now.to_f * 1000

lastPrime = getLastPrime(NUMBER)
puts "Last prime: #{lastPrime}"

endTimeMs = Time.now.to_f * 1000
durationMs = (endTimeMs - startTimeMs).to_i

puts "Execution time: #{durationMs}ms"