def index
  for y in -39..39
    puts

    for x in -39..39
      i = mandelbrot(
        x / 40.0,
        y / 40.0
      )

      if i == 0
        print("*")
      else
        print(" ")
      end
    end
  end

  puts
end

def mandelbrot(x, y)
  cr = y - 0.5
  ci = x
  zi = 0.0
  zr = 0.0
  i = 0

  loop do
    i += 1

    temp = zr * zi

    zr2 = zr * zr
    zi2 = zi * zi

    zr = zr2 - zi2 + cr
    zi = temp + temp + ci

    if zi2 + zr2 > 16
      return i
    end

    if i > 5000
      return 0
    end
  end
end

startTimeMs = Time.now.to_f * 1000

index

endTimeMs = Time.now.to_f * 1000
durationMs = (endTimeMs - startTimeMs).to_i

puts "Execution time: #{durationMs}ms"