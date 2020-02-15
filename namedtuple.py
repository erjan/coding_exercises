#I struggled greatly with this exercise - did not understand that headers can be simply read and put in as IS!
'''
The first line contains an integer , the total number of students.
The second line contains the names of the columns in any order.
The next  lines contains the ID, NAME ,MARKS  and CLASS, under their respective column names.
Print the average marks of the list corrected to 2 decimal places.
'''

from collections import namedtuple
if __name__ == '__main__':
    n = int(input())

    students = list()        
    headers = input()
    student = namedtuple('student',headers)    
    total = 0
    for i in range(n):
        row = input().split()        
        cur_student = student(row[0], row[1], row[2], row[3])
        cur_mark = float(cur_student.MARKS)
        total += cur_mark
    print('%.2f' %(total/n))
    
   
