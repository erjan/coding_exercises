Write a function that accepts a multi-dimensional array arr and a depth n, and returns a flattened version of that array.

A multi-dimensional array is a recursive data structure that contains integers or other multi-dimensional arrays.

A flattened array is a version of that array with some or all of the 
sub-arrays removed and replaced with the actual elements in that sub-array. This flattening operation
should only be done if the current depth of nesting is greater than n. The depth of the elements in the first array are considered to be 0.

Please solve it without the built-in Array.flat method.



var flat = function (arr, n) {
    return n === 0 ? arr : arr.reduce(
            (acc, e) => typeof(e) === "number" ? 
              (acc.push(e), acc) : (acc.push(...flat(e, n-1)), acc),
           []);
};
