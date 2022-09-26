import time, math

ARRAY_SIZE = 2000

def linpack(array_size : int):
  mflops_result = .0
  residn_result = .0
  time_result = .0
  eps_result = .0
  a = [[0] * array_size for i in range(array_size)]
  b = [0] * array_size
  x = [0] * array_size
  ipvt = [0] * array_size
  lda = array_size
  n = array_size

  ops = ((2.0e0 * n) * n * n) / 3.0 + 2.0 * (n * n)

  norma = __matgen(a, lda, n, b)

  start = time.time()

  info = __dgefa(a, lda, n, ipvt)
  __dgesl(a, lda, n, ipvt, b, 0)

  total = time.time() - start

  x = [i for i in b]

  norma = __matgen(a, lda, n, b)

  b = [-i for i in b]


  __dmxpy(n, b, n, lda, x, a)

  resid = .0
  normx = .0

  for i in range(n):
      resid = resid if resid > abs(b[i]) else abs(b[i])
      normx = normx if normx > abs(x[i]) else abs(x[i])

  eps_result = __epslon(1.0)
  residn_result = (resid / ((((n) * norma * normx) * eps_result)))
  residn_result += .005
  residn_result = (math.floor((residn_result * (100))))
  residn_result /= (100)
  time_result = total
  time_result += .005
  time_result = (math.floor((time_result * (100))))
  time_result /= (100)

  mflops_result = ops / (1.0e6 * total)
  mflops_result += .0005
  mflops_result = (math.floor((mflops_result * (1000))))
  mflops_result /= (1000)

  result = {
    "Norma" : norma,
    "Residual" : resid,
    "NormalisedResidual" : residn_result,
    "Eepsilon" : eps_result,
    "Time" : time_result,
    "MFLOPS" : mflops_result
  }

  print(result)

  return result

def __matgen(a, lda : int, n : int, b) -> float:
  iseed = [0] * 4
  iseed[0] = 1
  iseed[1] = 2
  iseed[2] = 3
  iseed[3] = 1325
  norma = .0

  for i in range(n):
    for j in range(n):
      a[j][i] = (__lran(iseed) - .5)
      norma = (a[j][i] if (a[j][i] > norma) else norma)

  for i in range(n):
    b[i] = 0.0

  for j in range(n):
    for i in range(n):
      b[i] += a[j][i]

  return norma

def __lran(seed) -> float:
  m1 = 494
  m2 = 322
  m3 = 2508
  m4 = 2549
  ipw2 = 4096
  r = 1.0 / ipw2
  it4 = seed[3] * m4
  it3 = math.floor(it4 / ipw2)
  it4 = it4 - ipw2 * it3
  it3 = it3 + seed[2] * m4 + seed[3] * m3
  it2 = math.floor(it3 / ipw2)
  it3 = it3 - ipw2 * it2
  it2 = it2 + seed[1] * m4 + seed[2] * m3 + seed[3] * m2
  it1 = math.floor(it2 / ipw2)
  it2 = it2 - ipw2 * it1
  it1 = it1 + seed[0] * m4 + seed[1] * m3 + seed[2] * m2 + seed[3] * m1
  it1 = it1 % ipw2
  seed[0] = it1
  seed[1] = it2
  seed[2] = it3
  seed[3] = it4
  result = r * (it1 + r * (it2 + r * (it3 + r * it4)))
  return result

def __dgefa(a, lda : int, n : int, ipvt) -> int:
  col_k = [ ]
  col_j = [ ]
  info = 0
  nm1 = (n - 1)
  if (nm1 >= 0): 
    for k in range(nm1):
      col_k = a[k]
      kp1 = (k + 1)
      l_ = (__idamax(n - k, col_k, k, 1) + k)
      ipvt[k] = l_
      if col_k[l_] != 0:
        if l_ != k:
          t = col_k[l_]
          col_k[l_] = col_k[k]
          col_k[k] = t
        t = -1.0 / col_k[k]
        __dscal(n - kp1, t, col_k, kp1, 1)
        for j in range(kp1, n):
          col_j = a[j]
          t = col_j[l_]
          if l_ != k: 
            col_j[l_] = col_j[k]
            col_j[k] = t
          __daxpy(n - kp1, t, col_k, kp1, 1, col_j, kp1, 1)
      else: 
        info = k
  ipvt[n - 1] = (n - 1)
  if (a[(n - 1)][(n - 1)] == 0): 
    info = (n - 1)
  return info

