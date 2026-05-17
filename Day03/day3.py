# Day 3: 30 Days of Python Programming

# 1. Declare your age as integer variable
age = 25

# 2. Declare your height as a float variable
height = 5.6

# 3. Declare a variable that store a complex number
complex_num = 1 + 4j

# 4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = float(input('Enter base of the triangle: '))
height = float(input('Enter height of the triangle: '))
area = 0.5 * base * height
print('The area of the triangle is:', area)

# 5.Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
side_a = float(input('Enter side of a triangle:'))
side_b = float(input('Enter side of a triangle: '))
side_c = float(input('Enter side of a triangle: '))
perimeter = side_a + side_b + side_c
print('The perimeter of the triangle is:', perimeter)

# 6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = float(input('Enter length of the rectangle: '))
width = float(input('Enter width of the rectangle: '))
area = length * width
perimeter = 2 * (length + width)
print('The area of the rectangle is:', area)
print('The perimeter of the rectangle is:', perimeter)

# 7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius = float(input('Enter radius of the circle: '))
pi = 3.14
area = pi * radius * radius
circum = 2 * pi * radius
print('The area of the circle is:', area)
print('The circumference of the circle is:', circum)

# 8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
slope_8 = 2
x_intercept = 1
y_intercept = -2
print('The slope of the line is:', slope_8)
print('The x-intercept of the line is:', x_intercept)
print('The y-intercept of the line is:', y_intercept)

# 9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1, y1 = 2, 2
x2, y2 = 6, 10
slope_9 = (y2 - y1) / (x2 - x1)
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print('The slope between the points is:', slope_9)
print('The Euclidean distance between the points is:', distance)

# 10. Compare the slopes in tasks 8 and 9.
print('Are the slopes in tasks 8 and 9 equal:', slope_8 == slope_9)

# 11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
x = -3
y = x**2 + 6*x + 9
print('The value of y when x is -3 is:', y)

x = 0
y = x**2 + 6*x + 9
print('The value of y when x is 0 is:', y)

x = 3
y = x**2 + 6*x + 9
print('The value of y when x is 3 is:', y)

x = -6
y = x**2 + 6*x + 9
print('The value of y when x is -6 is:', y)

# 12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
length_python = len('python')
length_dragon = len('dragon')
print('Length of python:', length_python)
print('Length of dragon:', length_dragon)
print('Is the length of python equal to the length of dragon?',
      length_python == length_dragon)

# 13. Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('Is "on" found in both "python" and "dragon"?',
      'on' in 'python' and 'on' in 'dragon')

# 14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sentence = 'I hope this course is not full of jargon.'
print('Is "jargon" in the sentence?', 'jargon' in sentence)

# 15. There is no 'on' in both dragon and python.
print('Is "on" not found in both "dragon" and "python"?',
      'on' not in 'dragon' and 'on' not in 'python')

# 16. Find the length of the text python and convert the value to float and convert it to string
length_python = len('python')
length_float = float(length_python)
length_str = str(length_float)
print('Length of "python" as a float:', length_float)
print('Length of "python" as a string: ', length_str)

# 17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
number = int(input('Enter a number: '))
is_even = number % 2 == 0
print(is_even, 'is an even number.')

# 18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
floor_division = 7 // 3
int_value = int(2.7)
print('Is the floor division of 7 by 3 equal to the int converted value of 2.7?',
      floor_division == int_value)

# 19. Check if type of '10' is equal to type of 10
print('Is the type of "10" equal to the type of 10?', type('10') == type(10))

# 20. Check if int('9.8') is equal to 10
print('Is int("9.8") equal to 10?', int(float('9.8')) == 10)

# 21. Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = float(input('Enter hours worked: '))
rate_per_hour = float(input('Enter rate per hour: '))
pay = hours * rate_per_hour
print('The pay of the person is:', pay)

# 22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years = float(input('Enter number of years: '))
seconds_in_year = 365 * 24 * 60 * 60
total_seconds = years * seconds_in_year
print('The number of seconds a person can live is:', total_seconds)

# 23. Write a Python script that displays the following table
i = 1
print(i, 1, i, i**2, i**3)
i = 2
print(i, 1, i, i**2, i**3)
i = 3
print(i, 1, i, i**2, i**3)
i = 4
print(i, 1, i, i**2, i**3)
i = 5
print(i, 1, i, i**2, i**3)
