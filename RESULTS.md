# Results

## Algorithms

### primes/Simple

| Language | Time, s | Startup time, s | Total time, s | Memory, MiB |
| :------- | ------: | --------------: | ------------: | ----------: |
| C++ (clang) |  0.350<sub>±0.003</sub> |  0.003<sub>±0.001</sub> |  0.352<sub>±0.003</sub> |       3.36<sub>±0.87</sub> |
| C++ (gcc) |  0.361<sub>±0.012</sub> |  0.003<sub>±0.000</sub> |  0.363<sub>±0.012</sub> |       1.84<sub>±0.84</sub> |
| C (clang) |  0.347<sub>±0.003</sub> |  0.001<sub>±0.000</sub> |  0.349<sub>±0.003</sub> |       1.50<sub>±0.35</sub> |
| C (gcc) |  0.349<sub>±0.003</sub> |  0.001<sub>±0.000</sub> |  0.350<sub>±0.003</sub> |       0.89<sub>±0.27</sub> |
| Fortran (gfortran) |  0.350<sub>±0.005</sub> |  0.002<sub>±0.001</sub> |  0.352<sub>±0.005</sub> |       1.30<sub>±0.03</sub> |
| Go |  0.418<sub>±0.012</sub> |  0.002<sub>±0.000</sub> |  0.421<sub>±0.012</sub> |       2.93<sub>±0.00</sub> |
| Java |  0.376<sub>±0.004</sub> |  0.043<sub>±0.001</sub> |  0.420<sub>±0.005</sub> |      40.23<sub>±0.39</sub> |
| Java (GraalVM) |  0.370<sub>±0.003</sub> |  0.084<sub>±0.001</sub> |  0.456<sub>±0.003</sub> |      79.97<sub>±3.39</sub> |
| JavaScript (Node) |  0.369<sub>±0.019</sub> |  0.029<sub>±0.002</sub> |  0.398<sub>±0.020</sub> |      45.82<sub>±1.72</sub> |
| JavaScript (GraalVM) |  0.830<sub>±0.021</sub> |  0.392<sub>±0.029</sub> |  1.189<sub>±0.033</sub> |     349.41<sub>±4.05</sub> |
| Kotlin (JVM) |  0.359<sub>±0.003</sub> |  0.051<sub>±0.006</sub> |  0.410<sub>±0.007</sub> |      41.79<sub>±0.57</sub> |
| Kotlin (Native) |  0.357<sub>±0.071</sub> |  0.003<sub>±0.001</sub> |  0.360<sub>±0.072</sub> |       4.19<sub>±0.13</sub> |
| Perl | 28.071<sub>±0.183</sub> |  0.015<sub>±0.006</sub> | 28.085<sub>±0.184</sub> |       7.37<sub>±0.05</sub> |
| PHP |  3.483<sub>±0.040</sub> |  0.017<sub>±0.001</sub> |  3.500<sub>±0.039</sub> |      19.29<sub>±0.08</sub> |
| PHP (JIT: tracing) |  1.288<sub>±0.021</sub> |  0.021<sub>±0.000</sub> |  1.308<sub>±0.021</sub> |      22.50<sub>±0.09</sub> |
| PHP (JIT: function) |  1.469<sub>±0.027</sub> |  0.021<sub>±0.001</sub> |  1.490<sub>±0.027</sub> |      22.63<sub>±0.10</sub> |
| Python (CPython) | 10.763<sub>±0.067</sub> |  0.018<sub>±0.001</sub> | 10.781<sub>±0.066</sub> |       8.89<sub>±0.05</sub> |
| Python (PyPy) |  0.483<sub>±0.022</sub> |  0.037<sub>±0.003</sub> |  0.517<sub>±0.023</sub> |      53.11<sub>±0.22</sub> |
| Ruby | 11.894<sub>±0.143</sub> |  0.062<sub>±0.031</sub> | 11.949<sub>±0.147</sub> |      15.69<sub>±0.01</sub> |
| Ruby (JIT) | 10.733<sub>±0.036</sub> |  0.056<sub>±0.003</sub> | 10.790<sub>±0.038</sub> |      16.13<sub>±0.06</sub> |
| Ruby (JRuby) | 13.283<sub>±0.923</sub> |  2.547<sub>±0.131</sub> | 15.754<sub>±0.906</sub> |     513.30<sub>±56.20</sub> |
| Rust |  0.345<sub>±0.002</sub> |  0.002<sub>±0.001</sub> |  0.347<sub>±0.001</sub> |       1.85<sub>±0.06</sub> |
| Swift |  0.627<sub>±0.037</sub> |  0.253<sub>±0.677</sub> |  0.862<sub>±0.641</sub> |     169.25<sub>±20.59</sub> |
| Swift (Optimized) |  0.347<sub>±0.001</sub> |  0.343<sub>±0.312</sub> |  0.681<sub>±0.287</sub> |     175.77<sub>±20.52</sub> |
| Swift (Compiled) |  0.348<sub>±0.001</sub> |  0.006<sub>±0.000</sub> |  0.353<sub>±0.001</sub> |      13.88<sub>±1.29</sub> |


