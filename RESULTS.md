### primes/Simple

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.440<sub>±0.008</sub> |       3.00<sub>±1.58</sub> |
| Java (Naive) |  0.486<sub>±0.059</sub> |      39.51<sub>±1.53</sub> |
| Java (Naive (GraalVM)) |  0.849<sub>±0.064</sub> |     128.19<sub>±9.90</sub> |
| JavaScript |  0.526<sub>±0.035</sub> |      37.78<sub>±3.12</sub> |
| JavaScript (GraalVM) |  0.610<sub>±0.087</sub> |      99.86<sub>±4.82</sub> |
| PHP (Naive) |  3.076<sub>±0.192</sub> |      17.21<sub>±0.20</sub> |
| PHP (JIT: tracing) |  1.538<sub>±0.179</sub> |      20.32<sub>±0.25</sub> |
| PHP (JIT: function) |  1.772<sub>±0.278</sub> |      20.26<sub>±0.36</sub> |
| Rust |  0.445<sub>±0.013</sub> |       1.71<sub>±0.07</sub> |


### primes/Atkin

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.222<sub>±0.110</sub> |      88.96<sub>±0.14</sub> |
| Java (Naive) |  0.276<sub>±0.048</sub> |     170.44<sub>±9.20</sub> |
| Java (Naive (GraalVM)) |  0.747<sub>±0.068</sub> |     292.14<sub>±15.80</sub> |
| JavaScript |  0.453<sub>±0.051</sub> |     205.27<sub>±2.06</sub> |
| JavaScript (GraalVM) |  1.808<sub>±0.294</sub> |     883.98<sub>±12.45</sub> |
| PHP (Naive) |  1.749<sub>±0.137</sub> |     348.35<sub>±1.26</sub> |
| PHP (JIT: tracing) |  1.931<sub>±0.278</sub> |     352.00<sub>±0.30</sub> |
| PHP (JIT: function) |  1.361<sub>±0.110</sub> |     351.67<sub>±0.16</sub> |
| Ruby (Naive) |  3.071<sub>±0.308</sub> |     163.64<sub>±0.53</sub> |
| Ruby (JIT) |  2.850<sub>±0.508</sub> |     164.23<sub>±0.55</sub> |
| Ruby (JRuby) |  5.118<sub>±0.458</sub> |     492.05<sub>±53.97</sub> |
| Ruby (TruffleRuby) |  1.984<sub>±0.074</sub> |     910.04<sub>±45.45</sub> |
| Ruby (TruffleRuby JVM) |  6.166<sub>±0.961</sub> |     893.27<sub>±34.88</sub> |
| Rust |  0.216<sub>±0.074</sub> |      77.49<sub>±0.13</sub> |


### collatz/MaxSequence

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.075<sub>±0.002</sub> |       2.22<sub>±0.99</sub> |
| Java (Naive) |  0.147<sub>±0.033</sub> |      35.99<sub>±0.15</sub> |
| Java (Naive (GraalVM)) |  0.502<sub>±0.062</sub> |      74.37<sub>±2.80</sub> |
| JavaScript |  0.989<sub>±0.029</sub> |      33.56<sub>±2.12</sub> |
| JavaScript (GraalVM) |  1.020<sub>±0.032</sub> |     125.41<sub>±4.46</sub> |
| PHP (Naive) |  1.101<sub>±0.325</sub> |      17.38<sub>±0.46</sub> |
| PHP (JIT: tracing) |  0.448<sub>±0.060</sub> |      20.55<sub>±0.20</sub> |
| PHP (JIT: function) |  0.611<sub>±0.054</sub> |      20.25<sub>±0.24</sub> |
| Rust |  0.077<sub>±0.010</sub> |       1.70<sub>±1.06</sub> |


