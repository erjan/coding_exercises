Write a generator function that returns a generator object which yields the fibonacci sequence.

The fibonacci sequence is defined by the relation Xn = Xn-1 + Xn-2.

The first few numbers of the series are 0, 1, 1, 2, 3, 5, 8, 13.



/**
 * @return {Generator<number>}
 */
var fibGenerator = function*() {

    a = 0;
    a2 = 1;
    while(true){
        yield a;
        [a,a2] = [a2,a+a2];
    }
};

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */
