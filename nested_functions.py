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
  def get_first(a,b):
    return a
  return pair(get_first)

def cdr(pair):
  def get_last(a,b):
    return b
  return pair(get_last)

print(car(cons(3,4)))
print(cdr(cons(3,4)))
