#include <iostream>
#include <vector>
#include <cmath>
#include <chrono>

const int ARRAY_SIZE = 2000;

struct LinpackResult {
    double Norma;
    double Residual;
    double NormalisedResidual;
    double Epsilon;
    double Time;
    double MFLOPS;
};

int64_t second() {
    return std::chrono::duration_cast<std::chrono::milliseconds>(
        std::chrono::high_resolution_clock::now().time_since_epoch()
    ).count();
}

double lran(std::vector<int>& seed) {
    const int m1 = 494, m2 = 322, m3 = 2508, m4 = 2549, ipw2 = 4096;
    const double r = 1.0 / ipw2;
    int it1, it2, it3, it4;
    double result;

    it4 = seed[3] * m4;
    it3 = it4 / ipw2;
    it4 -= ipw2 * it3;
    it3 += seed[2] * m4 + seed[3] * m3;
    it2 = it3 / ipw2;
    it3 -= ipw2 * it2;
    it2 += seed[1] * m4 + seed[2] * m3 + seed[3] * m2;
    it1 = it2 / ipw2;
    it2 -= ipw2 * it1;
    it1 += seed[0] * m4 + seed[1] * m3 + seed[2] * m2 + seed[3] * m1;
    it1 %= ipw2;

    seed[0] = it1;
    seed[1] = it2;
    seed[2] = it3;
    seed[3] = it4;

    result = r * (it1 + r * (it2 + r * (it3 + r * it4)));

    return result;
}

double matgen(std::vector<std::vector<double>>& a, int lda, int n, std::vector<double>& b) {
    double norma = 0.0;
    std::vector<int> iseed = {1, 2, 3, 1325};

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            a[j][i] = lran(iseed) - 0.5;
            if (a[j][i] > norma) {
                norma = a[j][i];
            }
        }
    }
    for (int i = 0; i < n; ++i) {
        b[i] = 0.0;
    }
    for (int j = 0; j < n; ++j) {
        for (int i = 0; i < n; ++i) {
            b[i] += a[j][i];
        }
    }

    return norma;
}

void daxpy(int n, double da, std::vector<double>& dx, int dx_off, int incx, std::vector<double>& dy, int dy_off, int incy) {
    int ix = 0, iy = 0;

    if (n > 0 && da != 0) {
        if (incx != 1 || incy != 1) {
            if (incx < 0) ix = (-n + 1) * incx;
            if (incy < 0) iy = (-n + 1) * incy;
            for (int i = 0; i < n; i++) {
                dy[iy + dy_off] += da * dx[ix + dx_off];
                ix += incx;
                iy += incy;
            }
        } else {
            for (int i = 0; i < n; i++) {
                dy[i + dy_off] += da * dx[i + dx_off];
            }
        }
    }
}

double ddot(int n, std::vector<double>& dx, int dx_off, int incx, std::vector<double>& dy, int dy_off, int incy) {
    double dtemp = 0.0;
    int ix = 0, iy = 0;

    if (n > 0) {
        if (incx != 1 || incy != 1) {
            if (incx < 0) ix = (-n + 1) * incx;
            if (incy < 0) iy = (-n + 1) * incy;
            for (int i = 0; i < n; i++) {
                dtemp += dx[ix + dx_off] * dy[iy + dy_off];
                ix += incx;
                iy += incy;
            }
        } else {
            for (int i = 0; i < n; i++) {
                dtemp += dx[i + dx_off] * dy[i + dy_off];
            }
        }
    }
    return dtemp;
}

void dscal(int n, double da, std::vector<double>& dx, int dx_off, int incx) {
    if (n > 0) {
        if (incx != 1) {
            for (int i = 0; i < n * incx; i += incx) {
                dx[i + dx_off] *= da;
            }
        } else {
            for (int i = 0; i < n; i++) {
                dx[i + dx_off] *= da;
            }
        }
    }
}

int idamax(int n, std::vector<double>& dx, int dx_off, int incx) {
    double dmax, dtemp;
    int ix = 0, itemp = 0;

    if (n < 1) {
        itemp = -1;
    } else if (n == 1) {
        itemp = 0;
    } else if (incx != 1) {
        dmax = std::abs(dx[0 + dx_off]);
        ix = 1 + incx;
        for (int i = 1; i < n; i++) {
            dtemp = std::abs(dx[ix + dx_off]);
            if (dtemp > dmax) {
                itemp = i;
                dmax = dtemp;
            }
            ix += incx;
        }
    } else {
        itemp = 0;
        dmax = std::abs(dx[0 + dx_off]);
        for (int i = 1; i < n; i++) {
            dtemp = std::abs(dx[i + dx_off]);
            if (dtemp > dmax) {
                itemp = i;
                dmax = dtemp;
            }
        }
    }
    return itemp;
}

double epslon(double x) {
    double a = 4.0 / 3.0;
    double eps = 0.0;
    while (eps == 0) {
        double b = a - 1.0;
        double c = b + b + b;
        eps = std::abs(c - 1.0);
    }
    return eps * std::abs(x);
}

void dmxpy(int n1, std::vector<double>& y, int n2, int ldm, std::vector<double>& x, std::vector<std::vector<double>>& m) {
    for (int j = 0; j < n2; j++) {
        for (int i = 0; i < n1; i++) {
            y[i] += x[j] * m[j][i];
        }
    }
}

