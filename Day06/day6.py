# Day 6 - Tuples

# Exercise: Level 1

# 1. Create an empty tuple
empty_tuple = ()
# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ("Sana", "Hana", "Rania")
brothers = ("Ahmad", "Uthman", "Omar")
# 3. Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
print(siblings)
# 4. How many siblings do you have?
num_sib = len(siblings)
# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
mother = ("Fatima",)
father = ("Kamal",)
family_members = siblings + mother + father
print(family_members)

# Exercise Level 2

# 1. Unpack siblings and parents from family_members
bro1, bro2, bro3, sis1, sis2, sis3, mother, father = family_members
# 2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("apple", "banana", "strawberry")
veggies = ("carrot", "lettuce", "cucumber")
animal_products = ("milk", "cheese", "yogurt")
food_stuff_tp = fruits + veggies + animal_products
print(food_stuff_tp)

# 3. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
# 4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
mid = len(food_stuff_tp) // 2
print(food_stuff_tp[mid]) 

# 5. Slice out the first three items and the last three items from food_stuff_lt list
first_three = food_stuff_lt[:3]
print(first_three)
last_three = food_stuff_lt[-3:]
print(last_three)

# 6. Delete the food_stuff_tp tuple completely
del food_stuff_tp
# 7. Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

# Check if 'Estonia' is a nordic country
print('Estonia' in nordic_countries)
# Check if 'Iceland' is a nordic country
print('Iceland' in nordic_countries)
