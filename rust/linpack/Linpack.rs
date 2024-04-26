use std::time::{Duration, Instant};

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

use rand::Rng;

fn matgen(a: &mut Vec<Vec<f64>>, b: &mut Vec<f64>, n: usize) {
    assert_eq!(a.len(), n);
    assert_eq!(a[0].len(), n);
    assert_eq!(b.len(), n);

    let mut rng = rand::thread_rng();
    for i in 0..n {
        for j in 0..n {
            a[i][j] = rng.gen();
        }
        b[i] = rng.gen();
    }
}

fn lran(seed: &mut i32) -> f64 {
    const MULTIPLIER: i32 = 1366;
    const ADDEND: i32 = 150889;
    const PMOD: i32 = 714025;
    
    *seed = (*seed * MULTIPLIER + ADDEND) % PMOD;
    (*seed as f64) / PMOD as f64 - 0.5
}

fn dgefa(a: &mut Vec<Vec<f64>>, ipvt: &mut Vec<usize>, n: usize) {
    for k in 0..n-1 {
        let mut imax = k;
        let mut amax = a[k][k].abs();
        for i in k+1..n {
            let abs = a[i][k].abs();
            if abs > amax {
                imax = i;
                amax = abs;
            }
        }
        ipvt[k] = imax;
        if amax == 0.0 {
            panic!("Singular matrix");
        }
        if imax != k {
            a.swap(imax, k);
        }
        for i in k+1..n {
            a[i][k] /= a[k][k];
            for j in k+1..n {
                a[i][j] -= a[i][k] * a[k][j];
            }
        }
    }
    ipvt[n-1] = n-1;
    if a[n-1][n-1] == 0.0 {
        panic!("Singular matrix");
    }
}

fn dgesl(a: &Vec<Vec<f64>>, ipvt: &Vec<usize>, b: &mut Vec<f64>, n: usize) {
    for kb in 0..n {
        let k = n - (kb + 1);
        let l = ipvt[k];
        let t = b[l];
        b[l] = b[k];
        b[k] = t;
        for i in (k+1)..n {
            b[i] -= a[i][k] * t;
        }
    }
    for kb in 0..n {
        let k = n - (kb + 1);
        b[k] /= a[k][k];
        let t = -b[k];
        for i in 0..k {
            b[i] += a[i][k] * t;
        }
    }
}

fn daxpy(n: usize, da: f64, dx: &[f64], incx: usize, dy: &mut [f64], incy: usize) {
    let mut ix = 0;
    let mut iy = 0;
    for _ in 0..n {
        dy[iy] += da * dx[ix];
        ix += incx;
        iy += incy;
    }
}

fn ddot(n: usize, dx: &[f64], incx: usize, dy: &[f64], incy: usize) -> f64 {
    let mut ix = 0;
    let mut iy = 0;
    let mut dot = 0.0;
    for _ in 0..n {
        dot += dx[ix] * dy[iy];
        ix += incx;
        iy += incy;
    }
    dot
}

fn dscal(n: usize, da: f64, dx: &mut [f64], incx: usize) {
    let mut ix = 0;
    for _ in 0..n {
        dx[ix] *= da;
        ix += incx;
    }
}

fn idamax(n: usize, dx: &[f64], incx: usize) -> usize {
    let mut ix = 0;
    let mut imax = 0;
    let mut dmax = 0.0;
    for _ in 0..n {
        let abs = dx[ix].abs();
        if abs > dmax {
            imax = ix;
            dmax = abs;
        }
        ix += incx;
    }
    imax
}

