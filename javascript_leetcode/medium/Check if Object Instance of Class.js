
Write a function that checks if a given object is an instance of a given class or superclass.

There are no constraints on the data types that can be passed to the function.

/**
 * @param {Object} object
 * @param {Function} classFunction
 * @return {boolean}
 */
var checkIfInstanceOf = function(obj, classFunction) {
    while(obj!=null)
    {
        if(obj.constructor === classFunction)
        {
            return true;
        }

        obj = Object.getPrototypeOf(obj);

    }

    return false;
};

/**
 * checkIfInstanceOf(new Date(), Date); // true
 */
