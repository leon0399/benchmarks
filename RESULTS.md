### primes/Simple

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.342<sub>±0.046</sub> |       1.54<sub>±1.72</sub> |
| Java (Naive) |  0.382<sub>±0.080</sub> |      39.32<sub>±1.07</sub> |
| Java (GraalVM: Naive) |  0.728<sub>±0.011</sub> |     129.15<sub>±15.01</sub> |
| JavaScript (Node) |  0.411<sub>±0.045</sub> |      39.04<sub>±1.91</sub> |
| JavaScript (GraalVM Node) |  1.871<sub>±0.118</sub> |     783.03<sub>±16.62</sub> |
| PHP (Naive) |  2.399<sub>±0.157</sub> |      17.34<sub>±0.27</sub> |
| PHP (JIT: tracing) |  1.221<sub>±0.055</sub> |      20.45<sub>±0.40</sub> |
| PHP (JIT: function) |  1.439<sub>±0.189</sub> |      20.38<sub>±0.65</sub> |
| Ruby (Naive) |  8.857<sub>±0.228</sub> |      13.66<sub>±0.09</sub> |
| Ruby (JIT) |  6.079<sub>±0.341</sub> |      14.20<sub>±0.12</sub> |
| Ruby (JRuby) | 11.828<sub>±2.576</sub> |     366.82<sub>±54.59</sub> |
| Ruby (TruffleRuby) |  0.836<sub>±0.117</sub> |     667.92<sub>±14.19</sub> |
| Ruby (TruffleRuby JVM) |  3.983<sub>±0.596</sub> |     766.88<sub>±138.26</sub> |
| Ruby (GraalVM) |  0.782<sub>±0.059</sub> |     668.91<sub>±5.18</sub> |
| Ruby (GraalVM JVM) |  3.676<sub>±0.104</sub> |     709.51<sub>±89.45</sub> |
| Rust |  0.345<sub>±0.032</sub> |       1.69<sub>±0.06</sub> |


### primes/Atkin

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.212<sub>±0.103</sub> |      88.88<sub>±0.18</sub> |
| Java (Naive) |  0.279<sub>±0.326</sub> |     193.60<sub>±17.56</sub> |
| Java (GraalVM: Naive) |  0.662<sub>±0.093</sub> |     299.31<sub>±18.92</sub> |
| JavaScript (Node) |  0.337<sub>±0.053</sub> |     209.75<sub>±8.10</sub> |
| JavaScript (GraalVM Node) |  1.871<sub>±0.170</sub> |     995.14<sub>±86.95</sub> |
| PHP (Naive) |  1.448<sub>±0.128</sub> |     348.52<sub>±0.31</sub> |
| PHP (JIT: tracing) |  1.625<sub>±0.097</sub> |     352.02<sub>±0.28</sub> |
| PHP (JIT: function) |  1.139<sub>±0.052</sub> |     351.71<sub>±1.20</sub> |
| Python (Python 3) |  4.413<sub>±0.493</sub> |     245.85<sub>±0.15</sub> |
| Python (GraalVM Python) |  1.583<sub>±0.386</sub> |     923.79<sub>±102.99</sub> |
| Ruby (Naive) |  2.501<sub>±0.051</sub> |     160.60<sub>±0.07</sub> |
| Ruby (JIT) |  2.303<sub>±0.110</sub> |     161.15<sub>±0.12</sub> |
| Ruby (JRuby) |  3.666<sub>±0.267</sub> |     520.11<sub>±59.10</sub> |
| Ruby (TruffleRuby) |  1.412<sub>±0.092</sub> |     872.65<sub>±15.67</sub> |
| Ruby (TruffleRuby JVM) |  3.802<sub>±0.240</sub> |     958.58<sub>±107.00</sub> |
| Ruby (GraalVM) |  1.438<sub>±0.312</sub> |     875.83<sub>±42.02</sub> |
| Ruby (GraalVM JVM) |  3.775<sub>±0.242</sub> |     915.80<sub>±113.08</sub> |
| Rust |  0.166<sub>±0.028</sub> |      77.47<sub>±0.10</sub> |


