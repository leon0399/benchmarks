### primes/Simple

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.442<sub>±0.004</sub> |       1.48<sub>±1.71</sub> |
| Java (Naive) |  0.487<sub>±0.028</sub> |      38.29<sub>±1.51</sub> |
| Java (Naive (GraalVM)) |  0.850<sub>±0.019</sub> |     130.68<sub>±7.89</sub> |
| JavaScript |  0.542<sub>±0.068</sub> |      38.87<sub>±2.01</sub> |
| JavaScript (GraalVM) |  0.594<sub>±0.284</sub> |     100.01<sub>±7.78</sub> |
| PHP (Naive) |  3.179<sub>±0.383</sub> |      17.25<sub>±0.50</sub> |
| PHP (JIT: tracing) |  1.493<sub>±0.168</sub> |      20.35<sub>±0.31</sub> |
| PHP (JIT: function) |  1.742<sub>±0.091</sub> |      20.30<sub>±0.30</sub> |
| Rust |  0.440<sub>±0.005</sub> |       1.74<sub>±0.08</sub> |


### primes/Atkin

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.222<sub>±0.109</sub> |      88.79<sub>±0.90</sub> |
| Java (Naive) |  0.259<sub>±0.084</sub> |     171.70<sub>±11.96</sub> |
| Java (Naive (GraalVM)) |  0.749<sub>±0.083</sub> |     289.90<sub>±32.45</sub> |
| JavaScript |  0.450<sub>±0.071</sub> |     205.57<sub>±1.83</sub> |
| JavaScript (GraalVM) |  1.887<sub>±0.139</sub> |     884.23<sub>±83.68</sub> |
| PHP (Naive) |  1.776<sub>±0.118</sub> |     347.01<sub>±1.61</sub> |
| PHP (JIT: tracing) |  1.948<sub>±0.329</sub> |     351.90<sub>±2.82</sub> |
| PHP (JIT: function) |  1.289<sub>±0.226</sub> |     351.70<sub>±0.29</sub> |
| Ruby (Naive) |  2.893<sub>±0.412</sub> |     163.63<sub>±0.55</sub> |
| Ruby (JIT) |  2.678<sub>±0.319</sub> |     164.29<sub>±0.48</sub> |
| Ruby (JRuby) |  4.798<sub>±0.444</sub> |     512.46<sub>±56.93</sub> |
| Ruby (TruffleRuby) |  2.016<sub>±0.236</sub> |     929.06<sub>±49.47</sub> |
| Ruby (TruffleRuby JVM) |  5.843<sub>±0.392</sub> |     914.37<sub>±74.21</sub> |
| Rust |  0.207<sub>±0.119</sub> |      77.45<sub>±0.10</sub> |


### collatz/MaxSequence

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.075<sub>±0.001</sub> |       1.47<sub>±1.71</sub> |
| Java (Naive) |  0.147<sub>±0.037</sub> |      35.95<sub>±0.15</sub> |
| Java (Naive (GraalVM)) |  0.504<sub>±0.035</sub> |      75.51<sub>±3.34</sub> |
| JavaScript |  0.987<sub>±0.054</sub> |      31.89<sub>±2.00</sub> |
| JavaScript (GraalVM) |  1.016<sub>±0.026</sub> |     123.96<sub>±4.05</sub> |
| PHP (Naive) |  1.048<sub>±0.073</sub> |      17.48<sub>±0.25</sub> |
| PHP (JIT: tracing) |  0.434<sub>±0.054</sub> |      20.61<sub>±0.31</sub> |
| PHP (JIT: function) |  0.579<sub>±0.159</sub> |      20.36<sub>±0.38</sub> |
| Rust |  0.076<sub>±0.001</sub> |       1.70<sub>±0.17</sub> |


