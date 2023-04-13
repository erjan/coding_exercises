
'''
Write a function that accepts an integer
n and returns a counter function. This counter function
initially returns n and then returns 1 more than the previous value
every subsequent time it is called (n, n + 1, n + 2, etc).
'''


/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    return function() {
        return n++
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */

----------------------------------------------------------------------------
/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    let count = n - 1
    return function() {
        count++
        return count
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */
