NUMBER = 500000

def run(times)
  x = 0;

  for i in 0..times
    x = i * i
  end

  puts x
end

run(NUMBER)