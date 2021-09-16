### primes/Simple

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.386<sub>±0.056</sub> |       3.11<sub>±1.63</sub> |
| Java (Naive) |  0.481<sub>±0.003</sub> |      40.13<sub>±1.60</sub> |
| Java (GraalVM: Naive) |  0.840<sub>±0.003</sub> |     129.16<sub>±4.06</sub> |
| JavaScript (Node) |  0.533<sub>±0.102</sub> |      37.87<sub>±1.91</sub> |
| JavaScript (GraalVM Node) |  2.404<sub>±0.304</sub> |     806.79<sub>±35.01</sub> |
| PHP (Naive) |  2.983<sub>±0.144</sub> |      17.63<sub>±0.35</sub> |
| PHP (JIT: tracing) |  1.538<sub>±0.168</sub> |      20.51<sub>±0.24</sub> |
| PHP (JIT: function) |  1.832<sub>±0.127</sub> |      20.57<sub>±0.40</sub> |
| Ruby (Naive) | 11.296<sub>±0.597</sub> |      13.69<sub>±0.02</sub> |
| Ruby (JIT) |  7.606<sub>±0.417</sub> |      14.18<sub>±0.10</sub> |
| Ruby (JRuby) | 14.881<sub>±0.666</sub> |     354.82<sub>±21.53</sub> |
| Ruby (TruffleRuby) |  1.087<sub>±0.095</sub> |     670.01<sub>±7.38</sub> |
| Ruby (TruffleRuby JVM) |  4.807<sub>±0.507</sub> |     680.09<sub>±80.29</sub> |
| Ruby (GraalVM) |  1.030<sub>±0.169</sub> |     666.89<sub>±8.09</sub> |
| Ruby (GraalVM JVM) |  4.398<sub>±0.222</sub> |     694.18<sub>±73.28</sub> |
| Rust |  0.440<sub>±0.003</sub> |       1.73<sub>±0.07</sub> |


### primes/Atkin

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.221<sub>±0.130</sub> |      88.89<sub>±0.17</sub> |
| Java (Naive) |  0.283<sub>±0.058</sub> |     194.18<sub>±15.50</sub> |
| Java (GraalVM: Naive) |  0.698<sub>±0.082</sub> |     317.25<sub>±21.41</sub> |
| JavaScript (Node) |  0.390<sub>±0.048</sub> |     210.24<sub>±1.81</sub> |
| JavaScript (GraalVM Node) |  2.395<sub>±0.245</sub> |     986.04<sub>±25.28</sub> |
| PHP (Naive) |  1.777<sub>±0.092</sub> |     345.84<sub>±1.45</sub> |
| PHP (JIT: tracing) |  1.990<sub>±0.262</sub> |     348.09<sub>±0.17</sub> |
| PHP (JIT: function) |  1.351<sub>±0.295</sub> |     347.59<sub>±0.14</sub> |
| Python (CPython) |  5.375<sub>±0.354</sub> |     245.79<sub>±0.09</sub> |
| Python (PyPy) |  1.411<sub>±0.093</sub> |     316.81<sub>±0.48</sub> |
| Python (GraalVM) |  1.639<sub>±0.845</sub> |     865.79<sub>±62.83</sub> |
| Ruby (Naive) |  3.244<sub>±0.507</sub> |     160.57<sub>±0.05</sub> |
| Ruby (JIT) |  2.861<sub>±0.374</sub> |     161.16<sub>±0.11</sub> |
| Ruby (JRuby) |  4.573<sub>±0.923</sub> |     487.29<sub>±76.27</sub> |
| Ruby (TruffleRuby) |  1.830<sub>±0.127</sub> |     880.26<sub>±14.48</sub> |
| Ruby (TruffleRuby JVM) |  5.059<sub>±0.484</sub> |     905.62<sub>±141.63</sub> |
| Ruby (GraalVM) |  1.811<sub>±0.187</sub> |     873.68<sub>±12.45</sub> |
| Ruby (GraalVM JVM) |  4.972<sub>±0.496</sub> |     951.22<sub>±113.78</sub> |
| Rust |  0.206<sub>±0.004</sub> |      77.43<sub>±0.09</sub> |


