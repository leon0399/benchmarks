### primes/Simple

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.384<sub>±0.056</sub> |       3.06<sub>±1.59</sub> |
| Java (Naive) |  0.481<sub>±0.023</sub> |      39.99<sub>±1.68</sub> |
| Java (GraalVM: Naive) |  0.844<sub>±0.003</sub> |     130.57<sub>±9.34</sub> |
| JavaScript (Node) |  0.555<sub>±0.033</sub> |      39.12<sub>±1.93</sub> |
| JavaScript (GraalVM Node) |  2.170<sub>±0.075</sub> |     783.06<sub>±32.35</sub> |
| PHP (Naive) |  3.015<sub>±0.141</sub> |      17.33<sub>±0.32</sub> |
| PHP (JIT: tracing) |  1.491<sub>±0.439</sub> |      20.68<sub>±0.27</sub> |
| PHP (JIT: function) |  1.710<sub>±0.397</sub> |      20.36<sub>±0.31</sub> |
| Ruby (Naive) | 11.058<sub>±0.746</sub> |      13.69<sub>±0.07</sub> |
| Ruby (JIT) |  7.733<sub>±0.323</sub> |      14.12<sub>±0.17</sub> |
| Ruby (JRuby) | 14.500<sub>±2.628</sub> |     342.23<sub>±42.39</sub> |
| Ruby (TruffleRuby) |  0.985<sub>±0.060</sub> |     669.48<sub>±2.39</sub> |
| Ruby (TruffleRuby JVM) |  4.513<sub>±0.673</sub> |     707.20<sub>±93.67</sub> |
| Ruby (GraalVM) |  0.988<sub>±0.028</sub> |     675.85<sub>±14.69</sub> |
| Ruby (GraalVM JVM) |  4.538<sub>±0.137</sub> |     729.22<sub>±50.20</sub> |
| Rust |  0.440<sub>±0.002</sub> |       1.79<sub>±0.13</sub> |


### primes/Atkin

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.225<sub>±0.089</sub> |      89.01<sub>±0.16</sub> |
| Java (Naive) |  0.261<sub>±0.084</sub> |     176.47<sub>±20.96</sub> |
| Java (GraalVM: Naive) |  0.707<sub>±0.028</sub> |     304.07<sub>±19.09</sub> |
| JavaScript (Node) |  0.388<sub>±0.012</sub> |     209.95<sub>±2.08</sub> |
| JavaScript (GraalVM Node) |  2.303<sub>±0.218</sub> |     995.04<sub>±21.93</sub> |
| PHP (Naive) |  1.733<sub>±0.060</sub> |     347.02<sub>±0.24</sub> |
| PHP (JIT: tracing) |  1.880<sub>±0.083</sub> |     350.66<sub>±0.16</sub> |
| PHP (JIT: function) |  1.306<sub>±0.054</sub> |     350.40<sub>±0.35</sub> |
| Python (CPython) |  5.583<sub>±0.480</sub> |     245.78<sub>±0.09</sub> |
| Python (PyPy) |  1.296<sub>±0.146</sub> |     317.10<sub>±0.13</sub> |
| Python (GraalVM) |  1.997<sub>±0.455</sub> |     930.68<sub>±15.55</sub> |
| Ruby (Naive) |  3.136<sub>±0.094</sub> |     160.62<sub>±0.07</sub> |
| Ruby (JIT) |  3.009<sub>±0.182</sub> |     161.14<sub>±0.16</sub> |
| Ruby (JRuby) |  4.269<sub>±0.210</sub> |     478.84<sub>±50.14</sub> |
| Ruby (TruffleRuby) |  1.764<sub>±0.114</sub> |     875.30<sub>±25.01</sub> |
| Ruby (TruffleRuby JVM) |  4.636<sub>±1.718</sub> |     972.62<sub>±40.54</sub> |
| Ruby (GraalVM) |  1.769<sub>±0.042</sub> |     875.77<sub>±17.94</sub> |
| Ruby (GraalVM JVM) |  4.670<sub>±0.469</sub> |     913.06<sub>±102.09</sub> |
| Rust |  0.205<sub>±0.006</sub> |      77.47<sub>±0.07</sub> |


