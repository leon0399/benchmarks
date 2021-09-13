fn mandelbrot(x: f64, y: f64) -> i64 {
    let cr = y - 0.5;
    let ci = x;

    let mut zi = 0.0;
    let mut zr = 0.0;
    let mut i: i64 = 0;

    loop {
        i += 1;

        let temp = zr * zi;

        let zr2 = zr * zr;
        let zi2 = zi * zi;

        zr = zr2 - zi2 + cr;
        zi = temp + temp + ci;

        if zi2 + zr2 > 16.0 {
            return i;
        }

        if i > 5000 {
            return 0;
        }
    }
}

fn index() {
    for y in -39..39 {
        println!();

        for x in -39..39 {
            let i = mandelbrot(
                x as f64 / 40.0,
                y as f64 / 40.0
            );

            if i== 0 {
                print!("*");
            } else {
                print!(" ");
            }
        }
    }
}

fn main() {
    index();
}