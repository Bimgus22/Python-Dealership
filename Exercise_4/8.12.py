def make_sandwich(*items):
    print("You ordered a sandwich with the following items:")
    for item in items:
        print(f"- {item}")
    print()

make_sandwich("lettuce", "tomato", "turkey")
make_sandwich("peanut butter", "jelly")
make_sandwich("ham", "cheese", "pickles", "mustard")
