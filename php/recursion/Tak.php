<?php
function tak($x, $y, $z) {
    return $y < $x
        ? tak(tak($x - 1, $y, $z), tak($y - 1, $z, $x), tak($z - 1, $x, $y))
        : $z;
}

(function () {
    $startTimeMs = floor(microtime(true) * 1000);

    echo tak(30, 22, 12), "\n";

    $endTimeMs = floor(microtime(true) * 1000);
    $durationMs = $endTimeMs - $startTimeMs;
  
    echo "Execution time: " . $durationMs . "ms\n";
})();
