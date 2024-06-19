# Results

## Algorithms

### primes/Simple

| Language | Time, s | Startup time, s | Total time, s | Memory, MiB |
| :------- | ------: | --------------: | ------------: | ----------: |
| C++ (clang) |  0.349<sub>±0.003</sub> |  0.003<sub>±0.000</sub> |  0.352<sub>±0.003</sub> |       1.47<sub>±0.74</sub> |
| C++ (gcc) |  0.346<sub>±0.004</sub> |  0.003<sub>±0.000</sub> |  0.349<sub>±0.004</sub> |       1.48<sub>±0.73</sub> |
| Java |  0.365<sub>±0.004</sub> |  0.046<sub>±0.278</sub> |  0.403<sub>±0.256</sub> |      40.35<sub>±0.12</sub> |
| Java (GraalVM) |  0.368<sub>±0.007</sub> |  0.080<sub>±0.006</sub> |  0.456<sub>±0.004</sub> |      76.60<sub>±2.31</sub> |
| JavaScript (Node) |  0.357<sub>±0.027</sub> |  0.025<sub>±0.002</sub> |  0.381<sub>±0.029</sub> |      44.84<sub>±0.93</sub> |
| JavaScript (GraalVM) |  0.734<sub>±0.024</sub> |  0.320<sub>±0.005</sub> |  1.054<sub>±0.025</sub> |     346.48<sub>±7.03</sub> |
| PHP |  3.351<sub>±0.032</sub> |  0.016<sub>±0.001</sub> |  3.368<sub>±0.032</sub> |      18.46<sub>±0.17</sub> |
| PHP (JIT: tracing) |  1.258<sub>±0.065</sub> |  0.018<sub>±0.001</sub> |  1.276<sub>±0.065</sub> |      21.78<sub>±0.25</sub> |
| PHP (JIT: function) |  1.439<sub>±0.094</sub> |  0.019<sub>±0.001</sub> |  1.460<sub>±0.094</sub> |      21.54<sub>±0.12</sub> |
| Python (CPython) | 11.549<sub>±0.022</sub> |  0.012<sub>±0.001</sub> | 11.562<sub>±0.022</sub> |       7.41<sub>±0.23</sub> |
| Python (PyPy) |  0.445<sub>±0.014</sub> |  0.032<sub>±0.001</sub> |  0.476<sub>±0.015</sub> |      52.93<sub>±0.83</sub> |
| Ruby | 10.653<sub>±0.403</sub> |  0.050<sub>±0.026</sub> | 10.702<sub>±0.390</sub> |      15.77<sub>±0.09</sub> |
| Ruby (JIT) | 10.611<sub>±0.069</sub> |  0.051<sub>±0.001</sub> | 10.661<sub>±0.068</sub> |      16.39<sub>±0.10</sub> |
| Ruby (JRuby) | 12.274<sub>±0.417</sub> |  2.084<sub>±0.111</sub> | 14.295<sub>±0.412</sub> |     513.50<sub>±38.65</sub> |
| Rust |  0.340<sub>±0.002</sub> |  0.002<sub>±0.002</sub> |  0.343<sub>±0.002</sub> |       1.80<sub>±0.04</sub> |


### primes/Atkin

