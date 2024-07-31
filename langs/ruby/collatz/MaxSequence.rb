NUMBER = 500_000

def collats(x)
    len = 0

    while x > 1 do
        if x % 2 == 0
            x = x / 2
        else
            x = 3 * x + 1
        end

        len += 1
    end

    return len
end

def findMaxCollatz(to)
    result = [1, 1]

    for number in 1..to
        len = collats(number)

        if len > result[1]
            result = [number, len]
        end
    end

    return result
end

startTimeMs = Time.now.to_f * 1000

puts findMaxCollatz(NUMBER)

endTimeMs = Time.now.to_f * 1000
durationMs = (endTimeMs - startTimeMs).to_i

puts "Execution time: #{durationMs}ms"