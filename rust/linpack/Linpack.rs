use std::time::{Duration, Instant};
use std::vec::Vec;

const ARRAY_SIZE: usize = 2000;

struct LinpackResult {
    norma: f64,
    residual: f64,
    normalised_residual: f64,
    epsilon: f64,
    time: f64,
    mflops: f64,
}

fn second() -> f64 {
    let now = Instant::now();
    now.elapsed().as_secs_f64()
}

fn matgen(a: &mut Vec<Vec<f64>>, n: usize, b: &mut Vec<f64>) -> f64 {
    let mut norma = 0.0;
    let mut iseed = [1, 2, 3, 1325];
    for i in 0..n {
        for j in 0..n {
            a[j][i] = lran(&mut iseed) - 0.5;
            norma = norma.max(a[j][i].abs());
        }
    }
    for i in 0..n {
        b[i] = 0.0;
        for j in 0..n {
            b[i] += a[j][i];
        }
    }
    norma
}

fn lran(seed: &mut [i32; 4]) -> f64 {
    let m1 = 494;
    let m2 = 322;
    let m3 = 2508;
    let m4 = 2549;
    let ipw2 = 4096;
    let mut it1 = seed[0] * m1 + seed[1] * m2 + seed[2] * m3 + seed[3] * m4;
    it1 %= ipw2;
    seed[0] = it1;
    1.0 / ipw2 as f64 * it1 as f64
}

fn dgefa(a: &mut Vec<Vec<f64>>, n: usize, ipvt: &mut Vec<usize>) -> usize {
    let mut info = 0;
    let nm1 = n - 1;
    for k in 0..nm1 {
        let mut l = k;
        for i in k+1..n {
            if a[i][k].abs() > a[l][k].abs() {
                l = i;
            }
        }
        ipvt[k] = l;
        if a[l][k] == 0.0 {
            info = k;
            continue;
        }
        if l != k {
            for j in 0..n {
                a[l][j] = a[k][j];
                a[k][j] = a[l][j];
            }
        }
        for i in k+1..n {
            let mult = a[i][k] / a[k][k];
            a[i][k] = mult;
            for j in k+1..n {
                a[i][j] -= mult * a[k][j];
            }
        }
    }
    ipvt[n-1] = n-1;
    if a[n-1][n-1] == 0.0 {
        info = n-1;
    }
    info
}

fn dgesl(a: &Vec<Vec<f64>>, n: usize, ipvt: &Vec<usize>, b: &mut Vec<f64>, job: usize) {
    if job == 0 {
        for k in 0..n-1 {
            let l = ipvt[k];
            let temp = b[l];
            b[l] = b[k];
            b[k] = temp;
            for i in k+1..n {
                b[i] -= a[i][k] * b[k];
            }
        }
        for k in (0..n).rev() {
            b[k] /= a[k][k];
            let temp = b[k];
            for i in 0..k {
                b[i] -= a[i][k] * temp;
            }
        }
    } else {
        for k in 0..n {
            let temp = b[k];
            for i in 0..k {
                b[k] -= a[k][i] * b[i];
            }
            b[k] = temp / a[k][k];
        }
        for k in (0..n-1).rev() {
            let l = ipvt[k];
            let temp = b[l];
            b[l] = b[k];
            b[k] = temp;
            for i in k+1..n {
                b[k] -= a[i][k] * b[i];
            }
        }
    }
}

fn ddot(n: usize, dx: &Vec<f64>, dy: &Vec<f64>) -> f64 {
    let mut dtemp = 0.0;
    for i in 0..n {
        dtemp += dx[i] * dy[i];
    }
    dtemp
}

fn daxpy(n: usize, da: f64, dx: &Vec<f64>, dy: &mut Vec<f64>) {
    for i in 0..n {
        dy[i] += da * dx[i];
    }
}

fn dscal(n: usize, da: f64, dx: &mut Vec<f64>) {
    for i in 0..n {
        dx[i] *= da;
    }
}

fn idamax(n: usize, dx: &Vec<f64>) -> usize {
    let mut dmax = 0.0;
    let mut itemp = 0;
    for i in 0..n {
        if dx[i].abs() > dmax {
            itemp = i;
            dmax = dx[i].abs();
        }
    }
    itemp
}

fn main() {
    let start = Instant::now();
    let mut a = vec![vec![0.0; ARRAY_SIZE]; ARRAY_SIZE];
    let mut b = vec![0.0; ARRAY_SIZE];
    let mut ipvt = vec![0; ARRAY_SIZE];
    let norma = matgen(&mut a, ARRAY_SIZE, &mut b);
    let info = dgefa(&mut a, ARRAY_SIZE, &mut ipvt);
    dgesl(&a, ARRAY_SIZE, &ipvt, &mut b, 0);
    let duration = start.elapsed();
    println!("Time elapsed in expensive_function() is: {:?}", duration);
}
