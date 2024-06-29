package main

import (
    "fmt"
    "time"
)

func tak(x, y, z int) int {
    if y < x {
        return tak(tak(x-1, y, z), tak(y-1, z, x), tak(z-1, x, y))
    }
    return z
}

func main() {
    startTime := time.Now()

    result := tak(30, 22, 12)
    fmt.Println(result)

    endTime := time.Now()
    duration := endTime.Sub(startTime).Milliseconds()

    fmt.Printf("Execution time: %dms\n", duration)
}
