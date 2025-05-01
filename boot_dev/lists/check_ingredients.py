"""
Complete the check_ingredient_match function. It accepts two lists of strings:

recipe: The list of ingredients needed.
ingredients: The list of ingredients the character has.
It should return two values:

A float representing the percentage of required ingredients the character has.
A new list of ingredients the character is missing but that are required.
"""
# Inputs:
#  - Recipe: ['Orc Tears', 'Ogre Ear', 'Goblin Giggles', 'Witch Broom', 'Giant Toenail Clipping', 'Centipede Foot', 'Dog Hair', 'Bald Eagle Dandruff']
#  - Ingredients: ['Unicorn Hair', 'Dragon Scale', 'Phoenix Feather', 'Troll Tusk', 'Griffin Feather', 'Mandrake Root', 'Goblin Ear', 'Bald Eagle Dandruff']
#
# Expecting: (12.5, ['Orc Tears', 'Ogre Ear', 'Goblin Giggles', 'Witch Broom', 'Giant Toenail Clipping', 'Centipede Foot', 'Dog Hair'])
# Actual:    (100.0, ['Orc Tears', 'Ogre Ear', 'Goblin Giggles', 'Witch Broom', 'Giant Toenail Clipping', 'Centipede Foot', 'Dog Hair'])
# Fail
# ============= FAIL ==============
# 2 pa
recipe_one =  ['Orc Tears', 'Ogre Ear', 'Goblin Giggles', 'Witch Broom', 'Giant Toenail Clipping', 'Centipede Foot', 'Dog Hair', 'Bald Eagle Dandruff']
ingredients_one = ['Unicorn Hair', 'Dragon Scale', 'Phoenix Feather', 'Troll Tusk', 'Griffin Feather', 'Mandrake Root', 'Goblin Ear', 'Bald Eagle Dandruff']


def check_ingredient_match(recipe, ingredients):
    total = len(recipe)
    percentage = len(ingredients) / total

    not_in_list = []
    counter = 0

    for items in recipe:
        if items not in ingredients:
            not_in_list.append(items)
        else:
            counter += 1

    return (counter / total) * 100, not_in_list


print(check_ingredient_match(recipe_one, ingredients_one))