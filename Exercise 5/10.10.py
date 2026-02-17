def count_word(filename, word):
    try:
        with open(filename, encoding="utf-8") as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print(f"{filename} not found.")
    else:
        count = contents.lower().count(word.lower())
        print(f"The word '{word}' appears {count} times in {filename}.")


files = ["alice.txt", "moby_dick.txt"]

for file in files:
    count_word(file, "the")