### primes/Atkin

| Language | Time, s | Startup time, s | Total time, s | Memory, MiB |
| :------- | ------: | --------------: | ------------: | ----------: |
| C++ (clang) |  0.315<sub>±0.041</sub> |  0.013<sub>±0.002</sub> |  0.329<sub>±0.040</sub> |      89.13<sub>±0.05</sub> |
| C++ (gcc) |  0.225<sub>±0.017</sub> |  0.013<sub>±0.001</sub> |  0.238<sub>±0.017</sub> |      89.11<sub>±0.08</sub> |
| Go |  0.254<sub>±0.028</sub> |  0.010<sub>±0.001</sub> |  0.264<sub>±0.029</sub> |      79.00<sub>±0.55</sub> |
| Java |  0.223<sub>±0.028</sub> |  0.064<sub>±0.002</sub> |  0.285<sub>±0.029</sub> |     179.96<sub>±2.68</sub> |
| Java (GraalVM) |  0.368<sub>±0.046</sub> |  0.105<sub>±0.002</sub> |  0.466<sub>±0.048</sub> |     236.20<sub>±2.04</sub> |
| JavaScript (Node) |  0.363<sub>±0.025</sub> |  0.080<sub>±0.002</sub> |  0.440<sub>±0.025</sub> |     228.43<sub>±0.89</sub> |
| JavaScript (GraalVM) |  3.136<sub>±0.655</sub> |  0.436<sub>±0.015</sub> |  3.540<sub>±0.661</sub> |     749.39<sub>±41.34</sub> |
| PHP |  2.151<sub>±0.067</sub> |  0.033<sub>±0.002</sub> |  2.184<sub>±0.067</sub> |     239.43<sub>±0.05</sub> |
| PHP (JIT: tracing) |  1.202<sub>±0.025</sub> |  0.039<sub>±0.003</sub> |  1.238<sub>±0.027</sub> |     242.66<sub>±0.14</sub> |
| PHP (JIT: function) |  1.222<sub>±0.026</sub> |  0.038<sub>±0.007</sub> |  1.268<sub>±0.032</sub> |     242.68<sub>±0.09</sub> |
| Python (CPython) |  4.331<sub>±0.019</sub> |  0.019<sub>±0.001</sub> |  4.352<sub>±0.019</sub> |     192.73<sub>±0.14</sub> |
| Python (PyPy) |  1.353<sub>±0.036</sub> |  0.056<sub>±0.001</sub> |  1.409<sub>±0.036</sub> |     303.93<sub>±0.24</sub> |
| Ruby |  3.115<sub>±0.129</sub> |  0.087<sub>±0.003</sub> |  3.207<sub>±0.130</sub> |     158.32<sub>±0.04</sub> |
| Ruby (JIT) |  2.298<sub>±0.055</sub> |  0.076<sub>±0.005</sub> |  2.383<sub>±0.054</sub> |     158.85<sub>±0.11</sub> |
| Ruby (JRuby) |  3.686<sub>±0.231</sub> |  2.620<sub>±0.171</sub> |  6.574<sub>±0.175</sub> |     615.31<sub>±68.38</sub> |
| Rust |  0.178<sub>±0.008</sub> |  0.010<sub>±0.001</sub> |  0.190<sub>±0.009</sub> |      77.54<sub>±0.03</sub> |


