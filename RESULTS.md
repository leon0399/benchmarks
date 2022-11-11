### primes/Simple

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.345<sub>±0.040</sub> |       1.47<sub>±1.63</sub> |
| C++ (gcc) |  0.344<sub>±0.005</sub> |       3.14<sub>±0.08</sub> |
| Java |  0.420<sub>±0.076</sub> |      39.75<sub>±1.66</sub> |
| Java (GraalVM) |  0.755<sub>±0.045</sub> |     129.39<sub>±12.48</sub> |
| JavaScript (Node) |  0.426<sub>±0.023</sub> |      39.29<sub>±1.87</sub> |
| JavaScript (GraalVM) |  1.997<sub>±0.042</sub> |     794.79<sub>±11.78</sub> |
| PHP |  3.433<sub>±0.057</sub> |      17.07<sub>±0.41</sub> |
| PHP (JIT: tracing) |  1.288<sub>±0.030</sub> |      20.37<sub>±0.20</sub> |
| PHP (JIT: function) |  1.430<sub>±0.182</sub> |      20.36<sub>±0.19</sub> |
| Ruby | 10.803<sub>±0.326</sub> |      13.64<sub>±0.07</sub> |
| Ruby (JIT) |  9.352<sub>±0.452</sub> |      14.12<sub>±0.09</sub> |
| Ruby (JRuby) | 16.935<sub>±1.430</sub> |     315.99<sub>±29.11</sub> |
| Ruby (TruffleRuby) |  0.890<sub>±0.138</sub> |     662.68<sub>±8.46</sub> |
| Ruby (TruffleRuby JVM) |  4.051<sub>±0.449</sub> |     633.17<sub>±22.95</sub> |
| Ruby (GraalVM) |  0.865<sub>±0.068</sub> |     660.77<sub>±10.23</sub> |
| Ruby (GraalVM JVM) |  4.105<sub>±0.077</sub> |     614.62<sub>±49.86</sub> |
| Rust |  0.347<sub>±0.002</sub> |       1.68<sub>±0.12</sub> |


### primes/Atkin

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.234<sub>±0.011</sub> |      89.01<sub>±0.13</sub> |
| C++ (gcc) |  0.213<sub>±0.010</sub> |      88.98<sub>±0.07</sub> |
| Java |  0.442<sub>±0.061</sub> |     189.23<sub>±2.52</sub> |
| Java (GraalVM) |  0.873<sub>±0.106</sub> |     292.09<sub>±19.65</sub> |
| JavaScript (Node) |  0.376<sub>±0.026</sub> |     210.13<sub>±0.44</sub> |
| JavaScript (GraalVM) |  2.077<sub>±0.342</sub> |     992.22<sub>±80.50</sub> |
| PHP |  2.196<sub>±0.023</sub> |     344.15<sub>±0.24</sub> |
| PHP (JIT: tracing) |  1.945<sub>±0.024</sub> |     347.87<sub>±0.19</sub> |
| PHP (JIT: function) |  1.334<sub>±0.019</sub> |     347.36<sub>±0.34</sub> |
| Python (CPython) |  6.411<sub>±0.043</sub> |     245.74<sub>±0.11</sub> |
| Python (PyPy) |  1.392<sub>±0.061</sub> |     316.89<sub>±0.30</sub> |
| Python (GraalVM) |  1.710<sub>±0.108</sub> |     908.07<sub>±33.57</sub> |
| Ruby |  2.815<sub>±0.040</sub> |     160.56<sub>±0.09</sub> |
| Ruby (JIT) |  2.737<sub>±0.119</sub> |     161.11<sub>±0.16</sub> |
| Ruby (JRuby) |  4.173<sub>±0.998</sub> |     522.36<sub>±27.55</sub> |
| Ruby (TruffleRuby) |  1.660<sub>±0.124</sub> |     866.87<sub>±52.16</sub> |
| Ruby (TruffleRuby JVM) |  4.320<sub>±0.157</sub> |     953.71<sub>±70.29</sub> |
| Ruby (GraalVM) |  1.620<sub>±0.127</sub> |     864.70<sub>±37.03</sub> |
| Ruby (GraalVM JVM) |  4.262<sub>±0.107</sub> |     935.60<sub>±79.69</sub> |
| Rust |  0.192<sub>±0.013</sub> |      77.48<sub>±0.06</sub> |


