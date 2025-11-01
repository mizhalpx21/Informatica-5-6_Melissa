dictionary_food = {
        "almond milk": 30,
        "milk": 73,
        "sour Cream, cultured": 26,
        "plain, low-fat": 77,
        "egg": 75,
        "egg substitute": 30,
        "parmesan Cheese, grated": 22,
        "cottage Cheese, low fat": 20,
        "peanuts, roasted": 166,
        "sunflower seeds, dry roasted": 165,
        "edamame, boiled": 127,
        "lentils, boiled": 115,
        "shrimp, boiled": 28,
        "swai, bake": 89,
        "tomato": 8,
        "broccoli": 7,
        "watermelon": 11,
        "peaches": 15,
        "oatmeal, instant": 77,
        "ranch": 73
    }

def main():

    clean_list = "\n".join(dictionary_food)
    print(f"Todays menu: {clean_list}")

    for i in dictionary_food:
        print(i)

    food = input("Type the name of a food: ").lower()
    while food not in dictionary_food:
        food = input("Not in the menu. Try again: ").lower()
     
    food2 = input("Type the name of a food: ").lower()
    while food2 not in dictionary_food:
        food2 = input("Not in the menu. Try again: ").lower()

    if {food, food2} == {"watermelon", "milk"}:
        print("DOO NOT COMBINE THOSE FOODS")
    else:
        print(f"The total calories of {food} and {food2} is {dictionary_food[food] + dictionary_food[food2]} calories.")



main()







