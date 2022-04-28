if __name__ == '__main__':

    #get the digits only
    s = "2a1b17x5768s3" 

    i = 0
    j = 0
    res = list()
    while i < len(s):
        j = i
        temp = ''
        while j < len(s) and s[j].isdigit():
            temp += s[j]
            j += 1

        res.append("".join(temp))
        i = j+1

    print(res)