### collatz/MaxSequence

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.060<sub>±0.032</sub> |       1.48<sub>±1.62</sub> |
| Java |  0.142<sub>±0.100</sub> |      36.26<sub>±0.11</sub> |
| Java (GraalVM) |  0.512<sub>±0.057</sub> |      74.91<sub>±5.05</sub> |
| JavaScript (Node) |  0.778<sub>±0.014</sub> |      32.04<sub>±1.95</sub> |
| JavaScript (GraalVM) |  1.045<sub>±0.050</sub> |     457.38<sub>±6.13</sub> |
| PHP |  1.366<sub>±0.042</sub> |      17.28<sub>±0.28</sub> |
| PHP (JIT: tracing) |  0.404<sub>±0.013</sub> |      20.53<sub>±0.15</sub> |
| PHP (JIT: function) |  0.497<sub>±0.019</sub> |      20.31<sub>±1.70</sub> |
| Ruby |  2.644<sub>±0.018</sub> |      13.33<sub>±0.05</sub> |
| Ruby (JIT) |  0.792<sub>±0.048</sub> |      13.80<sub>±0.09</sub> |
| Ruby (JRuby) |  2.796<sub>±0.101</sub> |     335.11<sub>±34.02</sub> |
| Ruby (TruffleRuby) |  0.510<sub>±0.020</sub> |     436.38<sub>±6.86</sub> |
| Ruby (TruffleRuby JVM) |  2.931<sub>±0.190</sub> |     564.19<sub>±9.97</sub> |
| Ruby (GraalVM) |  0.519<sub>±0.036</sub> |     440.34<sub>±4.07</sub> |
| Ruby (GraalVM JVM) |  2.869<sub>±0.063</sub> |     569.31<sub>±129.41</sub> |
| Rust |  0.060<sub>±0.000</sub> |       1.68<sub>±0.04</sub> |


### mandelbrot/Simple

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.034<sub>±0.001</sub> |       3.10<sub>±1.64</sub> |
| C++ (gcc) |  0.034<sub>±0.000</sub> |       1.48<sub>±1.67</sub> |
| Java |  0.085<sub>±0.082</sub> |      37.38<sub>±0.94</sub> |
| Java (GraalVM) |  0.446<sub>±0.058</sub> |      74.26<sub>±5.66</sub> |
| JavaScript (Node) |  0.078<sub>±0.003</sub> |      39.19<sub>±2.00</sub> |
| JavaScript (GraalVM) |  0.441<sub>±0.010</sub> |     506.45<sub>±6.57</sub> |
| PHP |  0.702<sub>±0.011</sub> |      17.40<sub>±0.25</sub> |
| PHP (JIT: tracing) |  0.127<sub>±0.004</sub> |      20.53<sub>±1.58</sub> |
| PHP (JIT: function) |  0.167<sub>±0.017</sub> |      20.43<sub>±0.26</sub> |
| Ruby |  1.812<sub>±0.056</sub> |      13.68<sub>±0.08</sub> |
| Ruby (JIT) |  1.396<sub>±0.043</sub> |      14.21<sub>±0.14</sub> |
| Ruby (JRuby) |  3.276<sub>±0.075</sub> |     341.49<sub>±27.59</sub> |
| Ruby (TruffleRuby) |  0.400<sub>±0.061</sub> |     628.82<sub>±8.06</sub> |
| Ruby (TruffleRuby JVM) |  3.190<sub>±0.130</sub> |     602.92<sub>±15.51</sub> |
| Ruby (GraalVM) |  0.385<sub>±0.038</sub> |     627.31<sub>±5.54</sub> |
| Ruby (GraalVM JVM) |  3.137<sub>±0.095</sub> |     613.91<sub>±36.93</sub> |
| Rust |  0.035<sub>±0.018</sub> |       1.73<sub>±0.07</sub> |