| Language | Time, s | Startup time, s | Total time, s | Memory, MiB |
| :------- | ------: | --------------: | ------------: | ----------: |
| C++ (clang) |  0.235<sub>±0.006</sub> |  0.010<sub>±0.000</sub> |  0.245<sub>±0.006</sub> |      89.05<sub>±0.12</sub> |
| C++ (gcc) |  0.221<sub>±0.006</sub> |  0.010<sub>±0.001</sub> |  0.231<sub>±0.006</sub> |      89.11<sub>±0.05</sub> |
| Java |  0.214<sub>±0.004</sub> |  0.053<sub>±0.001</sub> |  0.267<sub>±0.003</sub> |     178.35<sub>±1.47</sub> |
| Java (GraalVM) |  0.322<sub>±0.025</sub> |  0.093<sub>±0.002</sub> |  0.414<sub>±0.027</sub> |     237.78<sub>±4.13</sub> |
| JavaScript (Node) |  0.315<sub>±0.010</sub> |  0.067<sub>±0.002</sub> |  0.381<sub>±0.011</sub> |     229.17<sub>±1.25</sub> |
| JavaScript (GraalVM) |  2.472<sub>±0.091</sub> |  0.348<sub>±0.053</sub> |  2.839<sub>±0.047</sub> |     808.37<sub>±40.84</sub> |
| PHP |  1.918<sub>±0.059</sub> |  0.025<sub>±0.001</sub> |  1.943<sub>±0.060</sub> |     239.53<sub>±0.48</sub> |
| PHP (JIT: tracing) |  1.037<sub>±0.025</sub> |  0.028<sub>±0.002</sub> |  1.065<sub>±0.024</sub> |     241.93<sub>±0.47</sub> |
| PHP (JIT: function) |  1.055<sub>±0.009</sub> |  0.028<sub>±0.000</sub> |  1.083<sub>±0.009</sub> |     242.70<sub>±0.49</sub> |
| Python (CPython) |  6.317<sub>±0.084</sub> |  0.013<sub>±0.001</sub> |  6.329<sub>±0.083</sub> |     245.70<sub>±0.05</sub> |
| Python (PyPy) |  1.246<sub>±0.012</sub> |  0.055<sub>±0.003</sub> |  1.299<sub>±0.013</sub> |     303.93<sub>±0.14</sub> |
| Ruby |  2.578<sub>±0.059</sub> |  0.071<sub>±0.005</sub> |  2.648<sub>±0.062</sub> |     158.46<sub>±0.04</sub> |
| Ruby (JIT) |  1.864<sub>±0.037</sub> |  0.072<sub>±0.002</sub> |  1.940<sub>±0.038</sub> |     158.98<sub>±0.11</sub> |
| Ruby (JRuby) |  2.963<sub>±0.082</sub> |  2.105<sub>±0.035</sub> |  5.056<sub>±0.077</sub> |     611.73<sub>±17.98</sub> |
| Rust |  0.160<sub>±0.003</sub> |  0.010<sub>±0.001</sub> |  0.170<sub>±0.004</sub> |      77.54<sub>±0.07</sub> |


### collatz/MaxSequence

| Language | Time, s | Startup time, s | Total time, s | Memory, MiB |
| :------- | ------: | --------------: | ------------: | ----------: |
| C++ (clang) |  0.059<sub>±0.001</sub> |  0.003<sub>±0.000</sub> |  0.062<sub>±0.001</sub> |       1.47<sub>±0.94</sub> |
| Java |  0.097<sub>±0.001</sub> |  0.048<sub>±0.007</sub> |  0.147<sub>±0.006</sub> |      41.98<sub>±1.71</sub> |
| Java (GraalVM) |  0.096<sub>±0.002</sub> |  0.102<sub>±0.002</sub> |  0.194<sub>±0.004</sub> |      78.58<sub>±0.60</sub> |
| JavaScript (Node) |  0.646<sub>±0.007</sub> |  0.025<sub>±0.001</sub> |  0.670<sub>±0.006</sub> |      43.87<sub>±1.03</sub> |
| JavaScript (GraalVM) |  0.902<sub>±0.018</sub> |  0.338<sub>±0.021</sub> |  1.229<sub>±0.034</sub> |     338.93<sub>±6.41</sub> |
| PHP |  1.400<sub>±0.107</sub> |  0.017<sub>±0.001</sub> |  1.418<sub>±0.106</sub> |      18.27<sub>±0.18</sub> |
| PHP (JIT: tracing) |  0.389<sub>±0.009</sub> |  0.019<sub>±0.000</sub> |  0.408<sub>±0.009</sub> |      21.84<sub>±0.22</sub> |
| PHP (JIT: function) |  0.463<sub>±0.014</sub> |  0.019<sub>±0.001</sub> |  0.482<sub>±0.015</sub> |      21.60<sub>±0.11</sub> |
| Python (CPython) |  7.312<sub>±0.047</sub> |  0.012<sub>±0.001</sub> |  7.324<sub>±0.047</sub> |       7.35<sub>±0.31</sub> |
| Python (PyPy) |  0.125<sub>±0.002</sub> |  0.030<sub>±0.002</sub> |  0.156<sub>±0.003</sub> |      53.07<sub>±0.14</sub> |
| Ruby |  2.574<sub>±0.030</sub> |  0.050<sub>±0.002</sub> |  2.623<sub>±0.031</sub> |      15.66<sub>±0.07</sub> |
| Ruby (JIT) |  0.903<sub>±0.034</sub> |  0.051<sub>±0.001</sub> |  0.954<sub>±0.034</sub> |      16.27<sub>±0.09</sub> |
| Ruby (JRuby) |  1.215<sub>±0.065</sub> |  2.043<sub>±0.028</sub> |  3.242<sub>±0.097</sub> |     520.25<sub>±55.95</sub> |
| Rust |  0.049<sub>±0.000</sub> |  0.002<sub>±0.001</sub> |  0.052<sub>±0.001</sub> |       1.82<sub>±0.03</sub> |


