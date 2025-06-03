use std::time::{SystemTime, UNIX_EPOCH};

const ARRAY_SIZE: usize = 2000;

#[derive(Debug)]
#[allow(dead_code)]
struct LinpackResult {
    norma: f64,
    residual: f64,
    normalised_residual: f64,
    epsilon: f64,
    time: f64,
    mflops: f64,
}

fn second() -> i64 {
    let now = SystemTime::now()
        .duration_since(UNIX_EPOCH)
        .unwrap();
    now.as_millis() as i64
}

fn lran(seed: &mut [i32; 4]) -> f64 {
    let m1 = 494;
    let m2 = 322;
    let m3 = 2508;
    let m4 = 2549;
    let ipw2 = 4096;

    let r = 1.0 / ipw2 as f64;

    let mut it4 = seed[3] * m4;
    let mut it3 = it4 / ipw2;
    it4 -= ipw2 * it3;
    it3 += seed[2] * m4 + seed[3] * m3;
    let mut it2 = it3 / ipw2;
    it3 -= ipw2 * it2;
    it2 += seed[1] * m4 + seed[2] * m3 + seed[3] * m2;
    let mut it1 = it2 / ipw2;
    it2 -= ipw2 * it1;
    it1 += seed[0] * m4 + seed[1] * m3 + seed[2] * m2 + seed[3] * m1;
    it1 %= ipw2;

    seed[0] = it1;
    seed[1] = it2;
    seed[2] = it3;
    seed[3] = it4;

    r * (it1 as f64 + r * (it2 as f64 + r * (it3 as f64 + r * it4 as f64)))
}