### collatz/MaxSequence

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.075<sub>±0.001</sub> |       2.96<sub>±1.49</sub> |
| Java (Naive) |  0.145<sub>±0.008</sub> |      36.25<sub>±0.13</sub> |
| Java (GraalVM: Naive) |  0.499<sub>±0.030</sub> |      77.14<sub>±3.68</sub> |
| JavaScript (Node) |  0.988<sub>±0.036</sub> |      33.78<sub>±2.00</sub> |
| JavaScript (GraalVM Node) |  1.264<sub>±0.045</sub> |     471.27<sub>±10.50</sub> |
| PHP (Naive) |  1.042<sub>±0.115</sub> |      17.53<sub>±0.04</sub> |
| PHP (JIT: tracing) |  0.426<sub>±0.002</sub> |      20.52<sub>±0.32</sub> |
| PHP (JIT: function) |  0.572<sub>±0.011</sub> |      20.46<sub>±0.36</sub> |
| Ruby (Naive) |  3.103<sub>±0.107</sub> |      13.33<sub>±0.06</sub> |
| Ruby (JIT) |  0.828<sub>±0.068</sub> |      13.73<sub>±0.13</sub> |
| Ruby (JRuby) |  3.208<sub>±0.467</sub> |     304.26<sub>±34.05</sub> |
| Ruby (TruffleRuby) |  0.555<sub>±0.010</sub> |     439.89<sub>±0.66</sub> |
| Ruby (TruffleRuby JVM) |  3.170<sub>±0.220</sub> |     599.91<sub>±46.08</sub> |
| Ruby (GraalVM) |  0.569<sub>±0.121</sub> |     436.27<sub>±5.00</sub> |
| Ruby (GraalVM JVM) |  3.120<sub>±0.234</sub> |     585.25<sub>±54.73</sub> |
| Rust |  0.075<sub>±0.001</sub> |       1.73<sub>±0.07</sub> |


### mandelbrot/Simple

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.043<sub>±0.053</sub> |       3.11<sub>±1.62</sub> |
| Java (Naive) |  0.083<sub>±0.001</sub> |      37.85<sub>±0.49</sub> |
| Java (GraalVM: Naive) |  0.437<sub>±0.061</sub> |      76.29<sub>±6.11</sub> |
| JavaScript (Node) |  0.089<sub>±0.001</sub> |      37.11<sub>±1.79</sub> |
| JavaScript (GraalVM Node) |  0.461<sub>±0.073</sub> |     496.93<sub>±8.73</sub> |
| PHP (Naive) |  0.511<sub>±0.036</sub> |      17.35<sub>±0.40</sub> |
| PHP (JIT: tracing) |  0.160<sub>±0.007</sub> |      20.52<sub>±0.29</sub> |
| PHP (JIT: function) |  0.210<sub>±0.036</sub> |      20.62<sub>±0.22</sub> |
| Ruby (Naive) |  1.959<sub>±0.275</sub> |      13.61<sub>±0.12</sub> |
| Ruby (JIT) |  1.584<sub>±0.063</sub> |      14.18<sub>±0.09</sub> |
| Ruby (JRuby) |  4.107<sub>±0.519</sub> |     343.66<sub>±47.81</sub> |
| Ruby (TruffleRuby) |  0.441<sub>±0.088</sub> |     628.04<sub>±9.39</sub> |
| Ruby (TruffleRuby JVM) |  3.453<sub>±0.267</sub> |     696.45<sub>±116.99</sub> |
| Ruby (GraalVM) |  0.365<sub>±0.035</sub> |     628.17<sub>±7.84</sub> |
| Ruby (GraalVM JVM) |  3.366<sub>±0.181</sub> |     626.62<sub>±53.97</sub> |
| Rust |  0.041<sub>±0.001</sub> |       1.70<sub>±0.06</sub> |


