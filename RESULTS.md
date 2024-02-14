### primes/Simple

| Language | Time, s | Total time, s | Memory, MiB |
| :------- | ------: | ------------: | ----------: |
| C++ (clang) |  0.368<sub>±0.007</sub> |  0.374<sub>±0.016</sub> |       2.98<sub>±0.70</sub> |
| C++ (gcc) |  0.378<sub>±0.017</sub> |  0.383<sub>±0.019</sub> |       1.46<sub>±0.94</sub> |
| Java |  0.402<sub>±0.015</sub> |  0.468<sub>±0.193</sub> |      40.46<sub>±0.37</sub> |
| Java (GraalVM) |  0.410<sub>±0.024</sub> |  0.846<sub>±0.203</sub> |     140.21<sub>±6.31</sub> |
| JavaScript (Node) |  0.447<sub>±0.023</sub> |  0.496<sub>±0.026</sub> |      45.73<sub>±1.07</sub> |
| JavaScript (GraalVM) |  2.437<sub>±0.169</sub> |  2.732<sub>±0.216</sub> |     757.44<sub>±31.80</sub> |
| PHP |  0.004<sub>±0.000</sub> |  4.487<sub>±0.372</sub> |      17.66<sub>±0.17</sub> |
| PHP (JIT: tracing) |  0.002<sub>±0.000</sub> |  2.105<sub>±0.246</sub> |      20.94<sub>±0.16</sub> |
| PHP (JIT: function) |  0.002<sub>±0.000</sub> |  1.913<sub>±0.364</sub> |      20.65<sub>±0.14</sub> |
| Ruby | 12.487<sub>±0.347</sub> | 12.543<sub>±0.332</sub> |      13.46<sub>±0.04</sub> |
| Ruby (JIT) | 12.589<sub>±0.153</sub> | 12.755<sub>±0.160</sub> |     270.16<sub>±0.08</sub> |
| Ruby (JRuby) | 17.297<sub>±0.661</sub> | 19.467<sub>±0.859</sub> |     436.55<sub>±21.80</sub> |
| Ruby (TruffleRuby) |  0.990<sub>±0.154</sub> |  1.065<sub>±0.260</sub> |     668.58<sub>±1.99</sub> |
| Ruby (TruffleRuby JVM) |  2.323<sub>±0.228</sub> |  6.075<sub>±0.480</sub> |     745.68<sub>±72.69</sub> |
| Ruby (GraalVM) |  0.925<sub>±0.280</sub> |  1.014<sub>±0.300</sub> |     670.45<sub>±7.87</sub> |
| Ruby (GraalVM JVM) |  2.300<sub>±0.246</sub> |  5.672<sub>±0.204</sub> |     745.94<sub>±40.90</sub> |
| Rust |  0.368<sub>±0.007</sub> |  0.372<sub>±0.007</sub> |       1.72<sub>±0.11</sub> |


### primes/Atkin

