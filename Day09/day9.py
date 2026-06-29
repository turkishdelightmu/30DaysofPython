# Day 9 - Conditionals

# 💻 Exercises: Level 1

# 1. Age check (driving eligibility)

age = int(input("Enter your age: "))

if age >= 18:
    print("You are old enough to learn to drive.")
else:
    print(f"You need {18 - age} more years to learn to drive.")

# 2. Compare age with mine

my_age = 25
your_age = int(input("Enter your age: "))

diff = abs(my_age - your_age)

if your_age > my_age:
    if diff == 1:
        print("You are 1 year older than me.")
    else:
        print(f"You are {diff} years older than me.")
elif your_age < my_age:
    if diff == 1:
        print("You are 1 year younger than me.")
    else:
        print(f"You are {diff} years younger than me.")
else:
    print("We are the same age.")

# 3. Compare two numbers

a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")


# 💻 Exercises: Level 2

# 1. Grade system

score = int(input("Enter score: "))

if 90 <= score <= 100:
    print("Grade: A")
elif 80 <= score <= 89:
    print("Grade: B")
elif 70 <= score <= 79:
    print("Grade: C")
elif 60 <= score <= 69:
    print("Grade: D")
elif 0 <= score <= 59:
    print("Grade: F")
else:
    print("Invalid score")

# 2. Season checker

month = input("Enter month: ").capitalize()

if month in ["September", "October", "November"]:
    print("Autumn")
elif month in ["December", "January", "February"]:
    print("Winter")
elif month in ["March", "April", "May"]:
    print("Spring")
elif month in ["June", "July", "August"]:
    print("Summer")
else:
    print("Invalid month")


# 3. Fruit list check

fruits = ['banana', 'orange', 'mango', 'lemon']

fruit = input("Enter fruit: ").lower()

if fruit in fruits:
    print("That fruit already exists in the list")
else:
    fruits.append(fruit)
    print(fruits)


# 💻 Exercises: Level 3

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }

# 1. Middle skill

if 'skills' in person:
    skills = person['skills']
    print(skills[len(skills) // 2])

# 2. Python skill check

if 'skills' in person:
    print('Python' in person['skills'])

# 3. Developer type

skills = person.get('skills', [])

if 'JavaScript' in skills and 'React' in skills and len(skills) == 2:
    print("Front end developer")
elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
    print("Backend developer")
elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
    print("Fullstack developer")
else:
    print("Unknown title")

# 4. Marriage and country check

if person.get('is_married') and person.get('country') == 'Finland':
    print(
        f"{person['first_name']} {person['last_name']} lives in Finland. He is married.")
