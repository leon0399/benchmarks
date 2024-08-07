# Results

## Algorithms

### primes/Simple

| Language | Time, s | %99 Time, s | %95 Time, s | %50 Time, s | %5 Time, s | Startup time, s | Total time, s | Memory, MiB |
| :------- | ------: | ----------: |  ---------: |  ---------: |  --------: | --------------: | ------------: | ----------: |
| C++ (clang) |  0.054<sub>±0.000</sub> |  0.055 |  0.055 |  0.054 |  0.053 |  0.002<sub>±0.000</sub> |  0.056<sub>±0.001</sub> |       1.81<sub>±0.72</sub> |
| C++ (gcc) |  0.053<sub>±0.001</sub> |  0.054 |  0.054 |  0.053 |  0.052 |  0.002<sub>±0.000</sub> |  0.055<sub>±0.001</sub> |       1.81<sub>±0.02</sub> |
| C (clang) |  0.055<sub>±0.001</sub> |  0.057 |  0.057 |  0.055 |  0.055 |  0.001<sub>±0.000</sub> |  0.057<sub>±0.001</sub> |       1.14<sub>±0.31</sub> |
| C (gcc) |  0.054<sub>±0.001</sub> |  0.055 |  0.055 |  0.054 |  0.054 |  0.001<sub>±0.000</sub> |  0.056<sub>±0.001</sub> |       1.14<sub>±0.39</sub> |
| Fortran (gfortran) |  0.054<sub>±0.000</sub> |  0.055 |  0.055 |  0.054 |  0.054 |  0.001<sub>±0.000</sub> |  0.056<sub>±0.001</sub> |       1.29<sub>±0.45</sub> |
| Go |  0.063<sub>±0.001</sub> |  0.064 |  0.064 |  0.063 |  0.062 |  0.002<sub>±0.000</sub> |  0.065<sub>±0.000</sub> |       2.92<sub>±0.00</sub> |
| Java |  0.069<sub>±0.003</sub> |  0.076 |  0.074 |  0.069 |  0.067 |  0.040<sub>±0.003</sub> |  0.108<sub>±0.003</sub> |      40.45<sub>±0.79</sub> |
| Java (GraalVM) |  0.075<sub>±0.002</sub> |  0.079 |  0.078 |  0.075 |  0.074 |  0.080<sub>±0.011</sub> |  0.159<sub>±0.013</sub> |      80.09<sub>±3.77</sub> |
| JavaScript (Node) |  0.067<sub>±0.003</sub> |  0.073 |  0.071 |  0.067 |  0.062 |  0.028<sub>±0.001</sub> |  0.095<sub>±0.004</sub> |      44.05<sub>±1.05</sub> |
| JavaScript (GraalVM) |  0.458<sub>±0.025</sub> |  0.505 |  0.501 |  0.458 |  0.433 |  0.379<sub>±0.020</sub> |  0.837<sub>±0.027</sub> |     336.66<sub>±8.63</sub> |
| Kotlin (JVM) |  0.062<sub>±0.004</sub> |  0.070 |  0.070 |  0.062 |  0.059 |  0.047<sub>±0.003</sub> |  0.110<sub>±0.005</sub> |      41.68<sub>±0.86</sub> |
| Kotlin (Native) |  0.065<sub>±0.003</sub> |  0.068 |  0.068 |  0.065 |  0.059 |  0.003<sub>±0.002</sub> |  0.068<sub>±0.003</sub> |       4.28<sub>±0.11</sub> |
| Lua |  0.423<sub>±0.016</sub> |  0.453 |  0.449 |  0.423 |  0.409 |  0.002<sub>±0.001</sub> |  0.424<sub>±0.016</sub> |       1.56<sub>±0.46</sub> |
| Lua (LuaJIT) |  0.051<sub>±0.000</sub> |  0.052 |  0.052 |  0.051 |  0.051 |  0.001<sub>±0.001</sub> |  0.052<sub>±0.001</sub> |       2.28<sub>±0.05</sub> |
| Perl |  3.297<sub>±0.023</sub> |  3.342 |  3.332 |  3.297 |  3.269 |  0.014<sub>±0.015</sub> |  3.315<sub>±0.019</sub> |       7.30<sub>±0.08</sub> |
| PHP |  0.506<sub>±0.044</sub> |  0.613 |  0.599 |  0.506 |  0.481 |  0.021<sub>±0.003</sub> |  0.526<sub>±0.046</sub> |      23.10<sub>±0.17</sub> |
| PHP (JIT: tracing) |  0.075<sub>±0.005</sub> |  0.085 |  0.085 |  0.075 |  0.070 |  0.025<sub>±0.002</sub> |  0.100<sub>±0.007</sub> |      26.57<sub>±0.19</sub> |
| PHP (JIT: function) |  0.103<sub>±0.013</sub> |  0.127 |  0.124 |  0.103 |  0.089 |  0.023<sub>±0.001</sub> |  0.126<sub>±0.013</sub> |      26.39<sub>±0.11</sub> |
| Python (CPython) |  1.739<sub>±0.036</sub> |  1.823 |  1.817 |  1.739 |  1.721 |  0.017<sub>±0.001</sub> |  1.757<sub>±0.036</sub> |       8.96<sub>±0.05</sub> |
| Python (PyPy) |  0.097<sub>±0.008</sub> |  0.114 |  0.111 |  0.097 |  0.089 |  0.032<sub>±0.002</sub> |  0.129<sub>±0.010</sub> |      53.38<sub>±0.27</sub> |
| Python (Numba) |  0.303<sub>±0.045</sub> |  0.429 |  0.385 |  0.303 |  0.285 |  0.764<sub>±0.206</sub> |  1.057<sub>±0.214</sub> |     105.72<sub>±2.09</sub> |
| Ruby |  5.347<sub>±0.143</sub> |  5.672 |  5.587 |  5.347 |  5.215 |  0.056<sub>±0.030</sub> |  5.430<sub>±0.139</sub> |      15.68<sub>±0.12</sub> |
| Ruby (JIT) |  5.031<sub>±0.121</sub> |  5.379 |  5.277 |  5.031 |  5.004 |  0.052<sub>±0.005</sub> |  5.084<sub>±0.119</sub> |      16.25<sub>±0.09</sub> |
| Ruby (JRuby) |  4.533<sub>±0.103</sub> |  4.672 |  4.666 |  4.533 |  4.375 |  2.162<sub>±0.125</sub> |  6.671<sub>±0.126</sub> |     359.57<sub>±19.06</sub> |
| Rust |  0.053<sub>±0.001</sub> |  0.054 |  0.054 |  0.053 |  0.052 |  0.002<sub>±0.001</sub> |  0.055<sub>±0.001</sub> |       1.75<sub>±0.07</sub> |
| Swift |  2.938<sub>±0.019</sub> |  2.971 |  2.961 |  2.938 |  2.912 |  0.254<sub>±0.573</sub> |  3.190<sub>±0.469</sub> |     165.90<sub>±14.32</sub> |
| Swift (Optimized) |  0.055<sub>±0.002</sub> |  0.061 |  0.061 |  0.055 |  0.054 |  0.309<sub>±0.216</sub> |  0.362<sub>±0.177</sub> |     172.12<sub>±14.75</sub> |
| Swift (Compiled) |  0.056<sub>±0.004</sub> |  0.066 |  0.065 |  0.056 |  0.054 |  0.006<sub>±0.001</sub> |  0.062<sub>±0.005</sub> |      11.08<sub>±1.42</sub> |


