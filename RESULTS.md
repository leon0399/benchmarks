### primes/Simple

| Language | Time, s | Total time, s | Memory, MiB |
| :------- | ------: | ------------: | ----------: |
| C++ (clang) |  0.350<sub>±0.013</sub> |  0.353<sub>±0.012</sub> |       1.46<sub>±0.91</sub> |
| C++ (gcc) |  0.346<sub>±0.006</sub> |  0.349<sub>±0.006</sub> |       1.46<sub>±0.92</sub> |
| Java |  0.379<sub>±0.005</sub> |  0.423<sub>±0.032</sub> |      51.68<sub>±1.35</sub> |
| Java (GraalVM) |  0.377<sub>±0.012</sub> |  0.462<sub>±0.064</sub> |      96.60<sub>±2.11</sub> |
| JavaScript (Node) |  0.390<sub>±0.010</sub> |  0.414<sub>±0.010</sub> |      46.61<sub>±1.52</sub> |
| JavaScript (GraalVM) |  2.744<sub>±0.325</sub> |  3.064<sub>±0.310</sub> |     449.31<sub>±16.46</sub> |
| PHP |  3.504<sub>±0.031</sub> |  3.517<sub>±0.031</sub> |      18.40<sub>±0.10</sub> |
| PHP (JIT: tracing) |  3.550<sub>±0.094</sub> |  3.564<sub>±0.095</sub> |      20.77<sub>±0.25</sub> |
| PHP (JIT: function) |  1.566<sub>±0.142</sub> |  1.581<sub>±0.145</sub> |      21.32<sub>±0.20</sub> |
| Ruby | 10.534<sub>±0.129</sub> | 10.581<sub>±0.118</sub> |      15.75<sub>±0.12</sub> |
| Ruby (JIT) | 10.469<sub>±0.176</sub> | 10.515<sub>±0.176</sub> |      16.28<sub>±0.10</sub> |
| Ruby (JRuby) | 12.124<sub>±0.599</sub> | 14.045<sub>±0.701</sub> |     492.95<sub>±9.57</sub> |
| Rust |  0.347<sub>±0.001</sub> |  0.349<sub>±0.001</sub> |       1.75<sub>±0.05</sub> |


### primes/Atkin

| Language | Time, s | Total time, s | Memory, MiB |
| :------- | ------: | ------------: | ----------: |
| C++ (clang) |  0.226<sub>±0.018</sub> |  0.232<sub>±0.018</sub> |      89.05<sub>±0.11</sub> |
| C++ (gcc) |  0.202<sub>±0.007</sub> |  0.208<sub>±0.007</sub> |      89.05<sub>±0.05</sub> |
| Java |  0.202<sub>±0.005</sub> |  0.243<sub>±0.005</sub> |     187.30<sub>±0.23</sub> |
| Java (GraalVM) |  0.310<sub>±0.039</sub> |  0.382<sub>±0.045</sub> |     243.83<sub>±3.32</sub> |
| JavaScript (Node) |  0.308<sub>±0.015</sub> |  0.356<sub>±0.014</sub> |     228.05<sub>±1.10</sub> |
| JavaScript (GraalVM) |  2.611<sub>±0.299</sub> |  2.914<sub>±0.296</sub> |     804.83<sub>±115.35</sub> |
| PHP |  1.996<sub>±0.031</sub> |  2.010<sub>±0.032</sub> |     240.66<sub>±0.17</sub> |
| PHP (JIT: tracing) |  1.765<sub>±0.024</sub> |  1.779<sub>±0.023</sub> |     243.20<sub>±0.31</sub> |
| PHP (JIT: function) |  1.151<sub>±0.028</sub> |  1.170<sub>±0.027</sub> |     243.61<sub>±0.21</sub> |
| Python (CPython) |  6.258<sub>±0.059</sub> |  6.268<sub>±0.059</sub> |     245.77<sub>±0.03</sub> |
| Python (PyPy) |  1.186<sub>±0.013</sub> |  1.220<sub>±0.012</sub> |     304.18<sub>±0.16</sub> |
| Ruby |  2.533<sub>±0.037</sub> |  2.588<sub>±0.038</sub> |     158.27<sub>±0.11</sub> |
| Ruby (JIT) |  1.803<sub>±0.036</sub> |  1.861<sub>±0.038</sub> |     158.89<sub>±0.05</sub> |
| Ruby (JRuby) |  3.012<sub>±0.067</sub> |  5.022<sub>±0.051</sub> |     609.38<sub>±29.59</sub> |
| Rust |  0.150<sub>±0.006</sub> |  0.156<sub>±0.006</sub> |      77.48<sub>±0.02</sub> |


### collatz/MaxSequence

