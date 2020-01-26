#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#Bonus: Can you do this in one pass?

if __name__ == "__main__":
    l = list( int(i) for i in input().split(' '))
    k = int(input())

    found = False
    for el in range(len(l)):
        check = k - l[el]
        if check in l:
            found = Tru            
    print(found)