### primes/Atkin

| Language | Time, s | %99 Time, s | %95 Time, s | %50 Time, s | %5 Time, s | Startup time, s | Total time, s | Memory, MiB |
| :------- | ------: | ----------: |  ---------: |  ---------: |  --------: | --------------: | ------------: | ----------: |
| C++ (clang) |  0.244<sub>±0.208</sub> |  0.841 |  0.620 |  0.244 |  0.213 |  0.012<sub>±0.001</sub> |  0.256<sub>±0.208</sub> |      89.09<sub>±0.03</sub> |
| C++ (gcc) |  0.217<sub>±0.020</sub> |  0.254 |  0.250 |  0.217 |  0.194 |  0.013<sub>±0.001</sub> |  0.230<sub>±0.021</sub> |      89.09<sub>±0.06</sub> |
| Go |  0.180<sub>±0.012</sub> |  0.208 |  0.202 |  0.180 |  0.172 |  0.003<sub>±0.000</sub> |  0.183<sub>±0.012</sub> |      79.45<sub>±0.66</sub> |
| Java |  0.221<sub>±0.011</sub> |  0.238 |  0.238 |  0.221 |  0.209 |  0.051<sub>±0.003</sub> |  0.272<sub>±0.014</sub> |     187.36<sub>±1.75</sub> |
| Java (GraalVM) |  0.347<sub>±0.029</sub> |  0.388 |  0.388 |  0.347 |  0.306 |  0.091<sub>±0.007</sub> |  0.440<sub>±0.032</sub> |     244.36<sub>±13.99</sub> |
| JavaScript (Node) |  0.366<sub>±0.029</sub> |  0.409 |  0.405 |  0.366 |  0.324 |  0.072<sub>±0.004</sub> |  0.438<sub>±0.034</sub> |     226.77<sub>±0.99</sub> |
| JavaScript (GraalVM) |  2.896<sub>±0.200</sub> |  3.250 |  3.167 |  2.896 |  2.657 |  0.412<sub>±0.023</sub> |  3.316<sub>±0.194</sub> |     797.01<sub>±38.81</sub> |
| PHP |  2.051<sub>±0.051</sub> |  2.151 |  2.134 |  2.051 |  1.993 |  0.021<sub>±0.002</sub> |  2.072<sub>±0.051</sub> |     245.12<sub>±0.15</sub> |
| PHP (JIT: tracing) |  1.117<sub>±0.061</sub> |  1.218 |  1.211 |  1.117 |  1.062 |  0.024<sub>±0.002</sub> |  1.140<sub>±0.061</sub> |     248.59<sub>±0.18</sub> |
| PHP (JIT: function) |  1.148<sub>±0.036</sub> |  1.243 |  1.225 |  1.148 |  1.130 |  0.025<sub>±0.002</sub> |  1.174<sub>±0.037</sub> |     248.50<sub>±0.09</sub> |
| Python (CPython) |  4.375<sub>±0.071</sub> |  4.450 |  4.438 |  4.375 |  4.246 |  0.018<sub>±0.001</sub> |  4.394<sub>±0.072</sub> |     192.65<sub>±0.13</sub> |
| Python (PyPy) |  1.287<sub>±0.034</sub> |  1.376 |  1.358 |  1.287 |  1.271 |  0.054<sub>±0.002</sub> |  1.340<sub>±0.035</sub> |     303.95<sub>±0.26</sub> |
| Ruby |  2.867<sub>±0.057</sub> |  2.963 |  2.961 |  2.867 |  2.807 |  0.075<sub>±0.004</sub> |  2.943<sub>±0.057</sub> |     158.21<sub>±0.11</sub> |
| Ruby (JIT) |  2.165<sub>±0.053</sub> |  2.228 |  2.225 |  2.165 |  2.088 |  0.074<sub>±0.005</sub> |  2.237<sub>±0.056</sub> |     158.79<sub>±0.11</sub> |
| Ruby (JRuby) |  3.323<sub>±0.111</sub> |  3.414 |  3.410 |  3.323 |  3.120 |  2.497<sub>±0.324</sub> |  5.699<sub>±0.343</sub> |     602.69<sub>±29.44</sub> |
| Rust |  0.171<sub>±0.006</sub> |  0.183 |  0.181 |  0.171 |  0.164 |  0.009<sub>±0.001</sub> |  0.180<sub>±0.006</sub> |      77.52<sub>±0.08</sub> |


