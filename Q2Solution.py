#Solution to question 2 goes here
def determine_mushroom():
    gills = input("Does your mushroom have gills? (yes/no): ").lower()

    forest = input("Does your mushroom grow in a forest? (yes/no): ").lower()

    ring = input("Does your mushroom have a ring? (yes/no): ").lower()

    if gills == "no":
        print("The mushroom you are thinking of is: Cepe de bordeaux.")
    elif forest == "no" and ring == "yes":
        print("The mushroom you are thinking of is: Coprin chevelu.")
    elif forest == "no" and ring == "no":
        print("The mushroom you are thinking of is: Agaric jaunissant.")
    elif ring == "yes":
        print("The mushroom you are thinking of is: Amanite tue-mouche.")
    elif ring == "no" and gills == "yes" and forest == "yes":
        convex_cup = input("Does your mushroom have a convex cup? (yes/no): ").lower()
        if convex_cup == "yes":
            print("The mushroom you are thinking of is: Pied Bleu.")
        else:
            print("The mushroom you are thinking of is: Girolle.")
    else:
        print("Sorry, I couldn't determine the mushroom.")

determine_mushroom()