fn linpack(array_size: usize) -> LinpackResult {
    let mut a = vec![vec![0.0; array_size]; array_size];
    let mut b = vec![0.0; array_size];
    let mut x = vec![0.0; array_size];
    let mut ipvt = vec![0; array_size];
    let mut norma = 0.0;
    let mut resid = 0.0;
    let mut residn = 0.0;
    let mut eps = 0.0;
    let mut time = 0.0;
    let mut mflops = 0.0;

    let mut seed = 1325;
    let mut kase = 0;
    let mut n = array_size;

    while n <= array_size {
        kase += 1;
        matgen(&mut a, &mut b, n);
        let start = second();
        dgefa(&mut a, &mut ipvt, n);
        dgesl(&a, &ipvt, &mut b, n);
        time += second() - start;
        for i in 0..n {
            x[i] = b[i];
        }
        norma = 0.0;
        for i in 0..n {
            for j in 0..n {
                norma = f64::max(norma, a[i][j].abs());
            }
        }
        for i in 0..n {
            b[i] = 0.0;
            for j in 0..n {
                b[i] += a[i][j] * x[j];
            }
        }
        resid = 0.0;
        for i in 0..n {
            resid = f64::max(resid, (x[i] - b[i]).abs());
        }
        eps = epslon(&1.0);
        residn = resid / (n as f64 * norma * eps);
        time = time / kase as f64;
        mflops = 2.0 * n as f64 * n as f64 * n as f64 / 3.0 / 1e6 / time;
        n += 1000;
    }

    LinpackResult {
        norma,
        residual: resid,
        normalised_residual: residn,
        epsilon: eps,
        time,
        mflops,
    }
}

fn epslon(x: &f64) -> f64 {
    let mut a = 1.0;
    let mut b = 1.0;
    while (a + 1.0) != 1.0 {
        b /= 2.0;
        a = b + 1.0;
    }
    b * 2.0
}

fn main() {
    let start_time = Instant::now();
    let result = linpack(ARRAY_SIZE);
    let duration = start_time.elapsed();

    println!("Linpack Result: {:?}", result);
    println!("Execution time: {:?}", duration);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_matgen() {
        let mut a = vec![vec![0.0; 3]; 3];
        let mut b = vec![0.0; 3];
        matgen(&mut a, &mut b, 3);
        assert_eq!(a.len(), 3);
        assert_eq!(a[0].len(), 3);
        assert_eq!(b.len(), 3);
    }

    #[test]
    fn test_lran() {
        let mut seed = 1325;
        let r = lran(&mut seed);
        assert!(r >= -0.5 && r < 0.5);
    }

    #[test]
    fn test_dgefa() {
        let mut a = vec![
            vec![1.0, 2.0, 3.0],
            vec![4.0, 5.0, 6.0],
            vec![7.0, 8.0, 9.0],
        ];
        let mut ipvt = vec![0; 3];
        dgefa(&mut a, &mut ipvt, 3);
        assert_eq!(ipvt, vec![2, 2, 2]);
    }

    #[test]
    fn test_dgesl() {
        let a = vec![
            vec![1.0, 2.0, 3.0],
            vec![4.0, 5.0, 6.0],
            vec![7.0, 8.0, 9.0],
        ];
        let ipvt = vec![2, 2, 2];
        let mut b = vec![1.0, 2.0, 3.0];
        dgesl(&a, &ipvt, &mut b, 3);
        assert_eq!(b, vec![-0.5, 1.0, 0.0]);
    }

    #[test]
    fn test_daxpy() {
        let mut dy = vec![1.0, 2.0, 3.0];
        let dx = vec![1.0, 2.0, 3.0];
        daxpy(3, 2.0, &dx, 1, &mut dy, 1);
        assert_eq!(dy, vec![3.0, 6.0, 9.0]);
    }

    #[test]
    fn test_ddot() {
        let dx = vec![1.0, 2.0, 3.0];
        let dy = vec![1.0, 2.0, 3.0];
        let dot = ddot(3, &dx, 1, &dy, 1);
        assert_eq!(dot, 14.0);
    }

    #[test]
    fn test_dscal() {
        let mut dx = vec![1.0, 2.0, 3.0];
        dscal(3, 2.0, &mut dx, 1);
        assert_eq!(dx, vec![2.0, 4.0, 6.0]);
    }

    #[test]
    fn test_idamax() {
        let dx = vec![1.0, 2.0, 3.0];
        let imax = idamax(3, &dx, 1);
        assert_eq!(imax, 2);
    }

    #[test]
    fn test_linpack() {
        let result = linpack(100);
        assert!(result.norma > 0.0);
        assert!(result.residual > 0.0);
        assert!(result.normalised_residual > 0.0);
        assert!(result.epsilon > 0.0);
        assert!(result.time > 0.0);
        assert!(result.mflops > 0.0);
    }
}