### collatz/MaxSequence

| Language | Time, s | %99 Time, s | %95 Time, s | %50 Time, s | %5 Time, s | Startup time, s | Total time, s | Memory, MiB |
| :------- | ------: | ----------: |  ---------: |  ---------: |  --------: | --------------: | ------------: | ----------: |
| C++ (clang) |  0.060<sub>±0.001</sub> |  0.063 |  0.063 |  0.060 |  0.059 |  0.002<sub>±0.000</sub> |  0.063<sub>±0.001</sub> |       1.80<sub>±0.48</sub> |
| Go |  0.098<sub>±0.006</sub> |  0.105 |  0.103 |  0.098 |  0.088 |  0.002<sub>±0.000</sub> |  0.100<sub>±0.006</sub> |       2.92<sub>±0.00</sub> |
| Java |  0.099<sub>±0.006</sub> |  0.117 |  0.112 |  0.099 |  0.097 |  0.051<sub>±0.003</sub> |  0.150<sub>±0.009</sub> |      41.71<sub>±1.08</sub> |
| Java (GraalVM) |  0.107<sub>±0.010</sub> |  0.129 |  0.124 |  0.107 |  0.098 |  0.100<sub>±0.009</sub> |  0.202<sub>±0.017</sub> |      83.68<sub>±3.11</sub> |
| JavaScript (Node) |  0.661<sub>±0.010</sub> |  0.676 |  0.675 |  0.661 |  0.647 |  0.026<sub>±0.002</sub> |  0.687<sub>±0.011</sub> |      42.68<sub>±0.97</sub> |
| JavaScript (GraalVM) |  1.010<sub>±0.029</sub> |  1.044 |  1.042 |  1.010 |  0.968 |  0.368<sub>±0.019</sub> |  1.369<sub>±0.035</sub> |     333.56<sub>±7.96</sub> |
| PHP |  1.480<sub>±0.037</sub> |  1.568 |  1.549 |  1.480 |  1.449 |  0.019<sub>±0.001</sub> |  1.499<sub>±0.037</sub> |      23.02<sub>±0.10</sub> |
| PHP (JIT: tracing) |  0.498<sub>±0.015</sub> |  0.522 |  0.521 |  0.498 |  0.481 |  0.023<sub>±0.001</sub> |  0.522<sub>±0.015</sub> |      26.52<sub>±0.12</sub> |
| PHP (JIT: function) |  0.583<sub>±0.019</sub> |  0.623 |  0.619 |  0.583 |  0.571 |  0.023<sub>±0.001</sub> |  0.605<sub>±0.018</sub> |      26.51<sub>±0.16</sub> |
| Python (CPython) |  5.712<sub>±0.037</sub> |  5.778 |  5.770 |  5.712 |  5.675 |  0.017<sub>±0.001</sub> |  5.729<sub>±0.037</sub> |       8.91<sub>±0.05</sub> |
| Python (PyPy) |  0.131<sub>±0.005</sub> |  0.142 |  0.142 |  0.131 |  0.129 |  0.033<sub>±0.003</sub> |  0.164<sub>±0.005</sub> |      52.92<sub>±0.17</sub> |
| Python (Numba) |  0.333<sub>±0.032</sub> |  0.416 |  0.399 |  0.333 |  0.320 |  0.774<sub>±0.036</sub> |  1.113<sub>±0.067</sub> |     106.71<sub>±0.97</sub> |
| Ruby |  2.767<sub>±0.057</sub> |  2.883 |  2.873 |  2.767 |  2.722 |  0.057<sub>±0.004</sub> |  2.826<sub>±0.057</sub> |      15.64<sub>±0.15</sub> |
| Ruby (JIT) |  1.008<sub>±0.016</sub> |  1.029 |  1.024 |  1.008 |  0.983 |  0.049<sub>±0.001</sub> |  1.058<sub>±0.016</sub> |      16.12<sub>±0.10</sub> |
| Ruby (JRuby) |  1.219<sub>±0.073</sub> |  1.379 |  1.368 |  1.219 |  1.173 |  2.171<sub>±0.066</sub> |  3.432<sub>±0.101</sub> |     517.49<sub>±53.41</sub> |
| Rust |  0.051<sub>±0.002</sub> |  0.056 |  0.055 |  0.051 |  0.050 |  0.002<sub>±0.001</sub> |  0.053<sub>±0.002</sub> |       1.81<sub>±0.08</sub> |


