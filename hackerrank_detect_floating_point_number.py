

'''
You are given a string .
Your task is to verify that N  is a floating point number.
'''

if '__main__' == __name__:


    T = int(input())
    for _ in range(T):
        
        try:
            status = True
                
            n = input()
            if n == '0':
                status = False
            if n[0] == '+' and n[1] == '-':
                status = False
            elif n[0] == '-' and n[1] == '+':
                status = False
            elif n.isnumeric() == False and  (n[0] != '+' and n[0] != '-' and n[0]!= '.') and n.count('.') > 1:
                status = False
                
            n = float(n)
          
            #print(n)

        except ValueError:
            status = False

        print(status)
