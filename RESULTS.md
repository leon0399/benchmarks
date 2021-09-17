### primes/Simple

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.339<sub>±0.006</sub> |       1.48<sub>±1.53</sub> |
| C++ (gcc) |  0.338<sub>±0.008</sub> |       1.48<sub>±0.05</sub> |
| Java |  0.387<sub>±0.018</sub> |      38.14<sub>±1.12</sub> |
| Java (GraalVM) |  0.727<sub>±0.077</sub> |     131.92<sub>±8.01</sub> |
| JavaScript (Node) |  0.420<sub>±0.017</sub> |      37.34<sub>±2.02</sub> |
| JavaScript (GraalVM) |  2.015<sub>±0.273</sub> |     786.80<sub>±8.73</sub> |
| PHP |  2.452<sub>±0.149</sub> |      17.44<sub>±0.29</sub> |
| PHP (JIT: tracing) |  1.312<sub>±0.236</sub> |      20.50<sub>±0.27</sub> |
| PHP (JIT: function) |  1.481<sub>±0.136</sub> |      20.27<sub>±0.12</sub> |
| Ruby |  8.710<sub>±0.211</sub> |      13.71<sub>±0.08</sub> |
| Ruby (JIT) |  6.265<sub>±0.385</sub> |      14.16<sub>±0.11</sub> |
| Ruby (JRuby) | 11.688<sub>±0.838</sub> |     381.17<sub>±141.15</sub> |
| Ruby (TruffleRuby) |  0.798<sub>±0.049</sub> |     663.36<sub>±25.78</sub> |
| Ruby (TruffleRuby JVM) |  3.831<sub>±0.193</sub> |     763.76<sub>±172.61</sub> |
| Ruby (GraalVM) |  0.812<sub>±0.059</sub> |     668.61<sub>±12.68</sub> |
| Ruby (GraalVM JVM) |  3.760<sub>±0.202</sub> |     729.97<sub>±160.21</sub> |
| Rust |  0.342<sub>±0.004</sub> |       1.67<sub>±0.14</sub> |


### primes/Atkin

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.187<sub>±0.037</sub> |      88.89<sub>±0.15</sub> |
| C++ (gcc) |  0.184<sub>±0.023</sub> |      88.97<sub>±0.07</sub> |
| Java |  0.235<sub>±0.026</sub> |     194.97<sub>±18.91</sub> |
| Java (GraalVM) |  0.638<sub>±0.055</sub> |     307.38<sub>±16.02</sub> |
| JavaScript (Node) |  0.328<sub>±0.022</sub> |     208.02<sub>±1.97</sub> |
| JavaScript (GraalVM) |  1.996<sub>±0.290</sub> |     984.36<sub>±68.12</sub> |
| PHP |  1.587<sub>±0.084</sub> |     348.69<sub>±0.51</sub> |
| PHP (JIT: tracing) |  1.698<sub>±0.145</sub> |     352.32<sub>±0.18</sub> |
| PHP (JIT: function) |  1.160<sub>±0.035</sub> |     351.67<sub>±1.76</sub> |
| Python (CPython) |  4.380<sub>±0.229</sub> |     245.73<sub>±0.08</sub> |
| Python (PyPy) |  1.159<sub>±0.078</sub> |     316.59<sub>±0.42</sub> |
| Python (GraalVM) |  1.604<sub>±0.117</sub> |     921.82<sub>±47.16</sub> |
| Ruby |  2.559<sub>±0.166</sub> |     160.56<sub>±0.09</sub> |
| Ruby (JIT) |  2.356<sub>±0.049</sub> |     161.17<sub>±0.09</sub> |
| Ruby (JRuby) |  3.575<sub>±0.315</sub> |     496.34<sub>±83.62</sub> |
| Ruby (TruffleRuby) |  1.559<sub>±0.139</sub> |     884.94<sub>±30.67</sub> |
| Ruby (TruffleRuby JVM) |  3.848<sub>±0.194</sub> |     939.21<sub>±63.71</sub> |
| Ruby (GraalVM) |  1.529<sub>±0.073</sub> |     861.11<sub>±59.40</sub> |
| Ruby (GraalVM JVM) |  3.881<sub>±0.127</sub> |     990.00<sub>±112.41</sub> |
| Rust |  0.167<sub>±0.022</sub> |      77.49<sub>±0.07</sub> |


