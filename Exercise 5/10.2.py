filename = "learning_python.txt"

with open(filename) as file_object:
    for line in file_object:
        modified_line = line.replace("Python", "C")
        print(modified_line.rstrip())