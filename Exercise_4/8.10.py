magicians = ["Houdini", "Copperfield", "Blaine", "Davidson"]

def show_magicians(names):
    for name in names:
        print(name)

def make_great(names):
    for i in range(len(names)):
        names[i] = "The Great " + names[i]

make_great(magicians)

show_magicians(magicians)