### collatz/MaxSequence

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.058<sub>±0.001</sub> |       3.05<sub>±0.11</sub> |
| Java |  0.113<sub>±0.012</sub> |      36.15<sub>±0.04</sub> |
| Java (GraalVM) |  0.458<sub>±0.060</sub> |      75.26<sub>±2.46</sub> |
| JavaScript (Node) |  0.766<sub>±0.006</sub> |      31.84<sub>±2.09</sub> |
| JavaScript (GraalVM) |  1.007<sub>±0.030</sub> |     462.57<sub>±10.59</sub> |
| PHP |  0.838<sub>±0.097</sub> |      17.35<sub>±0.21</sub> |
| PHP (JIT: tracing) |  0.332<sub>±0.018</sub> |      20.66<sub>±0.33</sub> |
| PHP (JIT: function) |  0.452<sub>±0.086</sub> |      20.55<sub>±0.29</sub> |
| Ruby |  2.492<sub>±0.069</sub> |      13.36<sub>±0.05</sub> |
| Ruby (JIT) |  0.658<sub>±0.045</sub> |      13.75<sub>±0.09</sub> |
| Ruby (JRuby) |  2.608<sub>±0.389</sub> |     334.11<sub>±29.66</sub> |
| Ruby (TruffleRuby) |  0.461<sub>±0.114</sub> |     438.64<sub>±5.54</sub> |
| Ruby (TruffleRuby JVM) |  2.633<sub>±0.047</sub> |     578.66<sub>±124.13</sub> |
| Ruby (GraalVM) |  0.452<sub>±0.051</sub> |     437.95<sub>±4.62</sub> |
| Ruby (GraalVM JVM) |  2.624<sub>±0.044</sub> |     580.24<sub>±21.63</sub> |
| Rust |  0.061<sub>±0.002</sub> |       1.74<sub>±0.11</sub> |


### mandelbrot/Simple

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.033<sub>±0.000</sub> |       2.94<sub>±1.46</sub> |
| C++ (gcc) |  0.033<sub>±0.001</sub> |       3.13<sub>±1.65</sub> |
| Java |  0.066<sub>±0.083</sub> |      37.34<sub>±0.39</sub> |
| Java (GraalVM) |  0.411<sub>±0.028</sub> |      74.21<sub>±6.91</sub> |
| JavaScript (Node) |  0.071<sub>±0.002</sub> |      37.24<sub>±1.94</sub> |
| JavaScript (GraalVM) |  0.421<sub>±0.038</sub> |     503.81<sub>±9.09</sub> |
| PHP |  0.414<sub>±0.068</sub> |      17.58<sub>±0.20</sub> |
| PHP (JIT: tracing) |  0.125<sub>±0.003</sub> |      20.73<sub>±0.30</sub> |
| PHP (JIT: function) |  0.169<sub>±0.027</sub> |      20.49<sub>±0.19</sub> |
| Ruby |  1.633<sub>±0.083</sub> |      13.66<sub>±0.08</sub> |
| Ruby (JIT) |  1.349<sub>±0.162</sub> |      14.11<sub>±0.07</sub> |
| Ruby (JRuby) |  3.331<sub>±0.478</sub> |     366.97<sub>±87.58</sub> |
| Ruby (TruffleRuby) |  0.385<sub>±0.083</sub> |     629.66<sub>±7.48</sub> |
| Ruby (TruffleRuby JVM) |  2.804<sub>±0.151</sub> |     632.03<sub>±21.95</sub> |
| Ruby (GraalVM) |  0.315<sub>±0.066</sub> |     626.93<sub>±3.27</sub> |
| Ruby (GraalVM JVM) |  2.880<sub>±0.137</sub> |     615.78<sub>±11.38</sub> |
| Rust |  0.033<sub>±0.001</sub> |       1.67<sub>±0.06</sub> |