| Language | Time, s | Total time, s | Memory, MiB |
| :------- | ------: | ------------: | ----------: |
| C++ (clang) |  0.333<sub>±0.180</sub> |  0.345<sub>±0.181</sub> |      88.86<sub>±0.15</sub> |
| C++ (gcc) |  0.261<sub>±0.018</sub> |  0.272<sub>±0.019</sub> |      88.94<sub>±0.36</sub> |
| Java |  0.263<sub>±0.133</sub> |  0.325<sub>±0.152</sub> |     176.82<sub>±2.33</sub> |
| Java (GraalVM) |  0.367<sub>±0.159</sub> |  0.785<sub>±0.149</sub> |     299.32<sub>±10.59</sub> |
| JavaScript (Node) |  0.404<sub>±0.036</sub> |  0.492<sub>±0.034</sub> |     225.58<sub>±1.16</sub> |
| JavaScript (GraalVM) |  2.738<sub>±0.151</sub> |  2.992<sub>±0.190</sub> |     988.07<sub>±37.59</sub> |
| PHP |  0.003<sub>±0.001</sub> |  2.945<sub>±0.692</sub> |     344.95<sub>±0.63</sub> |
| PHP (JIT: tracing) |  0.001<sub>±0.000</sub> |  1.494<sub>±0.157</sub> |     348.50<sub>±0.83</sub> |
| PHP (JIT: function) |  0.002<sub>±0.000</sub> |  1.707<sub>±0.359</sub> |     349.29<sub>±0.84</sub> |
| Python (CPython) |  7.582<sub>±0.100</sub> |  7.601<sub>±0.093</sub> |     245.69<sub>±0.07</sub> |
| Python (PyPy) |  1.577<sub>±0.081</sub> |  1.631<sub>±0.111</sub> |     314.83<sub>±0.24</sub> |
| Python (GraalVM) |  1.812<sub>±0.098</sub> |  2.093<sub>±0.114</sub> |     874.98<sub>±22.01</sub> |
| Ruby |  3.315<sub>±0.239</sub> |  3.394<sub>±0.243</sub> |     159.22<sub>±0.84</sub> |
| Ruby (JIT) |  2.324<sub>±0.120</sub> |  2.524<sub>±0.130</sub> |     415.89<sub>±0.09</sub> |
| Ruby (JRuby) |  3.322<sub>±0.282</sub> |  5.609<sub>±0.268</sub> |     546.75<sub>±28.56</sub> |
| Ruby (TruffleRuby) |  2.125<sub>±0.339</sub> |  2.220<sub>±0.283</sub> |     917.53<sub>±27.15</sub> |
| Ruby (TruffleRuby JVM) |  2.831<sub>±0.345</sub> |  5.974<sub>±0.450</sub> |    1052.46<sub>±14.40</sub> |
| Ruby (GraalVM) |  2.069<sub>±0.193</sub> |  2.146<sub>±0.196</sub> |     908.52<sub>±16.56</sub> |
| Ruby (GraalVM JVM) |  2.654<sub>±0.222</sub> |  5.931<sub>±0.351</sub> |     943.74<sub>±39.69</sub> |
| Rust |  0.210<sub>±0.016</sub> |  0.222<sub>±0.015</sub> |      77.48<sub>±0.08</sub> |


### collatz/MaxSequence

| Language | Time, s | Total time, s | Memory, MiB |
| :------- | ------: | ------------: | ----------: |
| C++ (clang) |  0.062<sub>±0.001</sub> |  0.066<sub>±0.001</sub> |       1.40<sub>±0.77</sub> |
| Java |  0.105<sub>±0.016</sub> |  0.160<sub>±0.025</sub> |      38.02<sub>±0.88</sub> |
| Java (GraalVM) |  0.101<sub>±0.008</sub> |  0.516<sub>±0.012</sub> |      84.07<sub>±2.71</sub> |
| JavaScript (Node) |  0.735<sub>±0.019</sub> |  0.788<sub>±0.053</sub> |      42.86<sub>±1.00</sub> |
| JavaScript (GraalVM) |  0.954<sub>±0.022</sub> |  1.171<sub>±0.046</sub> |     468.02<sub>±7.14</sub> |
| PHP |  0.002<sub>±0.000</sub> |  1.993<sub>±0.210</sub> |      17.49<sub>±0.10</sub> |
| PHP (JIT: tracing) |  0.001<sub>±0.000</sub> |  0.552<sub>±0.161</sub> |      21.08<sub>±0.12</sub> |
| PHP (JIT: function) |  0.001<sub>±0.000</sub> |  0.788<sub>±0.220</sub> |      20.80<sub>±0.22</sub> |
| Ruby |  3.108<sub>±0.073</sub> |  3.162<sub>±0.088</sub> |      13.42<sub>±0.06</sub> |
| Ruby (JIT) |  1.210<sub>±0.042</sub> |  1.423<sub>±0.136</sub> |     270.11<sub>±0.07</sub> |
| Ruby (JRuby) |  1.737<sub>±0.270</sub> |  4.017<sub>±0.340</sub> |     407.16<sub>±29.11</sub> |
| Ruby (TruffleRuby) |  0.582<sub>±0.117</sub> |  0.646<sub>±0.120</sub> |     439.87<sub>±26.57</sub> |
| Ruby (TruffleRuby JVM) |  0.842<sub>±0.044</sub> |  3.925<sub>±0.158</sub> |     600.31<sub>±22.60</sub> |
| Ruby (GraalVM) |  0.575<sub>±0.040</sub> |  0.629<sub>±0.061</sub> |     438.92<sub>±23.05</sub> |
| Ruby (GraalVM JVM) |  0.804<sub>±0.048</sub> |  4.010<sub>±0.312</sub> |     596.93<sub>±23.67</sub> |
| Rust |  0.060<sub>±0.001</sub> |  0.062<sub>±0.001</sub> |       1.65<sub>±0.06</sub> |


