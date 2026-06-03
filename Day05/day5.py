# Day 5 - Lists

# Exercise - Level 1

# 1.Declare an empty list
empty_list = list()

# 2.Declare a list with more than 5 items
web_techs = ['HTML', 'CSS', 'JS', 'React', 'Python']

# 3.Find the length of your list
print(len(web_techs))

# 4.Get the first item, the middle item and the last item of the list
first_item = web_techs[0]
middle_item = web_techs[2]  # web_techs[len(web_techs) // 2]
last_item = web_techs[-1]
print(first_item, middle_item, last_item)

# 5.Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Aisha', 25, 1.68, 'Single', '124 Main Street']

# 6.Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon']

# 7.Print the list using print()
print(it_companies)

# 8. Print the number of companies in the list
print(len(it_companies))

# 9. Print the first, middle and last company
first_company = it_companies[0]
middle_company = it_companies[len(it_companies) // 2]
last_company = it_companies[-1]
print(first_company, middle_company, last_company)

# 10. Print the list after modifying one of the companies
it_companies[0] = 'Meta'
print(it_companies)

# 11. Add an IT company to it_companies
it_companies.append('Tesla')
print(it_companies)

# 12. Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies) // 2, 'Reddit')
print(it_companies)

# 13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[3] = it_companies[3].upper()
print(it_companies)

# 14. Join the it_companies with a string '#;  '
joined_companies = '#;  '.join(it_companies)
print(joined_companies)

# 15. Check if a certain company exists in the it_companies list.
company_check = 'Google' in it_companies
print(company_check)

# 16. Sort the list using sort() method
it_companies.sort()
print(it_companies)

# 17. Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# 18. Slice out the first 3 companies from the list
first_three = it_companies[:3]
print(first_three)

# 19. Slice out the last 3 companies from the list
last_three = it_companies[-3:]
print(last_three)

# 20. Slice out the middle IT company or companies from the list
middle_index = it_companies[2:5]
print(middle_index)

# 21. Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)

# 22. Remove the middle IT company or companies from the list
it_companies.pop(2)
print(it_companies)

# 23. Remove the last IT company from the list
it_companies.pop(-1)
print(it_companies)

# 24. Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# 25. Destroy the IT companies list
del it_companies

# 26. Join the following lists: front_end and back_end.
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)

# 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
redux_index = full_stack.index('Redux')
full_stack[redux_index + 1: redux_index + 1] = ['Python', 'SQL']

# Exercise - Level 2

# 1. The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages.sort()
min_age = ages[0]
max_age = ages[-1]
print(f'Min age: {min_age}, Max age: {max_age}')

# Add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)
print(ages)

# Find the median age (one middle item or two middle items divided by two)
ages.sort()
mid = len(ages) // 2
median_age = (ages[mid] + ages[mid - 1]) / 2
print(f'Median age: {median_age}')

# Find the average age (sum of all items divided by their number )
average = sum(ages) / len(ages)
print(f'Average age: {average}')

# Find the range of the ages (max minus min)
age_range = max_age - min_age
print(f'Age range: {age_range}')

# Compare the value of (min - average) and (max - average), use abs() method
min_diff = abs(min_age - average)
max_diff = abs(max_age - average)
print(f'Min - Average: {min_diff}, Max - Average: {max_diff}')

