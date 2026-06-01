# Day 4

# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

str1 = 'Thirty'
str2 = 'Days'
str3 = 'Of'
str4 = 'Python'
concatenated_str = str1 + ' ' + str2 + ' ' + str3 + ' ' + str4
print(concatenated_str)

# 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.

str5 = 'Coding'
str6 = 'For'
str7 = 'All'
concatenated_str2 = str5 + ' ' + str6 + ' ' + str7
print(concatenated_str2)

# 3. Declare a variable named company and assign it to an initial value "Coding For All".

company = 'Coding For All'

# 4. Print the variable company using print().
print(company)

# 5. Print the length of the company string using len() method and print().
print(len(company))

# 6. Change all the characters to uppercase letters using upper() method.
print(company.upper())

# 7. Change all the characters to lowercase letters using lower() method.
print(company.lower())

# 8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9. Cut(slice) out the first word of Coding For All string.
first_word = company[:6]
print(first_word)

# 10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
print('Does the string contain "Coding"?', 'Coding' in company)

# 11. Replace the word coding in the string 'Coding For All' to Python.
replaced_str = company.replace('Coding', 'Python')
print(replaced_str)

# 12. Change Python for Everyone to Python for All using the replace method or other methods.
original_str = 'Python for Everyone'
modified_str = original_str.replace('Everyone', 'All')
print(modified_str)

# 13. Split the string 'Coding For All' using space as the separator (split()) .
split_str = company.split(' ')
print(split_str)

# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
companies_str = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
companies_list = companies_str.split(', ')
print(companies_list)

# 15. What is the character at index 0 in the string Coding For All.
first_char = company[0]
print('The character at index 0 is:', first_char)

# 16. What is the last index of the string Coding For All.
last_index = len(company) - 1
print('The last index of the string is:', last_index)

# 17. What character is at index 10 in "Coding For All" string.
char_at_index_10 = company[10]
print('The character at index 10 is:', char_at_index_10)

# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
phrase = 'Python For Everyone'
acronym = ''.join(word[0] for word in phrase.split())
print('The acronym for "Python For Everyone" is:', acronym)

# 19. Create an acronym or an abbreviation for the name 'Coding For All'.
phrase2 = 'Coding For All'
acronym2 = ''.join(word[0] for word in phrase2.split())
print('The acronym for "Coding For All" is:', acronym2)

# 20. Use index to determine the position of the first occurrence of C in Coding For All.
index_c = company.index('C')
print('The index of the first occurrence of "C" is:', index_c)

# 21. Use index to determine the position of the first occurrence of F in Coding For All.
index_f = company.index('F')
print(' The index of the first occurrence of "F" is:', index_f)

# 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
company_people = 'Coding For All People'
index_l = company_people.rfind('l')
print('The index of the last occurrence of "l" is:', index_l)

# 23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
index_because = sentence.find('because')
print('The index of the first occurrence of "because" is:', index_because)

# 24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
index_because_last = sentence.rindex('because')
print('The index of the last occurrence of "because" is:', index_because_last)

# 25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sliced_phrase = sentence[31:54]
print('The sliced phrase is:', sliced_phrase)

# 26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
index_because_first = sentence.find('because')
print('The index of the first occurrence of "because" is:', index_because_first)

# 27. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sliced_phrase2 = sentence[31:54]
print('The sliced phrase is:', sliced_phrase2)

# 28. Does "Coding For All" start with a substring Coding?
print('Does "Coding For All" start with "Coding"?', company.startswith('Coding'))

# 29. Does "Coding For All" end with a substring coding?
print('Does "Coding For All" end with "coding"?', company.endswith('coding'))

# 30. '   Coding For All      '  , remove the left and right trailing spaces in the given string.
str_with_spaces = '   Coding For All    '
print('Original string:', repr(str_with_spaces))
trimmed_str = str_with_spaces.strip()
print('Trimmed string:', repr(trimmed_str))

# 31. Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python

var1 = '30DaysOfPython'
var2 = 'thirty_days_of_python'
print('Is var1 a valid identifier?', var1.isidentifier())
print('Is var2 a valid identifier?', var2.isidentifier())

# 32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_libraries = ' # '.join(libraries)
print('Joined libraries:', joined_libraries)

# 33. Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.

print('I am enjoying this challenge.\nI just wonder what is next. ')

# 34. Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki

print('Name\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')

# 35. Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.

radius = 10
area = 3.14 * radius ** 2
formatted_str = 'The area of a circle with radius {} is {} meters square.'.format(
    radius, int(area))
print(formatted_str)

# 36. Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144

num1 = 8
num2 = 6
print('{} + {} = {}'.format(num1, num2, num1 + num2))
print('{} - {} = {}'.format(num1, num2, num1 - num2))
print('{} * {} = {}'.format(num1, num2, num1 * num2))
print('{} / {} = {:.2f}'.format(num1, num2, num1 / num2))
print('{} % {} = {}'.format(num1, num2, num1 % num2))
print('{} // {} = {}'.format(num1, num2, num1 // num2))
print('{} ** {} = {}'.format(num1, num2, num1 ** num2))