### collatz/MaxSequence

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.075<sub>±0.001</sub> |       1.48<sub>±1.61</sub> |
| Java (Naive) |  0.145<sub>±0.024</sub> |      36.45<sub>±0.14</sub> |
| Java (GraalVM: Naive) |  0.500<sub>±0.061</sub> |      73.25<sub>±3.87</sub> |
| JavaScript (Node) |  0.982<sub>±0.048</sub> |      32.40<sub>±1.99</sub> |
| JavaScript (GraalVM Node) |  1.283<sub>±0.109</sub> |     470.00<sub>±10.52</sub> |
| PHP (Naive) |  1.042<sub>±0.534</sub> |      17.43<sub>±0.18</sub> |
| PHP (JIT: tracing) |  0.430<sub>±0.007</sub> |      20.49<sub>±0.39</sub> |
| PHP (JIT: function) |  0.575<sub>±0.012</sub> |      20.36<sub>±0.37</sub> |
| Ruby (Naive) |  3.222<sub>±0.090</sub> |      13.35<sub>±0.11</sub> |
| Ruby (JIT) |  0.815<sub>±0.046</sub> |      13.80<sub>±0.09</sub> |
| Ruby (JRuby) |  3.702<sub>±0.601</sub> |     286.40<sub>±51.64</sub> |
| Ruby (TruffleRuby) |  0.554<sub>±0.025</sub> |     439.63<sub>±4.49</sub> |
| Ruby (TruffleRuby JVM) |  3.057<sub>±0.119</sub> |     579.71<sub>±19.39</sub> |
| Ruby (GraalVM) |  0.580<sub>±0.237</sub> |     439.70<sub>±2.21</sub> |
| Ruby (GraalVM JVM) |  3.099<sub>±0.049</sub> |     574.23<sub>±41.53</sub> |
| Rust |  0.076<sub>±0.001</sub> |       1.68<sub>±0.18</sub> |


### mandelbrot/Simple

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.042<sub>±0.001</sub> |       1.48<sub>±1.56</sub> |
| Java (Naive) |  0.083<sub>±0.011</sub> |      38.01<sub>±0.45</sub> |
| Java (GraalVM: Naive) |  0.435<sub>±0.032</sub> |      77.28<sub>±4.43</sub> |
| JavaScript (Node) |  0.097<sub>±0.005</sub> |      39.60<sub>±0.41</sub> |
| JavaScript (GraalVM Node) |  0.624<sub>±0.094</sub> |     503.75<sub>±5.95</sub> |
| PHP (Naive) |  0.513<sub>±0.038</sub> |      17.41<sub>±0.28</sub> |
| PHP (JIT: tracing) |  0.159<sub>±0.002</sub> |      20.83<sub>±0.23</sub> |
| PHP (JIT: function) |  0.208<sub>±0.001</sub> |      20.77<sub>±0.18</sub> |
| Ruby (Naive) |  2.028<sub>±0.638</sub> |      13.73<sub>±0.06</sub> |
| Ruby (JIT) |  1.493<sub>±0.485</sub> |      14.13<sub>±0.03</sub> |
| Ruby (JRuby) |  4.099<sub>±0.266</sub> |     346.69<sub>±31.29</sub> |
| Ruby (TruffleRuby) |  0.371<sub>±0.077</sub> |     629.04<sub>±5.81</sub> |
| Ruby (TruffleRuby JVM) |  3.407<sub>±0.119</sub> |     620.59<sub>±24.71</sub> |
| Ruby (GraalVM) |  0.481<sub>±0.048</sub> |     633.09<sub>±5.74</sub> |
| Ruby (GraalVM JVM) |  3.317<sub>±0.326</sub> |     621.96<sub>±93.00</sub> |
| Rust |  0.042<sub>±0.000</sub> |       1.73<sub>±0.09</sub> |


### treap/Naive

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.211<sub>±0.003</sub> |       3.31<sub>±0.21</sub> |
| Go |  0.287<sub>±0.037</sub> |       7.80<sub>±2.04</sub> |
| JavaScript (Node) |  0.954<sub>±0.117</sub> |      78.12<sub>±2.15</sub> |
| JavaScript (GraalVM Node) |  3.428<sub>±0.287</sub> |     807.44<sub>±13.41</sub> |
| PHP (Naive) |  3.771<sub>±0.360</sub> |      17.52<sub>±0.25</sub> |
| PHP (JIT: tracing) |  2.031<sub>±0.092</sub> |      20.94<sub>±0.23</sub> |
| PHP (JIT: function) |  2.123<sub>±0.201</sub> |      20.66<sub>±0.34</sub> |
| Python (CPython) |  8.500<sub>±0.384</sub> |       8.36<sub>±0.08</sub> |
| Python (PyPy) |  2.916<sub>±0.123</sub> |      73.83<sub>±1.51</sub> |
| Python (GraalVM) |  3.510<sub>±0.460</sub> |     873.18<sub>±11.32</sub> |
| Ruby (Naive) |  6.544<sub>±0.439</sub> |      13.83<sub>±0.15</sub> |
| Ruby (JIT) |  5.515<sub>±1.869</sub> |      14.56<sub>±0.12</sub> |
| Ruby (JRuby) |  6.738<sub>±0.796</sub> |     239.97<sub>±20.57</sub> |
| Ruby (TruffleRuby) |  2.079<sub>±0.421</sub> |     699.73<sub>±22.34</sub> |
| Ruby (TruffleRuby JVM) |  4.540<sub>±0.940</sub> |     813.88<sub>±204.05</sub> |
| Ruby (GraalVM) |  1.814<sub>±0.061</sub> |     695.68<sub>±23.62</sub> |
| Ruby (GraalVM JVM) |  4.784<sub>±0.172</sub> |     844.82<sub>±147.75</sub> |