### mandelbrot/Simple

| Language | Time, s | Total time, s | Memory, MiB |
| :------- | ------: | ------------: | ----------: |
| C++ (clang) |  0.035<sub>±0.001</sub> |  0.039<sub>±0.001</sub> |       1.40<sub>±0.93</sub> |
| C++ (gcc) |  0.033<sub>±0.001</sub> |  0.037<sub>±0.001</sub> |       1.40<sub>±0.91</sub> |
| Java |  0.051<sub>±0.002</sub> |  0.101<sub>±0.005</sub> |      40.17<sub>±1.00</sub> |
| Java (GraalVM) |  0.056<sub>±0.003</sub> |  0.464<sub>±0.016</sub> |      82.61<sub>±3.63</sub> |
| JavaScript (Node) |  0.050<sub>±0.002</sub> |  0.092<sub>±0.004</sub> |      44.68<sub>±1.00</sub> |
| JavaScript (GraalVM) |  0.237<sub>±0.020</sub> |  0.517<sub>±0.031</sub> |     466.32<sub>±1.86</sub> |
| PHP |  0.001<sub>±0.000</sub> |  1.022<sub>±0.182</sub> |      17.66<sub>±0.20</sub> |
| PHP (JIT: tracing) |  0.000<sub>±0.000</sub> |  0.158<sub>±0.051</sub> |      21.22<sub>±0.18</sub> |
| PHP (JIT: function) |  0.000<sub>±0.000</sub> |  0.197<sub>±0.077</sub> |      20.66<sub>±0.24</sub> |
| Ruby |  2.031<sub>±0.263</sub> |  2.097<sub>±0.262</sub> |      13.54<sub>±0.06</sub> |
| Ruby (JIT) |  1.568<sub>±0.104</sub> |  1.753<sub>±0.105</sub> |     270.19<sub>±0.06</sub> |
| Ruby (JRuby) |  2.488<sub>±0.262</sub> |  4.714<sub>±0.250</sub> |     476.17<sub>±32.26</sub> |
| Ruby (TruffleRuby) |  0.446<sub>±0.035</sub> |  0.517<sub>±0.034</sub> |     634.78<sub>±2.39</sub> |
| Ruby (TruffleRuby JVM) |  1.127<sub>±0.101</sub> |  4.015<sub>±0.242</sub> |     627.02<sub>±23.99</sub> |
| Ruby (GraalVM) |  0.452<sub>±0.104</sub> |  0.529<sub>±0.116</sub> |     636.97<sub>±3.00</sub> |
| Ruby (GraalVM JVM) |  1.107<sub>±0.143</sub> |  4.161<sub>±0.293</sub> |     649.16<sub>±25.42</sub> |
| Rust |  0.034<sub>±0.001</sub> |  0.037<sub>±0.002</sub> |       1.74<sub>±0.08</sub> |


### treap/Naive

