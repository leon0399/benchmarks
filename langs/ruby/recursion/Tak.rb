def tak(x, y, z)
    return y < x ? tak(tak(x - 1, y, z), tak(y - 1, z, x), tak(z - 1, x, y)) : z;
end

startTimeMs = Time.now.to_f * 1000

puts tak(30, 22, 12);

endTimeMs = Time.now.to_f * 1000
durationMs = (endTimeMs - startTimeMs).to_i

puts "Execution time: #{durationMs}ms"
