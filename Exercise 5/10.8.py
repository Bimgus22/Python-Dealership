filenames = ["cats.txt", "dogs.txt"]

for filename in filenames:
    try:
        with open(filename) as file_object:
            print(f"\nReading {filename}:")
            contents = file_object.read()
            print(contents)
    except FileNotFoundError:
        print(f"Sorry, the file {filename} was not found.")