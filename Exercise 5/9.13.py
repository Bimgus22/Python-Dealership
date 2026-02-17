from collections import OrderedDict

glossary = OrderedDict()

glossary["list"] = "A collection of items in a particular order."
glossary["tuple"] = "An immutable (unchangeable) list."
glossary["dictionary"] = "A collection of key-value pairs."
glossary["loop"] = "A way to repeat a block of code."
glossary["class"] = "A blueprint for creating objects."

for word, definition in glossary.items():
    print(f"{word.title()}: {definition}\n")
