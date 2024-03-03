#1
import os

def list_contents(p):
    print("Contents in:", p)
    for e in os.listdir(p):
        if os.path.isdir(os.path.join(p, e)):
            print("Dir:", e)
        elif os.path.isfile(os.path.join(p, e)):
            print("File:", e)

p = input("Path: ")
list_contents(p)

#2
import os

def check_access(p):
    print("Path:", p)
    print("Exists:", os.path.exists(p))
    print("Readability:", os.access(p, os.R_OK))
    print("Writability:", os.access(p, os.W_OK))
    print("Executability:", os.access(p, os.X_OK))

tp = input("Path: ")
check_access(tp)

#3
import os.path

def check_path(path):
    if os.path.exists(path):
        print(f"The path '{path}' exists.")
        
        directory_name, file_name = os.path.split(path)
        if file_name:
            print(f"Filename: {file_name}")
        else:
            print("The given path is a directory.")
        
        print(f"Directory portion: {directory_name}")
    else:
        print(f"The path '{path}' does not exist.")

given_path = input("The path: ")
check_path(given_path)

#4
def count_lines(filename):
    with open(filename, 'r') as file:
        line_count = sum(1 for line in file)
    print(line_count)

filename = input("filename: ")
count_lines(filename)

#5
def list_file(file_name, my_list):
    with open(file_name, 'w') as file:
        for item in my_list:
            file.write(f"{item}")

my_list = ['Apple', 'Banana']
file_name = 'file.txt'
list_file(file_name, my_list)

print(file_name)

#6
import string

def gen_files():
    for char in string.ascii_uppercase:
        with open(f"{char}.txt", 'w') as file:
            file.write(f"This is the file for letter {char}.")

gen_files()

#7
def copy(first_file, second_file):
    with open(first_file, 'r') as src:
        contents = src.read()
    with open(second_file, 'w') as dest:
        dest.write(contents)

# Example usage
first_file = 'first.txt'
second_file = 'second.txt'
copy(first_file, second_file)

print("ok")

#8
import os

def del_file(path):
    if not os.path.exists(path):
        print("does not exist.")
        return
    
    if not os.access(path, os.W_OK):
        print("not accessible for deletion.")
        return
    
    os.remove(path)
    print("deleted.")

file_path = input("path: ")
del_file(file_path)