int dgefa(std::vector<std::vector<double>>& a, int lda, int n, std::vector<int>& ipvt) {
    std::vector<double> col_k, col_j;
    double t;
    int j, k, kp1, l, nm1 = 0;
    int info = 0;

    nm1 = n - 1;

    if (nm1 >= 0) {
        for (k = 0; k < nm1; k++) {
            col_k = a[k];
            kp1 = k + 1;

            l = idamax(n - k, col_k, k, 1) + k;
            ipvt[k] = l;

            if (col_k[l] != 0) {
                if (l != k) {
                    t = col_k[l];
                    col_k[l] = col_k[k];
                    col_k[k] = t;
                }

                t = -1.0 / col_k[k];
                dscal(n - (kp1), t, col_k, kp1, 1);

                for (j = kp1; j < n; j++) {
                    col_j = a[j];
                    t = col_j[l];
                    if (l != k) {
                        col_j[l] = col_j[k];
                        col_j[k] = t;
                    }
                    daxpy(n - (kp1), t, col_k, kp1, 1, col_j, kp1, 1);
                }
            } else {
                info = k;
            }
        }
    }
    ipvt[n - 1] = n - 1;
    if (a[n - 1][n - 1] == 0) {
        info = n - 1;
    }

    return info;
}

void dgesl(std::vector<std::vector<double>>& a, int lda, int n, std::vector<int>& ipvt, std::vector<double>& b, int job) {
    double t;
    int k, kb, l, nm1, kp1 = 0;

    nm1 = n - 1;

    if (job == 0) {
        if (nm1 >= 1) {
            for (k = 0; k < nm1; k++) {
                l = ipvt[k];
                t = b[l];
                if (l != k) {
                    b[l] = b[k];
                    b[k] = t;
                }
                kp1 = k + 1;
                daxpy(n - (kp1), t, a[k], kp1, 1, b, kp1, 1);
            }
        }

        for (kb = 0; kb < n; kb++) {
            k = n - (kb + 1);
            b[k] /= a[k][k];
            t = -b[k];
            daxpy(k, t, a[k], 0, 1, b, 0, 1);
        }
    } else {
        for (k = 0; k < n; k++) {
            t = ddot(k, a[k], 0, 1, b, 0, 1);
            b[k] = (b[k] - t) / a[k][k];
        }

        if (nm1 >= 1) {
            for (kb = 1; kb < nm1; kb++) {
                k = n - (kb + 1);
                kp1 = k + 1;
                b[k] += ddot(n - (kp1), a[k], kp1, 1, b, kp1, 1);
                l = ipvt[k];
                if (l != k) {
                    t = b[l];
                    b[l] = b[k];
                    b[k] = t;
                }
            }
        }
    }
}

LinpackResult linpack(int array_size) {
    double mflops_result = 0.0;
    double residn_result = 0.0;
    double time_result = 0.0;
    double eps_result = 0.0;

    std::vector<std::vector<double>> a(array_size, std::vector<double>(array_size));
    std::vector<double> b(array_size);
    std::vector<double> x(array_size);
    std::vector<int> ipvt(array_size);

    double ops, total, norma, normx = 0.0;
    double resid, time = 0.0;
    int n, lda = 0;
    lda = array_size;
    n = array_size;
    double nf = static_cast<double>(n);

    ops = (2.0 * nf * nf * nf) / 3.0 + 2.0 * (nf * nf);

    norma = matgen(a, lda, n, b);
    time = static_cast<double>(second()) / 1000.0;
    dgefa(a, lda, n, ipvt);
    dgesl(a, lda, n, ipvt, b, 0);
    total = static_cast<double>(second()) / 1000.0 - time;

    for (int i = 0; i < n; i++) {
        x[i] = b[i];
    }
    norma = matgen(a, lda, n, b);
    for (int i = 0; i < n; i++) {
        b[i] = -b[i];
    }
    dmxpy(n, b, n, lda, x, a);
    resid = 0.0;
    normx = 0.0;
    for (int i = 0; i < n; i++) {
        resid = std::max(resid, std::abs(b[i]));
        normx = std::max(normx, std::abs(x[i]));
    }

    eps_result = epslon(1.0);

    residn_result = resid / (static_cast<double>(n) * norma * normx * eps_result);
    residn_result += 0.005; // for rounding
    residn_result = std::round(residn_result * 100) / 100;

    time_result = total;
    time_result += 0.005; // for rounding
    time_result = std::round(time_result * 100) / 100;

    mflops_result = ops / (1.0e6 * total);
    mflops_result += 0.0005; // for rounding
    mflops_result = std::round(mflops_result * 1000) / 1000;

    LinpackResult result = {norma, resid, residn_result, eps_result, time_result, mflops_result};

    std::cout << "Norma: " << result.Norma << "\n";
    std::cout << "Residual: " << result.Residual << "\n";
    std::cout << "NormalisedResidual: " << result.NormalisedResidual << "\n";
    std::cout << "Epsilon: " << result.Epsilon << "\n";
    std::cout << "Time: " << result.Time << "\n";
    std::cout << "MFLOPS: " << result.MFLOPS << "\n";

    return result;
}

int main() {
    int64_t startTimeMs = second();

    linpack(ARRAY_SIZE);

    int64_t endTimeMs = second();
    int64_t durationMs = endTimeMs - startTimeMs;

    std::cout << "Execution time: " << durationMs << "ms\n";

    return 0;
}