| Language | Time, s | Total time, s | Memory, MiB |
| :------- | ------: | ------------: | ----------: |
| C++ (clang) |  0.057<sub>±0.000</sub> |  0.059<sub>±0.000</sub> |       1.52<sub>±0.05</sub> |
| Java |  0.099<sub>±0.004</sub> |  0.140<sub>±0.004</sub> |      41.92<sub>±0.99</sub> |
| Java (GraalVM) |  0.098<sub>±0.004</sub> |  0.186<sub>±0.008</sub> |      85.10<sub>±2.96</sub> |
| JavaScript (Node) |  0.658<sub>±0.008</sub> |  0.679<sub>±0.008</sub> |      42.72<sub>±1.12</sub> |
| JavaScript (GraalVM) |  0.950<sub>±0.017</sub> |  1.252<sub>±0.016</sub> |     330.97<sub>±11.06</sub> |
| PHP |  1.394<sub>±0.013</sub> |  1.404<sub>±0.014</sub> |      18.46<sub>±0.21</sub> |
| PHP (JIT: tracing) |  1.385<sub>±0.026</sub> |  1.398<sub>±0.025</sub> |      21.09<sub>±0.18</sub> |
| PHP (JIT: function) |  0.486<sub>±0.006</sub> |  0.501<sub>±0.007</sub> |      21.62<sub>±0.16</sub> |
| Ruby |  2.625<sub>±0.032</sub> |  2.669<sub>±0.031</sub> |      15.69<sub>±0.09</sub> |
| Ruby (JIT) |  0.914<sub>±0.034</sub> |  0.959<sub>±0.035</sub> |      16.16<sub>±0.10</sub> |
| Ruby (JRuby) |  1.215<sub>±0.025</sub> |  3.164<sub>±0.033</sub> |     432.19<sub>±53.91</sub> |
| Rust |  0.057<sub>±0.001</sub> |  0.059<sub>±0.001</sub> |       1.77<sub>±0.05</sub> |


### mandelbrot/Simple

| Language | Time, s | Total time, s | Memory, MiB |
| :------- | ------: | ------------: | ----------: |
| C++ (clang) |  0.031<sub>±0.001</sub> |  0.034<sub>±0.000</sub> |       3.15<sub>±0.95</sub> |
| C++ (gcc) |  0.031<sub>±0.000</sub> |  0.033<sub>±0.000</sub> |       1.45<sub>±0.94</sub> |
| Java |  0.055<sub>±0.002</sub> |  0.099<sub>±0.007</sub> |      45.29<sub>±2.55</sub> |
| Java (GraalVM) |  0.050<sub>±0.004</sub> |  0.139<sub>±0.012</sub> |      84.48<sub>±2.52</sub> |
| JavaScript (Node) |  0.046<sub>±0.002</sub> |  0.070<sub>±0.002</sub> |      47.64<sub>±0.95</sub> |
| JavaScript (GraalVM) |  0.209<sub>±0.010</sub> |  0.506<sub>±0.020</sub> |     330.93<sub>±2.60</sub> |
| PHP |  0.703<sub>±0.004</sub> |  0.714<sub>±0.005</sub> |      18.46<sub>±0.16</sub> |
| PHP (JIT: tracing) |  0.688<sub>±0.023</sub> |  0.702<sub>±0.023</sub> |      20.96<sub>±0.20</sub> |
| PHP (JIT: function) |  0.156<sub>±0.001</sub> |  0.170<sub>±0.001</sub> |      21.64<sub>±0.17</sub> |
| Ruby |  1.775<sub>±0.062</sub> |  1.831<sub>±0.062</sub> |      15.79<sub>±0.09</sub> |
| Ruby (JIT) |  1.355<sub>±0.030</sub> |  1.400<sub>±0.031</sub> |      16.35<sub>±0.09</sub> |
| Ruby (JRuby) |  2.149<sub>±0.073</sub> |  4.125<sub>±0.070</sub> |     483.46<sub>±21.56</sub> |
| Rust |  0.032<sub>±0.001</sub> |  0.034<sub>±0.001</sub> |       1.77<sub>±0.02</sub> |


### treap/Naive

