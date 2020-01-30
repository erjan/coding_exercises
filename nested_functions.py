# Good morning! Here's your coding interview problem for today.
# This problem was asked by Jane Street.
# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns 
# the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
# Given this implementation of cons:

#sit for 30 mins and did it myself

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
Implement car and cdr.
#-----------------------------------
def cons(a, b):
    def pair(f):
      return f(a, b)
    return pair


def car(pair):
  return pair(lambda a,b:a)

def cdr(pair):
  return pair(lambda a,b:b)

print(car(cons(3,4)))