### mandelbrot/Simple

| Language | Time, s | %99 Time, s | %95 Time, s | %50 Time, s | %5 Time, s | Startup time, s | Total time, s | Memory, MiB |
| :------- | ------: | ----------: |  ---------: |  ---------: |  --------: | --------------: | ------------: | ----------: |
| C++ (clang) |  0.033<sub>±0.000</sub> |  0.034 |  0.034 |  0.033 |  0.033 |  0.002<sub>±0.000</sub> |  0.035<sub>±0.001</sub> |       1.82<sub>±0.77</sub> |
| C++ (gcc) |  0.034<sub>±0.001</sub> |  0.035 |  0.035 |  0.034 |  0.033 |  0.002<sub>±0.000</sub> |  0.036<sub>±0.001</sub> |       1.82<sub>±0.75</sub> |
| C# (csc) |  0.108<sub>±0.001</sub> |  0.110 |  0.109 |  0.108 |  0.106 |  0.012<sub>±0.001</sub> |  0.120<sub>±0.002</sub> |      25.29<sub>±1.00</sub> |
| C# (mcs) |  0.111<sub>±0.003</sub> |  0.114 |  0.114 |  0.111 |  0.106 |  0.012<sub>±0.001</sub> |  0.123<sub>±0.003</sub> |      25.31<sub>±0.86</sub> |
| Go |  0.035<sub>±0.001</sub> |  0.036 |  0.036 |  0.035 |  0.034 |  0.002<sub>±0.000</sub> |  0.037<sub>±0.001</sub> |       2.92<sub>±0.14</sub> |
| Java |  0.057<sub>±0.001</sub> |  0.060 |  0.060 |  0.057 |  0.056 |  0.049<sub>±0.005</sub> |  0.106<sub>±0.005</sub> |      44.40<sub>±1.85</sub> |
| Java (GraalVM) |  0.052<sub>±0.003</sub> |  0.060 |  0.060 |  0.052 |  0.051 |  0.096<sub>±0.005</sub> |  0.149<sub>±0.005</sub> |      84.26<sub>±3.50</sub> |
| JavaScript (Node) |  0.051<sub>±0.002</sub> |  0.056 |  0.055 |  0.051 |  0.049 |  0.028<sub>±0.004</sub> |  0.080<sub>±0.006</sub> |      47.56<sub>±1.01</sub> |
| JavaScript (GraalVM) |  0.254<sub>±0.018</sub> |  0.285 |  0.282 |  0.254 |  0.233 |  0.386<sub>±0.020</sub> |  0.643<sub>±0.034</sub> |     335.32<sub>±7.59</sub> |
| Lua |  0.551<sub>±0.014</sub> |  0.571 |  0.565 |  0.551 |  0.525 |  0.002<sub>±0.001</sub> |  0.553<sub>±0.014</sub> |       1.57<sub>±0.53</sub> |
| Lua (LuaJIT) |  0.031<sub>±0.000</sub> |  0.032 |  0.032 |  0.031 |  0.031 |  0.001<sub>±0.000</sub> |  0.032<sub>±0.001</sub> |       2.34<sub>±0.04</sub> |
| PHP |  0.734<sub>±0.014</sub> |  0.761 |  0.757 |  0.734 |  0.721 |  0.019<sub>±0.001</sub> |  0.755<sub>±0.014</sub> |      23.07<sub>±0.10</sub> |
| PHP (JIT: tracing) |  0.122<sub>±0.003</sub> |  0.128 |  0.128 |  0.122 |  0.120 |  0.022<sub>±0.001</sub> |  0.145<sub>±0.004</sub> |      26.51<sub>±0.11</sub> |
| PHP (JIT: function) |  0.173<sub>±0.020</sub> |  0.218 |  0.214 |  0.173 |  0.161 |  0.025<sub>±0.003</sub> |  0.199<sub>±0.021</sub> |      26.46<sub>±0.11</sub> |
| Python (CPython) |  3.449<sub>±0.040</sub> |  3.533 |  3.519 |  3.449 |  3.410 |  0.017<sub>±0.002</sub> |  3.466<sub>±0.040</sub> |       9.11<sub>±0.03</sub> |
| Python (PyPy) |  0.050<sub>±0.001</sub> |  0.052 |  0.052 |  0.050 |  0.048 |  0.032<sub>±0.002</sub> |  0.081<sub>±0.003</sub> |      54.64<sub>±0.23</sub> |
| Python (Numba) |  0.322<sub>±0.017</sub> |  0.365 |  0.357 |  0.322 |  0.314 |  0.715<sub>±0.072</sub> |  1.046<sub>±0.085</sub> |     105.40<sub>±1.52</sub> |
| Ruby |  1.953<sub>±0.042</sub> |  2.033 |  2.031 |  1.953 |  1.925 |  0.052<sub>±0.004</sub> |  2.006<sub>±0.040</sub> |      15.79<sub>±0.12</sub> |
| Ruby (JIT) |  1.429<sub>±0.043</sub> |  1.523 |  1.505 |  1.429 |  1.387 |  0.051<sub>±0.004</sub> |  1.479<sub>±0.044</sub> |      16.16<sub>±0.10</sub> |
| Ruby (JRuby) |  2.357<sub>±0.076</sub> |  2.488 |  2.455 |  2.357 |  2.239 |  2.154<sub>±0.158</sub> |  4.605<sub>±0.169</sub> |     549.95<sub>±62.82</sub> |
| Rust |  0.032<sub>±0.000</sub> |  0.033 |  0.033 |  0.032 |  0.032 |  0.002<sub>±0.001</sub> |  0.034<sub>±0.001</sub> |       1.79<sub>±0.09</sub> |


