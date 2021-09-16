### primes/Simple

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.345<sub>±0.045</sub> |       3.03<sub>±1.62</sub> |
| Java (Naive) |  0.381<sub>±0.105</sub> |      39.81<sub>±1.72</sub> |
| Java (GraalVM: Naive) |  0.732<sub>±0.089</sub> |     129.81<sub>±10.88</sub> |
| JavaScript (Node) |  0.422<sub>±0.086</sub> |      38.89<sub>±2.40</sub> |
| JavaScript (GraalVM Node) |  1.942<sub>±0.284</sub> |     783.70<sub>±51.04</sub> |
| PHP (Naive) |  2.411<sub>±0.077</sub> |      17.36<sub>±0.85</sub> |
| PHP (JIT: tracing) |  1.247<sub>±0.470</sub> |      20.40<sub>±0.42</sub> |
| PHP (JIT: function) |  1.404<sub>±0.101</sub> |      20.36<sub>±0.41</sub> |
| Ruby (Naive) |  8.656<sub>±0.189</sub> |      13.67<sub>±0.17</sub> |
| Ruby (JIT) |  5.943<sub>±7.313</sub> |      14.15<sub>±0.12</sub> |
| Ruby (JRuby) | 11.178<sub>±0.835</sub> |     397.46<sub>±224.66</sub> |
| Ruby (TruffleRuby) |  0.779<sub>±0.266</sub> |     669.06<sub>±17.68</sub> |
| Ruby (TruffleRuby JVM) |  3.633<sub>±0.352</sub> |     718.97<sub>±232.25</sub> |
| Ruby (GraalVM) |  0.786<sub>±0.070</sub> |     668.66<sub>±15.90</sub> |
| Ruby (GraalVM JVM) |  3.660<sub>±0.137</sub> |     758.98<sub>±143.46</sub> |
| Rust |  0.339<sub>±0.041</sub> |       1.73<sub>±0.13</sub> |


### primes/Atkin

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.193<sub>±0.045</sub> |      88.96<sub>±0.82</sub> |
| Java (Naive) |  0.255<sub>±0.113</sub> |     193.72<sub>±18.24</sub> |
| Java (GraalVM: Naive) |  0.654<sub>±0.143</sub> |     313.44<sub>±20.34</sub> |
| JavaScript (Node) |  0.358<sub>±0.083</sub> |     208.95<sub>±1.63</sub> |
| JavaScript (GraalVM Node) |  1.951<sub>±0.306</sub> |     987.49<sub>±84.77</sub> |
| PHP (Naive) |  1.599<sub>±0.214</sub> |     350.08<sub>±0.37</sub> |
| PHP (JIT: tracing) |  1.687<sub>±0.246</sub> |     353.66<sub>±0.34</sub> |
| PHP (JIT: function) |  1.124<sub>±0.107</sub> |     353.30<sub>±0.38</sub> |
| Ruby (Naive) |  2.458<sub>±0.167</sub> |     160.55<sub>±0.13</sub> |
| Ruby (JIT) |  2.273<sub>±0.132</sub> |     161.16<sub>±2.07</sub> |
| Ruby (JRuby) |  3.509<sub>±0.476</sub> |     522.79<sub>±88.20</sub> |
| Ruby (TruffleRuby) |  1.404<sub>±0.097</sub> |     879.03<sub>±26.09</sub> |
| Ruby (TruffleRuby JVM) |  3.799<sub>±0.530</sub> |     926.65<sub>±122.15</sub> |
| Ruby (GraalVM) |  1.418<sub>±0.107</sub> |     878.56<sub>±28.20</sub> |
| Ruby (GraalVM JVM) |  3.787<sub>±0.176</sub> |     901.14<sub>±156.63</sub> |
| Rust |  0.170<sub>±0.065</sub> |      77.46<sub>±0.49</sub> |


