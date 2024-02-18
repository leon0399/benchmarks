### primes/Simple

| Language | Time, s | Total time, s | Memory, MiB |
| :------- | ------: | ------------: | ----------: |
| C++ (clang) |  0.345<sub>±0.011</sub> |  0.348<sub>±0.011</sub> |       1.46<sub>±0.78</sub> |
| C++ (gcc) |  0.345<sub>±0.002</sub> |  0.348<sub>±0.005</sub> |       2.95<sub>±0.91</sub> |
| Java |  0.368<sub>±0.008</sub> |  0.407<sub>±0.015</sub> |      39.75<sub>±1.16</sub> |
| Java (GraalVM) |  0.369<sub>±0.029</sub> |  0.455<sub>±0.107</sub> |      79.05<sub>±2.53</sub> |
| JavaScript (Node) |  0.365<sub>±0.018</sub> |  0.392<sub>±0.017</sub> |      43.77<sub>±1.09</sub> |
| JavaScript (GraalVM) |  0.824<sub>±0.053</sub> |  1.157<sub>±0.058</sub> |     353.64<sub>±6.32</sub> |
| PHP |  3.522<sub>±0.020</sub> |  3.539<sub>±0.021</sub> |      18.31<sub>±0.19</sub> |
| PHP (JIT: tracing) |  1.397<sub>±0.046</sub> |  1.415<sub>±0.047</sub> |      21.64<sub>±0.15</sub> |
| PHP (JIT: function) |  1.538<sub>±0.045</sub> |  1.554<sub>±0.046</sub> |      21.68<sub>±0.10</sub> |
| Python (CPython) | 12.240<sub>±0.092</sub> | 12.252<sub>±0.092</sub> |       7.41<sub>±0.08</sub> |
| Python (PyPy) |  0.490<sub>±0.024</sub> |  0.525<sub>±0.027</sub> |      53.31<sub>±0.19</sub> |
| Ruby | 11.140<sub>±0.063</sub> | 11.214<sub>±0.039</sub> |      15.86<sub>±0.10</sub> |
| Ruby (JIT) | 11.274<sub>±0.147</sub> | 11.335<sub>±0.144</sub> |      16.31<sub>±0.10</sub> |
| Ruby (JRuby) | 13.038<sub>±0.176</sub> | 15.324<sub>±0.507</sub> |     503.79<sub>±49.28</sub> |
| Rust |  0.349<sub>±0.013</sub> |  0.352<sub>±0.013</sub> |       1.73<sub>±0.06</sub> |


### primes/Atkin

| Language | Time, s | Total time, s | Memory, MiB |
| :------- | ------: | ------------: | ----------: |
| C++ (clang) |  0.232<sub>±0.017</sub> |  0.244<sub>±0.018</sub> |      88.84<sub>±0.12</sub> |
| C++ (gcc) |  0.221<sub>±0.020</sub> |  0.230<sub>±0.020</sub> |      88.95<sub>±0.12</sub> |
| Java |  0.203<sub>±0.037</sub> |  0.248<sub>±0.039</sub> |     185.45<sub>±1.44</sub> |
| Java (GraalVM) |  0.328<sub>±0.055</sub> |  0.425<sub>±0.059</sub> |     241.80<sub>±2.55</sub> |
| JavaScript (Node) |  0.365<sub>±0.026</sub> |  0.431<sub>±0.030</sub> |     226.72<sub>±1.04</sub> |
| JavaScript (GraalVM) |  2.618<sub>±0.081</sub> |  2.969<sub>±0.096</sub> |     800.75<sub>±52.15</sub> |
| PHP |  2.043<sub>±0.026</sub> |  2.057<sub>±0.027</sub> |     240.66<sub>±0.28</sub> |
| PHP (JIT: tracing) |  1.115<sub>±0.055</sub> |  1.131<sub>±0.055</sub> |     243.91<sub>±0.28</sub> |
| PHP (JIT: function) |  1.150<sub>±0.024</sub> |  1.167<sub>±0.024</sub> |     243.90<sub>±0.10</sub> |
| Python (CPython) |  6.824<sub>±0.083</sub> |  6.837<sub>±0.083</sub> |     245.69<sub>±0.02</sub> |
| Python (PyPy) |  1.340<sub>±0.031</sub> |  1.379<sub>±0.041</sub> |     304.22<sub>±0.21</sub> |
| Ruby |  2.785<sub>±0.097</sub> |  2.861<sub>±0.100</sub> |     158.29<sub>±0.15</sub> |
| Ruby (JIT) |  1.993<sub>±0.033</sub> |  2.065<sub>±0.033</sub> |     158.90<sub>±0.07</sub> |
| Ruby (JRuby) |  3.439<sub>±0.103</sub> |  5.783<sub>±0.125</sub> |     595.58<sub>±45.54</sub> |
| Rust |  0.205<sub>±0.040</sub> |  0.215<sub>±0.042</sub> |      77.51<sub>±0.07</sub> |


