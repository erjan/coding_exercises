'''

Your code needs to read data n from the standard 
input stream (console), calculate the 
prime number of the n, calculate the result and print it to the standard output stream (console).

'''

n = int(input())
def isprime(i):
    is_prime = True 
    for j in range(2,int(i**0.5+1)):
        if i%j==0:
            is_prime = False
    return is_prime
i,s = 2,0
while s<n:
    if isprime(i):
        s  +=1
    i +=1
print(i-1)