| Language | Time, s | Total time, s | Memory, MiB |
| :------- | ------: | ------------: | ----------: |
| C++ (clang) |  0.262<sub>±0.039</sub> |  0.267<sub>±0.039</sub> |       3.12<sub>±0.12</sub> |
| C++ (gcc) |  0.227<sub>±0.011</sub> |  0.231<sub>±0.012</sub> |       3.04<sub>±0.11</sub> |
| Go |  0.326<sub>±0.008</sub> |  0.329<sub>±0.008</sub> |       6.25<sub>±0.42</sub> |
| Java |  0.681<sub>±0.071</sub> |  0.742<sub>±0.075</sub> |     152.01<sub>±0.90</sub> |
| Java (GraalVM) |  0.690<sub>±0.099</sub> |  1.109<sub>±0.054</sub> |     329.11<sub>±27.05</sub> |
| JavaScript (Node) |  1.046<sub>±0.048</sub> |  1.097<sub>±0.048</sub> |      85.99<sub>±1.17</sub> |
| JavaScript (GraalVM) |  3.137<sub>±0.077</sub> |  3.387<sub>±0.080</sub> |     812.64<sub>±8.18</sub> |
| Kotlin (JVM) | -1.000<sub>±0.000</sub> |  0.692<sub>±0.100</sub> |     152.66<sub>±22.21</sub> |
| Kotlin (Native) | -1.000<sub>±0.000</sub> |  3.738<sub>±0.066</sub> |       3.80<sub>±0.06</sub> |
| PHP |  0.007<sub>±0.001</sub> |  7.039<sub>±0.761</sub> |      17.52<sub>±0.34</sub> |
| PHP (JIT: tracing) |  0.005<sub>±0.001</sub> |  5.517<sub>±0.613</sub> |      21.01<sub>±0.20</sub> |
| PHP (JIT: function) |  0.006<sub>±0.001</sub> |  5.539<sub>±0.831</sub> |      21.07<sub>±0.22</sub> |
| Python (CPython) | 14.322<sub>±0.244</sub> | 14.336<sub>±0.245</sub> |       8.38<sub>±0.07</sub> |
| Python (PyPy) |  3.404<sub>±0.180</sub> |  3.645<sub>±0.175</sub> |      73.51<sub>±3.61</sub> |
| Python (GraalVM) |  3.814<sub>±0.299</sub> |  4.171<sub>±0.307</sub> |     872.88<sub>±6.07</sub> |
| Ruby |  7.016<sub>±0.139</sub> |  7.066<sub>±0.145</sub> |      13.92<sub>±0.08</sub> |
| Ruby (JIT) |  3.917<sub>±0.201</sub> |  4.284<sub>±0.233</sub> |     270.66<sub>±0.06</sub> |
| Ruby (JRuby) |  5.439<sub>±0.593</sub> |  7.811<sub>±0.447</sub> |     219.47<sub>±12.83</sub> |
| Ruby (TruffleRuby) |  1.968<sub>±0.172</sub> |  2.089<sub>±0.192</sub> |     698.93<sub>±3.08</sub> |
| Ruby (TruffleRuby JVM) |  2.434<sub>±0.271</sub> |  5.534<sub>±0.315</sub> |     921.98<sub>±53.33</sub> |
| Ruby (GraalVM) |  1.928<sub>±0.258</sub> |  2.044<sub>±0.256</sub> |     703.11<sub>±12.50</sub> |
| Ruby (GraalVM JVM) |  2.338<sub>±0.037</sub> |  5.537<sub>±0.270</sub> |     921.67<sub>±83.04</sub> |


### recursion/Tak

