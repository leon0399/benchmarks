use rand::Rng;
use std::time::Instant;

const ARRAY_SIZE: usize = 2000;

struct LinpackResult {
    norma: f64,
    residual: f64,
    residn_result: f64,
    eps_result: f64,
    time_result: f64,
    mflops_result: f64,
}

fn second() -> f64 {
    let start = Instant::now();
    start.elapsed().as_secs_f64()
}

// Implement matgen, lran, dgefa, dgesl, daxpy, ddot, dscal, idamax, epslon, dmxpy functions here
fn matgen(a: &mut Vec<Vec<f64>>, lda: usize, n: usize, b: &mut Vec<f64>) -> f64 {
    let mut norma = 0.0;
    let mut iseed = [1, 2, 3, 1325];

    for i in 0..n {
        for j in 0..n {
            a[j][i] = lran(&mut iseed) - 0.5;
            norma = norma.max(a[j][i]);
        }
    }

    for i in 0..n {
        b[i] = 0.0;
    }

    for j in 0..n {
        for i in 0..n {
            b[i] += a[j][i];
        }
    }

    norma
}

fn lran(iseed: &mut [i32; 4]) -> f64 {
    let m1 = 494;
    let m2 = 322;
    let m3 = 2508;
    let m4 = 2549;
    let ipw2 = 4096;

    let r = 1.0 / ipw2 as f64;

    let mut it4 = iseed[3] * m4;
    let mut it3 = it4 / ipw2;
    it4 = it4 - ipw2 * it3;
    it3 = it3 + iseed[2] * m4 + iseed[3] * m3;
    let mut it2 = it3 / ipw2;
    it3 = it3 - ipw2 * it2;
    it2 = it2 + iseed[1] * m4 + iseed[2] * m3 + iseed[3] * m2;
    let mut it1 = it2 / ipw2;
    it2 = it2 - ipw2 * it1;
    it1 = it1 + iseed[0] * m4 + iseed[1] * m3 + iseed[2] * m2 + iseed[3] * m1;
    it1 = it1 % ipw2;

    iseed[0] = it1;
    iseed[1] = it2;
    iseed[2] = it3;
    iseed[3] = it4;

    r * (it1 as f64 + r * (it2 as f64 + r * (it3 as f64 + r * it4 as f64)))
}

fn linpack(array_size: usize) -> LinpackResult {
    let mut a = vec![vec![0.0; array_size]; array_size];
    let mut b = vec![0.0; array_size];
    let mut x = vec![0.0; array_size];
    let mut ipvt = vec![0; array_size];

    let ops = (2.0e0 * array_size as f64).powi(3) + 2.0 * (array_size as f64).powi(2);
    let mut norma = matgen(&mut a, array_size, array_size, &mut b);

    let start = Instant::now();
    let info = dgefa(&mut a, array_size, array_size, &mut ipvt);
    dgesl(&mut a, array_size, array_size, &mut ipvt, &mut b, 0);
    let total = start.elapsed().as_secs_f64();

    for i in 0..array_size {
        x[i] = b[i];
    }

    norma = matgen(&mut a, array_size, array_size, &mut b);
    for i in 0..array_size {
        b[i] = -b[i];
    }

    dmxpy(array_size, &mut b, array_size, array_size, &x, &a);
    let mut resid = 0.0;
    let mut normx = 0.0;
    for i in 0..array_size {
        resid = resid.max(b[i].abs());
        normx = normx.max(x[i].abs());
    }

    let eps = epslon(1.0);
    let residn = resid / ((array_size as f64 * norma * normx * eps).max(1.0));
    let time = total;
    let mflops = ops / (1.0e6 * total);

    LinpackResult {
        norma,
        residual: resid,
        residn_result: residn,
        eps_result: eps,
        time_result: time,
        mflops_result: mflops,
    }
}

fn main() {
    println!("{:?}", linpack(ARRAY_SIZE));
}

fn main() {
    linpack(ARRAY_SIZE);
}
