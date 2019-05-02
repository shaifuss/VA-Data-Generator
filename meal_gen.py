import xlrd
import classes
import random
import numpy as np
from enum import Enum


class scale(Enum):
    HI = 3
    MED = 2
    LOW = 1


meals = []


def rand_meals():
    veggies = ["artichoke", "asparagus", "alfalfa", "sprouts", "chickpeas", "beans",
               "lentils", "peas", "beans", "broccoli", "brussel sprouts", "cabbage",
               "kohlrabi", "cauliflower", "celery", "endive", "beets", "kale", "spinach",
               "anise", "basil", "cilantro", "dill", "fennel", "oregano", "parsley",
               "rosemary", "sage", "thyme", "lettuce", "arugula", "mushrooms", "spinach",
               "okra", "onions", "chives", "garlic", "leek", "onion", "shallot",
               "scallions", "parsley", "peppers", "hot pepper", "rhubarb", "carrot",
               "ginger", "parsnip", "rutabaga", "radish", "wasabi", "horseradish",
               "sweet potato", "yam", "turnip", "corn", "squash", "pumpkin",
               "tomato"]

    protein_list = ["cheese", "eggs", "soy", "fish", "chicken", "beef", "lamb", "turkey", "milk", "nuts"]

    starch = ["bread", "rice", "potatoes", "cereal", "tortilla", "cornbread", "pasta", "grains"]
    fruit = ["apples", "pears", "plums", "apricots", "cherries", "coconuts", "dates", "berries", "lychees", "mangoes",
             "peaches", "oranges", "lemons", "limes", "pomeloes", "strawberries", "melon", "watermelon"]

    cuisine_list = ['mexican', 'mediterranean', 'french', 'asian', 'italian', 'fusion', 'persian']
    for i in range(0, 1500):
        meal_veggies = np.random.choice(veggies, 12)
        extract_num = random.randint(0, 12)
        meal_veggies = meal_veggies[:len(meal_veggies) - extract_num]

        meal_protein = np.random.choice(protein_list, 3)
        extract_num = random.randint(0, 3)
        meal_protein = meal_protein[:len(meal_protein) - extract_num]

        meal_starch = np.random.choice(starch, 3)
        extract_num = random.randint(0, 3)
        meal_starch = meal_protein[:len(meal_starch) - extract_num]

        meal_fruit = np.random.choice(fruit, 3)
        extract_num = random.randint(0, 3)
        meal_fruit = meal_protein[:len(meal_fruit) - extract_num]



        veggie_dict = classes.VegDict()
        for veg in meal_veggies:
            veggie_dict[veg] = 1

        protein_dict = classes.ProteinDict()
        for pro in meal_protein:
            protein_dict[pro] = 1

        starch_dict = classes.StarchDict()
        for starch in meal_starch:
            starch_dict[starch] = 1

        fruit_dict = classes.FruitDict()
        for fruit in meal_fruit:
            fruit_dict[fruit] = 1

        # fat dependant here
        if protein_dict['cheese'] == 1 or protein_dict['beef'] == 1 or protein_dict['lamb'] == 1:
            fat = np.random.choice([3, 2, 1], 1, p=[0.7, 0.2, 0.1])
        else:
            fat = np.random.choice([3, 2, 1], 1, p=[0.2, 0.4, 0.3])

        if len(meal_protein) >= 2:
            protein = np.random.choice([3, 2, 1], 1, p=[0.8, 0.2, 0])
        else:
            protein = np.random.choice([3, 2, 1], 1, p=[0.2, 0.5, 0.3])

        if len(meal_starch) >= 2:
            carbs = np.random.choice([3, 2, 1], 1, p=[0.6, 0.2, 0.2])
        else:
            carbs = np.random.choice([3, 2, 1], 1, p=[0.2, 0.4, 0.4])

        nuts = protein_dict['nuts']

        if veggie_dict['hot pepper']:
            spicy = np.random.choice([3, 2, 1], 1, p=[0.9, 0.1, 0])
        else:
            spicy = np.random.choice([3, 2, 1], 1, p=[0.1, 0.3, 0.6])

        price = np.random.choice([3, 2, 1], 1, p=[0.2, 0.4, 0.4])

        cuisine = np.random.choice(cuisine_list, 1)

        portion = np.random.choice([3, 2, 1], 1, p=[0.3, 0.3, 0.4])

        salt = np.random.choice([3, 2, 1], 1, p=[0.2, 0.3, 0.5])

        if len(meal_fruit) >= 2:
            sweet = np.random.choice([3, 2, 1], 1, p=[0.6, 0.2, 0.2])
        else:
            sweet = np.random.choice([3, 2, 1], 1, p=[0.3, 0.3, 0.4])

        if fruit_dict['oranges'] == 1 or fruit_dict['lemons'] == 1 or fruit_dict['limes'] == 1 or fruit_dict["pomeloes"] == 1:
            sour = np.random.choice([3, 2, 1], 1, p=[0.75, 0.2, 0.05])
        else:
            sour = np.random.choice([3, 2, 1], 1, p=[0.2, 0.3, 0.5])

        if len(meal_fruit) + len(meal_veggies) >= 9:
            fiber = np.random.choice([3, 2, 1], 1, p=[0.6, 0.2, 0.2])
        else:
            fiber = np.random.choice([3, 2, 1], 1, p=[0.2, 0.4, 0.4])






        # gluten conditional
        gluten = False
        if starch_dict['bread'] == 1 or starch_dict['cereal'] == 1 or starch_dict['tortilla'] == 1:
            gluten = True

        meat = False
        if protein_dict['chicken'] == 1 or protein_dict['beef'] == 1 or protein_dict['lamb'] == 1 or protein_dict['turkey'] == 1:
                meat = True

        fish = protein_dict['fish']

        dairy = False
        if protein_dict['cheese'] == 1 or protein_dict['milk'] == 1:
            dairy = True