### io/Load

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.095<sub>±0.004</sub> |       1.48<sub>±1.62</sub> |
| Go |  0.156<sub>±0.001</sub> |       2.68<sub>±0.14</sub> |
| Java (Naive) |  0.283<sub>±0.056</sub> |      76.07<sub>±2.26</sub> |
| Java (GraalVM: Naive) |  0.838<sub>±0.066</sub> |     173.96<sub>±13.46</sub> |
| JavaScript (Node) |  1.366<sub>±0.041</sub> |      65.23<sub>±1.45</sub> |
| JavaScript (GraalVM Node) |  4.436<sub>±0.282</sub> |     901.63<sub>±27.07</sub> |
| PHP (Naive) |  0.108<sub>±0.002</sub> |      17.48<sub>±0.20</sub> |
| PHP (JIT: tracing) |  0.102<sub>±0.029</sub> |      20.43<sub>±0.09</sub> |
| PHP (JIT: function) |  0.104<sub>±0.001</sub> |      20.53<sub>±0.10</sub> |
| Python (CPython) |  0.134<sub>±0.003</sub> |       7.20<sub>±0.47</sub> |
| Python (PyPy) |  0.118<sub>±0.109</sub> |      64.39<sub>±0.45</sub> |
| Python (GraalVM) |  3.393<sub>±0.246</sub> |     798.34<sub>±14.82</sub> |
| Ruby (Naive) |  0.266<sub>±0.053</sub> |      13.73<sub>±0.10</sub> |
| Ruby (JIT) |  0.506<sub>±0.204</sub> |      14.04<sub>±0.20</sub> |
| Ruby (JRuby) |  2.686<sub>±0.269</sub> |     183.79<sub>±11.21</sub> |
| Ruby (TruffleRuby) |  1.178<sub>±0.109</sub> |     686.06<sub>±24.68</sub> |
| Ruby (TruffleRuby JVM) |  5.069<sub>±0.417</sub> |     636.72<sub>±35.08</sub> |
| Ruby (GraalVM) |  1.205<sub>±0.227</sub> |     668.86<sub>±54.41</sub> |
| Ruby (GraalVM JVM) |  4.855<sub>±0.211</sub> |     602.97<sub>±39.16</sub> |
| Rust |  0.094<sub>±0.032</sub> |       1.73<sub>±0.07</sub> |


### io/NoLoad

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.001<sub>±0.000</sub> |       1.48<sub>±1.61</sub> |
| Go |  0.001<sub>±0.000</sub> |       2.68<sub>±2.00</sub> |
| Java (Naive) |  0.027<sub>±0.001</sub> |      34.63<sub>±0.30</sub> |
| Java (GraalVM: Naive) |  0.381<sub>±0.004</sub> |      61.98<sub>±5.30</sub> |
| JavaScript (Node) |  0.032<sub>±0.069</sub> |      33.98<sub>±1.89</sub> |
| JavaScript (GraalVM Node) |  0.275<sub>±0.017</sub> |     393.98<sub>±10.71</sub> |
| PHP (Naive) |  0.012<sub>±0.001</sub> |      17.44<sub>±0.39</sub> |
| PHP (JIT: tracing) |  0.012<sub>±0.002</sub> |      20.48<sub>±0.28</sub> |
| PHP (JIT: function) |  0.013<sub>±0.001</sub> |      20.36<sub>±0.16</sub> |
| Python (CPython) |  0.029<sub>±0.002</sub> |       7.22<sub>±0.59</sub> |
| Python (PyPy) |  0.029<sub>±0.074</sub> |      55.57<sub>±0.25</sub> |
| Python (GraalVM) |  0.235<sub>±0.046</sub> |     325.78<sub>±11.57</sub> |
| Ruby (Naive) |  0.067<sub>±0.002</sub> |      13.32<sub>±0.04</sub> |
| Ruby (JIT) |  0.268<sub>±0.021</sub> |      13.66<sub>±0.05</sub> |
| Ruby (JRuby) |  2.002<sub>±0.042</sub> |     181.36<sub>±8.71</sub> |
| Ruby (TruffleRuby) |  0.095<sub>±0.021</sub> |     215.81<sub>±3.91</sub> |
| Ruby (TruffleRuby JVM) |  2.576<sub>±0.033</sub> |     512.95<sub>±4.43</sub> |
| Ruby (GraalVM) |  0.094<sub>±0.005</sub> |     215.74<sub>±1.64</sub> |
| Ruby (GraalVM JVM) |  2.794<sub>±0.250</sub> |     507.86<sub>±8.27</sub> |
| Rust |  0.001<sub>±0.002</sub> |       1.70<sub>±1.12</sub> |