# 1. Find the middle country(ies) in the countries list
countries = [
    'Afghanistan',
    'Albania',
    'Algeria',
    'Andorra',
    'Angola',
    'Antigua and Barbuda',
    'Argentina',
    'Armenia',
    'Australia',
    'Austria',
    'Azerbaijan',
    'Bahamas',
    'Bahrain',
    'Bangladesh',
    'Barbados',
    'Belarus',
    'Belgium',
    'Belize',
    'Benin',
    'Bhutan',
    'Bolivia',
    'Bosnia and Herzegovina',
    'Botswana',
    'Brazil',
    'Brunei',
    'Bulgaria',
    'Burkina Faso',
    'Burundi',
    'Cabo Verde',
    'Cambodia',
    'Cameroon',
    'Canada',
    'Central African Republic',
    'Chad',
    'Chile',
    'China',
    'Colombia',
    'Comoros',
    'Congo, Democratic Republic of the',
    'Congo, Republic of the',
    'Costa Rica',
    "Côte d'Ivoire",
    'Croatia',
    'Cuba',
    'Cyprus',
    'Czech Republic',
    'Denmark',
    'Djibouti',
    'Dominica',
    'Dominican Republic',
    'East Timor (Timor-Leste)',
    'Ecuador',
    'Egypt',
    'El Salvador',
    'Equatorial Guinea',
    'Eritrea',
    'Estonia',
    'Eswatini',
    'Ethiopia',
    'Fiji',
    'Finland',
    'France',
    'Gabon',
    'Gambia',
    'Georgia',
    'Germany',
    'Ghana',
    'Greece',
    'Grenada',
    'Guatemala',
    'Guinea',
    'Guinea-Bissau',
    'Guyana',
    'Haiti',
    'Honduras',
    'Hungary',
    'Iceland',
    'India',
    'Indonesia',
    'Iran',
    'Iraq',
    'Ireland',
    'Israel',
    'Italy',
    'Jamaica',
    'Japan',
    'Jordan',
    'Kazakhstan',
    'Kenya',
    'Kiribati',
    'Korea, North',
    'Korea, South',
    'Kuwait',
    'Kyrgyzstan',
    'Laos',
    'Latvia',
    'Lebanon',
    'Lesotho',
    'Liberia',
    'Libya',
    'Liechtenstein',
    'Lithuania',
    'Luxembourg',
    'Madagascar',
    'Malawi',
    'Malaysia',
    'Maldives',
    'Mali',
    'Malta',
    'Marshall Islands',
    'Mauritania',
    'Mauritius',
    'Mexico',
    'Micronesia',
    'Moldova',
    'Monaco',
    'Mongolia',
    'Montenegro',
    'Morocco',
    'Mozambique',
    'Myanmar',
    'Namibia',
    'Nauru',
    'Nepal',
    'Netherlands',
    'New Zealand',
    'Nicaragua',
    'Niger',
    'Nigeria',
    'North Macedonia',
    'Norway',
    'Oman',
    'Pakistan',
    'Palau',
    'Palestine',
    'Panama',
    'Papua New Guinea',
    'Paraguay',
    'Peru',
    'Philippines',
    'Poland',
    'Portugal',
    'Qatar',
    'Romania',
    'Russia',
    'Rwanda',
    'Saint Kitts and Nevis',
    'Saint Lucia',
    'Saint Vincent and the Grenadines',
    'Samoa',
    'San Marino',
    'Sao Tome and Principe',
    'Saudi Arabia',
    'Senegal',
    'Serbia',
    'Seychelles',
    'Sierra Leone',
    'Singapore',
    'Slovakia',
    'Slovenia',
    'Solomon Islands',
    'Somalia',
    'South Africa',
    'South Sudan',
    'Spain',
    'Sri Lanka',
    'Sudan',
    'Suriname',
    'Sweden',
    'Switzerland',
    'Syria',
    'Tajikistan',
    'Tanzania',
    'Thailand',
    'Togo',
    'Tonga',
    'Trinidad and Tobago',
    'Tunisia',
    'Turkey',
    'Turkmenistan',
    'Tuvalu',
    'Uganda',
    'Ukraine',
    'United Arab Emirates',
    'United Kingdom',
    'United States',
    'Uruguay',
    'Uzbekistan',
    'Vanuatu',
    'Vatican City',
    'Venezuela',
    'Vietnam',
    'Yemen',
    'Zambia',
    'Zimbabwe'
]

n = len(countries)
middle_countries = countries[(n-1) // 2: (n+2) // 2]
print(middle_countries)


# 2. Divide the countries list into two equal lists if it is even if not one more country for the first half.
half = len(countries) // 2 + len(countries) % 2
first_half = countries[:half]
second_half = countries[half:]
print(first_half)
print(second_half)

# 3. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
countries = ['China', 'Russia', 'USA',
             'Finland', 'Sweden', 'Norway', 'Denmark']
first_three, scandic = countries[:3], countries[3:]
print(f'First three countries: {first_three}')
print(f'Scandic countries: {scandic}')