### treap/Naive

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.217<sub>±0.007</sub> |       3.14<sub>±0.22</sub> |
| C++ (gcc) |  0.183<sub>±0.004</sub> |       3.32<sub>±0.21</sub> |
| Go |  0.302<sub>±0.011</sub> |       7.59<sub>±2.11</sub> |
| Java |  0.683<sub>±0.056</sub> |     139.79<sub>±11.19</sub> |
| Java (GraalVM) |  1.093<sub>±0.171</sub> |     352.25<sub>±161.44</sub> |
| JavaScript (Node) |  0.970<sub>±0.088</sub> |      77.59<sub>±1.50</sub> |
| JavaScript (GraalVM) |  2.804<sub>±0.040</sub> |     820.02<sub>±10.32</sub> |
| Kotlin (JVM) |  0.585<sub>±0.060</sub> |     138.97<sub>±0.65</sub> |
| Kotlin (Native) |  3.319<sub>±0.025</sub> |       4.11<sub>±0.40</sub> |
| PHP |  4.795<sub>±0.023</sub> |      17.32<sub>±0.27</sub> |
| PHP (JIT: tracing) |  2.911<sub>±0.036</sub> |      20.65<sub>±0.19</sub> |
| PHP (JIT: function) |  3.018<sub>±0.039</sub> |      20.46<sub>±0.20</sub> |
| Python (CPython) | 12.598<sub>±0.048</sub> |       8.43<sub>±0.05</sub> |
| Python (PyPy) |  2.894<sub>±0.261</sub> |      74.10<sub>±7.33</sub> |
| Python (GraalVM) |  3.235<sub>±0.046</sub> |     870.78<sub>±8.85</sub> |
| Ruby |  6.109<sub>±0.102</sub> |      13.84<sub>±0.07</sub> |
| Ruby (JIT) |  5.185<sub>±0.073</sub> |      14.54<sub>±0.06</sub> |
| Ruby (JRuby) |  5.874<sub>±0.342</sub> |     244.77<sub>±32.67</sub> |
| Ruby (TruffleRuby) |  1.698<sub>±0.158</sub> |     695.42<sub>±19.12</sub> |
| Ruby (TruffleRuby JVM) |  4.344<sub>±0.255</sub> |    1027.42<sub>±268.16</sub> |
| Ruby (GraalVM) |  1.630<sub>±0.082</sub> |     695.14<sub>±12.50</sub> |
| Ruby (GraalVM JVM) |  4.161<sub>±0.105</sub> |     744.08<sub>±69.94</sub> |


### recursion/Tak

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.045<sub>±0.004</sub> |       1.47<sub>±1.69</sub> |
| C++ (gcc) |  0.057<sub>±0.002</sub> |       1.53<sub>±1.69</sub> |
| PHP |  1.186<sub>±0.055</sub> |      17.25<sub>±1.66</sub> |
| PHP (JIT: tracing) |  0.410<sub>±0.010</sub> |      20.47<sub>±0.23</sub> |
| PHP (JIT: function) |  0.418<sub>±0.009</sub> |      20.33<sub>±0.30</sub> |
| Python (CPython) |  4.348<sub>±0.056</sub> |       7.16<sub>±0.57</sub> |
| Python (PyPy) |  0.801<sub>±0.034</sub> |      63.30<sub>±0.50</sub> |
| Python (GraalVM) |  1.190<sub>±0.173</sub> |     722.47<sub>±0.61</sub> |
| Ruby |  1.415<sub>±0.035</sub> |      13.27<sub>±0.08</sub> |
| Ruby (JIT) |  0.653<sub>±0.029</sub> |      13.79<sub>±0.18</sub> |
| Ruby (JRuby) |  2.163<sub>±0.183</sub> |     174.73<sub>±4.97</sub> |
| Ruby (TruffleRuby) |  0.774<sub>±0.051</sub> |     580.90<sub>±6.67</sub> |
| Ruby (TruffleRuby JVM) |  2.987<sub>±0.119</sub> |     810.34<sub>±227.00</sub> |
| Ruby (GraalVM) |  0.757<sub>±0.123</sub> |     584.32<sub>±6.46</sub> |
| Ruby (GraalVM JVM) |  2.984<sub>±0.077</sub> |     826.95<sub>±79.00</sub> |


### io/Load

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.090<sub>±0.059</sub> |       2.98<sub>±1.51</sub> |
| C++ (gcc) |  0.091<sub>±0.003</sub> |       3.08<sub>±1.61</sub> |
| Go |  0.145<sub>±0.023</sub> |       2.68<sub>±0.00</sub> |
| Java |  0.246<sub>±0.037</sub> |      76.15<sub>±5.02</sub> |
| Java (GraalVM) |  0.823<sub>±0.034</sub> |     175.25<sub>±20.05</sub> |
| JavaScript (Node) |  1.162<sub>±0.018</sub> |      65.76<sub>±3.69</sub> |
| JavaScript (GraalVM) |  3.911<sub>±0.263</sub> |     897.14<sub>±48.04</sub> |
| PHP |  0.105<sub>±0.016</sub> |      17.18<sub>±0.31</sub> |
| PHP (JIT: tracing) |  0.096<sub>±0.002</sub> |      20.37<sub>±0.24</sub> |
| PHP (JIT: function) |  0.095<sub>±0.004</sub> |      20.49<sub>±0.44</sub> |
| Python (CPython) |  0.175<sub>±0.015</sub> |       7.28<sub>±0.45</sub> |
| Python (PyPy) |  0.118<sub>±0.009</sub> |      64.41<sub>±0.18</sub> |
| Python (GraalVM) |  2.824<sub>±0.095</sub> |     809.24<sub>±16.91</sub> |
| Ruby |  0.221<sub>±0.031</sub> |      13.73<sub>±0.03</sub> |
| Ruby (JIT) |  0.297<sub>±0.036</sub> |      14.07<sub>±0.11</sub> |
| Ruby (JRuby) |  2.198<sub>±0.096</sub> |     195.26<sub>±11.00</sub> |
| Ruby (TruffleRuby) |  1.113<sub>±0.079</sub> |     680.73<sub>±19.89</sub> |
| Ruby (TruffleRuby JVM) |  4.435<sub>±0.297</sub> |     621.67<sub>±38.71</sub> |
| Ruby (GraalVM) |  1.127<sub>±0.039</sub> |     690.28<sub>±15.90</sub> |
| Ruby (GraalVM JVM) |  4.419<sub>±0.125</sub> |     618.78<sub>±6.30</sub> |
| Rust |  0.081<sub>±0.011</sub> |       1.73<sub>±0.07</sub> |