fn matgen(a: &mut Vec<Vec<f64>>, _lda: usize, n: usize, b: &mut Vec<f64>) -> f64 {
    let mut norma = 0.0;
    let mut iseed = [1, 2, 3, 1325];

    for i in 0..n {
        for j in 0..n {
            a[j][i] = lran(&mut iseed) - 0.5;
            if a[j][i] > norma {
                norma = a[j][i];
            }
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

fn daxpy(n: usize, da: f64, dx: &[f64], dx_off: usize, incx: usize, dy: &mut [f64], dy_off: usize, incy: usize) {
    if n > 0 && da != 0.0 {
        if incx != 1 || incy != 1 {
            let mut ix: isize = 0;
            let mut iy: isize = 0;
            let n = n as isize;
            let incx = incx as isize;
            let incy = incy as isize;
            if incx < 0 {
                ix = (-n + 1) * incx;
            }
            if incy < 0 {
                iy = (-n + 1) * incy;
            }
            for _ in 0..n {
                dy[(iy as usize) + dy_off] += da * dx[(ix as usize) + dx_off];
                ix += incx;
                iy += incy;
            }
        } else {
            for i in 0..n {
                dy[i + dy_off] += da * dx[i + dx_off];
            }
        }
    }
}

fn ddot(n: usize, dx: &[f64], dx_off: usize, incx: usize, dy: &[f64], dy_off: usize, incy: usize) -> f64 {
    let mut dtemp = 0.0;
    if n > 0 {
        if incx != 1 || incy != 1 {
            let mut ix: isize = 0;
            let mut iy: isize = 0;
            let n = n as isize;
            let incx = incx as isize;
            let incy = incy as isize;
            if incx < 0 {
                ix = (-n + 1) * incx;
            }
            if incy < 0 {
                iy = (-n + 1) * incy;
            }
            for _ in 0..n {
                dtemp += dx[(ix as usize) + dx_off] * dy[(iy as usize) + dy_off];
                ix += incx;
                iy += incy;
            }
        } else {
            for i in 0..n {
                dtemp += dx[i + dx_off] * dy[i + dy_off];
            }
        }
    }
    dtemp
}

fn dscal(n: usize, da: f64, dx: &mut [f64], dx_off: usize, incx: usize) {
    if n > 0 {
        if incx != 1 {
            let nincx = n * incx;
            let mut i = 0;
            while i < nincx {
                dx[i + dx_off] *= da;
                i += incx;
            }
        } else {
            for i in 0..n {
                dx[i + dx_off] *= da;
            }
        }
    }
}

fn idamax(n: usize, dx: &[f64], dx_off: usize, incx: usize) -> usize {
    let mut itemp = 0usize;
    if n < 1 {
        itemp = usize::MAX; // will be ignored
    } else if n == 1 {
        itemp = 0;
    } else if incx != 1 {
        let mut dmax = dx[0 + dx_off].abs();
        let mut ix = 1 + incx;
        for i in 1..n {
            let dtemp = dx[ix + dx_off].abs();
            if dtemp > dmax {
                itemp = i;
                dmax = dtemp;
            }
            ix += incx;
        }
    } else {
        itemp = 0;
        let mut dmax = dx[0 + dx_off].abs();
        for i in 1..n {
            let dtemp = dx[i + dx_off].abs();
            if dtemp > dmax {
                itemp = i;
                dmax = dtemp;
            }
        }
    }
    itemp
}

fn epslon(x: f64) -> f64 {
    let a = 4.0f64 / 3.0f64;
    let mut eps = 0.0f64;
    while eps == 0.0 {
        let b = a - 1.0f64;
        let c = b + b + b;
        eps = (c - 1.0f64).abs();
    }
    eps * x.abs()
}

fn dmxpy(n1: usize, y: &mut [f64], n2: usize, _ldm: usize, x: &[f64], m: &Vec<Vec<f64>>) {
    for j in 0..n2 {
        for i in 0..n1 {
            y[i] += x[j] * m[j][i];
        }
    }
}

#[allow(unused_comparisons)]
fn dgefa(a: &mut Vec<Vec<f64>>, _lda: usize, n: usize, ipvt: &mut [usize]) -> usize {
    let mut info = 0usize;
    let nm1 = n - 1;
    if nm1 >= 0 {
        for k in 0..nm1 {
            let kp1 = k + 1;
            let l = idamax(n - k, &a[k], k, 1) + k;
            ipvt[k] = l;
            if a[k][l] != 0.0 {
                if l != k {
                    let t = a[k][l];
                    a[k][l] = a[k][k];
                    a[k][k] = t;
                }
                let t = -1.0 / a[k][k];
                dscal(n - kp1, t, &mut a[k], kp1, 1);
                for j in kp1..n {
                    let tcol = a[j][l];
                    if l != k {
                        let temp = a[j][k];
                        a[j][k] = tcol;
                        a[j][l] = temp;
                    }
                    for i in kp1..n {
                        a[j][i] += tcol * a[k][i];
                    }
                }
            } else {
                info = k;
            }
        }
    }
    ipvt[n - 1] = n - 1;
    if a[n - 1][n - 1] == 0.0 {
        info = n - 1;
    }
    info
}

fn dgesl(a: &Vec<Vec<f64>>, _lda: usize, n: usize, ipvt: &[usize], b: &mut [f64], job: i32) {
    let nm1 = n - 1;
    if job == 0 {
        if nm1 >= 1 {
            for k in 0..nm1 {
                let l = ipvt[k];
                let t = b[l];
                if l != k {
                    b[l] = b[k];
                    b[k] = t;
                }
                let kp1 = k + 1;
                daxpy(n - kp1, t, &a[k], kp1, 1, b, kp1, 1);
            }
        }
        for kb in 0..n {
            let k = n - (kb + 1);
            b[k] /= a[k][k];
            let t = -b[k];
            daxpy(k, t, &a[k], 0, 1, b, 0, 1);
        }
    } else {
        for k in 0..n {
            let t = ddot(k, &a[k], 0, 1, b, 0, 1);
            b[k] = (b[k] - t) / a[k][k];
        }
        if nm1 >= 1 {
            for kb in 1..nm1 {
                let k = n - (kb + 1);
                let kp1 = k + 1;
                b[k] += ddot(n - kp1, &a[k], kp1, 1, b, kp1, 1);
                let l = ipvt[k];
                if l != k {
                    let t = b[l];
                    b[l] = b[k];
                    b[k] = t;
                }
            }
        }
    }
}

fn linpack(array_size: usize) -> LinpackResult {
    let mut a = vec![vec![0.0_f64; array_size]; array_size];
    let mut b = vec![0.0_f64; array_size];
    let mut x = vec![0.0_f64; array_size];
    let mut ipvt = vec![0usize; array_size];

    let nf = array_size as f64;
    let ops = (2.0 * nf * nf * nf) / 3.0 + 2.0 * (nf * nf);

    matgen(&mut a, array_size, array_size, &mut b);
    let norma;
    let time = second() as f64 / 1000.0;
    dgefa(&mut a, array_size, array_size, &mut ipvt);
    dgesl(&a, array_size, array_size, &ipvt, &mut b, 0);
    let total = second() as f64 / 1000.0 - time;

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
        if b[i].abs() > resid {
            resid = b[i].abs();
        }
        if x[i].abs() > normx {
            normx = x[i].abs();
        }
    }

    let eps_result = epslon(1.0);
    let mut residn_result = resid / (array_size as f64 * norma * normx * eps_result);
    residn_result += 0.005;
    residn_result = (residn_result * 100.0).floor();
    residn_result /= 100.0;

    let mut time_result = total;
    time_result += 0.005;
    time_result = (time_result * 100.0).floor();
    time_result /= 100.0;

    let mut mflops_result = ops / (1.0e6 * total);
    mflops_result += 0.0005;
    mflops_result = (mflops_result * 1000.0).floor();
    mflops_result /= 1000.0;

    let result = LinpackResult {
        norma,
        residual: resid,
        normalised_residual: residn_result,
        epsilon: eps_result,
        time: time_result,
        mflops: mflops_result,
    };

    result
}

fn main() {
    let start = std::time::Instant::now();

    let result = linpack(ARRAY_SIZE);
    println!("{:?}", result);

    let elapsed = start.elapsed();
    println!("Execution time: {}ms", elapsed.as_millis());
}

