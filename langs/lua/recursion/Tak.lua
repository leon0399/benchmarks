local function tak(x, y, z)
    if y < x then
        return tak(tak(x - 1, y, z), tak(y - 1, z, x), tak(z - 1, x, y))
    else
        return z
    end
end

local function benchmark()
    local startTime = os.clock() * 1000

    print(tak(30, 22, 12))

    local endTime = os.clock() * 1000
    local duration = endTime - startTime

    print("Execution time: " .. duration .. "ms")
end

benchmark()
