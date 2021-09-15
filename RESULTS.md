### primes/Simple

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.344<sub>±0.047</sub> |       2.96<sub>±1.55</sub> |
| Java (Naive) |  0.389<sub>±0.071</sub> |      39.57<sub>±1.78</sub> |
| Java (GraalVM: Naive) |  0.736<sub>±0.057</sub> |     130.70<sub>±15.26</sub> |
| JavaScript (Node) |  0.430<sub>±0.113</sub> |      38.05<sub>±1.46</sub> |
| JavaScript (GraalVM Node) |  1.914<sub>±0.396</sub> |     778.52<sub>±46.92</sub> |
| PHP (Naive) |  2.439<sub>±0.148</sub> |      17.33<sub>±0.46</sub> |
| PHP (JIT: tracing) |  1.221<sub>±1.449</sub> |      20.40<sub>±0.35</sub> |
| PHP (JIT: function) |  1.406<sub>±0.235</sub> |      20.37<sub>±0.36</sub> |
| Rust |  0.347<sub>±0.052</sub> |       1.71<sub>±1.13</sub> |


### primes/Atkin

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.202<sub>±0.055</sub> |      88.87<sub>±0.26</sub> |
| Java (Naive) |  0.244<sub>±0.155</sub> |     161.73<sub>±14.71</sub> |
| Java (GraalVM: Naive) |  0.732<sub>±0.127</sub> |     287.44<sub>±23.02</sub> |
| JavaScript (Node) |  0.411<sub>±0.089</sub> |     205.74<sub>±5.26</sub> |
| JavaScript (GraalVM Node) |  3.871<sub>±1.675</sub> |     859.25<sub>±16.82</sub> |
| PHP (Naive) |  1.484<sub>±0.234</sub> |     350.10<sub>±3.00</sub> |
| PHP (JIT: tracing) |  1.612<sub>±0.164</sub> |     353.64<sub>±0.34</sub> |
| PHP (JIT: function) |  1.134<sub>±0.080</sub> |     353.30<sub>±0.33</sub> |
| Ruby (Naive) |  2.416<sub>±0.156</sub> |     163.59<sub>±0.55</sub> |
| Ruby (JIT) |  2.239<sub>±0.103</sub> |     164.19<sub>±0.55</sub> |
| Ruby (JRuby) |  4.252<sub>±0.532</sub> |     496.12<sub>±60.62</sub> |
| Ruby (TruffleRuby) |  2.343<sub>±0.438</sub> |     861.17<sub>±22.77</sub> |
| Ruby (TruffleRuby JVM) |  6.475<sub>±4.737</sub> |     860.51<sub>±37.79</sub> |
| Ruby (GraalVM) |  6.187<sub>±1.688</sub> |     855.49<sub>±37.08</sub> |
| Rust |  0.175<sub>±0.063</sub> |      77.46<sub>±0.12</sub> |


### collatz/MaxSequence

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.059<sub>±0.050</sub> |       3.02<sub>±1.60</sub> |
| Java (Naive) |  0.119<sub>±0.083</sub> |      35.92<sub>±0.81</sub> |
| Java (GraalVM: Naive) |  0.462<sub>±0.096</sub> |      74.82<sub>±6.52</sub> |
| JavaScript (Node) |  0.768<sub>±0.135</sub> |      32.12<sub>±1.83</sub> |
| JavaScript (GraalVM Node) |  1.009<sub>±0.204</sub> |     470.14<sub>±20.10</sub> |
| PHP (Naive) |  0.829<sub>±0.095</sub> |      17.38<sub>±0.33</sub> |
| PHP (JIT: tracing) |  0.341<sub>±0.059</sub> |      20.64<sub>±0.36</sub> |
| PHP (JIT: function) |  0.462<sub>±0.076</sub> |      20.43<sub>±0.87</sub> |
| Rust |  0.060<sub>±0.008</sub> |       1.71<sub>±0.17</sub> |


### mandelbrot/Simple

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.034<sub>±0.067</sub> |       1.54<sub>±1.69</sub> |
| Java (Naive) |  0.070<sub>±0.054</sub> |      37.12<sub>±0.51</sub> |
| Java (GraalVM: Naive) |  0.415<sub>±0.088</sub> |      75.14<sub>±5.93</sub> |
| JavaScript (Node) |  0.072<sub>±0.106</sub> |      37.30<sub>±5.68</sub> |
| JavaScript (GraalVM Node) |  0.399<sub>±0.085</sub> |     503.86<sub>±9.67</sub> |
| PHP (Naive) |  0.409<sub>±0.072</sub> |      17.37<sub>±0.37</sub> |
| PHP (JIT: tracing) |  0.127<sub>±0.054</sub> |      20.63<sub>±0.65</sub> |
| PHP (JIT: function) |  0.170<sub>±0.106</sub> |      20.49<sub>±0.89</sub> |
| Rust |  0.033<sub>±0.082</sub> |       1.71<sub>±0.17</sub> |


