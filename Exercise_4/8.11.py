magicians = ["Houdini", "Copperfield", "Blaine", "Davidson"]

def show_magicians(names):
    for name in names:
        print(name)

def make_great(names):
    great_magicians = []
    for name in names:
        great_magicians.append("The Great " + name)
    return great_magicians

great_magicians = make_great(magicians)
print("Original magicians:")
show_magicians(magicians)
print("\nGreat magicians:")
show_magicians(great_magicians)