### treap/Naive

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.177<sub>±0.017</sub> |       3.09<sub>±0.29</sub> |
| C++ (gcc) |  0.155<sub>±0.003</sub> |       3.11<sub>±0.16</sub> |
| Go |  0.200<sub>±0.039</sub> |       9.30<sub>±1.81</sub> |
| Java |  0.424<sub>±0.023</sub> |     139.70<sub>±6.58</sub> |
| Java (GraalVM) |  0.775<sub>±0.079</sub> |     197.86<sub>±35.86</sub> |
| JavaScript (Node) |  0.796<sub>±0.097</sub> |      75.66<sub>±2.29</sub> |
| JavaScript (GraalVM) |  2.690<sub>±0.841</sub> |     803.20<sub>±8.52</sub> |
| Kotlin (JVM) |  0.431<sub>±0.017</sub> |     140.51<sub>±4.20</sub> |
| Kotlin (Native) |  2.218<sub>±0.312</sub> |       4.36<sub>±0.31</sub> |
| PHP |  2.629<sub>±0.078</sub> |      17.62<sub>±0.11</sub> |
| PHP (JIT: tracing) |  1.606<sub>±0.093</sub> |      20.71<sub>±0.17</sub> |
| PHP (JIT: function) |  1.702<sub>±0.266</sub> |      20.53<sub>±0.21</sub> |
| Python (CPython) |  6.597<sub>±0.199</sub> |       8.45<sub>±0.03</sub> |
| Python (PyPy) |  2.383<sub>±0.180</sub> |      74.03<sub>±0.88</sub> |
| Python (GraalVM) |  3.002<sub>±0.076</sub> |     874.05<sub>±6.20</sub> |
| Ruby |  5.170<sub>±0.319</sub> |      13.83<sub>±2.00</sub> |
| Ruby (JIT) |  4.793<sub>±0.381</sub> |      14.57<sub>±0.10</sub> |
| Ruby (JRuby) |  5.235<sub>±0.402</sub> |     244.06<sub>±11.73</sub> |
| Ruby (TruffleRuby) |  1.450<sub>±0.094</sub> |     678.90<sub>±29.41</sub> |
| Ruby (TruffleRuby JVM) |  3.831<sub>±0.157</sub> |     987.87<sub>±195.08</sub> |
| Ruby (GraalVM) |  1.550<sub>±0.160</sub> |     681.09<sub>±23.57</sub> |
| Ruby (GraalVM JVM) |  3.778<sub>±0.125</sub> |     902.18<sub>±119.33</sub> |


### recursion/Tak

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.042<sub>±0.001</sub> |       2.93<sub>±1.46</sub> |
| C++ (gcc) |  0.057<sub>±0.015</sub> |       1.47<sub>±1.55</sub> |
| PHP |  0.647<sub>±0.046</sub> |      17.49<sub>±0.17</sub> |
| PHP (JIT: tracing) |  0.298<sub>±0.013</sub> |      20.67<sub>±0.12</sub> |
| PHP (JIT: function) |  0.334<sub>±0.012</sub> |      20.41<sub>±0.35</sub> |
| Python (CPython) |  2.177<sub>±0.222</sub> |       7.21<sub>±0.05</sub> |
| Python (PyPy) |  0.565<sub>±0.059</sub> |      63.11<sub>±0.37</sub> |
| Python (GraalVM) |  1.117<sub>±0.047</sub> |     728.27<sub>±5.57</sub> |
| Ruby |  1.098<sub>±0.035</sub> |      13.29<sub>±0.08</sub> |
| Ruby (JIT) |  0.563<sub>±0.060</sub> |      13.76<sub>±0.10</sub> |
| Ruby (JRuby) |  1.978<sub>±0.234</sub> |     175.89<sub>±2.40</sub> |
| Ruby (TruffleRuby) |  0.673<sub>±0.041</sub> |     583.23<sub>±8.39</sub> |
| Ruby (TruffleRuby JVM) |  2.691<sub>±0.072</sub> |     881.62<sub>±177.33</sub> |
| Ruby (GraalVM) |  0.650<sub>±0.079</sub> |     580.98<sub>±6.10</sub> |
| Ruby (GraalVM JVM) |  2.693<sub>±0.075</sub> |     823.51<sub>±97.74</sub> |


