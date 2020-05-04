# Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

def f(n):
    binary_n = bin(n)
    binary_n = binary_n[2:]
    complement = ''
    for c in binary_n:
        if c == '0':
            complement += '1'
        else:
            complement += '0'
    result = int(complement, 2)
    print(result)
    return result

f(35)