### collatz/MaxSequence

| Language | Time, s | Total time, s | Memory, MiB |
| :------- | ------: | ------------: | ----------: |
| C++ (clang) |  0.058<sub>±0.001</sub> |  0.063<sub>±0.002</sub> |       3.18<sub>±0.95</sub> |
| Java |  0.102<sub>±0.003</sub> |  0.153<sub>±0.004</sub> |      41.85<sub>±0.99</sub> |
| Java (GraalVM) |  0.099<sub>±0.003</sub> |  0.194<sub>±0.006</sub> |      87.45<sub>±3.75</sub> |
| JavaScript (Node) |  0.640<sub>±0.018</sub> |  0.667<sub>±0.019</sub> |      44.41<sub>±0.94</sub> |
| JavaScript (GraalVM) |  0.968<sub>±0.026</sub> |  1.320<sub>±0.041</sub> |     333.89<sub>±8.86</sub> |
| PHP |  1.388<sub>±0.023</sub> |  1.403<sub>±0.023</sub> |      18.29<sub>±0.27</sub> |
| PHP (JIT: tracing) |  0.413<sub>±0.019</sub> |  0.430<sub>±0.019</sub> |      21.75<sub>±0.20</sub> |
| PHP (JIT: function) |  0.479<sub>±0.010</sub> |  0.494<sub>±0.010</sub> |      21.52<sub>±0.20</sub> |
| Python (CPython) |  7.658<sub>±0.069</sub> |  7.670<sub>±0.069</sub> |       7.45<sub>±0.26</sub> |
| Python (PyPy) |  0.140<sub>±0.007</sub> |  0.169<sub>±0.010</sub> |      52.87<sub>±0.30</sub> |
| Ruby |  2.753<sub>±0.020</sub> |  2.811<sub>±0.021</sub> |      15.66<sub>±0.09</sub> |
| Ruby (JIT) |  0.967<sub>±0.016</sub> |  1.024<sub>±0.009</sub> |      16.24<sub>±0.08</sub> |
| Ruby (JRuby) |  1.459<sub>±0.156</sub> |  3.796<sub>±0.159</sub> |     481.77<sub>±49.48</sub> |
| Rust |  0.051<sub>±0.001</sub> |  0.054<sub>±0.002</sub> |       1.66<sub>±0.02</sub> |


### mandelbrot/Simple