### collatz/MaxSequence

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.059<sub>±0.059</sub> |       3.03<sub>±1.62</sub> |
| Java (Naive) |  0.116<sub>±0.070</sub> |      36.27<sub>±0.39</sub> |
| Java (GraalVM: Naive) |  0.458<sub>±0.091</sub> |      74.89<sub>±4.11</sub> |
| JavaScript (Node) |  0.770<sub>±0.059</sub> |      32.00<sub>±1.98</sub> |
| JavaScript (GraalVM Node) |  1.009<sub>±0.068</sub> |     467.64<sub>±22.39</sub> |
| PHP (Naive) |  0.826<sub>±0.662</sub> |      17.39<sub>±0.37</sub> |
| PHP (JIT: tracing) |  0.339<sub>±0.032</sub> |      20.62<sub>±0.37</sub> |
| PHP (JIT: function) |  0.455<sub>±0.064</sub> |      20.37<sub>±0.39</sub> |
| Rust |  0.059<sub>±0.063</sub> |       1.71<sub>±1.13</sub> |


### mandelbrot/Simple

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.033<sub>±0.085</sub> |       3.09<sub>±1.68</sub> |
| Java (Naive) |  0.067<sub>±0.075</sub> |      37.40<sub>±0.50</sub> |
| Java (GraalVM: Naive) |  0.410<sub>±0.068</sub> |      75.54<sub>±4.38</sub> |
| JavaScript (Node) |  0.072<sub>±0.038</sub> |      38.91<sub>±8.07</sub> |
| JavaScript (GraalVM Node) |  0.397<sub>±0.073</sub> |     502.88<sub>±11.16</sub> |
| PHP (Naive) |  0.408<sub>±0.056</sub> |      17.47<sub>±0.78</sub> |
| PHP (JIT: tracing) |  0.124<sub>±0.025</sub> |      20.66<sub>±0.33</sub> |
| PHP (JIT: function) |  0.164<sub>±0.062</sub> |      20.55<sub>±0.46</sub> |
| Ruby (Naive) |  1.591<sub>±0.962</sub> |      13.68<sub>±0.16</sub> |
| Ruby (JIT) |  1.247<sub>±0.134</sub> |      14.15<sub>±0.11</sub> |
| Ruby (JRuby) |  3.189<sub>±0.506</sub> |     372.73<sub>±77.13</sub> |
| Ruby (TruffleRuby) |  0.311<sub>±0.111</sub> |     627.56<sub>±11.52</sub> |
| Ruby (TruffleRuby JVM) |  2.763<sub>±0.266</sub> |     622.38<sub>±181.95</sub> |
| Ruby (GraalVM) |  0.309<sub>±0.100</sub> |     627.12<sub>±11.34</sub> |
| Ruby (GraalVM JVM) |  2.740<sub>±0.445</sub> |     622.96<sub>±150.12</sub> |
| Rust |  0.033<sub>±0.017</sub> |       1.73<sub>±0.11</sub> |


### io/Load

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.074<sub>±0.069</sub> |       3.03<sub>±1.62</sub> |
| Go |  0.121<sub>±0.061</sub> |       2.69<sub>±2.13</sub> |
| Java (Naive) |  0.186<sub>±0.053</sub> |      76.69<sub>±11.28</sub> |
| Java (GraalVM: Naive) |  0.695<sub>±0.151</sub> |     172.15<sub>±16.04</sub> |
| JavaScript (Node) |  1.129<sub>±0.071</sub> |      65.39<sub>±8.39</sub> |
| JavaScript (GraalVM Node) |  3.671<sub>±0.475</sub> |     864.52<sub>±71.83</sub> |
| PHP (Naive) |  0.086<sub>±0.059</sub> |      17.34<sub>±0.39</sub> |
| PHP (JIT: tracing) |  0.081<sub>±0.035</sub> |      20.53<sub>±0.40</sub> |
| PHP (JIT: function) |  0.081<sub>±0.062</sub> |      20.47<sub>±0.69</sub> |
| Python (Python 3) |  0.107<sub>±0.026</sub> |       7.27<sub>±0.51</sub> |
| Python (GraalVM Python) |  2.612<sub>±0.582</sub> |     803.91<sub>±28.58</sub> |
| Ruby (Naive) |  0.206<sub>±0.102</sub> |      13.71<sub>±0.17</sub> |
| Ruby (JIT) |  0.241<sub>±0.305</sub> |      14.08<sub>±0.17</sub> |
| Ruby (JRuby) |  1.932<sub>±0.180</sub> |     194.70<sub>±13.66</sub> |
| Ruby (TruffleRuby) |  1.004<sub>±0.112</sub> |     690.34<sub>±39.28</sub> |
| Ruby (TruffleRuby JVM) |  3.871<sub>±0.280</sub> |     631.49<sub>±93.33</sub> |
| Ruby (GraalVM) |  1.024<sub>±0.149</sub> |     693.28<sub>±46.84</sub> |
| Ruby (GraalVM JVM) |  3.905<sub>±1.400</sub> |     630.41<sub>±57.56</sub> |
| Rust |  0.073<sub>±0.047</sub> |       1.73<sub>±0.13</sub> |