### collatz/MaxSequence

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.060<sub>±0.001</sub> |       1.53<sub>±1.72</sub> |
| Java (Naive) |  0.119<sub>±0.048</sub> |      36.32<sub>±0.19</sub> |
| Java (GraalVM: Naive) |  0.462<sub>±0.058</sub> |      75.52<sub>±3.75</sub> |
| JavaScript (Node) |  0.755<sub>±0.037</sub> |      33.78<sub>±2.02</sub> |
| JavaScript (GraalVM Node) |  0.987<sub>±0.045</sub> |     466.00<sub>±9.04</sub> |
| PHP (Naive) |  0.843<sub>±0.176</sub> |      17.44<sub>±0.30</sub> |
| PHP (JIT: tracing) |  0.342<sub>±0.030</sub> |      20.54<sub>±0.72</sub> |
| PHP (JIT: function) |  0.456<sub>±0.091</sub> |      20.47<sub>±0.38</sub> |
| Ruby (Naive) |  2.448<sub>±0.059</sub> |      13.34<sub>±0.13</sub> |
| Ruby (JIT) |  0.659<sub>±0.069</sub> |      13.76<sub>±0.08</sub> |
| Ruby (JRuby) |  2.614<sub>±0.357</sub> |     322.12<sub>±66.16</sub> |
| Ruby (TruffleRuby) |  0.472<sub>±0.101</sub> |     439.80<sub>±8.38</sub> |
| Ruby (TruffleRuby JVM) |  2.623<sub>±0.158</sub> |     578.42<sub>±123.43</sub> |
| Ruby (GraalVM) |  0.449<sub>±0.131</sub> |     439.19<sub>±7.54</sub> |
| Ruby (GraalVM JVM) |  2.553<sub>±0.112</sub> |     582.82<sub>±53.52</sub> |
| Rust |  0.060<sub>±0.019</sub> |       1.72<sub>±0.12</sub> |


### mandelbrot/Simple

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.033<sub>±0.069</sub> |       3.01<sub>±1.60</sub> |
| Java (Naive) |  0.067<sub>±0.025</sub> |      37.69<sub>±0.47</sub> |
| Java (GraalVM: Naive) |  0.413<sub>±0.063</sub> |      76.13<sub>±3.42</sub> |
| JavaScript (Node) |  0.073<sub>±0.010</sub> |      39.05<sub>±1.93</sub> |
| JavaScript (GraalVM Node) |  0.395<sub>±0.031</sub> |     504.03<sub>±12.03</sub> |
| PHP (Naive) |  0.407<sub>±0.061</sub> |      17.36<sub>±0.37</sub> |
| PHP (JIT: tracing) |  0.126<sub>±0.003</sub> |      20.66<sub>±0.32</sub> |
| PHP (JIT: function) |  0.173<sub>±0.040</sub> |      20.57<sub>±0.31</sub> |
| Ruby (Naive) |  1.577<sub>±0.140</sub> |      13.72<sub>±0.13</sub> |
| Ruby (JIT) |  1.279<sub>±0.206</sub> |      14.11<sub>±0.09</sub> |
| Ruby (JRuby) |  3.217<sub>±0.110</sub> |     369.43<sub>±25.24</sub> |
| Ruby (TruffleRuby) |  0.314<sub>±0.077</sub> |     625.93<sub>±6.85</sub> |
| Ruby (TruffleRuby JVM) |  2.763<sub>±0.063</sub> |     623.11<sub>±158.85</sub> |
| Ruby (GraalVM) |  0.307<sub>±0.069</sub> |     626.70<sub>±7.68</sub> |
| Ruby (GraalVM JVM) |  2.774<sub>±0.253</sub> |     628.10<sub>±202.89</sub> |
| Rust |  0.033<sub>±0.001</sub> |       1.68<sub>±0.11</sub> |


### io/Load

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.075<sub>±0.014</sub> |       1.50<sub>±1.75</sub> |
| Go |  0.123<sub>±0.100</sub> |       2.68<sub>±0.16</sub> |
| Java (Naive) |  0.198<sub>±0.034</sub> |      74.68<sub>±10.00</sub> |
| Java (GraalVM: Naive) |  0.718<sub>±0.050</sub> |     169.62<sub>±18.85</sub> |
| JavaScript (Node) |  1.120<sub>±0.071</sub> |      64.87<sub>±1.26</sub> |
| JavaScript (GraalVM Node) |  3.465<sub>±0.267</sub> |     879.10<sub>±67.08</sub> |
| PHP (Naive) |  0.089<sub>±0.005</sub> |      17.48<sub>±0.31</sub> |
| PHP (JIT: tracing) |  0.083<sub>±0.011</sub> |      20.66<sub>±0.37</sub> |
| PHP (JIT: function) |  0.082<sub>±0.008</sub> |      20.48<sub>±0.40</sub> |
| Python (Python 3) |  0.112<sub>±0.047</sub> |       7.27<sub>±0.48</sub> |
| Python (GraalVM Python) |  2.698<sub>±0.148</sub> |     801.11<sub>±33.66</sub> |
| Ruby (Naive) |  0.198<sub>±0.026</sub> |      13.68<sub>±0.10</sub> |
| Ruby (JIT) |  0.246<sub>±0.216</sub> |      14.07<sub>±0.14</sub> |
| Ruby (JRuby) |  1.986<sub>±0.103</sub> |     196.08<sub>±20.28</sub> |
| Ruby (TruffleRuby) |  1.051<sub>±0.157</sub> |     695.71<sub>±33.92</sub> |
| Ruby (TruffleRuby JVM) |  3.927<sub>±0.146</sub> |     640.08<sub>±46.99</sub> |
| Ruby (GraalVM) |  1.019<sub>±0.107</sub> |     688.20<sub>±32.80</sub> |
| Ruby (GraalVM JVM) |  3.884<sub>±0.198</sub> |     620.20<sub>±45.89</sub> |
| Rust |  0.074<sub>±0.034</sub> |       1.73<sub>±0.08</sub> |