| Language | Time, s | Total time, s | Memory, MiB |
| :------- | ------: | ------------: | ----------: |
| C++ (clang) |  0.032<sub>±0.000</sub> |  0.035<sub>±0.002</sub> |       1.53<sub>±0.95</sub> |
| C++ (gcc) |  0.031<sub>±0.001</sub> |  0.035<sub>±0.001</sub> |       1.47<sub>±0.89</sub> |
| Java |  0.055<sub>±0.002</sub> |  0.103<sub>±0.008</sub> |      44.00<sub>±2.00</sub> |
| Java (GraalVM) |  0.049<sub>±0.002</sub> |  0.139<sub>±0.004</sub> |      86.25<sub>±2.16</sub> |
| JavaScript (Node) |  0.048<sub>±0.001</sub> |  0.077<sub>±0.002</sub> |      47.53<sub>±0.81</sub> |
| JavaScript (GraalVM) |  0.234<sub>±0.029</sub> |  0.558<sub>±0.037</sub> |     338.96<sub>±5.95</sub> |
| PHP |  0.692<sub>±0.009</sub> |  0.708<sub>±0.010</sub> |      18.49<sub>±0.19</sub> |
| PHP (JIT: tracing) |  0.120<sub>±0.002</sub> |  0.134<sub>±0.002</sub> |      21.67<sub>±0.34</sub> |
| PHP (JIT: function) |  0.157<sub>±0.012</sub> |  0.172<sub>±0.012</sub> |      21.62<sub>±0.15</sub> |
| Python (CPython) |  3.242<sub>±0.041</sub> |  3.253<sub>±0.040</sub> |       7.75<sub>±0.06</sub> |
| Python (PyPy) |  0.051<sub>±0.003</sub> |  0.076<sub>±0.004</sub> |      54.68<sub>±0.22</sub> |
| Ruby |  1.943<sub>±0.068</sub> |  1.993<sub>±0.070</sub> |      15.86<sub>±0.12</sub> |
| Ruby (JIT) |  1.465<sub>±0.047</sub> |  1.514<sub>±0.045</sub> |      16.30<sub>±0.06</sub> |
| Ruby (JRuby) |  2.321<sub>±0.133</sub> |  4.612<sub>±0.259</sub> |     513.35<sub>±25.52</sub> |
| Rust |  0.032<sub>±0.001</sub> |  0.034<sub>±0.002</sub> |       1.76<sub>±0.09</sub> |


### treap/Naive

| Language | Time, s | Total time, s | Memory, MiB |
| :------- | ------: | ------------: | ----------: |
| C++ (clang) |  0.224<sub>±0.010</sub> |  0.227<sub>±0.009</sub> |       3.29<sub>±0.14</sub> |
| C++ (gcc) |  0.196<sub>±0.002</sub> |  0.200<sub>±0.003</sub> |       3.25<sub>±0.15</sub> |
| Go |  0.318<sub>±0.010</sub> |  0.320<sub>±0.011</sub> |       7.55<sub>±0.08</sub> |
| Java |  0.541<sub>±0.018</sub> |  0.594<sub>±0.018</sub> |     157.52<sub>±0.92</sub> |
| Java (GraalVM) |  0.529<sub>±0.083</sub> |  0.626<sub>±0.086</sub> |     224.14<sub>±30.48</sub> |
| JavaScript (Node) |  0.974<sub>±0.013</sub> |  1.009<sub>±0.011</sub> |      83.44<sub>±0.92</sub> |
| JavaScript (GraalVM) |  2.418<sub>±0.068</sub> |  2.878<sub>±0.083</sub> |     549.55<sub>±7.42</sub> |
| Kotlin (JVM) |  0.600<sub>±0.059</sub> |  0.650<sub>±0.061</sub> |     174.09<sub>±18.45</sub> |
| Kotlin (Native) |  1.000<sub>±0.027</sub> |  1.007<sub>±0.028</sub> |      22.75<sub>±1.20</sub> |
| PHP |  4.898<sub>±0.034</sub> |  4.911<sub>±0.034</sub> |      18.42<sub>±0.20</sub> |
| PHP (JIT: tracing) |  2.963<sub>±0.034</sub> |  2.981<sub>±0.034</sub> |      21.92<sub>±0.20</sub> |
| PHP (JIT: function) |  3.090<sub>±0.018</sub> |  3.106<sub>±0.019</sub> |      21.70<sub>±0.19</sub> |
| Python (CPython) | 13.089<sub>±0.077</sub> | 13.104<sub>±0.076</sub> |       8.47<sub>±0.07</sub> |
| Python (PyPy) |  2.920<sub>±0.058</sub> |  2.995<sub>±0.055</sub> |      62.26<sub>±0.79</sub> |
| Ruby |  5.914<sub>±0.095</sub> |  5.965<sub>±0.095</sub> |      17.65<sub>±0.05</sub> |
| Ruby (JIT) |  3.264<sub>±0.051</sub> |  3.314<sub>±0.051</sub> |      18.28<sub>±0.04</sub> |
| Ruby (JRuby) |  5.569<sub>±0.114</sub> |  7.800<sub>±0.116</sub> |     235.72<sub>±38.68</sub> |