### treap/Naive

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.210<sub>±0.002</sub> |       3.14<sub>±0.26</sub> |
| Go |  0.258<sub>±0.059</sub> |       7.71<sub>±2.08</sub> |
| Java (Naive) |  0.521<sub>±0.050</sub> |     139.61<sub>±0.95</sub> |
| Java (GraalVM: Naive) |  0.896<sub>±0.025</sub> |     197.68<sub>±7.99</sub> |
| JavaScript (Node) |  0.849<sub>±0.010</sub> |      75.61<sub>±2.51</sub> |
| JavaScript (GraalVM Node) |  3.134<sub>±0.135</sub> |     816.50<sub>±9.66</sub> |
| Kotlin (JVM) |  0.536<sub>±0.032</sub> |     140.61<sub>±5.98</sub> |
| Kotlin (Native) |  2.735<sub>±0.581</sub> |       4.50<sub>±0.08</sub> |
| PHP (Naive) |  3.273<sub>±0.612</sub> |      17.62<sub>±0.26</sub> |
| PHP (JIT: tracing) |  2.028<sub>±0.243</sub> |      20.75<sub>±0.23</sub> |
| PHP (JIT: function) |  2.115<sub>±0.073</sub> |      20.58<sub>±0.23</sub> |
| Python (CPython) |  8.226<sub>±0.289</sub> |       8.47<sub>±0.14</sub> |
| Python (PyPy) |  3.036<sub>±0.247</sub> |      73.79<sub>±1.02</sub> |
| Python (GraalVM) |  3.726<sub>±0.304</sub> |     875.56<sub>±12.05</sub> |
| Ruby (Naive) |  6.830<sub>±0.889</sub> |      13.81<sub>±0.12</sub> |
| Ruby (JIT) |  5.618<sub>±0.810</sub> |      14.52<sub>±0.11</sub> |
| Ruby (JRuby) |  6.444<sub>±0.548</sub> |     233.72<sub>±7.85</sub> |
| Ruby (TruffleRuby) |  1.910<sub>±0.221</sub> |     700.93<sub>±5.78</sub> |
| Ruby (TruffleRuby JVM) |  4.520<sub>±0.237</sub> |     896.86<sub>±174.50</sub> |
| Ruby (GraalVM) |  1.877<sub>±0.126</sub> |     695.57<sub>±16.42</sub> |
| Ruby (GraalVM JVM) |  4.654<sub>±0.310</sub> |     921.73<sub>±162.07</sub> |


### recursion/Tak

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.054<sub>±0.000</sub> |       1.48<sub>±1.70</sub> |
| PHP (Naive) |  0.835<sub>±0.005</sub> |      17.41<sub>±0.45</sub> |
| PHP (JIT: tracing) |  0.387<sub>±0.069</sub> |      20.43<sub>±0.28</sub> |
| PHP (JIT: function) |  0.420<sub>±0.042</sub> |      20.46<sub>±0.21</sub> |
| Python (CPython) |  2.555<sub>±0.088</sub> |       7.26<sub>±0.44</sub> |
| Python (PyPy) |  0.702<sub>±0.013</sub> |      63.31<sub>±0.21</sub> |
| Python (GraalVM) |  1.161<sub>±0.223</sub> |     725.02<sub>±21.05</sub> |
| Ruby (Naive) |  1.341<sub>±0.098</sub> |      13.30<sub>±0.06</sub> |
| Ruby (JIT) |  0.755<sub>±0.155</sub> |      13.71<sub>±0.13</sub> |
| Ruby (JRuby) |  2.520<sub>±0.183</sub> |     170.64<sub>±11.36</sub> |
| Ruby (TruffleRuby) |  0.841<sub>±0.099</sub> |     583.86<sub>±6.06</sub> |
| Ruby (TruffleRuby JVM) |  3.242<sub>±0.418</sub> |     816.89<sub>±58.79</sub> |
| Ruby (GraalVM) |  0.845<sub>±0.118</sub> |     583.90<sub>±8.13</sub> |
| Ruby (GraalVM JVM) |  3.212<sub>±0.303</sub> |     820.28<sub>±79.93</sub> |


