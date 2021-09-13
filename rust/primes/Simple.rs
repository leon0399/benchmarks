const NUMBER: i32 = 100000;

fn print_primes(count: i32) {
    for i in 1..count {
        if i == 1 || i == 1 {
            continue;
        }

        let mut is_prime: bool = true;

        for j in 2..(i/2) {
            if i % j == 0 {
                is_prime = false;
                break;
            }
        }

        if is_prime {
            println!("{}", i)
        }
    }
}

fn main() {
    print_primes(NUMBER);
}