### primes/Simple

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.343<sub>±0.018</sub> |       3.07<sub>±1.59</sub> |
| Java (Naive) |  0.486<sub>±0.140</sub> |      39.73<sub>±1.41</sub> |
| Java (GraalVM: Naive) |  0.848<sub>±0.016</sub> |     136.49<sub>±10.77</sub> |
| JavaScript (Node) |  0.529<sub>±0.125</sub> |      38.58<sub>±1.39</sub> |
| JavaScript (GraalVM Node) |  2.262<sub>±0.081</sub> |     784.72<sub>±65.64</sub> |
| PHP (Naive) |  2.986<sub>±0.038</sub> |      17.16<sub>±0.16</sub> |
| PHP (JIT: tracing) |  1.489<sub>±0.021</sub> |      20.45<sub>±0.46</sub> |
| PHP (JIT: function) |  1.714<sub>±0.095</sub> |      20.37<sub>±0.30</sub> |
| Ruby (Naive) | 11.075<sub>±0.197</sub> |      13.62<sub>±0.12</sub> |
| Ruby (JIT) |  7.648<sub>±0.988</sub> |      14.18<sub>±0.07</sub> |
| Ruby (JRuby) | 14.186<sub>±1.158</sub> |     361.14<sub>±30.45</sub> |
| Ruby (TruffleRuby) |  1.060<sub>±0.051</sub> |     672.24<sub>±5.10</sub> |
| Ruby (TruffleRuby JVM) |  5.072<sub>±0.587</sub> |     722.42<sub>±58.36</sub> |
| Ruby (GraalVM) |  0.971<sub>±0.088</sub> |     672.55<sub>±7.79</sub> |
| Ruby (GraalVM JVM) |  4.410<sub>±0.062</sub> |     731.32<sub>±215.37</sub> |
| Rust |  0.439<sub>±0.003</sub> |       1.73<sub>±0.07</sub> |


### primes/Atkin

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.220<sub>±0.013</sub> |      88.78<sub>±0.18</sub> |
| Java (Naive) |  0.256<sub>±0.092</sub> |     172.29<sub>±0.84</sub> |
| Java (GraalVM: Naive) |  0.732<sub>±0.054</sub> |     318.83<sub>±22.71</sub> |
| JavaScript (Node) |  0.390<sub>±0.031</sub> |     207.97<sub>±2.08</sub> |
| JavaScript (GraalVM Node) |  2.266<sub>±0.317</sub> |     998.37<sub>±77.35</sub> |
| PHP (Naive) |  1.781<sub>±0.099</sub> |     344.43<sub>±0.57</sub> |
| PHP (JIT: tracing) |  1.942<sub>±0.216</sub> |     347.84<sub>±0.30</sub> |
| PHP (JIT: function) |  1.380<sub>±0.073</sub> |     347.37<sub>±0.40</sub> |
| Python (CPython) |  5.531<sub>±0.427</sub> |     245.73<sub>±0.09</sub> |
| Python (PyPy) |  1.294<sub>±0.023</sub> |     317.10<sub>±0.42</sub> |
| Python (GraalVM) |  1.854<sub>±0.284</sub> |     905.61<sub>±87.95</sub> |
| Ruby (Naive) |  3.139<sub>±0.145</sub> |     160.58<sub>±0.05</sub> |
| Ruby (JIT) |  2.850<sub>±0.140</sub> |     161.19<sub>±0.10</sub> |
| Ruby (JRuby) |  4.444<sub>±0.414</sub> |     565.38<sub>±124.99</sub> |
| Ruby (TruffleRuby) |  1.768<sub>±0.059</sub> |     874.84<sub>±8.03</sub> |
| Ruby (TruffleRuby JVM) |  4.528<sub>±0.104</sub> |     941.35<sub>±10.95</sub> |
| Ruby (GraalVM) |  1.755<sub>±0.163</sub> |     884.32<sub>±25.09</sub> |
| Ruby (GraalVM JVM) |  4.634<sub>±0.124</sub> |     899.99<sub>±73.64</sub> |
| Rust |  0.201<sub>±0.026</sub> |      77.50<sub>±0.08</sub> |


### collatz/MaxSequence

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.075<sub>±0.001</sub> |       1.53<sub>±1.45</sub> |
| Java (Naive) |  0.144<sub>±0.008</sub> |      36.29<sub>±0.21</sub> |
| Java (GraalVM: Naive) |  0.494<sub>±0.003</sub> |      74.38<sub>±1.51</sub> |
| JavaScript (Node) |  0.984<sub>±0.034</sub> |      33.87<sub>±2.09</sub> |
| JavaScript (GraalVM Node) |  1.266<sub>±0.085</sub> |     474.26<sub>±5.68</sub> |
| PHP (Naive) |  1.030<sub>±0.024</sub> |      17.25<sub>±0.40</sub> |
| PHP (JIT: tracing) |  0.425<sub>±0.014</sub> |      20.50<sub>±0.22</sub> |
| PHP (JIT: function) |  0.573<sub>±0.156</sub> |      20.37<sub>±0.21</sub> |
| Ruby (Naive) |  3.106<sub>±0.450</sub> |      13.34<sub>±0.11</sub> |
| Ruby (JIT) |  0.785<sub>±0.119</sub> |      13.78<sub>±0.08</sub> |
| Ruby (JRuby) |  3.321<sub>±0.415</sub> |     345.29<sub>±58.70</sub> |
| Ruby (TruffleRuby) |  0.559<sub>±0.014</sub> |     439.87<sub>±3.89</sub> |
| Ruby (TruffleRuby JVM) |  3.145<sub>±0.188</sub> |     572.95<sub>±18.76</sub> |
| Ruby (GraalVM) |  0.578<sub>±0.179</sub> |     440.59<sub>±4.05</sub> |
| Ruby (GraalVM JVM) |  3.284<sub>±0.213</sub> |     562.52<sub>±17.34</sub> |
| Rust |  0.074<sub>±0.002</sub> |       1.73<sub>±0.07</sub> |


### mandelbrot/Simple

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.043<sub>±0.001</sub> |       1.48<sub>±1.73</sub> |
| Java (Naive) |  0.082<sub>±0.007</sub> |      37.43<sub>±0.43</sub> |
| Java (GraalVM: Naive) |  0.436<sub>±0.004</sub> |      74.84<sub>±1.56</sub> |
| JavaScript (Node) |  0.091<sub>±0.012</sub> |      36.97<sub>±2.05</sub> |
| JavaScript (GraalVM Node) |  0.504<sub>±0.065</sub> |     505.80<sub>±7.17</sub> |
| PHP (Naive) |  0.512<sub>±0.154</sub> |      17.52<sub>±0.21</sub> |
| PHP (JIT: tracing) |  0.161<sub>±0.005</sub> |      20.75<sub>±0.26</sub> |
| PHP (JIT: function) |  0.210<sub>±0.030</sub> |      20.53<sub>±0.25</sub> |
| Ruby (Naive) |  1.982<sub>±0.099</sub> |      13.68<sub>±0.09</sub> |
| Ruby (JIT) |  1.555<sub>±0.165</sub> |      14.13<sub>±0.05</sub> |
| Ruby (JRuby) |  4.132<sub>±0.749</sub> |     353.20<sub>±33.18</sub> |
| Ruby (TruffleRuby) |  0.418<sub>±0.106</sub> |     630.66<sub>±7.18</sub> |
| Ruby (TruffleRuby JVM) |  3.570<sub>±0.399</sub> |     619.73<sub>±44.04</sub> |
| Ruby (GraalVM) |  0.461<sub>±0.060</sub> |     634.25<sub>±6.27</sub> |
| Ruby (GraalVM JVM) |  3.536<sub>±0.497</sub> |     611.72<sub>±25.18</sub> |
| Rust |  0.041<sub>±0.001</sub> |       1.70<sub>±0.04</sub> |


### io/Load

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.094<sub>±0.005</sub> |       2.99<sub>±1.57</sub> |
| Go |  0.161<sub>±0.027</sub> |       2.68<sub>±0.15</sub> |
| Java (Naive) |  0.223<sub>±0.033</sub> |      75.21<sub>±7.98</sub> |
| Java (GraalVM: Naive) |  0.789<sub>±0.019</sub> |     171.85<sub>±3.52</sub> |
| JavaScript (Node) |  1.360<sub>±0.047</sub> |      65.48<sub>±1.66</sub> |
| JavaScript (GraalVM Node) |  4.435<sub>±0.302</sub> |     877.33<sub>±60.69</sub> |
| PHP (Naive) |  0.108<sub>±0.002</sub> |      17.36<sub>±0.72</sub> |
| PHP (JIT: tracing) |  0.102<sub>±0.010</sub> |      20.57<sub>±0.18</sub> |
| PHP (JIT: function) |  0.103<sub>±0.001</sub> |      20.31<sub>±0.29</sub> |
| Python (CPython) |  0.139<sub>±0.005</sub> |       7.25<sub>±0.06</sub> |
| Python (PyPy) |  0.114<sub>±0.001</sub> |      64.08<sub>±0.62</sub> |
| Python (GraalVM) |  3.611<sub>±0.424</sub> |     823.54<sub>±28.86</sub> |
| Ruby (Naive) |  0.272<sub>±0.012</sub> |      13.67<sub>±0.08</sub> |
| Ruby (JIT) |  0.379<sub>±0.072</sub> |      14.09<sub>±0.09</sub> |
| Ruby (JRuby) |  2.496<sub>±0.183</sub> |     192.70<sub>±9.77</sub> |
| Ruby (TruffleRuby) |  1.246<sub>±0.149</sub> |     693.52<sub>±39.04</sub> |
| Ruby (TruffleRuby JVM) |  5.146<sub>±0.445</sub> |     609.10<sub>±43.94</sub> |
| Ruby (GraalVM) |  1.379<sub>±0.140</sub> |     711.41<sub>±37.79</sub> |
| Ruby (GraalVM JVM) |  4.849<sub>±0.334</sub> |     605.60<sub>±16.81</sub> |
| Rust |  0.091<sub>±0.004</sub> |       1.73<sub>±0.11</sub> |


