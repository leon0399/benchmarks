### primes/Simple

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.442<sub>±0.003</sub> |       2.28<sub>±0.92</sub> |
| Java (Naive) |  0.488<sub>±0.053</sub> |      39.74<sub>±1.88</sub> |
| Java (GraalVM: Naive) |  0.845<sub>±0.037</sub> |     132.93<sub>±6.00</sub> |
| JavaScript (Node) |  0.529<sub>±0.071</sub> |      37.23<sub>±1.93</sub> |
| JavaScript (GraalVM Node) |  2.346<sub>±0.269</sub> |     787.00<sub>±38.11</sub> |
| PHP (Naive) |  3.069<sub>±0.302</sub> |      17.30<sub>±0.32</sub> |
| PHP (JIT: tracing) |  1.503<sub>±0.324</sub> |      20.48<sub>±0.33</sub> |
| PHP (JIT: function) |  1.775<sub>±0.156</sub> |      20.44<sub>±0.44</sub> |
| Rust |  0.441<sub>±0.005</sub> |       1.74<sub>±0.07</sub> |


### primes/Atkin

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.219<sub>±0.158</sub> |      88.86<sub>±0.16</sub> |
| Java (Naive) |  0.264<sub>±0.068</sub> |     171.54<sub>±15.41</sub> |
| Java (GraalVM: Naive) |  0.730<sub>±0.057</sub> |     286.32<sub>±31.45</sub> |
| JavaScript (Node) |  0.483<sub>±0.034</sub> |     205.58<sub>±2.13</sub> |
| JavaScript (GraalVM Node) |  2.237<sub>±0.186</sub> |     979.76<sub>±72.08</sub> |
| PHP (Naive) |  1.901<sub>±0.134</sub> |     344.24<sub>±1.37</sub> |
| PHP (JIT: tracing) |  2.045<sub>±0.177</sub> |     347.98<sub>±5.82</sub> |
| PHP (JIT: function) |  1.301<sub>±0.050</sub> |     353.29<sub>±0.29</sub> |
| Ruby (Naive) |  3.138<sub>±0.457</sub> |     163.64<sub>±0.35</sub> |
| Ruby (JIT) |  2.850<sub>±0.209</sub> |     164.27<sub>±0.51</sub> |
| Ruby (JRuby) |  4.730<sub>±0.527</sub> |     522.49<sub>±53.35</sub> |
| Ruby (TruffleRuby) |  2.052<sub>±0.359</sub> |     930.73<sub>±55.94</sub> |
| Ruby (TruffleRuby JVM) |  6.513<sub>±0.570</sub> |     911.21<sub>±67.91</sub> |
| Ruby (GraalVM) |  6.136<sub>±0.647</sub> |     928.62<sub>±65.93</sub> |
| Rust |  0.215<sub>±0.036</sub> |      77.50<sub>±0.29</sub> |


### collatz/MaxSequence

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.075<sub>±0.059</sub> |       1.47<sub>±1.70</sub> |
| Java (Naive) |  0.145<sub>±0.113</sub> |      36.08<sub>±0.20</sub> |
| Java (GraalVM: Naive) |  0.496<sub>±0.050</sub> |      75.04<sub>±4.52</sub> |
| JavaScript (Node) |  0.988<sub>±0.029</sub> |      31.51<sub>±1.96</sub> |
| JavaScript (GraalVM Node) |  1.278<sub>±0.042</sub> |     465.62<sub>±12.08</sub> |
| PHP (Naive) |  1.064<sub>±0.176</sub> |      17.25<sub>±0.28</sub> |
| PHP (JIT: tracing) |  0.434<sub>±0.025</sub> |      20.66<sub>±0.33</sub> |
| PHP (JIT: function) |  0.575<sub>±0.016</sub> |      20.34<sub>±0.37</sub> |
| Rust |  0.077<sub>±0.003</sub> |       1.79<sub>±0.11</sub> |


