'use strict';

const NUMBER = 500000;

function run(times) {
    var x = 0;

    for (var i = 0; i <= times; i++) {
        x = i * i;
    }

    console.log(x);
}

(async function() {
    run(NUMBER);
})();