def __dgesl(a, lda : int, n : int, ipvt, b, job : int) -> None:
  nm1 = n - 1
  if job == 0: 
    if (nm1 >= 1): 
      for k in range(nm1):
        l_ = ipvt[k]
        t = b[l_]
        if l_ != k:
          b[l_] = b[k]
          b[k] = t
        kp1 = k + 1
        __daxpy(n - kp1, t, a[k], kp1, 1, b, kp1, 1)
    for kb in range(n):
      k = n - (kb + 1)
      b[k] /= a[k][k]
      t = - b[k]
      __daxpy(k, t, a[k], 0, 1, b, 0, 1)
  else: 
    for k in range(n): 
      t = __ddot(k, a[k], 0, 1, b, 0, 1)
      b[k] = (b[k] - t) / a[k][k]
    if (nm1 >= 1): 
      for kb in range(1, nm1):
        k = (n - ((kb + 1)))
        kp1 = (k + 1)
        b[k] += __ddot(n - ((kp1)), a[k], kp1, 1, b, kp1, 1)
        l_ = ipvt[k]
        if (l_ != k): 
          t = b[l_]
          b[l_] = b[k]
          b[k] = t

def __daxpy(n : int, da : float, dx, dx_off : int, incx : int, dy, dy_off : int, incy : int) -> None:
  if (((n > 0)) and ((da != 0))): 
    if (incx != 1 or incy != 1): 
      ix = 0
      iy = 0
      if (incx < 0): 
        ix = (- n + 1) * incx
      if (incy < 0): 
        iy = (- n + 1) * incy
      for i in range(n): 
        dy[iy + dy_off] += (da * dx[ix + dx_off])
        ix += incx
        iy += incy
      return
    else: 
      for i in range(n):
        dy[i + dy_off] += da * dx[i + dx_off]

def __ddot(n : int, dx, dx_off : int, incx : int, dy, dy_off : int, incy : int) -> float:
  dtemp = (0)
  if (n > 0): 
    if (incx != 1 or incy != 1): 
      ix = 0
      iy = 0
      if (incx < 0): 
        ix = (- n + 1) * incx
      if (incy < 0): 
        iy = (- n + 1) * incy
      for i in range(n):
        dtemp += dx[ix + dx_off] * dy[iy + dy_off]
        ix += incx
        iy += incy
    else: 
      for i in range(n):
        dtemp += dx[i + dx_off] * dy[i + dy_off]
  return (dtemp)

def __dscal(n : int, da : float, dx, dx_off : int, incx : int) -> None:
  if (n > 0): 
    if (incx != 1): 
      nincx = (n * incx)
      for i in range(0, nincx, incx):
        dx[i + dx_off] *= da
    else: 
      for i in range(n):
        dx[i + dx_off] *= da

def __idamax(n : int, dx, dx_off : int, incx : int) -> int:
  itemp = 0
  if (n < 1): 
    itemp = -1
  elif (n == 1): 
    itemp = 0
  elif (incx != 1): 
    dmax = abs(dx[0 + dx_off])
    ix = (1 + incx)
    for i in range(n):
      dtemp = abs(dx[ix + dx_off])
      if (dtemp > dmax): 
        itemp = i
        dmax = dtemp
      ix += incx
  else: 
    itemp = 0
    dmax = abs(dx[0 + dx_off])
    for i in range(n): 
      dtemp = abs(dx[i + dx_off])
      if (dtemp > dmax): 
        itemp = i
        dmax = dtemp
  return (itemp)

def __epslon(x : float) -> float:
  a = 4.0e0 / 3.0e0
  eps = (0)
  while eps == 0:
    b = (a - 1.0)
    c = 3*b
    eps = abs(c - 1.0)
  return (eps * abs(x))

def __dmxpy(n1 : int, y, n2 : int, ldm : int, x, m) -> None:
  for j in range(n2):
    i = 0
    for i in range(n1): 
      y[i] += (x[j] * m[j][i])
      i += 1

def run():
  linpack(ARRAY_SIZE)

run()