| Language | Time, s | Total time, s | Memory, MiB |
| :------- | ------: | ------------: | ----------: |
| C++ (clang) |  0.222<sub>±0.011</sub> |  0.224<sub>±0.011</sub> |       3.14<sub>±0.07</sub> |
| C++ (gcc) |  0.190<sub>±0.006</sub> |  0.192<sub>±0.005</sub> |       3.32<sub>±0.14</sub> |
| Go |  0.299<sub>±0.003</sub> |  0.301<sub>±0.005</sub> |       9.53<sub>±1.11</sub> |
| Java |  0.543<sub>±0.008</sub> |  0.584<sub>±0.010</sub> |     156.76<sub>±0.91</sub> |
| Java (GraalVM) |  0.499<sub>±0.009</sub> |  0.582<sub>±0.011</sub> |     213.11<sub>±4.42</sub> |
| JavaScript (Node) |  0.885<sub>±0.017</sub> |  0.913<sub>±0.018</sub> |      83.56<sub>±1.20</sub> |
| JavaScript (GraalVM) |  2.065<sub>±0.124</sub> |  2.372<sub>±0.129</sub> |     551.30<sub>±15.00</sub> |
| Kotlin (JVM) |  0.545<sub>±0.008</sub> |  0.587<sub>±0.010</sub> |     156.59<sub>±0.83</sub> |
| Kotlin (Native) |  0.951<sub>±0.007</sub> |  0.957<sub>±0.009</sub> |      23.09<sub>±0.57</sub> |
| PHP |  4.821<sub>±0.033</sub> |  4.833<sub>±0.033</sub> |      18.46<sub>±0.16</sub> |
| PHP (JIT: tracing) |  4.541<sub>±0.008</sub> |  4.557<sub>±0.008</sub> |      21.22<sub>±0.29</sub> |
| PHP (JIT: function) |  3.098<sub>±0.022</sub> |  3.112<sub>±0.021</sub> |      21.66<sub>±0.16</sub> |
| Python (CPython) | 12.589<sub>±0.053</sub> | 12.601<sub>±0.053</sub> |       8.50<sub>±0.04</sub> |
| Python (PyPy) |  2.590<sub>±0.113</sub> |  2.644<sub>±0.112</sub> |      61.99<sub>±0.91</sub> |
| Ruby |  5.451<sub>±0.092</sub> |  5.494<sub>±0.092</sub> |      17.63<sub>±0.07</sub> |
| Ruby (JIT) |  3.043<sub>±0.048</sub> |  3.100<sub>±0.047</sub> |      18.27<sub>±0.06</sub> |
| Ruby (JRuby) |  5.084<sub>±0.165</sub> |  7.102<sub>±0.151</sub> |     223.86<sub>±32.71</sub> |


### recursion/Tak

| Language | Time, s | Total time, s | Memory, MiB |
| :------- | ------: | ------------: | ----------: |
| C++ (clang) |  0.046<sub>±0.001</sub> |  0.048<sub>±0.001</sub> |       1.52<sub>±0.85</sub> |
| C++ (gcc) |  0.055<sub>±0.001</sub> |  0.057<sub>±0.001</sub> |       2.96<sub>±0.92</sub> |
| JavaScript (Node) |  0.146<sub>±0.005</sub> |  0.168<sub>±0.008</sub> |      44.30<sub>±1.15</sub> |
| JavaScript (GraalVM) |  0.690<sub>±0.016</sub> |  0.987<sub>±0.017</sub> |     422.62<sub>±11.39</sub> |
| PHP |  1.176<sub>±0.010</sub> |  1.187<sub>±0.010</sub> |      18.24<sub>±0.22</sub> |
| PHP (JIT: tracing) |  0.953<sub>±0.023</sub> |  0.966<sub>±0.024</sub> |      20.85<sub>±0.09</sub> |
| PHP (JIT: function) |  0.424<sub>±0.004</sub> |  0.437<sub>±0.004</sub> |      21.75<sub>±0.09</sub> |
| Python (CPython) |  4.328<sub>±0.052</sub> |  4.338<sub>±0.053</sub> |       7.27<sub>±0.26</sub> |
| Python (PyPy) |  0.761<sub>±0.015</sub> |  0.785<sub>±0.014</sub> |      59.76<sub>±0.22</sub> |
| Ruby |  1.243<sub>±0.023</sub> |  1.287<sub>±0.023</sub> |      15.73<sub>±0.11</sub> |
| Ruby (JIT) |  0.283<sub>±0.004</sub> |  0.331<sub>±0.004</sub> |      16.23<sub>±0.05</sub> |
| Ruby (JRuby) |  0.623<sub>±0.031</sub> |  2.566<sub>±0.026</sub> |     184.84<sub>±2.41</sub> |


### linpack/Linpack

| Language | Time, s | Total time, s | Memory, MiB |
| :------- | ------: | ------------: | ----------: |
| Go |  2.606<sub>±0.184</sub> |  2.608<sub>±0.183</sub> |      36.85<sub>±0.44</sub> |
| JavaScript (Node) |  8.906<sub>±0.018</sub> |  8.938<sub>±0.054</sub> |     138.09<sub>±1.12</sub> |
| JavaScript (GraalVM) |  4.110<sub>±0.313</sub> |  4.622<sub>±0.296</sub> |     418.40<sub>±20.18</sub> |
| PHP | 84.604<sub>±2.245</sub> | 84.668<sub>±2.238</sub> |      90.64<sub>±0.21</sub> |
| PHP (JIT: tracing) | 85.131<sub>±0.221</sub> | 85.146<sub>±0.222</sub> |      92.86<sub>±0.13</sub> |
| PHP (JIT: function) | 29.954<sub>±0.749</sub> | 29.970<sub>±0.750</sub> |      93.72<sub>±0.25</sub> |
| Python (CPython) | 553.561<sub>±23.693</sub> | 553.577<sub>±23.694</sub> |     163.48<sub>±0.08</sub> |
| Python (PyPy) |  6.064<sub>±0.073</sub> |  6.097<sub>±0.024</sub> |     102.41<sub>±3.16</sub> |


