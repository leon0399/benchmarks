function tak(x, y, z) {
    if (y < x) {
        return tak(tak(x - 1, y, z), tak(y - 1, z, x), tak(z - 1, x, y))
    } else {
        return z
    }
}

const startTimeMs = new Date().getTime()
      
console.log(tak(30, 22, 12))

const endTimeMs = new Date().getTime()
const durationMs = endTimeMs - startTimeMs
console.log(`Execution time: ${durationMs}ms`)