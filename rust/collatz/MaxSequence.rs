const NUMBER: i32 = 500000;

fn collatz(mut x: i64) -> i64 {
    let mut len = 0;

    while x > 1 {
        if x % 2 == 0 {
            x = x / 2;
        } else {
            x = 3 * x + 1;
        }

        len += 1;
    }

    return len;
}

fn find_max_collatz(to: i64) -> (i64, i64) {
    let mut result: (i64, i64) = (1, 1);

    for number in 1..to {
        let len = collatz(number);

        if len > result.1 {
            result= (number, len);
        }
    }

    return result;
}

fn main() {
    let start = std::time::Instant::now();

    println!("{:?}", find_max_collatz(NUMBER as i64));

    let elapsed = start.elapsed();
    println!("Execution time: {}ms", elapsed.as_millis());
}