### mandelbrot/Simple

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.043<sub>±0.000</sub> |       3.07<sub>±1.61</sub> |
| Java (Naive) |  0.083<sub>±0.052</sub> |      37.17<sub>±0.66</sub> |
| Java (GraalVM: Naive) |  0.438<sub>±0.004</sub> |      74.94<sub>±5.28</sub> |
| JavaScript (Node) |  0.089<sub>±0.073</sub> |      38.36<sub>±2.03</sub> |
| JavaScript (GraalVM Node) |  0.484<sub>±0.037</sub> |     502.80<sub>±8.80</sub> |
| PHP (Naive) |  0.513<sub>±0.075</sub> |      17.35<sub>±0.41</sub> |
| PHP (JIT: tracing) |  0.160<sub>±0.004</sub> |      20.70<sub>±0.33</sub> |
| PHP (JIT: function) |  0.210<sub>±0.026</sub> |      20.59<sub>±0.27</sub> |
| Rust |  0.042<sub>±0.000</sub> |       1.69<sub>±0.08</sub> |


### io/Load

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.095<sub>±0.072</sub> |       1.50<sub>±1.66</sub> |
| Java (Naive) |  0.237<sub>±0.022</sub> |      76.87<sub>±10.12</sub> |
| Java (GraalVM: Naive) |  0.806<sub>±0.271</sub> |     171.93<sub>±13.82</sub> |
| JavaScript (Node) |  1.423<sub>±0.051</sub> |      60.95<sub>±1.65</sub> |
| JavaScript (GraalVM Node) |  4.497<sub>±0.354</sub> |     872.94<sub>±35.26</sub> |
| PHP (Naive) |  0.109<sub>±0.040</sub> |      17.39<sub>±0.37</sub> |
| PHP (JIT: tracing) |  0.104<sub>±0.022</sub> |      20.51<sub>±0.19</sub> |
| PHP (JIT: function) |  0.107<sub>±0.016</sub> |      20.50<sub>±0.34</sub> |
| Ruby (Naive) |  0.263<sub>±0.031</sub> |      13.66<sub>±0.11</sub> |
| Ruby (JIT) |  0.346<sub>±0.324</sub> |      14.02<sub>±0.13</sub> |
| Ruby (JRuby) |  2.500<sub>±0.201</sub> |     190.43<sub>±15.77</sub> |
| Ruby (TruffleRuby) |  1.323<sub>±0.124</sub> |     688.78<sub>±45.24</sub> |
| Ruby (TruffleRuby JVM) |  4.980<sub>±0.398</sub> |     607.36<sub>±54.26</sub> |
| Ruby (GraalVM) |  5.063<sub>±0.538</sub> |     613.37<sub>±32.52</sub> |
| Rust |  0.094<sub>±0.065</sub> |       1.70<sub>±0.14</sub> |


### io/NoLoad

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.001<sub>±0.000</sub> |       1.46<sub>±1.70</sub> |
| Java (Naive) |  0.029<sub>±0.002</sub> |      34.28<sub>±0.18</sub> |
| Java (GraalVM: Naive) |  0.383<sub>±0.305</sub> |      62.55<sub>±12.15</sub> |
| JavaScript (Node) |  0.032<sub>±0.062</sub> |      34.87<sub>±2.04</sub> |
| JavaScript (GraalVM Node) |  0.281<sub>±0.063</sub> |     406.14<sub>±35.36</sub> |
| PHP (Naive) |  0.014<sub>±0.001</sub> |      17.48<sub>±0.43</sub> |
| PHP (JIT: tracing) |  0.013<sub>±0.003</sub> |      20.47<sub>±0.28</sub> |
| PHP (JIT: function) |  0.014<sub>±0.006</sub> |      20.42<sub>±0.22</sub> |
| Ruby (Naive) |  0.070<sub>±0.012</sub> |      13.34<sub>±0.16</sub> |
| Ruby (JIT) |  0.291<sub>±0.059</sub> |      13.63<sub>±0.16</sub> |
| Ruby (JRuby) |  1.993<sub>±0.086</sub> |     181.62<sub>±19.49</sub> |
| Ruby (TruffleRuby) |  0.100<sub>±0.043</sub> |     220.61<sub>±9.45</sub> |
| Ruby (TruffleRuby JVM) |  2.626<sub>±0.317</sub> |     513.92<sub>±7.97</sub> |
| Ruby (GraalVM) |  2.650<sub>±0.362</sub> |     515.57<sub>±7.23</sub> |
| Rust |  0.001<sub>±0.000</sub> |       1.67<sub>±1.08</sub> |


