# Day 2: 30 Days of python programming

# Exercise: Level 1

# 1. Declare a first name variable and assign a value to it
first_name = 'Aisha'

# 2. Declare a last name variable and assign a value to it
last_name = 'Tan'

# 3. Declare a full name variable and assign a value to it
full_name = first_name + ' ' + last_name

# 4. Declare a country variable and assign a value to it
country = 'Turkey'

# 5. Declare a city variable and assign a value to it
city = 'Istanbul'

# 6. Declare an age variable and assign a value to it
age = 25

# 7. Declare a year variable and assign a value to it
year = 2024

# 8. Declare a variable is_married and assign a value to it
is_married = False

# 9. Declare a variable is_true and assign a value to it
is_true = True

# 10. Declare a variable is_light_on and assign a value to it
is_light_on = True

# 11. Declare multiple variables on one line
first_name, last_name, country, age, is_married = 'Aisha', 'Taneri', 'Turkey', 25, False
print(first_name, last_name, country, age, is_married)

# Exercise: Level 2

# 1. Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

# 2. Using len() find the length of your first name
# 3. Compare the length of your first name and your last name
compare_name_last_name = len(first_name) > len(last_name)
print(compare_name_last_name)

# 4. Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

# 5. Add num_one and num_two and assign to total
total = num_one + num_two
print(total)

# 6. Subtract num_two from num_one and assign to diff
diff = num_one - num_two
print(diff)

# 7. Multiply num_two and num_one and assign to product
times = num_one * num_two
print(times)

# 8. Divide num_one by num_two and assign to division
divi = num_one / num_two
print(divi)

# 9. Use modulus division and assign to remainder
per = num_one % num_two
print(per)

# 10. Calculate num_one to the power of num_two and assign to exp
power = num_one ** num_two
print(power)

# 11. Find floor division of num_one by num_two and assign to floor_division
flo_divi = num_one // num_two
print(flo_divi)

# 12. The radius of a circle is 30 meters
# 12a. Calculate the area of a circle
# 12b. Calculate the circumference of a circle
# 12c. Take radius as user input and calculate the area
rad = float(input('Enter radius of a circle: '))
area_of_circle = 3.14 * rad ** 2
print(area_of_circle)
circum_of_circle = 2 * 3.14 * rad
print(circum_of_circle)

# 13. Use input() to get first name, last name, country and age from user
first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
country = input('Enter your country: ')
age = input('Enter your age: ')
print(first_name, last_name, country, age)

# 14. Run help('keywords') to check Python reserved words
help('keywords')
