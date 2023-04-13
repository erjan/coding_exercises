Given an object, return a valid JSON string of that object. You may assume the object only 
inludes strings, integers, arrays, objects, booleans, and null. The returned string should 
not include extra spaces. The order of keys should be the same as the order returned by Object.keys().

Please solve it without using the built-in JSON.stringify method.

 

var jsonStringify = function(object) {
  if (object === null) {
    return 'null';
  }
  if (typeof object === 'string') {
    // return the string value surrounded by double quotes.
    return '"' + object + '"';
  }
  if (typeof object === 'number' || typeof object === 'boolean') {
    // return its string representation.
    return String(object);
  }
  if (Array.isArray(object)) {
    // Recursively convert each item to a JSON string and join them with commas.
    const items = object.map(item => jsonStringify(item)).join(',');
    return '[' + items + ']';
  }
  // Recursively convert each value to a JSON string and pair it with the corresponding key.
  if (typeof object === 'object') {
    const keys = Object.keys(object);
    const items = keys.map(key => '"' + key + '":' + jsonStringify(object[key]));
    return '{' + items.join(',') + '}';
  }
};