### collatz/MaxSequence

| Language | Time, s | Startup time, s | Total time, s | Memory, MiB |
| :------- | ------: | --------------: | ------------: | ----------: |
| C++ (clang) |  0.061<sub>±0.001</sub> |  0.003<sub>±0.000</sub> |  0.064<sub>±0.001</sub> |       3.31<sub>±0.68</sub> |
| Go |  0.103<sub>±0.006</sub> |  0.002<sub>±0.002</sub> |  0.105<sub>±0.007</sub> |       2.92<sub>±0.20</sub> |
| Java |  0.100<sub>±0.007</sub> |  0.054<sub>±0.003</sub> |  0.155<sub>±0.012</sub> |      41.84<sub>±0.21</sub> |
| Java (GraalVM) |  0.108<sub>±0.006</sub> |  0.104<sub>±0.002</sub> |  0.209<sub>±0.004</sub> |      81.93<sub>±2.39</sub> |
| JavaScript (Node) |  0.647<sub>±0.008</sub> |  0.029<sub>±0.002</sub> |  0.676<sub>±0.009</sub> |      44.57<sub>±1.10</sub> |
| JavaScript (GraalVM) |  1.006<sub>±0.042</sub> |  0.387<sub>±0.024</sub> |  1.393<sub>±0.063</sub> |     343.34<sub>±20.81</sub> |
| PHP |  1.397<sub>±0.029</sub> |  0.018<sub>±0.001</sub> |  1.415<sub>±0.030</sub> |      19.39<sub>±0.13</sub> |
| PHP (JIT: tracing) |  0.462<sub>±0.007</sub> |  0.020<sub>±0.001</sub> |  0.483<sub>±0.008</sub> |      22.70<sub>±0.16</sub> |
| PHP (JIT: function) |  0.545<sub>±0.002</sub> |  0.020<sub>±0.001</sub> |  0.565<sub>±0.002</sub> |      22.59<sub>±0.05</sub> |
| Python (CPython) |  5.667<sub>±0.022</sub> |  0.017<sub>±0.001</sub> |  5.685<sub>±0.023</sub> |       8.97<sub>±0.04</sub> |
| Python (PyPy) |  0.131<sub>±0.004</sub> |  0.033<sub>±0.003</sub> |  0.168<sub>±0.005</sub> |      52.98<sub>±0.25</sub> |
| Ruby |  2.705<sub>±0.014</sub> |  0.057<sub>±0.002</sub> |  2.765<sub>±0.013</sub> |      15.65<sub>±0.03</sub> |
| Ruby (JIT) |  1.022<sub>±0.038</sub> |  0.059<sub>±0.002</sub> |  1.078<sub>±0.037</sub> |      16.06<sub>±0.05</sub> |
| Ruby (JRuby) |  1.451<sub>±0.061</sub> |  2.570<sub>±0.033</sub> |  3.990<sub>±0.080</sub> |     498.55<sub>±49.93</sub> |
| Rust |  0.051<sub>±0.001</sub> |  0.002<sub>±0.002</sub> |  0.054<sub>±0.001</sub> |       1.76<sub>±0.06</sub> |


### mandelbrot/Simple

