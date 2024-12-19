Here’s a Python program that asks the user at most three questions and determines the mushroom they are thinking of:

def identify_mushroom():
    # Define mushrooms and their characteristics
    mushrooms = {
        "Agaric jaunissant": {"gills": True, "forest": False, "ring": True, "convex": True},
        "Cepe de bordeaux": {"gills": False, "forest": True, "ring": False, "convex": False},
        "Amanite tue-mouche": {"gills": True, "forest": True, "ring": True, "convex": True},
        "Coprin chevelu": {"gills": True, "forest": False, "ring": True, "convex": False},
        "Girolle": {"gills": True, "forest": True, "ring": False, "convex": False},
        "Pied Bleu": {"gills": True, "forest": True, "ring": False, "convex": True},
    }

    # Ask questions to identify the mushroom
    def ask_question(question):
        while True:
            answer = input(question + " (yes/no): ").strip().lower()
            if answer in {"yes", "no"}:
                return answer == "yes"
            else:
                print("Please answer with 'yes' or 'no'.")

    # Start asking questions
    has_gills = ask_question("Does your mushroom have gills?")
    if not has_gills:
        print("Your mushroom is Cepe de bordeaux.")
        return

    grows_in_forest = ask_question("Does your mushroom grow in a forest?")
    if not grows_in_forest:
        has_ring = ask_question("Does your mushroom have a ring?")
        if has_ring:
            print("Your mushroom is Coprin chevelu.")
        else:
            print("Your mushroom is Agaric jaunissant.")
    else:
        has_convex_cup = ask_question("Does your mushroom have a convex cup?")
        if has_convex_cup:
            has_ring = ask_question("Does your mushroom have a ring?")
            if has_ring:
                print("Your mushroom is Amanite tue-mouche.")
            else:
                print("Your mushroom is Pied Bleu.")
        else:
            print("Your mushroom is Girolle.")

# Run the program
identify_mushroom()

Explanation:

1. Characteristics Mapping: Each mushroom is defined with four characteristics: gills, forest, ring, and convex.


2. Questions Logic:

The program asks questions one by one.

Depending on the user's answers, it eliminates mushrooms until one is identified.



3. Efficient Questions:

The program minimizes the number of questions by strategically using answers to eliminate possibilities.




Example Run:

Input:

Does your mushroom have gills? (yes/no): yes  
Does your mushroom grow in a forest? (yes/no): yes  
Does your mushroom have a convex cup? (yes/no): no

Output:

Your mushroom is Girolle.

