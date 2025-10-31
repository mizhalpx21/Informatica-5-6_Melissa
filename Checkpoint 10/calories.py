def main():
    dictionary_food = {
        "Almond milk": 30,
        "Whole": 73,
        "Sour Cream, cultured": 26,
        "Plain, low-fat": 77,
        "egg": 75,
        "egg substitute": 30,
        "Parmesan Cheese, grated": 22,
        "Cottage Cheese, low fat": 20,
        "Peanuts, roasted": 166,
        "Sunflower seeds, dry roasted": 165,
        "Edamame, boiled": 127,
        "Lentils, boiled": 115,
        "Shrimp, boiled": 28,
        "Swai, bake": 89,
        "tomato": 8,
        "Broccoli": 7,
        "Watermellon": 11,
        "Peaches": 15,
        "Oatmeal, instant": 77,
        "Ranch": 73
    }

    clean_list = "\n".join(dictionary_food)
    print(f"Todays menu: {clean_list}")
    food = input("Type the name of one food: ")
    for f in food: 
        calories = int(input(f"Number of calories of [f]"))





   





main()