### io/NoLoad

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| C++ (clang) |  0.002<sub>±0.002</sub> |       1.47<sub>±1.57</sub> |
| Go |  0.001<sub>±0.001</sub> |       2.68<sub>±0.16</sub> |
| Java (Naive) |  0.023<sub>±0.003</sub> |      34.60<sub>±0.23</sub> |
| Java (GraalVM: Naive) |  0.373<sub>±0.016</sub> |      63.11<sub>±6.04</sub> |
| JavaScript (Node) |  0.025<sub>±0.005</sub> |      34.47<sub>±1.16</sub> |
| JavaScript (GraalVM Node) |  0.218<sub>±0.032</sub> |     411.81<sub>±19.91</sub> |
| PHP (Naive) |  0.011<sub>±0.045</sub> |      17.43<sub>±0.37</sub> |
| PHP (JIT: tracing) |  0.009<sub>±0.001</sub> |      20.43<sub>±0.31</sub> |
| PHP (JIT: function) |  0.010<sub>±0.001</sub> |      20.30<sub>±0.31</sub> |
| Python (Python 3) |  0.030<sub>±0.035</sub> |       7.28<sub>±0.42</sub> |
| Python (GraalVM Python) |  0.222<sub>±0.040</sub> |     329.40<sub>±21.49</sub> |
| Ruby (Naive) |  0.053<sub>±0.017</sub> |      13.25<sub>±0.15</sub> |
| Ruby (JIT) |  0.215<sub>±0.051</sub> |      13.74<sub>±0.12</sub> |
| Ruby (JRuby) |  1.559<sub>±0.100</sub> |     183.74<sub>±8.64</sub> |
| Ruby (TruffleRuby) |  0.080<sub>±0.037</sub> |     223.38<sub>±11.45</sub> |
| Ruby (TruffleRuby JVM) |  2.137<sub>±0.304</sub> |     534.15<sub>±14.40</sub> |
| Ruby (GraalVM) |  0.080<sub>±0.016</sub> |     220.73<sub>±12.94</sub> |
| Ruby (GraalVM JVM) |  2.150<sub>±0.357</sub> |     536.71<sub>±18.99</sub> |
| Rust |  0.001<sub>±0.001</sub> |       1.74<sub>±1.11</sub> |


### treap/Naive

| Language | Time, s | Memory, MiB |
| :------- | ------: | ----------: |
| JavaScript (Node) |  0.749<sub>±0.390</sub> |      77.23<sub>±1.46</sub> |
| JavaScript (GraalVM Node) |  2.605<sub>±0.163</sub> |     815.99<sub>±15.78</sub> |
| PHP (Naive) |  2.696<sub>±0.087</sub> |      17.41<sub>±0.34</sub> |
| PHP (JIT: tracing) |  1.651<sub>±0.055</sub> |      20.68<sub>±0.29</sub> |
| PHP (JIT: function) |  1.747<sub>±0.104</sub> |      20.49<sub>±0.31</sub> |
| Ruby (Naive) |  5.134<sub>±0.125</sub> |      13.87<sub>±0.18</sub> |
| Ruby (JIT) |  4.500<sub>±0.121</sub> |      14.55<sub>±0.10</sub> |
| Ruby (JRuby) |  5.189<sub>±0.690</sub> |     231.55<sub>±18.81</sub> |
| Ruby (TruffleRuby) |  1.439<sub>±0.065</sub> |     698.24<sub>±24.72</sub> |
| Ruby (TruffleRuby JVM) |  3.704<sub>±0.218</sub> |    1008.50<sub>±257.01</sub> |
| Ruby (GraalVM) |  1.451<sub>±0.043</sub> |     691.07<sub>±23.68</sub> |
| Ruby (GraalVM JVM) |  3.681<sub>±0.133</sub> |     840.06<sub>±192.01</sub> |


