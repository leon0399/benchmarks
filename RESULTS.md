### primes/Simple

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.440<sub>±0.002</sub> |       3.11<sub>±1.69</sub> |
| Java (Naive) |  0.499<sub>±0.017</sub> |      39.95<sub>±1.46</sub> |
| Java (GraalVM: Naive) |  0.821<sub>±0.022</sub> |     134.09<sub>±9.33</sub> |
| JavaScript (Node) |  0.532<sub>±0.004</sub> |      37.39<sub>±1.64</sub> |
| JavaScript (GraalVM Node) |  2.094<sub>±0.160</sub> |     772.61<sub>±22.00</sub> |
| PHP (Naive) |  3.132<sub>±0.177</sub> |      17.49<sub>±0.46</sub> |
| PHP (JIT: tracing) |  1.485<sub>±0.125</sub> |      20.41<sub>±0.24</sub> |
| PHP (JIT: function) |  1.746<sub>±0.225</sub> |      20.30<sub>±0.11</sub> |
| Ruby (Naive) | 11.283<sub>±0.519</sub> |      13.68<sub>±0.05</sub> |
| Ruby (JIT) |  7.751<sub>±0.334</sub> |      14.13<sub>±0.07</sub> |
| Ruby (JRuby) | 14.380<sub>±0.461</sub> |     353.34<sub>±70.71</sub> |
| Ruby (TruffleRuby) |  0.954<sub>±0.200</sub> |     668.22<sub>±4.59</sub> |
| Ruby (TruffleRuby JVM) |  4.648<sub>±0.417</sub> |     791.00<sub>±161.59</sub> |
| Ruby (GraalVM) |  0.959<sub>±0.043</sub> |     667.87<sub>±14.93</sub> |
| Ruby (GraalVM JVM) |  4.566<sub>±0.421</sub> |     729.67<sub>±233.38</sub> |
| Rust |  0.443<sub>±0.020</sub> |       1.78<sub>±0.10</sub> |


### primes/Atkin

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.226<sub>±0.012</sub> |      89.00<sub>±0.13</sub> |
| Java (Naive) |  0.270<sub>±0.102</sub> |     194.36<sub>±18.56</sub> |
| Java (GraalVM: Naive) |  0.677<sub>±0.029</sub> |     301.62<sub>±7.34</sub> |
| JavaScript (Node) |  0.375<sub>±0.026</sub> |     210.09<sub>±7.40</sub> |
| JavaScript (GraalVM Node) |  2.118<sub>±0.233</sub> |     982.33<sub>±15.66</sub> |
| PHP (Naive) |  1.747<sub>±0.058</sub> |     344.46<sub>±1.29</sub> |
| PHP (JIT: tracing) |  1.873<sub>±0.484</sub> |     347.96<sub>±0.42</sub> |
| PHP (JIT: function) |  1.363<sub>±0.044</sub> |     347.48<sub>±0.21</sub> |
| Python (CPython) |  5.359<sub>±0.229</sub> |     245.77<sub>±0.10</sub> |
| Python (PyPy) |  1.465<sub>±0.490</sub> |     316.95<sub>±2.74</sub> |
| Python (GraalVM) |  1.834<sub>±0.522</sub> |     924.10<sub>±110.26</sub> |
| Ruby (Naive) |  3.101<sub>±0.079</sub> |     160.57<sub>±0.09</sub> |
| Ruby (JIT) |  2.873<sub>±0.704</sub> |     161.27<sub>±0.12</sub> |
| Ruby (JRuby) |  4.363<sub>±0.422</sub> |     531.93<sub>±54.50</sub> |
| Ruby (TruffleRuby) |  1.734<sub>±0.130</sub> |     869.10<sub>±20.01</sub> |
| Ruby (TruffleRuby JVM) |  4.455<sub>±0.286</sub> |     922.29<sub>±133.69</sub> |
| Ruby (GraalVM) |  1.795<sub>±0.098</sub> |     876.77<sub>±40.07</sub> |
| Ruby (GraalVM JVM) |  4.502<sub>±0.178</sub> |     879.96<sub>±95.33</sub> |
| Rust |  0.209<sub>±0.008</sub> |      77.52<sub>±0.10</sub> |


