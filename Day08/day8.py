# Day 8 - Dictionary

# 1. Create an empty dictionary called dog
dog = {}
# 2. Add name, color, breed, legs, age to the dog dictionary
dog = {'name': 'Fluffy', 'color': 'white',
       'breed': 'Samoyed', 'legs': 4, 'age': 2}
# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student_dic = {
    'first_name': 'Aisha',
    'last_name': 'Tan',
    'gender': 'Female',
    'age': 25,
    'country': 'Mauritius',
    'is_married': True,
    'skills': ['Python', 'Swift'],
    'city': 'Beau Vallon',
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
# 4. Get the length of the student dictionary
print(len(student_dic))
# 5. Get the value of skills and check the data type, it should be a list
print(type(student_dic['skills']))
# 6. Modify the skills values by adding one or two skills
student_dic['skills'].append('HTML')
print(student_dic)
# 7. Get the dictionary keys as a list
keys = student_dic.keys()
print(keys)
# 8. Get the dictionary values as a list
values = student_dic.values()
print(values)
# 9. Change the dictionary to a list of tuples using items() method
print(student_dic.items())
# 10. Delete one of the items in the dictionary
student_dic.pop('first_name')
# 11. Delete one of the dictionaries
del dog
