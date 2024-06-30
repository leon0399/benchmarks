#!/usr/bin/env lua

function index()
    for y = -39, 38 do
        io.write("\n")
        
        for x = -39, 38 do
            local i = mandelbrot(
                x / 40.0,
                y / 40.0
            )

            if i == 0 then
                io.write("*")
            else
                io.write(" ")
            end
        end
    end

    io.write("\n")
end

function mandelbrot(x, y)
    local cr = y - 0.5
    local ci = x
    local zi = 0.0
    local zr = 0.0
    local i = 0

    while true do
        i = i + 1
        
        local temp = zr * zi
        
        local zr2 = zr * zr
        local zi2 = zi * zi
        
        zr = zr2 - zi2 + cr
        zi = temp + temp + ci
        
        if zi2 + zr2 > 16 then
            return i
        end
        
        if i > 5000 then
            return 0
        end
    end
end

local function main()
    local startTime = os.clock()
    
    index()
    
    local endTime = os.clock()
    local duration = (endTime - startTime) * 1000
    
    print(string.format("Execution time: %.0fms", duration))
end

main()
