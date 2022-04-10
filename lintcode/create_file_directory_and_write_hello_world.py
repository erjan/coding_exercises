'''

Please write Python code. If there may not be a file directory, import the 
os library and create a file directory, and write'Hello World!' into the newly created file.

Please write the relevant Python code in the write_hello_world.py file to 
create a new file directory and write'Hello World!' into it.
'''


def write_to_file(path):
        file = os.path.dirname(path)
        if not os.path.exists(file):
            os.mkdir(file)
        with open(path, 'w') as f:
            f.write(s)