### io/Load

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.095<sub>±0.012</sub> |       3.07<sub>±1.60</sub> |
| Go |  0.161<sub>±0.049</sub> |       2.68<sub>±0.14</sub> |
| Java (Naive) |  0.234<sub>±0.057</sub> |      76.87<sub>±11.57</sub> |
| Java (GraalVM: Naive) |  0.842<sub>±0.294</sub> |     171.75<sub>±25.72</sub> |
| JavaScript (Node) |  1.373<sub>±0.187</sub> |      65.71<sub>±2.26</sub> |
| JavaScript (GraalVM Node) |  4.312<sub>±0.561</sub> |     872.07<sub>±31.13</sub> |
| PHP (Naive) |  0.108<sub>±0.001</sub> |      17.44<sub>±0.37</sub> |
| PHP (JIT: tracing) |  0.103<sub>±0.003</sub> |      20.59<sub>±0.17</sub> |
| PHP (JIT: function) |  0.103<sub>±0.001</sub> |      20.40<sub>±0.26</sub> |
| Python (CPython) |  0.137<sub>±0.004</sub> |       7.32<sub>±0.39</sub> |
| Python (PyPy) |  0.121<sub>±0.015</sub> |      64.34<sub>±0.25</sub> |
| Python (GraalVM) |  3.196<sub>±0.202</sub> |     815.60<sub>±24.44</sub> |
| Ruby (Naive) |  0.314<sub>±0.063</sub> |      13.68<sub>±0.08</sub> |
| Ruby (JIT) |  0.300<sub>±0.049</sub> |      14.05<sub>±0.13</sub> |
| Ruby (JRuby) |  2.445<sub>±0.036</sub> |     189.11<sub>±11.25</sub> |
| Ruby (TruffleRuby) |  1.322<sub>±0.167</sub> |     716.15<sub>±50.91</sub> |
| Ruby (TruffleRuby JVM) |  5.096<sub>±0.378</sub> |     613.61<sub>±22.82</sub> |
| Ruby (GraalVM) |  1.240<sub>±0.296</sub> |     696.13<sub>±29.92</sub> |
| Ruby (GraalVM JVM) |  4.818<sub>±0.256</sub> |     600.41<sub>±25.55</sub> |
| Rust |  0.092<sub>±0.026</sub> |       1.74<sub>±0.12</sub> |


### io/NoLoad

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.001<sub>±0.000</sub> |       1.48<sub>±0.06</sub> |
| Go |  0.001<sub>±0.000</sub> |       2.68<sub>±0.15</sub> |
| Java (Naive) |  0.028<sub>±0.001</sub> |      34.46<sub>±0.16</sub> |
| Java (GraalVM: Naive) |  0.383<sub>±0.009</sub> |      63.26<sub>±2.15</sub> |
| JavaScript (Node) |  0.031<sub>±0.001</sub> |      35.39<sub>±2.00</sub> |
| JavaScript (GraalVM Node) |  0.271<sub>±0.020</sub> |     388.40<sub>±18.27</sub> |
| PHP (Naive) |  0.013<sub>±0.002</sub> |      17.16<sub>±0.32</sub> |
| PHP (JIT: tracing) |  0.011<sub>±0.003</sub> |      20.62<sub>±0.24</sub> |
| PHP (JIT: function) |  0.013<sub>±0.003</sub> |      20.27<sub>±0.42</sub> |
| Python (CPython) |  0.030<sub>±0.001</sub> |       7.15<sub>±0.28</sub> |
| Python (PyPy) |  0.030<sub>±0.002</sub> |      55.66<sub>±0.05</sub> |
| Python (GraalVM) |  0.261<sub>±0.029</sub> |     323.50<sub>±30.88</sub> |
| Ruby (Naive) |  0.067<sub>±0.023</sub> |      13.34<sub>±0.07</sub> |
| Ruby (JIT) |  0.267<sub>±0.074</sub> |      13.65<sub>±0.05</sub> |
| Ruby (JRuby) |  1.899<sub>±0.059</sub> |     180.50<sub>±5.84</sub> |
| Ruby (TruffleRuby) |  0.092<sub>±0.052</sub> |     219.50<sub>±3.98</sub> |
| Ruby (TruffleRuby JVM) |  2.512<sub>±0.040</sub> |     524.18<sub>±14.36</sub> |
| Ruby (GraalVM) |  0.092<sub>±0.035</sub> |     224.01<sub>±7.88</sub> |
| Ruby (GraalVM JVM) |  2.534<sub>±0.275</sub> |     524.25<sub>±13.12</sub> |
| Rust |  0.001<sub>±0.001</sub> |       0.64<sub>±1.09</sub> |