| Language | Time, s | Startup time, s | Total time, s | Memory, MiB |
| :------- | ------: | --------------: | ------------: | ----------: |
| C++ (clang) |  0.033<sub>±0.000</sub> |  0.002<sub>±0.000</sub> |  0.035<sub>±0.001</sub> |       3.25<sub>±0.82</sub> |
| C++ (gcc) |  0.032<sub>±0.001</sub> |  0.003<sub>±0.000</sub> |  0.035<sub>±0.001</sub> |       3.26<sub>±0.80</sub> |
| Go |  0.035<sub>±0.001</sub> |  0.002<sub>±0.000</sub> |  0.038<sub>±0.001</sub> |       2.93<sub>±0.24</sub> |
| Java |  0.058<sub>±0.004</sub> |  0.054<sub>±0.002</sub> |  0.112<sub>±0.005</sub> |      42.29<sub>±1.66</sub> |
| Java (GraalVM) |  0.053<sub>±0.002</sub> |  0.105<sub>±0.004</sub> |  0.155<sub>±0.006</sub> |      85.50<sub>±3.74</sub> |
| JavaScript (Node) |  0.054<sub>±0.002</sub> |  0.031<sub>±0.001</sub> |  0.084<sub>±0.002</sub> |      45.75<sub>±1.05</sub> |
| JavaScript (GraalVM) |  0.261<sub>±0.015</sub> |  0.382<sub>±0.021</sub> |  0.636<sub>±0.016</sub> |     335.98<sub>±6.67</sub> |
| PHP |  0.708<sub>±0.004</sub> |  0.017<sub>±0.005</sub> |  0.729<sub>±0.005</sub> |      19.48<sub>±0.09</sub> |
| PHP (JIT: tracing) |  0.122<sub>±0.001</sub> |  0.021<sub>±0.000</sub> |  0.143<sub>±0.001</sub> |      22.59<sub>±0.06</sub> |
| PHP (JIT: function) |  0.159<sub>±0.001</sub> |  0.021<sub>±0.001</sub> |  0.180<sub>±0.001</sub> |      22.59<sub>±0.14</sub> |
| Python (CPython) |  3.428<sub>±0.007</sub> |  0.018<sub>±0.000</sub> |  3.445<sub>±0.007</sub> |       9.15<sub>±0.09</sub> |
| Python (PyPy) |  0.052<sub>±0.001</sub> |  0.034<sub>±0.001</sub> |  0.086<sub>±0.002</sub> |      54.70<sub>±0.11</sub> |
| Ruby |  1.883<sub>±0.033</sub> |  0.059<sub>±0.004</sub> |  1.944<sub>±0.032</sub> |      15.74<sub>±0.06</sub> |
| Ruby (JIT) |  1.421<sub>±0.049</sub> |  0.057<sub>±0.005</sub> |  1.477<sub>±0.054</sub> |      16.23<sub>±0.05</sub> |
| Ruby (JRuby) |  2.440<sub>±0.133</sub> |  2.516<sub>±0.035</sub> |  4.922<sub>±0.151</sub> |     489.20<sub>±63.08</sub> |
| Rust |  0.032<sub>±0.000</sub> |  0.002<sub>±0.001</sub> |  0.034<sub>±0.001</sub> |       1.78<sub>±0.39</sub> |


### treap/Naive