### treap/Naive

| Language | Time, s | %99 Time, s | %95 Time, s | %50 Time, s | %5 Time, s | Startup time, s | Total time, s | Memory, MiB |
| :------- | ------: | ----------: |  ---------: |  ---------: |  --------: | --------------: | ------------: | ----------: |
| C++ (clang) |  0.227<sub>±0.007</sub> |  0.241 |  0.239 |  0.227 |  0.222 |  0.002<sub>±0.000</sub> |  0.229<sub>±0.007</sub> |       3.41<sub>±0.86</sub> |
| C++ (gcc) |  0.199<sub>±0.005</sub> |  0.204 |  0.204 |  0.199 |  0.191 |  0.002<sub>±0.000</sub> |  0.201<sub>±0.005</sub> |       2.64<sub>±0.89</sub> |
| Go |  0.325<sub>±0.010</sub> |  0.335 |  0.334 |  0.325 |  0.308 |  0.002<sub>±0.000</sub> |  0.327<sub>±0.009</sub> |       7.64<sub>±0.87</sub> |
| Java |  0.564<sub>±0.016</sub> |  0.594 |  0.592 |  0.564 |  0.551 |  0.052<sub>±0.002</sub> |  0.617<sub>±0.017</sub> |     155.96<sub>±18.74</sub> |
| Java (GraalVM) |  0.590<sub>±0.119</sub> |  0.825 |  0.822 |  0.590 |  0.515 |  0.098<sub>±0.011</sub> |  0.690<sub>±0.121</sub> |     229.96<sub>±54.75</sub> |
| JavaScript (Node) |  0.970<sub>±0.023</sub> |  1.015 |  1.010 |  0.970 |  0.947 |  0.036<sub>±0.001</sub> |  1.007<sub>±0.024</sub> |      83.42<sub>±0.93</sub> |
| JavaScript (GraalVM) |  2.433<sub>±0.081</sub> |  2.507 |  2.505 |  2.433 |  2.282 |  0.403<sub>±0.026</sub> |  2.846<sub>±0.090</sub> |     545.30<sub>±18.72</sub> |
| Kotlin (JVM) |  0.595<sub>±0.036</sub> |  0.677 |  0.657 |  0.595 |  0.560 |  0.048<sub>±0.005</sub> |  0.644<sub>±0.040</sub> |     157.74<sub>±20.11</sub> |
| Kotlin (Native) |  0.989<sub>±0.014</sub> |  1.004 |  1.004 |  0.989 |  0.967 |  0.009<sub>±0.001</sub> |  0.999<sub>±0.014</sub> |      23.91<sub>±0.99</sub> |
| Lua |  4.410<sub>±0.164</sub> |  4.752 |  4.706 |  4.410 |  4.271 |  0.004<sub>±0.005</sub> |  4.422<sub>±0.164</sub> |       3.16<sub>±0.21</sub> |
| Lua (LuaJIT) |  1.672<sub>±0.111</sub> |  1.927 |  1.863 |  1.672 |  1.556 |  0.002<sub>±0.001</sub> |  1.673<sub>±0.111</sub> |       4.14<sub>±0.08</sub> |
| PHP |  5.072<sub>±0.044</sub> |  5.177 |  5.152 |  5.072 |  5.036 |  0.020<sub>±0.001</sub> |  5.091<sub>±0.044</sub> |      23.17<sub>±0.12</sub> |
| PHP (JIT: tracing) |  3.124<sub>±0.035</sub> |  3.156 |  3.152 |  3.124 |  3.059 |  0.024<sub>±0.002</sub> |  3.149<sub>±0.034</sub> |      26.72<sub>±0.13</sub> |
| PHP (JIT: function) |  3.272<sub>±0.065</sub> |  3.455 |  3.404 |  3.272 |  3.247 |  0.024<sub>±0.001</sub> |  3.297<sub>±0.065</sub> |      26.53<sub>±0.12</sub> |
| Python (CPython) |  7.335<sub>±0.030</sub> |  7.384 |  7.382 |  7.335 |  7.306 |  0.018<sub>±0.001</sub> |  7.354<sub>±0.030</sub> |       9.83<sub>±0.08</sub> |
| Python (PyPy) |  2.809<sub>±0.067</sub> |  2.935 |  2.909 |  2.809 |  2.728 |  0.037<sub>±0.011</sub> |  2.844<sub>±0.066</sub> |      62.16<sub>±0.59</sub> |
| Ruby |  6.104<sub>±0.158</sub> |  6.486 |  6.451 |  6.104 |  6.052 |  0.054<sub>±0.005</sub> |  6.164<sub>±0.157</sub> |      17.46<sub>±0.10</sub> |
| Ruby (JIT) |  3.210<sub>±0.058</sub> |  3.343 |  3.329 |  3.210 |  3.182 |  0.051<sub>±0.002</sub> |  3.260<sub>±0.057</sub> |      18.12<sub>±0.10</sub> |
| Ruby (JRuby) |  5.521<sub>±0.273</sub> |  5.791 |  5.789 |  5.521 |  5.028 |  2.227<sub>±0.064</sub> |  7.715<sub>±0.280</sub> |     236.45<sub>±21.72</sub> |