### recursion/Tak

| Language | Time, s | Total time, s | Memory, MiB |
| :------- | ------: | ------------: | ----------: |
| C++ (clang) |  0.053<sub>±0.008</sub> |  0.056<sub>±0.009</sub> |       1.52<sub>±0.64</sub> |
| C++ (gcc) |  0.057<sub>±0.006</sub> |  0.059<sub>±0.006</sub> |       1.46<sub>±0.00</sub> |
| JavaScript (Node) |  0.146<sub>±0.015</sub> |  0.169<sub>±0.019</sub> |      44.36<sub>±0.14</sub> |
| JavaScript (GraalVM) |  0.909<sub>±0.070</sub> |  1.318<sub>±0.106</sub> |     415.32<sub>±8.58</sub> |
| PHP |  1.176<sub>±0.016</sub> |  1.189<sub>±0.016</sub> |      18.20<sub>±0.23</sub> |
| PHP (JIT: tracing) |  0.401<sub>±0.006</sub> |  0.418<sub>±0.005</sub> |      21.73<sub>±0.20</sub> |
| PHP (JIT: function) |  0.432<sub>±0.004</sub> |  0.447<sub>±0.004</sub> |      21.58<sub>±0.09</sub> |
| Python (CPython) |  4.474<sub>±0.010</sub> |  4.487<sub>±0.011</sub> |       6.82<sub>±0.05</sub> |
| Python (PyPy) |  0.817<sub>±0.033</sub> |  0.851<sub>±0.031</sub> |      59.78<sub>±0.09</sub> |
| Ruby |  1.320<sub>±0.054</sub> |  1.419<sub>±0.061</sub> |      15.62<sub>±0.12</sub> |
| Ruby (JIT) |  0.302<sub>±0.007</sub> |  0.354<sub>±0.007</sub> |      16.29<sub>±0.05</sub> |
| Ruby (JRuby) |  0.679<sub>±0.048</sub> |  2.995<sub>±0.064</sub> |     186.18<sub>±4.25</sub> |


### linpack/Linpack

| Language | Time, s | Total time, s | Memory, MiB |
| :------- | ------: | ------------: | ----------: |
| Go |  3.706<sub>±0.288</sub> |  3.710<sub>±0.287</sub> |      35.80<sub>±0.15</sub> |
| JavaScript (Node) |  9.506<sub>±0.264</sub> |  9.548<sub>±0.325</sub> |     138.10<sub>±1.52</sub> |
| JavaScript (GraalVM) |  4.415<sub>±0.182</sub> |  4.996<sub>±0.201</sub> |     410.26<sub>±9.81</sub> |
| PHP | 86.161<sub>±0.363</sub> | 86.174<sub>±0.349</sub> |      90.57<sub>±0.10</sub> |
| PHP (JIT: tracing) | 24.150<sub>±0.187</sub> | 24.168<sub>±0.190</sub> |      93.88<sub>±0.17</sub> |
| PHP (JIT: function) | 31.180<sub>±0.330</sub> | 31.197<sub>±0.328</sub> |      93.55<sub>±0.09</sub> |
| Python (CPython) | 630.060<sub>±14.024</sub> | 630.076<sub>±14.022</sub> |     163.50<sub>±0.09</sub> |
| Python (PyPy) |  6.979<sub>±0.098</sub> |  7.039<sub>±0.068</sub> |     102.28<sub>±3.36</sub> |