### io/NoLoad

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.001<sub>±0.001</sub> |       1.47<sub>±1.73</sub> |
| Go |  0.001<sub>±0.050</sub> |       2.68<sub>±2.14</sub> |
| Java (Naive) |  0.023<sub>±0.120</sub> |      34.49<sub>±0.26</sub> |
| Java (GraalVM: Naive) |  0.368<sub>±0.005</sub> |      62.26<sub>±3.06</sub> |
| JavaScript (Node) |  0.025<sub>±0.058</sub> |      35.29<sub>±2.00</sub> |
| JavaScript (GraalVM Node) |  0.222<sub>±0.045</sub> |     402.12<sub>±40.43</sub> |
| PHP (Naive) |  0.010<sub>±0.080</sub> |      17.26<sub>±0.42</sub> |
| PHP (JIT: tracing) |  0.010<sub>±0.005</sub> |      20.51<sub>±0.45</sub> |
| PHP (JIT: function) |  0.010<sub>±0.051</sub> |      20.40<sub>±0.76</sub> |
| Python (Python 3) |  0.023<sub>±0.074</sub> |       6.93<sub>±0.42</sub> |
| Python (GraalVM Python) |  0.183<sub>±0.065</sub> |     328.00<sub>±44.67</sub> |
| Ruby (Naive) |  0.054<sub>±0.067</sub> |      13.30<sub>±0.14</sub> |
| Ruby (JIT) |  0.212<sub>±0.086</sub> |      13.69<sub>±0.12</sub> |
| Ruby (JRuby) |  1.567<sub>±0.300</sub> |     184.56<sub>±26.57</sub> |
| Ruby (TruffleRuby) |  0.083<sub>±0.090</sub> |     220.98<sub>±11.44</sub> |
| Ruby (TruffleRuby JVM) |  2.133<sub>±0.635</sub> |     533.62<sub>±20.84</sub> |
| Ruby (GraalVM) |  0.080<sub>±0.061</sub> |     222.79<sub>±14.18</sub> |
| Ruby (GraalVM JVM) |  2.175<sub>±0.558</sub> |     534.43<sub>±19.26</sub> |
| Rust |  0.001<sub>±0.001</sub> |       1.66<sub>±1.66</sub> |


### treap/Naive

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| JavaScript (Node) |  0.719<sub>±0.097</sub> |      76.74<sub>±6.98</sub> |
| JavaScript (GraalVM Node) |  2.708<sub>±0.245</sub> |     818.54<sub>±37.88</sub> |
| PHP (Naive) |  2.640<sub>±0.254</sub> |      17.43<sub>±0.43</sub> |
| PHP (JIT: tracing) |  1.598<sub>±0.123</sub> |      20.73<sub>±0.32</sub> |
| PHP (JIT: function) |  1.722<sub>±0.120</sub> |      20.55<sub>±0.34</sub> |
| Ruby (Naive) |  5.149<sub>±0.242</sub> |      13.85<sub>±0.12</sub> |
| Ruby (JIT) |  4.467<sub>±0.206</sub> |      14.55<sub>±0.12</sub> |
| Ruby (JRuby) |  5.215<sub>±0.720</sub> |     244.93<sub>±25.66</sub> |
| Ruby (TruffleRuby) |  1.430<sub>±0.084</sub> |     698.58<sub>±36.49</sub> |
| Ruby (TruffleRuby JVM) |  3.705<sub>±0.247</sub> |     961.51<sub>±245.52</sub> |
| Ruby (GraalVM) |  1.428<sub>±0.084</sub> |     698.96<sub>±31.22</sub> |
| Ruby (GraalVM JVM) |  3.715<sub>±0.244</sub> |     941.60<sub>±214.20</sub> |


