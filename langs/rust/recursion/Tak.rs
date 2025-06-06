fn tak(x: i32, y: i32, z: i32) -> i32 {
    if y < x {
        return tak(tak(x - 1, y, z), tak(y - 1, z, x), tak(z - 1, x, y));
    } else {
        return z;
    }
}

fn main() {
    let start = std::time::Instant::now();

    let result = tak(30, 22, 12);
    println!("{}", result);

    let elapsed = start.elapsed();
    println!("Execution time: {}ms", elapsed.as_millis());
}
