Write a function that accepts another function and returns a curried version of that function.

A curried function is a function that accepts fewer or an equal number of parameters as the original function and returns either another curried function or the same value the original function would have returned.

In practical terms, if you called the original function like sum(1, 2, 3), you would call the curried version like csum(1)(2)(3), csum(1)(2, 3), csum(1, 2)(3), or csum(1, 2, 3). All these methods of calling the curried function should return the same value as the original.

 

/**
 * @param {Function} fn
 * @return {Function}
 */
const curry = function(fn) {
    const args = [];
    return function curried(...newArgs) {
        args.push(...newArgs);  // Add new toppings to existing ones
        if (args.length < fn.length) return curried;  // The curry isn't ready yet!
        return fn(...args);  // The curry is ready! :D
    };
};

/**
 * function sum(a, b) { return a + b; }
 * const csum = curry(sum);
 * csum(1)(2) // 3
 */