### collatz/MaxSequence

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.076<sub>±0.025</sub> |       1.54<sub>±1.71</sub> |
| Java (Naive) |  0.146<sub>±0.007</sub> |      36.27<sub>±0.10</sub> |
| Java (GraalVM: Naive) |  0.502<sub>±0.055</sub> |      74.94<sub>±2.21</sub> |
| JavaScript (Node) |  0.977<sub>±0.083</sub> |      33.93<sub>±1.91</sub> |
| JavaScript (GraalVM Node) |  1.259<sub>±0.029</sub> |     468.67<sub>±13.69</sub> |
| PHP (Naive) |  1.033<sub>±0.143</sub> |      17.39<sub>±0.18</sub> |
| PHP (JIT: tracing) |  0.427<sub>±0.031</sub> |      20.69<sub>±0.39</sub> |
| PHP (JIT: function) |  0.573<sub>±0.003</sub> |      20.56<sub>±0.30</sub> |
| Ruby (Naive) |  3.107<sub>±0.096</sub> |      13.34<sub>±1.97</sub> |
| Ruby (JIT) |  0.826<sub>±0.271</sub> |      13.79<sub>±0.08</sub> |
| Ruby (JRuby) |  3.191<sub>±0.200</sub> |     316.16<sub>±28.25</sub> |
| Ruby (TruffleRuby) |  0.582<sub>±0.133</sub> |     438.16<sub>±4.91</sub> |
| Ruby (TruffleRuby JVM) |  3.113<sub>±0.292</sub> |     574.44<sub>±53.43</sub> |
| Ruby (GraalVM) |  0.565<sub>±0.022</sub> |     436.11<sub>±3.17</sub> |
| Ruby (GraalVM JVM) |  3.052<sub>±0.158</sub> |     561.32<sub>±82.24</sub> |
| Rust |  0.076<sub>±0.001</sub> |       1.73<sub>±0.08</sub> |


### mandelbrot/Simple

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.043<sub>±0.000</sub> |       3.00<sub>±1.52</sub> |
| Java (Naive) |  0.082<sub>±0.073</sub> |      37.46<sub>±0.43</sub> |
| Java (GraalVM: Naive) |  0.437<sub>±0.003</sub> |      75.81<sub>±5.64</sub> |
| JavaScript (Node) |  0.089<sub>±0.001</sub> |      38.85<sub>±1.94</sub> |
| JavaScript (GraalVM Node) |  0.474<sub>±0.013</sub> |     504.46<sub>±6.75</sub> |
| PHP (Naive) |  0.515<sub>±0.107</sub> |      17.23<sub>±0.54</sub> |
| PHP (JIT: tracing) |  0.161<sub>±0.015</sub> |      20.73<sub>±0.09</sub> |
| PHP (JIT: function) |  0.208<sub>±0.006</sub> |      20.57<sub>±0.75</sub> |
| Ruby (Naive) |  1.954<sub>±0.049</sub> |      13.71<sub>±0.07</sub> |
| Ruby (JIT) |  1.488<sub>±0.324</sub> |      14.12<sub>±0.05</sub> |
| Ruby (JRuby) |  3.616<sub>±0.289</sub> |     391.15<sub>±59.70</sub> |
| Ruby (TruffleRuby) |  0.389<sub>±0.059</sub> |     628.45<sub>±5.25</sub> |
| Ruby (TruffleRuby JVM) |  3.339<sub>±0.212</sub> |     737.83<sub>±79.70</sub> |
| Ruby (GraalVM) |  0.431<sub>±0.056</sub> |     632.44<sub>±8.94</sub> |
| Ruby (GraalVM JVM) |  3.295<sub>±0.262</sub> |     657.83<sub>±121.07</sub> |
| Rust |  0.042<sub>±0.001</sub> |       1.69<sub>±1.10</sub> |


### treap/Naive

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.210<sub>±0.064</sub> |       3.34<sub>±0.23</sub> |
| Go |  0.251<sub>±0.065</sub> |       7.68<sub>±4.04</sub> |
| Java (Naive) |  0.507<sub>±0.021</sub> |     142.69<sub>±15.94</sub> |
| Java (GraalVM: Naive) |  0.892<sub>±0.056</sub> |     207.57<sub>±119.52</sub> |
| Java (JVM) |  0.570<sub>±0.071</sub> |     140.86<sub>±9.68</sub> |
| Java (Native) |  2.756<sub>±0.137</sub> |       4.43<sub>±0.12</sub> |
| JavaScript (Node) |  0.844<sub>±0.023</sub> |      76.02<sub>±1.66</sub> |
| JavaScript (GraalVM Node) |  3.062<sub>±0.110</sub> |     819.66<sub>±9.25</sub> |
| PHP (Naive) |  3.496<sub>±0.290</sub> |      17.43<sub>±0.21</sub> |
| PHP (JIT: tracing) |  2.200<sub>±0.221</sub> |      20.88<sub>±0.35</sub> |
| PHP (JIT: function) |  2.172<sub>±0.252</sub> |      20.45<sub>±0.27</sub> |
| Python (CPython) |  8.411<sub>±0.476</sub> |       8.44<sub>±0.11</sub> |
| Python (PyPy) |  2.950<sub>±0.203</sub> |      74.68<sub>±4.79</sub> |
| Python (GraalVM) |  3.434<sub>±0.200</sub> |     887.73<sub>±23.34</sub> |
| Ruby (Naive) |  6.694<sub>±1.633</sub> |      13.82<sub>±0.07</sub> |
| Ruby (JIT) |  5.739<sub>±0.229</sub> |      14.52<sub>±0.05</sub> |
| Ruby (JRuby) |  6.923<sub>±0.901</sub> |     234.41<sub>±8.13</sub> |
| Ruby (TruffleRuby) |  1.734<sub>±0.114</sub> |     682.41<sub>±29.86</sub> |
| Ruby (TruffleRuby JVM) |  4.563<sub>±0.416</sub> |     797.21<sub>±248.94</sub> |
| Ruby (GraalVM) |  1.817<sub>±0.138</sub> |     694.50<sub>±22.33</sub> |
| Ruby (GraalVM JVM) |  4.580<sub>±0.338</sub> |     756.96<sub>±177.32</sub> |


