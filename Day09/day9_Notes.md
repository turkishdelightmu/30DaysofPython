# 📘 Day 9 - Conditionals

Conditionals are used to control the flow of a program based on conditions. They allow Python to make decisions using `if`, `elif`, and `else`.

A condition always evaluates to **True or False**, and Python executes the matching block accordingly.

> 📝 **Note:** Indentation matters. Every block under `if`, `elif`, and `else` must be properly indented or the code will fail.

---

## Level 1

**1. Basic if-else (driving age check)**


age = int(input("Enter your age: "))

if age >= 18:
    print("You are old enough to learn to drive.")
else:
    print(f"You need {18 - age} more years to learn to drive.")

---

**2. Comparing ages using conditions**


my_age = 25
your_age = int(input("Enter your age: "))

diff = abs(my_age - your_age)

if your_age > my_age:
    print(f"You are {diff} years older than me.")
elif your_age < my_age:
    print(f"You are {diff} years younger than me.")
else:
    print("We are the same age.")

---

**3. Compare two numbers**


a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")

---

## Level 2

**4. Grade system**


score = int(input("Enter score: "))

if 90 <= score <= 100:
    print("Grade: A")
elif 80 <= score <= 89:
    print("Grade: B")
elif 70 <= score <= 79:
    print("Grade: C")
elif 60 <= score <= 69:
    print("Grade: D")
else:
    print("Grade: F")

---

**5. Season detection from month**

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

---

**6. Check if fruit exists in list**

fruits = ['banana', 'orange', 'mango', 'lemon']

fruit = input("Enter fruit: ").lower()

if fruit in fruits:
    print("That fruit already exists in the list")
else:
    fruits.append(fruit)
    print(fruits)

---

## Level 3

**7. Accessing dictionary conditionally**

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
}

---

**8. Middle skill extraction**

if 'skills' in person:
    skills = person['skills']
    print(skills[len(skills) // 2])

---

**9. Check for Python skill**

if 'skills' in person:
    print('Python' in person['skills'])

---

**10. Determine developer type**

skills = person.get('skills', [])

if 'JavaScript' in skills and 'React' in skills and len(skills) == 2:
    print("Front end developer")
elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
    print("Backend developer")
elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
    print("Fullstack developer")
else:
    print("Unknown title")

---

**11. Check marriage and country**


if person.get('is_married') and person.get('country') == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in Finland. He is married.")

---

## 🧠 Cheatsheet

| Concept             | Syntax            | Notes                        |
| ------------------- | ----------------- | ---------------------------- |
| if condition        | `if condition:`   | runs block if True           |
| else                | `else:`           | fallback block               |
| else if             | `elif condition:` | multiple conditions          |
| comparison          | `> < >= <= == !=` | returns True/False           |
| logical AND         | `and`             | all conditions must be True  |
| logical OR          | `or`              | at least one True            |
| membership          | `in`              | checks presence in list/dict |
| absolute difference | `abs(x - y)`      | useful for comparisons       |
| indentation         | 4 spaces          | required in Python           |