### mandelbrot/Simple

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.043<sub>±0.058</sub> |       1.48<sub>±1.73</sub> |
| Java (Naive) |  0.085<sub>±0.036</sub> |      37.36<sub>±0.34</sub> |
| Java (Naive (GraalVM)) |  0.440<sub>±0.063</sub> |      74.87<sub>±2.92</sub> |
| JavaScript |  0.107<sub>±0.011</sub> |      36.40<sub>±2.17</sub> |
| JavaScript (GraalVM) |  0.083<sub>±0.051</sub> |     101.72<sub>±5.26</sub> |
| PHP (Naive) |  0.561<sub>±0.080</sub> |      17.24<sub>±0.35</sub> |
| PHP (JIT: tracing) |  0.164<sub>±0.005</sub> |      20.59<sub>±0.35</sub> |
| PHP (JIT: function) |  0.219<sub>±0.049</sub> |      20.39<sub>±0.28</sub> |
| Rust |  0.042<sub>±0.001</sub> |       1.72<sub>±0.12</sub> |


### io/Load

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.094<sub>±0.007</sub> |       2.21<sub>±0.89</sub> |
| Java (Naive) |  0.231<sub>±0.075</sub> |      77.20<sub>±8.77</sub> |
| Java (Naive (GraalVM)) |  0.795<sub>±0.186</sub> |     175.15<sub>±19.96</sub> |
| JavaScript |  1.399<sub>±0.142</sub> |      60.99<sub>±1.84</sub> |
| JavaScript (GraalVM) |  0.828<sub>±0.217</sub> |     346.69<sub>±3.90</sub> |
| PHP (Naive) |  0.116<sub>±0.062</sub> |      17.37<sub>±0.33</sub> |
| PHP (JIT: tracing) |  0.109<sub>±0.033</sub> |      20.50<sub>±0.36</sub> |
| PHP (JIT: function) |  0.106<sub>±0.035</sub> |      20.39<sub>±0.45</sub> |
| Ruby (Naive) |  0.256<sub>±0.004</sub> |      13.65<sub>±2.03</sub> |
| Ruby (JIT) |  0.364<sub>±0.312</sub> |      14.00<sub>±0.12</sub> |
| Ruby (JRuby) |  2.484<sub>±0.249</sub> |     189.80<sub>±4.44</sub> |
| Ruby (TruffleRuby) |  1.297<sub>±0.216</sub> |     687.16<sub>±48.17</sub> |
| Ruby (TruffleRuby JVM) |  5.098<sub>±4.425</sub> |     603.17<sub>±100.29</sub> |
| Rust |  0.095<sub>±0.054</sub> |       1.71<sub>±0.10</sub> |


### io/NoLoad

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.001<sub>±0.002</sub> |       1.48<sub>±1.69</sub> |
| Java (Naive) |  0.029<sub>±0.006</sub> |      34.23<sub>±0.24</sub> |
| Java (Naive (GraalVM)) |  0.387<sub>±0.005</sub> |      62.14<sub>±4.14</sub> |
| JavaScript |  0.032<sub>±0.038</sub> |      34.19<sub>±1.20</sub> |
| JavaScript (GraalVM) |  0.032<sub>±0.002</sub> |      72.16<sub>±5.75</sub> |
| PHP (Naive) |  0.015<sub>±0.002</sub> |      17.38<sub>±0.38</sub> |
| PHP (JIT: tracing) |  0.014<sub>±0.001</sub> |      20.44<sub>±0.23</sub> |
| PHP (JIT: function) |  0.014<sub>±0.005</sub> |      20.35<sub>±0.28</sub> |
| Ruby (Naive) |  0.076<sub>±0.074</sub> |      13.23<sub>±0.11</sub> |
| Ruby (JIT) |  0.358<sub>±0.249</sub> |      13.62<sub>±0.07</sub> |
| Ruby (JRuby) |  2.040<sub>±0.439</sub> |     183.11<sub>±9.17</sub> |
| Ruby (TruffleRuby) |  0.108<sub>±0.291</sub> |     222.18<sub>±4.64</sub> |
| Ruby (TruffleRuby JVM) |  2.688<sub>±1.150</sub> |     490.19<sub>±27.07</sub> |
| Rust |  0.001<sub>±0.003</sub> |       1.15<sub>±0.59</sub> |