### io/NoLoad

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.001<sub>±0.001</sub> |       1.47<sub>±0.01</sub> |
| C++ (gcc) |  0.001<sub>±0.000</sub> |       1.47<sub>±0.06</sub> |
| Go |  0.002<sub>±0.003</sub> |       2.68<sub>±0.14</sub> |
| Java |  0.042<sub>±0.049</sub> |      34.48<sub>±0.20</sub> |
| Java (GraalVM) |  0.398<sub>±0.032</sub> |      62.96<sub>±1.21</sub> |
| JavaScript (Node) |  0.034<sub>±0.004</sub> |      35.50<sub>±2.07</sub> |
| JavaScript (GraalVM) |  0.278<sub>±0.017</sub> |     388.70<sub>±11.87</sub> |
| PHP |  0.016<sub>±0.001</sub> |      17.36<sub>±0.13</sub> |
| PHP (JIT: tracing) |  0.011<sub>±0.001</sub> |      20.35<sub>±0.18</sub> |
| PHP (JIT: function) |  0.012<sub>±0.001</sub> |      20.27<sub>±0.23</sub> |
| Python (CPython) |  0.038<sub>±0.048</sub> |       7.14<sub>±0.42</sub> |
| Python (PyPy) |  0.029<sub>±0.003</sub> |      55.70<sub>±0.13</sub> |
| Python (GraalVM) |  0.211<sub>±0.034</sub> |     319.96<sub>±9.87</sub> |
| Ruby |  0.065<sub>±0.007</sub> |      13.33<sub>±0.08</sub> |
| Ruby (JIT) |  0.268<sub>±0.021</sub> |      13.68<sub>±0.10</sub> |
| Ruby (JRuby) |  1.701<sub>±0.038</sub> |     182.28<sub>±3.99</sub> |
| Ruby (TruffleRuby) |  0.100<sub>±0.029</sub> |     224.73<sub>±5.13</sub> |
| Ruby (TruffleRuby JVM) |  2.395<sub>±0.201</sub> |     535.64<sub>±7.77</sub> |
| Ruby (GraalVM) |  0.095<sub>±0.019</sub> |     224.23<sub>±6.71</sub> |
| Ruby (GraalVM JVM) |  2.429<sub>±0.047</sub> |     529.22<sub>±10.82</sub> |
| Rust |  0.001<sub>±0.002</sub> |       0.63<sub>±1.11</sub> |


### linpack/Linpack

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| Go |  2.810<sub>±0.168</sub> |      36.78<sub>±0.23</sub> |
| JavaScript (Node) |  4.252<sub>±4.498</sub> |     128.67<sub>±1.54</sub> |
| JavaScript (GraalVM) |  4.424<sub>±0.189</sub> |     702.14<sub>±4.89</sub> |
| PHP | 84.826<sub>±0.532</sub> |     142.75<sub>±0.39</sub> |
| PHP (JIT: tracing) | 25.389<sub>±0.449</sub> |     146.68<sub>±0.38</sub> |
| PHP (JIT: function) | 32.809<sub>±0.173</sub> |     146.04<sub>±0.42</sub> |
| Python (CPython) | 560.058<sub>±2.887</sub> |     163.33<sub>±0.17</sub> |
| Python (PyPy) |  6.305<sub>±0.080</sub> |     107.82<sub>±4.55</sub> |
| Python (GraalVM) | 66.517<sub>±5.414</sub> |    1354.91<sub>±200.26</sub> |


