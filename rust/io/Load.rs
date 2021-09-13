const NUMBER: i64 = 500000;

fn run(times: i64) {
    let mut x = 0;
    for i in 0..times {
        x = i * i;
        println!("{}", x);
    }

    println!("{}", x);
}

fn main() {
    run(NUMBER);
}