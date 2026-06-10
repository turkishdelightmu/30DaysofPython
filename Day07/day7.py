# Day 7 - Sets

it_companies = {'Facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Exercise 1

# 1. Find the length of the set it_companies
length_set = len(it_companies)
print(f"Length of it_companies: {length_set}")
# 2. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(f"it_companies after adding Twitter: {it_companies}")
# 3. Insert multiple IT companies at once to the set it_companies
it_companies.update(['Meta', 'LinkedIn', 'Netflix'])
print(f"it_companies after adding multiple companies: {it_companies}")
# 4. Remove one of the companies from the set it_companies
it_companies.remove('Facebook')
print(f"it_companies after removing Facebook: {it_companies}")
# 5. What is the difference between remove and discard
# if an element is not found in the set, remove will raise a KeyError, while discard will not raise an error and will simply do nothing.

# Exercises: Level 2

# 1. Join A and B
A_union_B = A.union(B)
print(f"Union of A and B: {A_union_B}")
# 2. Find A intersection B
A_intersection_B = A.intersection(B)
print(f"Intersection of A and B: {A_intersection_B}")
# 3. Is A subset of B
A_is_subset_B = A.issubset(B)
print(f"Is A a subset of B? {A_is_subset_B}")
# 4. Are A and B disjoint sets
A_and_B_disjoint = A.isdisjoint(B)
print(f"Are A and B disjoint sets? {A_and_B_disjoint}")
# 5. Join A with B and B with A
A_union_B = A.union(B)
B_union_A = B.union(A)
print(f"Union of A and B: {A_union_B}")
print(f"Union of B and A: {B_union_A}")
# 6. What is the symmetric difference between A and B
A_symmetric_difference_B = A.symmetric_difference(B)
print(f"Symmetric difference between A and B: {A_symmetric_difference_B}")
# 7. Delete the sets completely
del A
del B


# Exercises: Level 3

# 1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)
length_age_list = len(age)
length_age_set = len(age_set)
print(f"Length of age list: {length_age_list}")
print(f"Length of age set: {length_age_set}")
length_age_list_is_bigger = length_age_list > length_age_set
print(f"Is the list bigger than the set? {length_age_list_is_bigger}")
# 2. Explain the difference between the following data types: string, list, tuple and set
# - String: A string is a sequence of characters enclosed in quotes. It is immutable, meaning it cannot be changed after it is created.
# - List: A list is an ordered collection of items that can be changed (mutable).
# - Tuple: A tuple is an ordered collection of items that cannot be changed (immutable).
# - Set: A set is an unordered collection of unique items.
# 3. I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people"
words = sentence.split()
unique_words = set(words)
number_of_unique_words = len(unique_words)
print(
    f"The number of unique words in the sentence is: {number_of_unique_words}")