| Language | Time, s | Startup time, s | Total time, s | Memory, MiB |
| :------- | ------: | --------------: | ------------: | ----------: |
| C++ (clang) |  0.234<sub>±0.011</sub> |  0.003<sub>±0.000</sub> |  0.237<sub>±0.011</sub> |       3.50<sub>±0.94</sub> |
| C++ (gcc) |  0.199<sub>±0.005</sub> |  0.003<sub>±0.000</sub> |  0.202<sub>±0.005</sub> |       3.44<sub>±0.92</sub> |
| Go |  0.313<sub>±0.006</sub> |  0.002<sub>±0.003</sub> |  0.315<sub>±0.006</sub> |       7.62<sub>±0.87</sub> |
| Java |  0.638<sub>±0.052</sub> |  0.080<sub>±0.010</sub> |  0.698<sub>±0.059</sub> |     151.77<sub>±0.37</sub> |
| Java (GraalVM) |  0.663<sub>±0.070</sub> |  0.120<sub>±0.009</sub> |  0.777<sub>±0.068</sub> |     237.80<sub>±17.02</sub> |
| JavaScript (Node) |  1.028<sub>±0.031</sub> |  0.039<sub>±0.002</sub> |  1.065<sub>±0.031</sub> |      84.64<sub>±1.34</sub> |
| JavaScript (GraalVM) |  2.636<sub>±0.076</sub> |  0.385<sub>±0.009</sub> |  3.020<sub>±0.082</sub> |     541.46<sub>±19.51</sub> |
| Kotlin (JVM) |  0.628<sub>±0.017</sub> |  0.061<sub>±0.002</sub> |  0.687<sub>±0.019</sub> |     154.92<sub>±0.99</sub> |
| Kotlin (Native) |  0.994<sub>±0.039</sub> |  0.009<sub>±0.001</sub> |  1.000<sub>±0.040</sub> |      23.33<sub>±1.34</sub> |
| PHP |  4.929<sub>±0.187</sub> |  0.016<sub>±0.001</sub> |  4.946<sub>±0.187</sub> |      19.49<sub>±0.11</sub> |
| PHP (JIT: tracing) |  3.011<sub>±0.034</sub> |  0.021<sub>±0.001</sub> |  3.033<sub>±0.034</sub> |      22.94<sub>±0.17</sub> |
| PHP (JIT: function) |  3.178<sub>±0.018</sub> |  0.020<sub>±0.001</sub> |  3.201<sub>±0.017</sub> |      22.65<sub>±0.12</sub> |
| Python (CPython) |  7.466<sub>±0.055</sub> |  0.020<sub>±0.001</sub> |  7.486<sub>±0.055</sub> |       9.87<sub>±0.13</sub> |
| Python (PyPy) |  2.903<sub>±0.154</sub> |  0.047<sub>±0.015</sub> |  2.943<sub>±0.152</sub> |      62.32<sub>±1.04</sub> |
| Ruby |  6.214<sub>±0.087</sub> |  0.056<sub>±0.003</sub> |  6.275<sub>±0.090</sub> |      17.55<sub>±0.09</sub> |
| Ruby (JIT) |  3.256<sub>±0.042</sub> |  0.058<sub>±0.005</sub> |  3.311<sub>±0.047</sub> |      18.11<sub>±0.10</sub> |
| Ruby (JRuby) |  6.295<sub>±0.290</sub> |  2.630<sub>±0.207</sub> |  9.056<sub>±0.418</sub> |     227.04<sub>±23.33</sub> |


### recursion/Tak

| Language | Time, s | Startup time, s | Total time, s | Memory, MiB |
| :------- | ------: | --------------: | ------------: | ----------: |
| C++ (clang) |  0.045<sub>±0.002</sub> |  0.003<sub>±0.000</sub> |  0.048<sub>±0.001</sub> |       1.84<sub>±0.02</sub> |
| C++ (gcc) |  0.026<sub>±0.001</sub> |  0.002<sub>±0.000</sub> |  0.028<sub>±0.000</sub> |       1.84<sub>±0.66</sub> |
| Go |  0.057<sub>±0.003</sub> |  0.002<sub>±0.000</sub> |  0.059<sub>±0.003</sub> |       2.93<sub>±0.17</sub> |
| Java |  0.042<sub>±0.001</sub> |  0.055<sub>±0.002</sub> |  0.096<sub>±0.003</sub> |      40.18<sub>±0.60</sub> |
| Java (GraalVM) |  0.072<sub>±0.017</sub> |  0.101<sub>±0.017</sub> |  0.196<sub>±0.031</sub> |      79.07<sub>±0.79</sub> |
| JavaScript (Node) |  0.154<sub>±0.010</sub> |  0.029<sub>±0.001</sub> |  0.183<sub>±0.010</sub> |      42.57<sub>±1.06</sub> |
| JavaScript (GraalVM) |  0.831<sub>±0.017</sub> |  0.382<sub>±0.049</sub> |  1.228<sub>±0.054</sub> |     423.46<sub>±9.27</sub> |
| Perl |  9.243<sub>±0.234</sub> |  0.008<sub>±0.000</sub> |  9.251<sub>±0.234</sub> |       5.82<sub>±0.11</sub> |
| PHP |  1.184<sub>±0.006</sub> |  0.017<sub>±0.000</sub> |  1.202<sub>±0.006</sub> |      19.44<sub>±0.15</sub> |
| PHP (JIT: tracing) |  0.400<sub>±0.004</sub> |  0.020<sub>±0.001</sub> |  0.420<sub>±0.005</sub> |      22.61<sub>±0.14</sub> |
| PHP (JIT: function) |  0.428<sub>±0.006</sub> |  0.020<sub>±0.002</sub> |  0.448<sub>±0.006</sub> |      22.46<sub>±0.12</sub> |
| Python (CPython) |  2.843<sub>±0.095</sub> |  0.018<sub>±0.001</sub> |  2.861<sub>±0.095</sub> |       9.00<sub>±0.39</sub> |
| Python (PyPy) |  0.805<sub>±0.008</sub> |  0.035<sub>±0.002</sub> |  0.841<sub>±0.009</sub> |      59.79<sub>±0.13</sub> |
| Ruby |  1.538<sub>±0.006</sub> |  0.057<sub>±0.002</sub> |  1.596<sub>±0.008</sub> |      15.63<sub>±0.10</sub> |
| Ruby (JIT) |  0.286<sub>±0.009</sub> |  0.057<sub>±0.001</sub> |  0.343<sub>±0.007</sub> |      16.00<sub>±0.07</sub> |
| Ruby (JRuby) |  0.677<sub>±0.045</sub> |  2.453<sub>±0.034</sub> |  3.067<sub>±0.063</sub> |     185.94<sub>±2.08</sub> |