### recursion/Tak

| Language | Time, s | %99 Time, s | %95 Time, s | %50 Time, s | %5 Time, s | Startup time, s | Total time, s | Memory, MiB |
| :------- | ------: | ----------: |  ---------: |  ---------: |  --------: | --------------: | ------------: | ----------: |
| C++ (clang) |  0.044<sub>±0.004</sub> |  0.054 |  0.052 |  0.044 |  0.043 |  0.002<sub>±0.000</sub> |  0.046<sub>±0.004</sub> |       1.82<sub>±0.65</sub> |
| C++ (gcc) |  0.026<sub>±0.004</sub> |  0.037 |  0.035 |  0.026 |  0.026 |  0.002<sub>±0.000</sub> |  0.028<sub>±0.004</sub> |       2.56<sub>±0.82</sub> |
| Go |  0.058<sub>±0.002</sub> |  0.063 |  0.062 |  0.058 |  0.056 |  0.002<sub>±0.000</sub> |  0.060<sub>±0.002</sub> |       2.92<sub>±0.20</sub> |
| Java |  0.043<sub>±0.001</sub> |  0.045 |  0.045 |  0.043 |  0.042 |  0.050<sub>±0.002</sub> |  0.094<sub>±0.002</sub> |      40.74<sub>±0.96</sub> |
| Java (GraalVM) |  0.059<sub>±0.011</sub> |  0.087 |  0.083 |  0.059 |  0.056 |  0.093<sub>±0.009</sub> |  0.157<sub>±0.019</sub> |      78.40<sub>±2.93</sub> |
| JavaScript (Node) |  0.168<sub>±0.011</sub> |  0.183 |  0.181 |  0.168 |  0.152 |  0.028<sub>±0.002</sub> |  0.194<sub>±0.013</sub> |      42.51<sub>±1.05</sub> |
| JavaScript (GraalVM) |  0.810<sub>±0.072</sub> |  0.945 |  0.923 |  0.810 |  0.726 |  0.414<sub>±0.037</sub> |  1.215<sub>±0.098</sub> |     419.66<sub>±9.09</sub> |
| Lua |  1.033<sub>±0.036</sub> |  1.128 |  1.099 |  1.033 |  1.015 |  0.002<sub>±0.000</sub> |  1.035<sub>±0.036</sub> |       1.55<sub>±0.45</sub> |
| Lua (LuaJIT) |  0.164<sub>±0.006</sub> |  0.173 |  0.171 |  0.164 |  0.155 |  0.001<sub>±0.000</sub> |  0.166<sub>±0.006</sub> |       2.27<sub>±0.06</sub> |
| Perl |  9.509<sub>±0.065</sub> |  9.607 |  9.605 |  9.509 |  9.429 |  0.007<sub>±0.001</sub> |  9.516<sub>±0.066</sub> |       5.86<sub>±0.15</sub> |
| PHP |  1.236<sub>±0.024</sub> |  1.285 |  1.277 |  1.236 |  1.211 |  0.019<sub>±0.001</sub> |  1.254<sub>±0.024</sub> |      23.13<sub>±0.18</sub> |
| PHP (JIT: tracing) |  0.413<sub>±0.010</sub> |  0.433 |  0.429 |  0.413 |  0.403 |  0.022<sub>±0.001</sub> |  0.436<sub>±0.011</sub> |      26.54<sub>±0.16</sub> |
| PHP (JIT: function) |  0.454<sub>±0.013</sub> |  0.465 |  0.465 |  0.454 |  0.432 |  0.025<sub>±0.002</sub> |  0.479<sub>±0.014</sub> |      26.44<sub>±0.20</sub> |
| Python (CPython) |  2.867<sub>±0.047</sub> |  2.928 |  2.925 |  2.867 |  2.802 |  0.018<sub>±0.001</sub> |  2.884<sub>±0.048</sub> |       8.87<sub>±0.05</sub> |
| Python (PyPy) |  0.800<sub>±0.013</sub> |  0.820 |  0.817 |  0.800 |  0.781 |  0.032<sub>±0.002</sub> |  0.832<sub>±0.012</sub> |      59.72<sub>±0.22</sub> |
| Python (Numba) |  0.329<sub>±0.015</sub> |  0.351 |  0.349 |  0.329 |  0.305 |  0.740<sub>±0.036</sub> |  1.060<sub>±0.050</sub> |     105.33<sub>±1.47</sub> |
| Ruby |  1.551<sub>±0.027</sub> |  1.619 |  1.605 |  1.551 |  1.534 |  0.052<sub>±0.003</sub> |  1.604<sub>±0.028</sub> |      15.71<sub>±0.09</sub> |
| Ruby (JIT) |  0.300<sub>±0.008</sub> |  0.316 |  0.314 |  0.300 |  0.292 |  0.052<sub>±0.001</sub> |  0.351<sub>±0.008</sub> |      15.99<sub>±0.09</sub> |
| Ruby (JRuby) |  0.682<sub>±0.056</sub> |  0.726 |  0.718 |  0.682 |  0.577 |  2.134<sub>±0.029</sub> |  2.821<sub>±0.070</sub> |     181.99<sub>±4.79</sub> |


