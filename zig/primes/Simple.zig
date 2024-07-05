const std = @import("std");

const NUMBER = 1000000;

fn getLastPrime(count: i32) u32 {
    var lastPrime: u32 = 0;

    var i: u32 = 3;
    while (i <= count) : (i += 2) {
        var isPrime = true;
        const limit: u32 = @intCast(std.math.sqrt(i));

        var j: u32 = 3;
        while (j <= limit) : (j += 2) {
            if (@mod(i, j) == 0) {
                isPrime = false;
                break;
            }
        }

        if (isPrime) {
            lastPrime = i;
        }
    }

    return lastPrime;
}

pub fn main() anyerror!void {
    const stdout = std.io.getStdOut().writer();
    
    const start_time = std.time.milliTimestamp();

    const last_prime = getLastPrime(NUMBER);
    try stdout.print("Last prime: {}\n", .{last_prime});

    const end_time = std.time.milliTimestamp();
    const duration = end_time - start_time;

    try stdout.print("Execution time: {}ms\n", .{duration});
}