### mandelbrot/Simple

| Language | Time, s | Startup time, s | Total time, s | Memory, MiB |
| :------- | ------: | --------------: | ------------: | ----------: |
| C++ (clang) |  0.032<sub>±0.001</sub> |  0.003<sub>±0.000</sub> |  0.035<sub>±0.001</sub> |       1.54<sub>±0.93</sub> |
| C++ (gcc) |  0.032<sub>±0.001</sub> |  0.003<sub>±0.000</sub> |  0.036<sub>±0.000</sub> |       1.47<sub>±0.77</sub> |
| Java |  0.058<sub>±0.001</sub> |  0.048<sub>±0.002</sub> |  0.107<sub>±0.003</sub> |      40.30<sub>±1.87</sub> |
| Java (GraalVM) |  0.050<sub>±0.006</sub> |  0.094<sub>±0.008</sub> |  0.144<sub>±0.016</sub> |      78.34<sub>±0.92</sub> |
| JavaScript (Node) |  0.048<sub>±0.000</sub> |  0.026<sub>±0.002</sub> |  0.074<sub>±0.002</sub> |      48.68<sub>±2.31</sub> |
| JavaScript (GraalVM) |  0.205<sub>±0.011</sub> |  0.333<sub>±0.007</sub> |  0.535<sub>±0.008</sub> |     338.80<sub>±3.43</sub> |
| PHP |  0.680<sub>±0.003</sub> |  0.016<sub>±0.001</sub> |  0.697<sub>±0.003</sub> |      18.31<sub>±0.24</sub> |
| PHP (JIT: tracing) |  0.118<sub>±0.001</sub> |  0.018<sub>±0.001</sub> |  0.136<sub>±0.001</sub> |      21.80<sub>±0.10</sub> |
| PHP (JIT: function) |  0.155<sub>±0.001</sub> |  0.019<sub>±0.000</sub> |  0.175<sub>±0.001</sub> |      21.74<sub>±0.25</sub> |
| Python (CPython) |  3.039<sub>±0.010</sub> |  0.012<sub>±0.001</sub> |  3.051<sub>±0.010</sub> |       7.79<sub>±0.09</sub> |
| Python (PyPy) |  0.048<sub>±0.001</sub> |  0.031<sub>±0.001</sub> |  0.080<sub>±0.001</sub> |      54.37<sub>±0.15</sub> |
| Ruby |  1.747<sub>±0.044</sub> |  0.050<sub>±0.002</sub> |  1.796<sub>±0.044</sub> |      15.82<sub>±0.08</sub> |
| Ruby (JIT) |  1.285<sub>±0.012</sub> |  0.051<sub>±0.001</sub> |  1.335<sub>±0.011</sub> |      16.45<sub>±0.08</sub> |
| Ruby (JRuby) |  1.931<sub>±0.150</sub> |  2.076<sub>±0.025</sub> |  4.014<sub>±0.165</sub> |     507.68<sub>±17.72</sub> |
| Rust |  0.032<sub>±0.001</sub> |  0.003<sub>±0.002</sub> |  0.034<sub>±0.002</sub> |       1.79<sub>±0.05</sub> |