### io/Load

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.094<sub>±0.001</sub> |       2.99<sub>±1.52</sub> |
| Go |  0.155<sub>±0.017</sub> |       2.68<sub>±0.00</sub> |
| Java (Naive) |  0.230<sub>±0.035</sub> |      76.51<sub>±11.27</sub> |
| Java (GraalVM: Naive) |  0.791<sub>±0.035</sub> |     178.46<sub>±13.27</sub> |
| JavaScript (Node) |  1.401<sub>±0.067</sub> |      63.81<sub>±2.10</sub> |
| JavaScript (GraalVM Node) |  4.310<sub>±0.595</sub> |     890.98<sub>±47.55</sub> |
| PHP (Naive) |  0.108<sub>±0.030</sub> |      17.41<sub>±0.22</sub> |
| PHP (JIT: tracing) |  0.103<sub>±0.002</sub> |      20.54<sub>±0.14</sub> |
| PHP (JIT: function) |  0.110<sub>±0.027</sub> |      20.48<sub>±0.11</sub> |
| Python (CPython) |  0.135<sub>±0.003</sub> |       7.29<sub>±0.35</sub> |
| Python (PyPy) |  0.116<sub>±0.050</sub> |      64.63<sub>±0.27</sub> |
| Python (GraalVM) |  3.221<sub>±0.405</sub> |     811.21<sub>±30.46</sub> |
| Ruby (Naive) |  0.254<sub>±0.006</sub> |      13.69<sub>±0.06</sub> |
| Ruby (JIT) |  0.303<sub>±0.055</sub> |      14.11<sub>±0.09</sub> |
| Ruby (JRuby) |  2.455<sub>±0.201</sub> |     191.89<sub>±6.48</sub> |
| Ruby (TruffleRuby) |  1.303<sub>±0.307</sub> |     697.43<sub>±35.10</sub> |
| Ruby (TruffleRuby JVM) |  4.965<sub>±0.356</sub> |     615.13<sub>±43.04</sub> |
| Ruby (GraalVM) |  1.269<sub>±0.298</sub> |     701.62<sub>±35.48</sub> |
| Ruby (GraalVM JVM) |  4.961<sub>±0.283</sub> |     615.21<sub>±21.80</sub> |
| Rust |  0.093<sub>±0.002</sub> |       1.69<sub>±0.19</sub> |


### io/NoLoad

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.002<sub>±0.000</sub> |       1.48<sub>±1.67</sub> |
| Go |  0.001<sub>±0.001</sub> |       2.77<sub>±0.09</sub> |
| Java (Naive) |  0.028<sub>±0.003</sub> |      34.52<sub>±0.16</sub> |
| Java (GraalVM: Naive) |  0.383<sub>±0.003</sub> |      61.88<sub>±2.95</sub> |
| JavaScript (Node) |  0.030<sub>±0.006</sub> |      35.49<sub>±2.00</sub> |
| JavaScript (GraalVM Node) |  0.249<sub>±0.013</sub> |     406.09<sub>±8.12</sub> |
| PHP (Naive) |  0.013<sub>±0.001</sub> |      17.36<sub>±0.31</sub> |
| PHP (JIT: tracing) |  0.013<sub>±0.002</sub> |      20.43<sub>±0.11</sub> |
| PHP (JIT: function) |  0.013<sub>±0.001</sub> |      20.55<sub>±0.37</sub> |
| Python (CPython) |  0.029<sub>±0.000</sub> |       7.29<sub>±0.37</sub> |
| Python (PyPy) |  0.028<sub>±0.004</sub> |      55.67<sub>±1.32</sub> |
| Python (GraalVM) |  0.256<sub>±0.028</sub> |     358.05<sub>±34.66</sub> |
| Ruby (Naive) |  0.069<sub>±0.005</sub> |      13.31<sub>±0.11</sub> |
| Ruby (JIT) |  0.260<sub>±0.053</sub> |      13.69<sub>±0.05</sub> |
| Ruby (JRuby) |  1.996<sub>±0.272</sub> |     182.72<sub>±6.40</sub> |
| Ruby (TruffleRuby) |  0.091<sub>±0.002</sub> |     220.25<sub>±5.30</sub> |
| Ruby (TruffleRuby JVM) |  2.729<sub>±0.282</sub> |     522.32<sub>±7.39</sub> |
| Ruby (GraalVM) |  0.097<sub>±0.007</sub> |     221.89<sub>±3.50</sub> |
| Ruby (GraalVM JVM) |  2.643<sub>±0.146</sub> |     519.15<sub>±11.37</sub> |
| Rust |  0.001<sub>±0.002</sub> |       1.68<sub>±1.04</sub> |


