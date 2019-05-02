
class VegDict:
    """

    """
    def __init__(self):
        self.contains_veg = dict.fromkeys(["artichoke", "asparagus", "alfalfa", "sprouts", "chickpeas", "beans",
                                           "lentils", "peas", "beans", "broccoli", "brussel sprouts", "cabbage",
                                           "kohlrabi", "cauliflower","celery", "endive", "beets", "kale", "spinach",
                                           "anise", "basil", "cilantro", "dill", "fennel", "oregano", "parsley",
                                           "rosemary", "sage", "thyme", "lettuce", "arugula", "mushrooms", "spinach",
                                           "okra", "onions", "chives", "garlic", "leek", "onion", "shallot",
                                           "scallions", "parsley", "peppers", "hot pepper", "rhubarb", "carrot",
                                           "ginger", "parsnip", "rutabaga", "radish", "wasabi", "horseradish",
                                           "sweet potato", "yam", "turnip", "corn", "squash", "pumpkin",
                                           "tomato"], 0)

class ProteinDict:
    """

    """
    def __init__(self):
        self.contains_protein = dict.fromkeys(["cheese", "eggs", "soy", "fish", "chicken", "beef", "lamb", "turkey",
                                               "milk"], 0)



class StarchDict:
    """

    """
    def __init__(self):
        self.contains_carb = dict.fromkeys(["bread", "rice", "potatoes", "cereal", "tortilla", "cornbread", "pasta",
                                            "grains"], 0)

class FruitDict:
    """

    """
    def __init__(self):
        self.contains_fruit = dict.fromkeys(["apples", "pears", "plums", "apricots", "cherries", "coconuts", "dates",
                                             "berries", "lychees", "mangoes", "peaches", "oranges", "lemons", "limes",
                                             "pomeloes", "strawberries", "melon", "watermelon"], 0)


class Reply:
    """

    """
    def __init__(self, answer, question):
        self.answer = answer
        self.question = question


class Question:
    """
    typ - {greeting, request_for_info, clarify, wrap_up}
    """
    def __init__(self, speaker, question, q_list, typ):
        self.speaker = speaker
        self.question = question
        self.ans = q_list
        self.typ = typ


class Answer:
    """
    typ - {greeting, info}
    """
    def __init__(self, speaker, text, ans_list, typ):
        self.speaker = speaker
        self.ans = text
        self.ans = ans_list
        self.typ = typ


class Order:
    """
    gluten - boolean v
    meat - boolean      # can potentially be eliminated with separate dicts
    fish - boolean      # can potentially be eliminated with separate dicts
    dairy - boolean     # can potentially be eliminated with separate dicts
    nuts - boolean v
    spicy - {hi, med, low} v
    price - {hi, med, low} v
    cuisine - {mex, french, italian...} v
    portion_size - {hi, med, low} v
    salt - {hi, med, low} v
    sweet - {hi, med, low}
    sour - {hi, med, low}
    fat - {hi, med, low} v
    protein - {hi, med, low} v
    carbs - {hi, med, low} v
    fiber - {hi, med, low}
    calories - {hi, med, low}
    cook_style - subset of {grilled, roasted, smoked, fried, steamed, sauteed, baked, raw}
    cook_level {rare, medium, well}
    meal - {breakfast, lunch, dinner, snack}   (use subset?)
    meal_density - {heavy, light}
    review - numeric (0.0 - 5.0)


    """
    def __init__(self, veg_dict, protein_dict, carb_dict, fruit_dict, gluten, meat, fish, dairy, nuts, spicy, price,
                 cuisine, portion_size, salt, sweet, sour, fat,
                 protein, carbs, fiber, calories, cook_style, cook_level, meal, meal_density, review):
        self.veg_dict = veg_dict
        self.protein_dict = protein_dict
        self.carb_dict = carb_dict
        self.fruit_dict = fruit_dict
        self.gluten = gluten
        self.meat = meat
        self.fish = fish
        self.dairy = dairy
        self.nuts = nuts
        self.spicy = spicy
        self.price = price
        self.cuisine = cuisine
        self.portion_size = portion_size
        self.salt = salt
        self.sweet = sweet
        self.sour = sour
        self.fat = fat
        self.protein = protein
        self.carbs = carbs
        self.fiber = fiber
        self.calories = calories
        self.cook_style = cook_style
        self.cook_level = cook_level
        self.meal = meal
        self.meal_density = meal_density
        self.review = review    # enforce domain?
