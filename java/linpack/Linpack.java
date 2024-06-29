package linpack;

import java.util.Arrays;
import java.util.Random;

public class Linpack {

    public static final int ARRAY_SIZE = 2000;

    public static class LinpackResult {
        public double norma;
        public double residual;
        public double normalisedResidual;
        public double epsilon;
        public double time;
        public double mflops;

        @Override
        public String toString() {
            return "LinpackResult{" +
                    "norma=" + norma +
                    ", residual=" + residual +
                    ", normalisedResidual=" + normalisedResidual +
                    ", epsilon=" + epsilon +
                    ", time=" + time +
                    ", mflops=" + mflops +
                    '}';
        }
    }

    public static long second() {
        return System.nanoTime() / 1000000;
    }

    public static double matgen(double[][] a, int lda, int n, double[] b) {
        double norma = 0.0;
        Random random = new Random(1325);

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                a[j][i] = random.nextDouble() - 0.5;
                if (a[j][i] > norma) {
                    norma = a[j][i];
                }
            }
        }
        Arrays.fill(b, 0.0);
        for (int j = 0; j < n; j++) {
            for (int i = 0; i < n; i++) {
                b[i] += a[j][i];
            }
        }
        return norma;
    }

    public static int dgefa(double[][] a, int lda, int n, int[] ipvt) {
        int info = 0;
        int nm1 = n - 1;

        if (nm1 >= 0) {
            for (int k = 0; k < nm1; k++) {
                int kp1 = k + 1;
                int l = idamax(n - k, a[k], k, 1) + k;
                ipvt[k] = l;

                if (a[k][l] != 0) {
                    if (l != k) {
                        double t = a[k][l];
                        a[k][l] = a[k][k];
                        a[k][k] = t;
                    }

                    double t = -1.0 / a[k][k];
                    dscal(n - kp1, t, a[k], kp1, 1);

                    for (int j = kp1; j < n; j++) {
                        double t2 = a[j][l];
                        if (l != k) {
                            a[j][l] = a[j][k];
                            a[j][k] = t2;
                        }
                        daxpy(n - kp1, t2, a[k], kp1, 1, a[j], kp1, 1);
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

    public static void dgesl(double[][] a, int lda, int n, int[] ipvt, double[] b, int job) {
        int nm1 = n - 1;

        if (job == 0) {
            if (nm1 >= 1) {
                for (int k = 0; k < nm1; k++) {
                    int l = ipvt[k];
                    double t = b[l];
                    if (l != k) {
                        b[l] = b[k];
                        b[k] = t;
                    }
                    daxpy(n - (k + 1), t, a[k], k + 1, 1, b, k + 1, 1);
                }
            }

            for (int kb = 0; kb < n; kb++) {
                int k = n - (kb + 1);
                b[k] /= a[k][k];
                double t = -b[k];
                daxpy(k, t, a[k], 0, 1, b, 0, 1);
            }
        } else {
            for (int k = 0; k < n; k++) {
                double t = ddot(k, a[k], 0, 1, b, 0, 1);
                b[k] = (b[k] - t) / a[k][k];
            }

            if (nm1 >= 1) {
                for (int kb = 1; kb < nm1; kb++) {
                    int k = n - (kb + 1);
                    int kp1 = k + 1;
                    b[k] += ddot(n - kp1, a[k], kp1, 1, b, kp1, 1);
                    int l = ipvt[k];
                    if (l != k) {
                        double t = b[l];
                        b[l] = b[k];
                        b[k] = t;
                    }
                }
            }
        }
    }

    public static void daxpy(int n, double da, double[] dx, int dxOff, int incx, double[] dy, int dyOff, int incy) {
        int ix = 0, iy = 0;

        if (n > 0 && da != 0) {
            if (incx != 1 || incy != 1) {
                if (incx < 0) ix = (-n + 1) * incx;
                if (incy < 0) iy = (-n + 1) * incy;

                for (int i = 0; i < n; i++) {
                    dy[iy + dyOff] += da * dx[ix + dxOff];
                    ix += incx;
                    iy += incy;
                }
            } else {
                for (int i = 0; i < n; i++) {
                    dy[i + dyOff] += da * dx[i + dxOff];
                }
            }
        }
    }

    public static double ddot(int n, double[] dx, int dxOff, int incx, double[] dy, int dyOff, int incy) {
        double dtemp = 0.0;
        int ix = 0, iy = 0;

        if (n > 0) {
            if (incx != 1 || incy != 1) {
                if (incx < 0) ix = (-n + 1) * incx;
                if (incy < 0) iy = (-n + 1) * incy;

                for (int i = 0; i < n; i++) {
                    dtemp += dx[ix + dxOff] * dy[iy + dyOff];
                    ix += incx;
                    iy += incy;
                }
            } else {
                for (int i = 0; i < n; i++) {
                    dtemp += dx[i + dxOff] * dy[i + dyOff];
                }
            }
        }
        return dtemp;
    }

    public static void dscal(int n, double da, double[] dx, int dxOff, int incx) {
        int nincx;

        if (n > 0) {
            if (incx != 1) {
                nincx = n * incx;
                for (int i = 0; i < nincx; i += incx) {
                    dx[i + dxOff] *= da;
                }
            } else {
                for (int i = 0; i < n; i++) {
                    dx[i + dxOff] *= da;
                }
            }
        }
    }

    public static int idamax(int n, double[] dx, int dxOff, int incx) {
        double dmax = 0.0, dtemp;
        int itemp = 0, ix = 0;

        if (n < 1) {
            itemp = -1;
        } else if (n == 1) {
            itemp = 0;
        } else if (incx != 1) {
            dmax = Math.abs(dx[0 + dxOff]);
            ix = 1 + incx;
            for (int i = 1; i < n; i++) {
                dtemp = Math.abs(dx[ix + dxOff]);
                if (dtemp > dmax) {
                    itemp = i;
                    dmax = dtemp;
                }
                ix += incx;
            }
        } else {
            dmax = Math.abs(dx[0 + dxOff]);
            for (int i = 1; i < n; i++) {
                dtemp = Math.abs(dx[i + dxOff]);
                if (dtemp > dmax) {
                    itemp = i;
                    dmax = dtemp;
                }
            }
        }
        return itemp;
    }

    public static double epslon(double x) {
        double a = 4.0 / 3.0;
        double eps = 0.0;

        while (eps == 0) {
            double b = a - 1.0;
            double c = b + b + b;
            eps = Math.abs(c - 1.0);
        }
        return eps * Math.abs(x);
    }

    public static void dmxpy(int n1, double[] y, int n2, int ldm, double[] x, double[][] m) {
        for (int j = 0; j < n2; j++) {
            for (int i = 0; i < n1; i++) {
                y[i] += x[j] * m[j][i];
            }
        }
    }

    public static LinpackResult linpack(int arraySize) {
        double mflopsResult = 0.0;
        double residnResult = 0.0;
        double timeResult = 0.0;
        double epsResult = 0.0;

        double[][] a = new double[arraySize][arraySize];
        double[] b = new double[arraySize];
        double[] x = new double[arraySize];
        double ops, total, norma, normx = 0.0;
        double resid, time;
        int n, lda = 0;
        int[] ipvt = new int[arraySize];

        lda = arraySize;
        n = arraySize;
        double nf = (double) n;

        ops = ((2.0 * nf) * nf * nf) / 3.0 + 2.0 * (nf * nf);

        norma = matgen(a, lda, n, b);
        time = (double) second() / 1000.0;
        dgefa(a, lda, n, ipvt);
        dgesl(a, lda, n, ipvt, b, 0);
        total = (double) second() / 1000.0 - time;

        System.arraycopy(b, 0, x, 0, n);
        norma = matgen(a, lda, n, b);
        for (int i = 0; i < n; i++) {
            b[i] = -b[i];
        }
        dmxpy(n, b, n, lda, x, a);
        resid = 0.0;
        normx = 0.0;
        for (int i = 0; i < n; i++) {
            resid = Math.max(resid, Math.abs(b[i]));
            normx = Math.max(normx, Math.abs(x[i]));
        }

        epsResult = epslon(1.0);

        residnResult = resid / (n * norma * normx * epsResult);
        residnResult = Math.round(residnResult * 100.0) / 100.0;

        timeResult = Math.round(total * 100.0) / 100.0;

        mflopsResult = ops / (1.0e6 * total);
        mflopsResult = Math.round(mflopsResult * 1000.0) / 1000.0;

        LinpackResult result = new LinpackResult();
        result.norma = norma;
        result.residual = resid;
        result.normalisedResidual = residnResult;
        result.epsilon = epsResult;
        result.time = timeResult;
        result.mflops = mflopsResult;

        System.out.println(result);

        return result;
    }

    public static void main(String[] args) {
        long startTimeMs = System.currentTimeMillis();

        linpack(ARRAY_SIZE);

        long endTimeMs = System.currentTimeMillis();
        long durationMs = endTimeMs - startTimeMs;

        System.out.printf("Execution time: %dms\n", durationMs);
    }
}