### io/Load

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.074<sub>±0.064</sub> |       3.00<sub>±1.58</sub> |
| Go |  0.123<sub>±0.056</sub> |       2.65<sub>±2.00</sub> |
| Java (Naive) |  0.199<sub>±0.058</sub> |      67.01<sub>±9.43</sub> |
| Java (GraalVM: Naive) |  0.731<sub>±0.122</sub> |     172.41<sub>±22.19</sub> |
| JavaScript (Node) |  1.133<sub>±0.091</sub> |      62.68<sub>±2.53</sub> |
| JavaScript (GraalVM Node) |  3.869<sub>±0.341</sub> |     823.98<sub>±54.93</sub> |
| PHP (Naive) |  0.086<sub>±0.041</sub> |      17.43<sub>±0.47</sub> |
| PHP (JIT: tracing) |  0.082<sub>±0.020</sub> |      20.54<sub>±0.35</sub> |
| PHP (JIT: function) |  0.082<sub>±0.022</sub> |      20.37<sub>±0.43</sub> |
| Python (Python 3) |  0.109<sub>±0.022</sub> |       7.28<sub>±0.53</sub> |
| Python (GraalVM Python) |  2.768<sub>±0.498</sub> |     790.27<sub>±35.95</sub> |
| Ruby (Naive) |  0.211<sub>±0.065</sub> |      13.65<sub>±0.15</sub> |
| Ruby (JIT) |  0.269<sub>±0.094</sub> |      14.07<sub>±0.28</sub> |
| Ruby (JRuby) |  2.046<sub>±0.338</sub> |     195.48<sub>±15.37</sub> |
| Ruby (TruffleRuby) |  1.058<sub>±0.408</sub> |     687.97<sub>±45.96</sub> |
| Ruby (TruffleRuby JVM) |  4.154<sub>±0.533</sub> |     597.88<sub>±52.87</sub> |
| Ruby (GraalVM) |  4.367<sub>±0.305</sub> |     610.00<sub>±53.33</sub> |
| Rust |  0.074<sub>±0.044</sub> |       1.73<sub>±1.14</sub> |


### io/NoLoad

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.001<sub>±0.001</sub> |       1.48<sub>±1.75</sub> |
| Go |  0.001<sub>±0.001</sub> |       2.65<sub>±2.65</sub> |
| Java (Naive) |  0.025<sub>±0.086</sub> |      34.26<sub>±0.24</sub> |
| Java (GraalVM: Naive) |  0.373<sub>±0.315</sub> |      63.79<sub>±7.41</sub> |
| JavaScript (Node) |  0.026<sub>±0.104</sub> |      35.14<sub>±4.12</sub> |
| JavaScript (GraalVM Node) |  0.231<sub>±0.157</sub> |     407.63<sub>±36.78</sub> |
| PHP (Naive) |  0.010<sub>±0.003</sub> |      17.27<sub>±0.38</sub> |
| PHP (JIT: tracing) |  0.010<sub>±0.044</sub> |      20.43<sub>±0.31</sub> |
| PHP (JIT: function) |  0.010<sub>±0.005</sub> |      20.43<sub>±0.37</sub> |
| Python (Python 3) |  0.024<sub>±0.073</sub> |       7.12<sub>±0.45</sub> |
| Python (GraalVM Python) |  0.207<sub>±0.118</sub> |     327.65<sub>±38.65</sub> |
| Ruby (Naive) |  0.055<sub>±0.065</sub> |      13.31<sub>±0.13</sub> |
| Ruby (JIT) |  0.239<sub>±0.108</sub> |      13.69<sub>±0.12</sub> |
| Ruby (JRuby) |  1.693<sub>±0.470</sub> |     183.47<sub>±23.38</sub> |
| Ruby (TruffleRuby) |  0.082<sub>±0.231</sub> |     222.66<sub>±12.48</sub> |
| Ruby (TruffleRuby JVM) |  2.262<sub>±0.133</sub> |     515.02<sub>±8.14</sub> |
| Ruby (GraalVM) |  2.244<sub>±0.359</sub> |     514.29<sub>±13.82</sub> |
| Rust |  0.001<sub>±0.001</sub> |       0.65<sub>±1.20</sub> |


