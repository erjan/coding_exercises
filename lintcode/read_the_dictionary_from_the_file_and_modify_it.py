'''

Given a file path path and 
a file format of json, you are asked 
to convert the data in the file to a dictionary 
and modify the age property to 18, then write the modified dictionary back to the file.

'''


import json

def get_write_dict(path:str):
    with open(path,'r') as json_file:
        
        data = json.load(json_file)

    data['age'] = 18

    with open(path, 'w') as outfile:
        json.dump(data,outfile)