| Language | Time, s | Total time, s | Memory, MiB |
| :------- | ------: | ------------: | ----------: |
| C++ (clang) |  0.066<sub>±0.004</sub> |  0.070<sub>±0.004</sub> |       1.45<sub>±0.72</sub> |
| C++ (gcc) |  0.084<sub>±0.005</sub> |  0.088<sub>±0.006</sub> |       3.00<sub>±0.90</sub> |
| JavaScript (Node) |  0.145<sub>±0.004</sub> |  0.186<sub>±0.006</sub> |      41.28<sub>±1.03</sub> |
| JavaScript (GraalVM) |  0.821<sub>±0.035</sub> |  1.034<sub>±0.072</sub> |     664.43<sub>±10.96</sub> |
| PHP |  0.001<sub>±0.000</sub> |  1.286<sub>±0.073</sub> |      17.61<sub>±0.21</sub> |
| PHP (JIT: tracing) |  0.000<sub>±0.000</sub> |  0.440<sub>±0.013</sub> |      20.91<sub>±0.21</sub> |
| PHP (JIT: function) |  0.000<sub>±0.000</sub> |  0.476<sub>±0.023</sub> |      20.66<sub>±0.18</sub> |
| Python (CPython) |  4.737<sub>±0.125</sub> |  4.750<sub>±0.124</sub> |       6.85<sub>±0.33</sub> |
| Python (PyPy) |  0.899<sub>±0.035</sub> |  0.935<sub>±0.035</sub> |      62.27<sub>±0.37</sub> |
| Python (GraalVM) |  1.169<sub>±0.237</sub> |  1.425<sub>±0.300</sub> |     724.94<sub>±4.03</sub> |
| Ruby |  1.473<sub>±0.097</sub> |  1.617<sub>±0.088</sub> |      13.43<sub>±0.06</sub> |
| Ruby (JIT) |  0.330<sub>±0.100</sub> |  0.516<sub>±0.106</sub> |     270.05<sub>±0.05</sub> |
| Ruby (JRuby) |  0.684<sub>±0.183</sub> |  2.950<sub>±0.220</sub> |     180.86<sub>±8.62</sub> |
| Ruby (TruffleRuby) |  0.806<sub>±0.049</sub> |  0.871<sub>±0.052</sub> |     581.11<sub>±29.39</sub> |
| Ruby (TruffleRuby JVM) |  0.832<sub>±0.059</sub> |  3.976<sub>±0.043</sub> |     794.12<sub>±56.47</sub> |
| Ruby (GraalVM) |  0.888<sub>±0.060</sub> |  0.950<sub>±0.064</sub> |     585.88<sub>±29.89</sub> |
| Ruby (GraalVM JVM) |  0.811<sub>±0.174</sub> |  3.862<sub>±0.280</sub> |     728.12<sub>±37.97</sub> |


### linpack/Linpack

| Language | Time, s | Total time, s | Memory, MiB |
| :------- | ------: | ------------: | ----------: |
| Go |  4.266<sub>±0.387</sub> |  4.276<sub>±0.386</sub> |      35.58<sub>±0.67</sub> |
| JavaScript (Node) |  4.672<sub>±0.212</sub> |  4.747<sub>±0.230</sub> |     135.18<sub>±0.55</sub> |
| JavaScript (GraalVM) |  5.364<sub>±0.404</sub> |  5.612<sub>±0.518</sub> |     699.30<sub>±4.10</sub> |
| PHP |  0.090<sub>±0.001</sub> | 89.600<sub>±0.756</sub> |     151.83<sub>±1.04</sub> |
| PHP (JIT: tracing) |  0.028<sub>±0.001</sub> | 28.241<sub>±1.004</sub> |     152.79<sub>±0.21</sub> |
| PHP (JIT: function) |  0.046<sub>±0.006</sub> | 46.101<sub>±6.494</sub> |     155.02<sub>±1.24</sub> |
| Python (CPython) | 734.398<sub>±41.083</sub> | 734.413<sub>±41.082</sub> |     163.19<sub>±0.11</sub> |
| Python (PyPy) |  7.850<sub>±0.184</sub> |  7.889<sub>±0.198</sub> |     107.62<sub>±1.41</sub> |
| Python (GraalVM) | 79.532<sub>±5.506</sub> | 80.584<sub>±6.160</sub> |    1383.20<sub>±23.47</sub> |


