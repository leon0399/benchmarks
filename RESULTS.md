### primes/Simple

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.342<sub>±0.018</sub> |       2.97<sub>±1.56</sub> |
| Java (Naive) |  0.385<sub>±0.095</sub> |      40.00<sub>±1.77</sub> |
| Java (GraalVM: Naive) |  0.729<sub>±0.021</sub> |     130.69<sub>±12.79</sub> |
| JavaScript (Node) |  0.439<sub>±0.025</sub> |      37.40<sub>±2.01</sub> |
| JavaScript (GraalVM Node) |  2.044<sub>±0.606</sub> |     782.93<sub>±53.50</sub> |
| PHP (Naive) |  2.436<sub>±0.410</sub> |      17.45<sub>±0.49</sub> |
| PHP (JIT: tracing) |  1.415<sub>±0.639</sub> |      20.50<sub>±0.62</sub> |
| PHP (JIT: function) |  1.544<sub>±0.772</sub> |      20.30<sub>±0.41</sub> |
| Ruby (Naive) |  8.745<sub>±4.333</sub> |      13.71<sub>±0.19</sub> |
| Ruby (JIT) |  6.037<sub>±0.915</sub> |      14.14<sub>±0.12</sub> |
| Ruby (JRuby) | 11.170<sub>±2.573</sub> |     413.73<sub>±89.32</sub> |
| Ruby (TruffleRuby) |  0.779<sub>±0.244</sub> |     670.48<sub>±20.07</sub> |
| Ruby (TruffleRuby JVM) |  3.586<sub>±0.393</sub> |     705.88<sub>±223.75</sub> |
| Ruby (GraalVM) |  0.787<sub>±0.079</sub> |     669.42<sub>±13.26</sub> |
| Ruby (GraalVM JVM) |  3.591<sub>±0.371</sub> |     709.02<sub>±249.35</sub> |
| Rust |  0.343<sub>±0.050</sub> |       1.71<sub>±0.09</sub> |


### primes/Atkin

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.190<sub>±0.134</sub> |      88.88<sub>±0.22</sub> |
| Java (Naive) |  0.253<sub>±0.195</sub> |     192.13<sub>±17.02</sub> |
| Java (GraalVM: Naive) |  0.715<sub>±1.079</sub> |     301.27<sub>±27.12</sub> |
| JavaScript (Node) |  0.344<sub>±0.099</sub> |     208.24<sub>±1.99</sub> |
| JavaScript (GraalVM Node) |  1.824<sub>±0.370</sub> |     984.69<sub>±77.98</sub> |
| PHP (Naive) |  1.577<sub>±0.255</sub> |     344.34<sub>±1.57</sub> |
| PHP (JIT: tracing) |  1.625<sub>±0.111</sub> |     347.86<sub>±1.55</sub> |
| PHP (JIT: function) |  1.132<sub>±0.141</sub> |     347.52<sub>±1.55</sub> |
| Ruby (Naive) |  2.494<sub>±0.110</sub> |     160.57<sub>±0.11</sub> |
| Ruby (JIT) |  2.310<sub>±0.150</sub> |     161.17<sub>±0.11</sub> |
| Ruby (JRuby) |  3.486<sub>±0.400</sub> |     532.08<sub>±73.97</sub> |
| Ruby (TruffleRuby) |  1.414<sub>±0.089</sub> |     880.38<sub>±35.65</sub> |
| Ruby (TruffleRuby JVM) |  3.678<sub>±0.428</sub> |     935.76<sub>±94.71</sub> |
| Ruby (GraalVM) |  1.428<sub>±0.103</sub> |     880.82<sub>±39.63</sub> |
| Ruby (GraalVM JVM) |  3.697<sub>±0.175</sub> |     911.69<sub>±139.29</sub> |
| Rust |  0.182<sub>±0.150</sub> |      77.46<sub>±0.29</sub> |