### io/Load

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.074<sub>±0.025</sub> |       1.48<sub>±1.69</sub> |
| C++ (gcc) |  0.072<sub>±0.014</sub> |       3.06<sub>±1.59</sub> |
| Go |  0.127<sub>±0.105</sub> |       2.68<sub>±0.14</sub> |
| Java |  0.182<sub>±0.051</sub> |      77.36<sub>±0.50</sub> |
| Java (GraalVM) |  0.699<sub>±0.133</sub> |     174.10<sub>±9.09</sub> |
| JavaScript (Node) |  1.117<sub>±0.046</sub> |      65.52<sub>±1.90</sub> |
| JavaScript (GraalVM) |  3.494<sub>±0.124</sub> |     849.90<sub>±40.99</sub> |
| PHP |  0.084<sub>±0.001</sub> |      17.44<sub>±0.43</sub> |
| PHP (JIT: tracing) |  0.082<sub>±0.028</sub> |      20.55<sub>±0.27</sub> |
| PHP (JIT: function) |  0.081<sub>±0.009</sub> |      20.36<sub>±0.18</sub> |
| Python (CPython) |  0.106<sub>±0.004</sub> |       7.30<sub>±0.17</sub> |
| Python (PyPy) |  0.094<sub>±0.059</sub> |      64.36<sub>±0.45</sub> |
| Python (GraalVM) |  2.733<sub>±0.183</sub> |     808.54<sub>±19.85</sub> |
| Ruby |  0.201<sub>±0.049</sub> |      13.67<sub>±0.07</sub> |
| Ruby (JIT) |  0.244<sub>±0.106</sub> |      14.07<sub>±0.11</sub> |
| Ruby (JRuby) |  2.005<sub>±0.141</sub> |     190.84<sub>±11.75</sub> |
| Ruby (TruffleRuby) |  1.037<sub>±0.161</sub> |     689.25<sub>±32.52</sub> |
| Ruby (TruffleRuby JVM) |  3.979<sub>±0.224</sub> |     636.79<sub>±121.86</sub> |
| Ruby (GraalVM) |  0.996<sub>±0.144</sub> |     686.32<sub>±26.78</sub> |
| Ruby (GraalVM JVM) |  3.953<sub>±0.056</sub> |     624.27<sub>±26.39</sub> |
| Rust |  0.072<sub>±0.001</sub> |       1.67<sub>±0.08</sub> |


### io/NoLoad

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.001<sub>±0.000</sub> |       1.47<sub>±0.01</sub> |
| C++ (gcc) |  0.001<sub>±0.000</sub> |       1.47<sub>±1.52</sub> |
| Go |  0.001<sub>±0.002</sub> |       2.68<sub>±0.16</sub> |
| Java |  0.024<sub>±0.002</sub> |      34.31<sub>±0.13</sub> |
| Java (GraalVM) |  0.373<sub>±0.005</sub> |      65.40<sub>±4.84</sub> |
| JavaScript (Node) |  0.025<sub>±0.007</sub> |      35.32<sub>±1.98</sub> |
| JavaScript (GraalVM) |  0.226<sub>±0.014</sub> |     406.38<sub>±29.38</sub> |
| PHP |  0.010<sub>±0.001</sub> |      17.20<sub>±0.15</sub> |
| PHP (JIT: tracing) |  0.010<sub>±0.001</sub> |      20.45<sub>±0.28</sub> |
| PHP (JIT: function) |  0.010<sub>±0.002</sub> |      20.43<sub>±0.21</sub> |
| Python (CPython) |  0.023<sub>±0.001</sub> |       6.82<sub>±0.39</sub> |
| Python (PyPy) |  0.024<sub>±0.001</sub> |      55.11<sub>±1.20</sub> |
| Python (GraalVM) |  0.192<sub>±0.034</sub> |     321.96<sub>±24.78</sub> |
| Ruby |  0.053<sub>±0.049</sub> |      13.34<sub>±0.09</sub> |
| Ruby (JIT) |  0.225<sub>±0.070</sub> |      13.68<sub>±0.07</sub> |
| Ruby (JRuby) |  1.594<sub>±0.066</sub> |     186.95<sub>±8.55</sub> |
| Ruby (TruffleRuby) |  0.078<sub>±0.002</sub> |     221.64<sub>±3.84</sub> |
| Ruby (TruffleRuby JVM) |  2.167<sub>±0.121</sub> |     530.74<sub>±9.55</sub> |
| Ruby (GraalVM) |  0.077<sub>±0.007</sub> |     219.88<sub>±4.77</sub> |
| Ruby (GraalVM JVM) |  2.168<sub>±0.054</sub> |     533.20<sub>±12.04</sub> |
| Rust |  0.001<sub>±0.001</sub> |       1.75<sub>±1.17</sub> |