### treap/Naive

| Language | Time, s | Startup time, s | Total time, s | Memory, MiB |
| :------- | ------: | --------------: | ------------: | ----------: |
| C++ (clang) |  0.223<sub>±0.006</sub> |  0.003<sub>±0.000</sub> |  0.226<sub>±0.006</sub> |       3.18<sub>±0.13</sub> |
| C++ (gcc) |  0.188<sub>±0.003</sub> |  0.003<sub>±0.000</sub> |  0.191<sub>±0.003</sub> |       3.17<sub>±0.15</sub> |
| Go |  0.304<sub>±0.006</sub> |  0.003<sub>±0.003</sub> |  0.309<sub>±0.005</sub> |       7.71<sub>±0.84</sub> |
| Java |  0.562<sub>±0.016</sub> |  0.056<sub>±0.002</sub> |  0.614<sub>±0.017</sub> |     154.04<sub>±0.71</sub> |
| Java (GraalVM) |  0.530<sub>±0.082</sub> |  0.097<sub>±0.003</sub> |  0.622<sub>±0.083</sub> |     214.47<sub>±44.79</sub> |
| JavaScript (Node) |  0.878<sub>±0.005</sub> |  0.037<sub>±0.002</sub> |  0.912<sub>±0.006</sub> |      85.18<sub>±1.04</sub> |
| JavaScript (GraalVM) |  2.016<sub>±0.032</sub> |  0.339<sub>±0.010</sub> |  2.347<sub>±0.039</sub> |     553.63<sub>±11.45</sub> |
| Kotlin (JVM) |  0.538<sub>±0.014</sub> |  0.054<sub>±0.017</sub> |  0.592<sub>±0.027</sub> |     193.02<sub>±16.86</sub> |
| Kotlin (Native) |  0.939<sub>±0.026</sub> |  0.009<sub>±0.003</sub> |  0.950<sub>±0.028</sub> |      24.39<sub>±1.08</sub> |
| PHP |  4.719<sub>±0.034</sub> |  0.016<sub>±0.001</sub> |  4.736<sub>±0.034</sub> |      18.41<sub>±0.16</sub> |
| PHP (JIT: tracing) |  2.891<sub>±0.046</sub> |  0.020<sub>±0.001</sub> |  2.910<sub>±0.045</sub> |      22.10<sub>±0.21</sub> |
| PHP (JIT: function) |  2.990<sub>±0.013</sub> |  0.019<sub>±0.001</sub> |  3.010<sub>±0.012</sub> |      21.80<sub>±0.19</sub> |
| Python (CPython) | 12.410<sub>±0.054</sub> |  0.014<sub>±0.002</sub> | 12.424<sub>±0.055</sub> |       8.43<sub>±0.04</sub> |
| Python (PyPy) |  2.655<sub>±0.076</sub> |  0.036<sub>±0.014</sub> |  2.692<sub>±0.079</sub> |      62.52<sub>±0.59</sub> |
| Ruby |  5.310<sub>±0.054</sub> |  0.052<sub>±0.002</sub> |  5.359<sub>±0.053</sub> |      17.65<sub>±0.08</sub> |
| Ruby (JIT) |  3.051<sub>±0.065</sub> |  0.051<sub>±0.001</sub> |  3.102<sub>±0.065</sub> |      18.38<sub>±0.08</sub> |
| Ruby (JRuby) |  5.054<sub>±0.054</sub> |  2.053<sub>±0.013</sub> |  7.100<sub>±0.060</sub> |     237.32<sub>±38.30</sub> |


### recursion/Tak