### collatz/MaxSequence

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.059<sub>±0.058</sub> |       3.05<sub>±1.59</sub> |
| Java (Naive) |  0.127<sub>±0.140</sub> |      36.35<sub>±1.71</sub> |
| Java (GraalVM: Naive) |  0.471<sub>±0.145</sub> |      75.67<sub>±5.57</sub> |
| JavaScript (Node) |  0.756<sub>±0.074</sub> |      33.73<sub>±2.08</sub> |
| JavaScript (GraalVM Node) |  0.991<sub>±0.156</sub> |     469.87<sub>±21.39</sub> |
| PHP (Naive) |  0.835<sub>±0.113</sub> |      17.40<sub>±0.35</sub> |
| PHP (JIT: tracing) |  0.342<sub>±0.169</sub> |      20.63<sub>±0.56</sub> |
| PHP (JIT: function) |  0.461<sub>±0.070</sub> |      20.43<sub>±0.37</sub> |
| Ruby (Naive) |  2.449<sub>±0.075</sub> |      13.33<sub>±1.99</sub> |
| Ruby (JIT) |  0.660<sub>±0.081</sub> |      13.75<sub>±0.13</sub> |
| Ruby (JRuby) |  2.550<sub>±0.490</sub> |     340.79<sub>±134.33</sub> |
| Ruby (TruffleRuby) |  0.452<sub>±0.051</sub> |     438.33<sub>±9.24</sub> |
| Ruby (TruffleRuby JVM) |  2.496<sub>±0.384</sub> |     569.52<sub>±100.08</sub> |
| Ruby (GraalVM) |  0.450<sub>±0.045</sub> |     437.59<sub>±6.08</sub> |
| Ruby (GraalVM JVM) |  2.490<sub>±0.329</sub> |     575.27<sub>±97.54</sub> |
| Rust |  0.060<sub>±0.009</sub> |       1.73<sub>±0.11</sub> |


### mandelbrot/Simple

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.033<sub>±0.043</sub> |       1.48<sub>±1.74</sub> |
| Java (Naive) |  0.084<sub>±0.831</sub> |      37.54<sub>±0.61</sub> |
| Java (GraalVM: Naive) |  0.416<sub>±0.184</sub> |      75.59<sub>±6.30</sub> |
| JavaScript (Node) |  0.072<sub>±0.051</sub> |      37.33<sub>±2.17</sub> |
| JavaScript (GraalVM Node) |  0.386<sub>±0.068</sub> |     503.05<sub>±11.06</sub> |
| PHP (Naive) |  0.416<sub>±0.086</sub> |      17.51<sub>±0.39</sub> |
| PHP (JIT: tracing) |  0.123<sub>±0.033</sub> |      20.61<sub>±0.37</sub> |
| PHP (JIT: function) |  0.165<sub>±0.048</sub> |      20.52<sub>±0.78</sub> |
| Ruby (Naive) |  1.608<sub>±0.144</sub> |      13.69<sub>±0.13</sub> |
| Ruby (JIT) |  1.244<sub>±0.123</sub> |      14.13<sub>±0.12</sub> |
| Ruby (JRuby) |  3.186<sub>±0.466</sub> |     377.29<sub>±102.81</sub> |
| Ruby (TruffleRuby) |  0.308<sub>±0.093</sub> |     626.13<sub>±9.95</sub> |
| Ruby (TruffleRuby JVM) |  2.703<sub>±0.328</sub> |     629.11<sub>±180.19</sub> |
| Ruby (GraalVM) |  0.307<sub>±0.134</sub> |     625.52<sub>±16.53</sub> |
| Ruby (GraalVM JVM) |  2.736<sub>±0.262</sub> |     616.50<sub>±141.24</sub> |
| Rust |  0.033<sub>±0.066</sub> |       1.74<sub>±1.16</sub> |


### io/Load

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.075<sub>±0.077</sub> |       1.53<sub>±1.69</sub> |
| Go |  0.122<sub>±0.033</sub> |       2.68<sub>±2.15</sub> |
| Java (Naive) |  0.186<sub>±0.057</sub> |      76.81<sub>±11.81</sub> |
| Java (GraalVM: Naive) |  0.710<sub>±0.066</sub> |     171.74<sub>±18.25</sub> |
| JavaScript (Node) |  1.138<sub>±0.105</sub> |      64.33<sub>±2.66</sub> |
| JavaScript (GraalVM Node) |  3.642<sub>±0.340</sub> |     874.81<sub>±64.20</sub> |
| PHP (Naive) |  0.084<sub>±0.073</sub> |      17.43<sub>±0.37</sub> |
| PHP (JIT: tracing) |  0.080<sub>±0.053</sub> |      20.53<sub>±0.34</sub> |
| PHP (JIT: function) |  0.080<sub>±0.075</sub> |      20.42<sub>±0.66</sub> |
| Python (Python 3) |  0.107<sub>±0.044</sub> |       7.27<sub>±0.51</sub> |
| Python (GraalVM Python) |  2.614<sub>±0.469</sub> |     808.12<sub>±46.06</sub> |
| Ruby (Naive) |  0.200<sub>±0.063</sub> |      13.69<sub>±2.00</sub> |
| Ruby (JIT) |  0.255<sub>±0.248</sub> |      14.06<sub>±0.12</sub> |
| Ruby (JRuby) |  1.955<sub>±0.384</sub> |     196.21<sub>±31.12</sub> |
| Ruby (TruffleRuby) |  1.019<sub>±0.215</sub> |     692.68<sub>±52.04</sub> |
| Ruby (TruffleRuby JVM) |  3.837<sub>±0.272</sub> |     620.71<sub>±74.70</sub> |
| Ruby (GraalVM) |  1.060<sub>±0.238</sub> |     694.44<sub>±41.17</sub> |
| Ruby (GraalVM JVM) |  3.846<sub>±0.306</sub> |     624.00<sub>±81.59</sub> |
| Rust |  0.073<sub>±0.075</sub> |       1.74<sub>±1.16</sub> |


