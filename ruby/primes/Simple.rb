# frozen_string_literal: true

NUMBER = 500_000

def getLastPrime(count)
  lastPrime = 2

  for i in (3..count).step(2) 
    isPrime = true
    limit = Math.sqrt(i).to_i

    for j in (3..limit).step(2)
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