### linpack/Linpack

| Language | Time, s | %99 Time, s | %95 Time, s | %50 Time, s | %5 Time, s | Startup time, s | Total time, s | Memory, MiB |
| :------- | ------: | ----------: |  ---------: |  ---------: |  --------: | --------------: | ------------: | ----------: |
| C++ (clang) |  2.114<sub>±0.051</sub> |  2.172 |  2.161 |  2.114 |  2.026 |  0.006<sub>±0.001</sub> |  2.119<sub>±0.051</sub> |      33.53<sub>±0.33</sub> |
| C++ (gcc) |  2.144<sub>±0.050</sub> |  2.231 |  2.220 |  2.144 |  2.087 |  0.005<sub>±0.001</sub> |  2.149<sub>±0.050</sub> |      33.84<sub>±0.36</sub> |
| Go |  2.759<sub>±0.191</sub> |  3.063 |  3.029 |  2.759 |  2.557 |  0.002<sub>±0.000</sub> |  2.761<sub>±0.191</sub> |      35.96<sub>±0.16</sub> |
| Java |  1.886<sub>±0.125</sub> |  2.203 |  2.122 |  1.886 |  1.810 |  0.069<sub>±0.003</sub> |  1.955<sub>±0.125</sub> |      95.72<sub>±0.53</sub> |
| Java (GraalVM) |  4.553<sub>±0.148</sub> |  4.955 |  4.820 |  4.553 |  4.480 |  0.081<sub>±0.008</sub> |  4.636<sub>±0.148</sub> |     147.55<sub>±1.76</sub> |
| JavaScript (Node) |  9.541<sub>±0.050</sub> |  9.640 |  9.606 |  9.541 |  9.475 |  0.044<sub>±0.003</sub> |  9.583<sub>±0.051</sub> |     140.05<sub>±0.81</sub> |
| JavaScript (GraalVM) |  4.450<sub>±0.075</sub> |  4.621 |  4.575 |  4.450 |  4.374 |  0.393<sub>±0.137</sub> |  4.872<sub>±0.136</sub> |     407.62<sub>±14.23</sub> |
| PHP | 89.654<sub>±1.538</sub> | 94.070 | 92.846 | 89.654 | 89.293 |  0.021<sub>±0.002</sub> | 89.678<sub>±1.537</sub> |      95.04<sub>±0.14</sub> |
| PHP (JIT: tracing) | 24.875<sub>±0.140</sub> | 25.000 | 24.998 | 24.875 | 24.657 |  0.025<sub>±0.005</sub> | 24.902<sub>±0.137</sub> |      98.57<sub>±0.09</sub> |
| PHP (JIT: function) | 32.051<sub>±0.181</sub> | 32.304 | 32.292 | 32.051 | 31.781 |  0.027<sub>±0.001</sub> | 32.078<sub>±0.181</sub> |      98.38<sub>±0.18</sub> |
| Python (CPython) | 491.429<sub>±21.018</sub> | 502.447 | 500.310 | 491.429 | 453.944 |  0.021<sub>±0.001</sub> | 491.451<sub>±21.018</sub> |     163.44<sub>±0.89</sub> |
| Python (PyPy) |  6.791<sub>±0.215</sub> |  7.093 |  7.034 |  6.791 |  6.480 |  0.042<sub>±0.057</sub> |  6.832<sub>±0.231</sub> |     101.99<sub>±2.28</sub> |


## Legend

| Field        | Description |
| :----------- | :---------- |
| Time         | Time spent in the algorithm itself, reported by the program itself. |
| Total time   | Total time spent from the start of the program to the end of the algorithm, measured by the benchmark. |
| Startup time | Time spent from the start of the program to the start of the algorithm, measured by the benchmark (Total time - Time). |
| Memory       | Peak memory usage during the algorithm, measured by the benchmark. |


