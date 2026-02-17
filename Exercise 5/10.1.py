filename = "learning_python.txt"

print("---- Reading entire file ----")
with open(filename) as file_object:
    contents = file_object.read()
    print(contents)
print("---- Looping over the file ----")
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
print("---- Storing lines in a list ----")
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())