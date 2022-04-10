'''

Given a csv file path path, you 
are asked to read the contents of the csv file, then
change 'name' in the first line to 'student_name', and 
then write the modified contents back to path.

'''


import csv

def get_write_csv(path:str):
    with open(path, 'r')as f:
        lines = f.readlines()
        lines[0] = lines[0].replace('name', 'student_name')
    with open(path, 'w') as f2:
        f2.writelines(lines)
    f2.close()
