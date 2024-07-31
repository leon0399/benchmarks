#!/usr/bin/env lua

local NUMBER = 1000000

local function getLastPrime(count)
    local lastPrime = 2

    -- Traverse each number from 3 to N, skipping even numbers
    for i = 3, count, 2 do
        local isPrime = true
        local limit = math.floor(math.sqrt(i))

        for j = 3, limit, 2 do
            if i % j == 0 then
                isPrime = false
                break
            end
        end

        if isPrime then
            lastPrime = i
        end
    end

    return lastPrime
end

local function main()
    local startTime = os.clock()

    local lastPrime = getLastPrime(NUMBER)
    print("Last prime: " .. lastPrime)

    local endTime = os.clock()
    local durationMs = (endTime - startTime) * 1000

    print("Execution time: " .. durationMs .. "ms")
end

main()
