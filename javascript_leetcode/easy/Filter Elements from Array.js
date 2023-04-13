Write a function that takes an input array of integers arr and a filtering function fn and returns a new array with a fewer or equal number of elements.

The returned array should only contain elements where fn(arr[i], i) evaluated to a truthy value.

Please solve it without the built-in Array.filter method.


/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {

    let res = []
    for(let i = 0; i < arr.length;i++){
        if (fn(arr[i], i)){
            res.push(arr[i])
        }
    }
    return res;
    
};