### io/NoLoad

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.001<sub>±0.001</sub> |       1.48<sub>±1.64</sub> |
| Go |  0.001<sub>±0.003</sub> |       2.68<sub>±0.15</sub> |
| Java (Naive) |  0.028<sub>±0.051</sub> |      34.49<sub>±0.18</sub> |
| Java (GraalVM: Naive) |  0.381<sub>±0.004</sub> |      62.73<sub>±3.72</sub> |
| JavaScript (Node) |  0.031<sub>±0.002</sub> |      33.47<sub>±1.92</sub> |
| JavaScript (GraalVM Node) |  0.261<sub>±0.038</sub> |     404.21<sub>±20.03</sub> |
| PHP (Naive) |  0.012<sub>±0.001</sub> |      17.23<sub>±0.79</sub> |
| PHP (JIT: tracing) |  0.012<sub>±0.005</sub> |      20.47<sub>±0.21</sub> |
| PHP (JIT: function) |  0.012<sub>±0.002</sub> |      20.43<sub>±0.19</sub> |
| Python (CPython) |  0.030<sub>±0.002</sub> |       6.89<sub>±0.33</sub> |
| Python (PyPy) |  0.027<sub>±0.001</sub> |      55.29<sub>±1.57</sub> |
| Python (GraalVM) |  0.261<sub>±0.087</sub> |     341.77<sub>±21.25</sub> |
| Ruby (Naive) |  0.068<sub>±0.025</sub> |      13.27<sub>±0.04</sub> |
| Ruby (JIT) |  0.252<sub>±0.034</sub> |      13.66<sub>±0.08</sub> |
| Ruby (JRuby) |  1.904<sub>±0.066</sub> |     180.99<sub>±6.76</sub> |
| Ruby (TruffleRuby) |  0.092<sub>±0.070</sub> |     225.61<sub>±2.91</sub> |
| Ruby (TruffleRuby JVM) |  2.620<sub>±0.073</sub> |     521.18<sub>±9.95</sub> |
| Ruby (GraalVM) |  0.093<sub>±0.007</sub> |     225.96<sub>±14.09</sub> |
| Ruby (GraalVM JVM) |  2.619<sub>±0.304</sub> |     520.61<sub>±5.64</sub> |
| Rust |  0.001<sub>±0.001</sub> |       1.68<sub>±1.11</sub> |


### treap/Naive

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| JavaScript (Node) |  0.853<sub>±0.009</sub> |      77.72<sub>±2.14</sub> |
| JavaScript (GraalVM Node) |  3.164<sub>±0.129</sub> |     819.83<sub>±30.01</sub> |
| PHP (Naive) |  3.289<sub>±0.521</sub> |      17.41<sub>±0.28</sub> |
| PHP (JIT: tracing) |  2.009<sub>±0.151</sub> |      20.57<sub>±0.23</sub> |
| PHP (JIT: function) |  2.127<sub>±0.034</sub> |      20.47<sub>±0.11</sub> |
| Python (CPython) |  8.653<sub>±0.482</sub> |       8.51<sub>±0.12</sub> |
| Python (PyPy) |  2.841<sub>±0.191</sub> |      73.64<sub>±1.01</sub> |
| Python (GraalVM) |  3.507<sub>±0.287</sub> |     883.35<sub>±13.61</sub> |
| Ruby (Naive) |  6.392<sub>±0.077</sub> |      13.80<sub>±0.09</sub> |
| Ruby (JIT) |  5.530<sub>±0.296</sub> |      14.53<sub>±0.06</sub> |
| Ruby (JRuby) |  6.824<sub>±0.771</sub> |     235.08<sub>±20.27</sub> |
| Ruby (TruffleRuby) |  1.784<sub>±0.073</sub> |     694.82<sub>±20.52</sub> |
| Ruby (TruffleRuby JVM) |  4.513<sub>±0.357</sub> |     829.85<sub>±73.65</sub> |
| Ruby (GraalVM) |  1.785<sub>±0.513</sub> |     694.95<sub>±20.14</sub> |
| Ruby (GraalVM JVM) |  4.519<sub>±0.325</sub> |     915.75<sub>±202.70</sub> |


