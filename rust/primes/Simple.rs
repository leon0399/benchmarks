const NUMBER: i32 = 100000;

fn get_last_prime(count: i32) -> i32
{
    let mut last_prime: i32 = 2;

    for i in 1..count {
        let mut is_prime: bool = true;

        for j in 2..(i/2) {
            if i % j == 0 {
                is_prime = false;
                break;
            }
        }

        if is_prime {
            last_prime = i;
            
        }
    }

    last_prime
}

fn main() {
    let start = std::time::Instant::now();

    let last_ptime = get_last_prime(NUMBER);
    println!("Last prime: {}", last_ptime);

    let elapsed = start.elapsed();
    println!("Execution time: {}ms", elapsed.as_millis());
}