### mandelbrot/Simple

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.043<sub>±0.053</sub> |       1.51<sub>±1.69</sub> |
| Java (Naive) |  0.084<sub>±0.050</sub> |      37.20<sub>±0.53</sub> |
| Java (Naive (GraalVM)) |  0.439<sub>±0.041</sub> |      76.44<sub>±4.30</sub> |
| JavaScript |  0.106<sub>±0.046</sub> |      36.80<sub>±2.14</sub> |
| JavaScript (GraalVM) |  0.081<sub>±0.047</sub> |     100.15<sub>±5.59</sub> |
| PHP (Naive) |  0.514<sub>±0.100</sub> |      17.45<sub>±0.35</sub> |
| PHP (JIT: tracing) |  0.161<sub>±0.001</sub> |      20.51<sub>±0.35</sub> |
| PHP (JIT: function) |  0.214<sub>±0.049</sub> |      20.56<sub>±0.30</sub> |
| Rust |  0.042<sub>±0.025</sub> |       1.76<sub>±0.09</sub> |


### io/Load

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.096<sub>±0.053</sub> |       1.47<sub>±1.68</sub> |
| Java (Naive) |  0.234<sub>±0.055</sub> |      77.93<sub>±3.06</sub> |
| Java (Naive (GraalVM)) |  0.796<sub>±0.245</sub> |     172.63<sub>±12.25</sub> |
| JavaScript |  1.395<sub>±0.156</sub> |      61.10<sub>±1.85</sub> |
| JavaScript (GraalVM) |  0.850<sub>±0.252</sub> |     350.99<sub>±5.71</sub> |
| PHP (Naive) |  0.109<sub>±0.052</sub> |      17.42<sub>±0.30</sub> |
| PHP (JIT: tracing) |  0.104<sub>±0.051</sub> |      20.47<sub>±0.32</sub> |
| PHP (JIT: function) |  0.105<sub>±0.067</sub> |      20.40<sub>±0.40</sub> |
| Ruby (Naive) |  0.263<sub>±0.048</sub> |      13.67<sub>±0.06</sub> |
| Ruby (JIT) |  0.321<sub>±0.361</sub> |      14.04<sub>±0.16</sub> |
| Ruby (JRuby) |  2.441<sub>±0.270</sub> |     188.81<sub>±23.35</sub> |
| Ruby (TruffleRuby) |  1.251<sub>±0.131</sub> |     681.85<sub>±38.33</sub> |
| Ruby (TruffleRuby JVM) |  4.785<sub>±0.153</sub> |     605.22<sub>±35.12</sub> |
| Rust |  0.094<sub>±0.017</sub> |       1.73<sub>±0.07</sub> |


### io/NoLoad

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.001<sub>±0.000</sub> |       1.48<sub>±0.06</sub> |
| Java (Naive) |  0.029<sub>±0.065</sub> |      34.22<sub>±0.20</sub> |
| Java (Naive (GraalVM)) |  0.385<sub>±0.059</sub> |      61.90<sub>±7.60</sub> |
| JavaScript |  0.031<sub>±0.002</sub> |      33.54<sub>±1.85</sub> |
| JavaScript (GraalVM) |  0.032<sub>±0.006</sub> |      72.31<sub>±3.90</sub> |
| PHP (Naive) |  0.013<sub>±0.003</sub> |      17.32<sub>±0.24</sub> |
| PHP (JIT: tracing) |  0.012<sub>±0.001</sub> |      20.48<sub>±0.16</sub> |
| PHP (JIT: function) |  0.015<sub>±0.028</sub> |      20.48<sub>±1.61</sub> |
| Ruby (Naive) |  0.069<sub>±0.033</sub> |      13.29<sub>±0.07</sub> |
| Ruby (JIT) |  0.302<sub>±0.048</sub> |      13.68<sub>±0.12</sub> |
| Ruby (JRuby) |  2.009<sub>±0.095</sub> |     181.08<sub>±4.63</sub> |
| Ruby (TruffleRuby) |  0.101<sub>±0.080</sub> |     222.50<sub>±4.07</sub> |
| Ruby (TruffleRuby JVM) |  2.534<sub>±0.328</sub> |     507.58<sub>±23.89</sub> |
| Rust |  0.001<sub>±0.003</sub> |       1.67<sub>±1.08</sub> |