### io/NoLoad

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.001<sub>±0.000</sub> |       1.47<sub>±1.78</sub> |
| Go |  0.001<sub>±0.002</sub> |       2.68<sub>±2.13</sub> |
| Java (Naive) |  0.029<sub>±0.060</sub> |      34.56<sub>±1.00</sub> |
| Java (GraalVM: Naive) |  0.374<sub>±0.372</sub> |      63.51<sub>±8.34</sub> |
| JavaScript (Node) |  0.025<sub>±0.065</sub> |      33.54<sub>±2.04</sub> |
| JavaScript (GraalVM Node) |  0.230<sub>±0.057</sub> |     405.69<sub>±47.20</sub> |
| PHP (Naive) |  0.009<sub>±0.003</sub> |      17.41<sub>±0.59</sub> |
| PHP (JIT: tracing) |  0.009<sub>±0.047</sub> |      20.40<sub>±0.48</sub> |
| PHP (JIT: function) |  0.009<sub>±0.001</sub> |      20.43<sub>±0.47</sub> |
| Python (Python 3) |  0.023<sub>±0.033</sub> |       6.97<sub>±0.34</sub> |
| Python (GraalVM Python) |  0.185<sub>±0.084</sub> |     327.69<sub>±30.16</sub> |
| Ruby (Naive) |  0.053<sub>±0.034</sub> |      13.29<sub>±0.15</sub> |
| Ruby (JIT) |  0.212<sub>±0.100</sub> |      13.69<sub>±0.14</sub> |
| Ruby (JRuby) |  1.543<sub>±0.090</sub> |     185.66<sub>±27.23</sub> |
| Ruby (TruffleRuby) |  0.076<sub>±0.063</sub> |     221.93<sub>±6.83</sub> |
| Ruby (TruffleRuby JVM) |  2.090<sub>±0.330</sub> |     527.62<sub>±15.07</sub> |
| Ruby (GraalVM) |  0.076<sub>±0.057</sub> |     220.59<sub>±9.32</sub> |
| Ruby (GraalVM JVM) |  2.086<sub>±0.330</sub> |     530.32<sub>±16.77</sub> |
| Rust |  0.001<sub>±0.059</sub> |       1.67<sub>±1.67</sub> |


### treap/Naive

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| JavaScript (Node) |  0.756<sub>±0.284</sub> |      76.25<sub>±1.93</sub> |
| JavaScript (GraalVM Node) |  2.746<sub>±0.510</sub> |     817.61<sub>±30.92</sub> |
| PHP (Naive) |  2.651<sub>±0.129</sub> |      17.41<sub>±0.35</sub> |
| PHP (JIT: tracing) |  1.638<sub>±0.129</sub> |      20.75<sub>±0.35</sub> |
| PHP (JIT: function) |  1.719<sub>±0.147</sub> |      20.58<sub>±0.82</sub> |
| Ruby (Naive) |  5.153<sub>±0.626</sub> |      13.86<sub>±0.19</sub> |
| Ruby (JIT) |  4.494<sub>±0.141</sub> |      14.54<sub>±0.13</sub> |
| Ruby (JRuby) |  5.096<sub>±0.663</sub> |     228.87<sub>±60.18</sub> |
| Ruby (TruffleRuby) |  1.477<sub>±0.103</sub> |     699.13<sub>±33.58</sub> |
| Ruby (TruffleRuby JVM) |  3.693<sub>±0.475</sub> |     906.45<sub>±197.60</sub> |
| Ruby (GraalVM) |  1.497<sub>±0.113</sub> |     702.12<sub>±32.60</sub> |
| Ruby (GraalVM JVM) |  3.713<sub>±0.854</sub> |     923.42<sub>±234.05</sub> |


