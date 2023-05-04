Given a function fn, return a new function that is identical to the original function except that it ensures fn is called at most once.

The first time the returned function is called, it should return the same result as fn.
Every subsequent time it is called, it should return undefined.

/**
 * @param {Function} fn
 * @return {Function}
 */
var once = function(fn) {
    var counter = 0;
    return function(...args){
        if (counter ===0){
            counter = counter+1;
            return fn(...args)

        }
        else{
            return undefined;
        }
    }
};