| Language | Time, s | Startup time, s | Total time, s | Memory, MiB |
| :------- | ------: | --------------: | ------------: | ----------: |
| C++ (clang) |  0.046<sub>±0.001</sub> |  0.003<sub>±0.000</sub> |  0.049<sub>±0.001</sub> |       1.47<sub>±0.77</sub> |
| C++ (gcc) |  0.057<sub>±0.001</sub> |  0.003<sub>±0.000</sub> |  0.060<sub>±0.001</sub> |       1.53<sub>±0.67</sub> |
| JavaScript (Node) |  0.143<sub>±0.011</sub> |  0.025<sub>±0.002</sub> |  0.168<sub>±0.013</sub> |      45.28<sub>±1.01</sub> |
| JavaScript (GraalVM) |  0.659<sub>±0.015</sub> |  0.323<sub>±0.036</sub> |  0.984<sub>±0.040</sub> |     410.40<sub>±10.25</sub> |
| PHP |  1.161<sub>±0.015</sub> |  0.016<sub>±0.001</sub> |  1.177<sub>±0.015</sub> |      18.23<sub>±0.17</sub> |
| PHP (JIT: tracing) |  0.388<sub>±0.002</sub> |  0.018<sub>±0.001</sub> |  0.406<sub>±0.002</sub> |      21.56<sub>±0.16</sub> |
| PHP (JIT: function) |  0.408<sub>±0.013</sub> |  0.019<sub>±0.001</sub> |  0.427<sub>±0.014</sub> |      21.38<sub>±0.16</sub> |
| Python (CPython) |  4.304<sub>±0.036</sub> |  0.012<sub>±0.000</sub> |  4.316<sub>±0.036</sub> |       7.39<sub>±0.20</sub> |
| Python (PyPy) |  0.765<sub>±0.031</sub> |  0.031<sub>±0.001</sub> |  0.796<sub>±0.032</sub> |      59.74<sub>±0.13</sub> |
| Ruby |  1.218<sub>±0.006</sub> |  0.050<sub>±0.002</sub> |  1.270<sub>±0.006</sub> |      15.79<sub>±0.14</sub> |
| Ruby (JIT) |  0.286<sub>±0.012</sub> |  0.050<sub>±0.001</sub> |  0.335<sub>±0.013</sub> |      16.30<sub>±0.13</sub> |
| Ruby (JRuby) |  0.587<sub>±0.031</sub> |  2.017<sub>±0.015</sub> |  2.604<sub>±0.030</sub> |     185.73<sub>±3.85</sub> |


### linpack/Linpack

| Language | Time, s | Startup time, s | Total time, s | Memory, MiB |
| :------- | ------: | --------------: | ------------: | ----------: |
| Go |  2.680<sub>±0.140</sub> |  0.004<sub>±0.003</sub> |  2.689<sub>±0.140</sub> |      33.95<sub>±0.11</sub> |
| JavaScript (Node) |  8.951<sub>±0.076</sub> |  0.039<sub>±0.004</sub> |  8.990<sub>±0.079</sub> |     139.29<sub>±0.21</sub> |
| JavaScript (GraalVM) |  3.661<sub>±0.089</sub> |  0.326<sub>±0.002</sub> |  3.985<sub>±0.089</sub> |     407.01<sub>±3.09</sub> |
| PHP | 83.828<sub>±0.116</sub> |  0.018<sub>±0.042</sub> | 83.846<sub>±0.145</sub> |      90.32<sub>±0.22</sub> |
| PHP (JIT: tracing) | 23.703<sub>±0.482</sub> |  0.020<sub>±0.004</sub> | 23.723<sub>±0.486</sub> |      93.62<sub>±0.22</sub> |
| PHP (JIT: function) | 28.718<sub>±0.157</sub> |  0.022<sub>±0.000</sub> | 28.739<sub>±0.157</sub> |      93.42<sub>±0.34</sub> |
| Python (CPython) | 572.390<sub>±21.161</sub> |  0.019<sub>±0.005</sub> | 572.407<sub>±21.161</sub> |     163.52<sub>±0.10</sub> |
| Python (PyPy) |  6.029<sub>±0.114</sub> |  0.042<sub>±0.082</sub> |  6.068<sub>±0.173</sub> |     102.38<sub>±3.14</sub> |


## Legend

| Field        | Description |
| :----------- | :---------- |
| Time         | Time spent in the algorithm itself, reported by the program itself. |
| Total time   | Total time spent from the start of the program to the end of the algorithm, measured by the benchmark. |
| Startup time | Time spent from the start of the program to the start of the algorithm, measured by the benchmark (Total time - Time). |
| Memory       | Peak memory usage during the algorithm, measured by the benchmark. |