### linpack/Linpack

| Language | Time, s | Startup time, s | Total time, s | Memory, MiB |
| :------- | ------: | --------------: | ------------: | ----------: |
| C++ (clang) |  2.516<sub>±0.265</sub> |  0.005<sub>±0.001</sub> |  2.522<sub>±0.265</sub> |      33.55<sub>±0.42</sub> |
| C++ (gcc) |  2.367<sub>±0.120</sub> |  0.006<sub>±0.000</sub> |  2.373<sub>±0.120</sub> |      33.57<sub>±0.43</sub> |
| Go |  3.388<sub>±0.194</sub> |  0.003<sub>±0.005</sub> |  3.391<sub>±0.192</sub> |      33.91<sub>±0.40</sub> |
| Java |  2.440<sub>±0.050</sub> |  0.075<sub>±0.004</sub> |  2.514<sub>±0.052</sub> |      92.43<sub>±0.37</sub> |
| Java (GraalVM) |  4.844<sub>±0.072</sub> |  0.090<sub>±0.009</sub> |  4.931<sub>±0.068</sub> |     147.00<sub>±3.93</sub> |
| JavaScript (Node) |  9.139<sub>±0.062</sub> |  0.046<sub>±0.031</sub> |  9.241<sub>±0.067</sub> |     138.18<sub>±2.89</sub> |
| JavaScript (GraalVM) |  4.770<sub>±0.124</sub> |  0.413<sub>±0.111</sub> |  5.254<sub>±0.160</sub> |     402.36<sub>±33.30</sub> |
| PHP | 84.654<sub>±0.418</sub> |  0.020<sub>±0.008</sub> | 84.674<sub>±0.423</sub> |      87.48<sub>±0.67</sub> |
| PHP (JIT: tracing) | 23.757<sub>±0.060</sub> |  0.023<sub>±0.003</sub> | 23.780<sub>±0.060</sub> |      92.62<sub>±0.34</sub> |
| PHP (JIT: function) | 29.919<sub>±0.205</sub> |  0.027<sub>±0.004</sub> | 29.943<sub>±0.204</sub> |      94.52<sub>±0.98</sub> |
| Python (CPython) | 530.242<sub>±5.094</sub> |  0.024<sub>±0.002</sub> | 530.268<sub>±5.094</sub> |     163.41<sub>±0.05</sub> |
| Python (PyPy) |  6.691<sub>±0.049</sub> |  0.046<sub>±0.081</sub> |  6.786<sub>±0.072</sub> |     102.30<sub>±3.30</sub> |


## Legend

| Field        | Description |
| :----------- | :---------- |
| Time         | Time spent in the algorithm itself, reported by the program itself. |
| Total time   | Total time spent from the start of the program to the end of the algorithm, measured by the benchmark. |
| Startup time | Time spent from the start of the program to the start of the algorithm, measured by the benchmark (Total time - Time). |
| Memory       | Peak memory usage during the algorithm, measured by the benchmark. |


