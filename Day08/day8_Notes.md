# 📘 Day 8 - Dictionaries

A dictionary is a collection of key:value pairs. Unlike lists or tuples, items are accessed by key instead of index. Dictionaries are **mutable** — you can add, change, and remove items after creation.

> 📝 **Note:** `dct.clear()` and `del dct` are not the same. `clear()` empties the dictionary but the variable still exists (`{}`). `del` destroys the variable completely — accessing it after raises `NameError`.

---

## Level 1

**1. Create an empty dictionary called `dog`**
```python
dog = {}
```

**2. Add name, color, breed, legs, age to the dog dictionary**
```python
dog = {'name': 'Fluffy', 'color': 'white',
       'breed': 'Samoyed', 'legs': 4, 'age': 2}
```

**3. Create a student dictionary with first_name, last_name, gender, age, marital status, skills, country, city, address**
```python
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
```

**4. Get the length of the student dictionary**
```python
print(len(student_dic))
# 9
```

**5. Get the value of skills and check its data type**
```python
print(type(student_dic['skills']))
# <class 'list'>
```

---

## Level 2

**6. Modify skills by adding one or two more skills**
```python
student_dic['skills'].append('HTML')
print(student_dic)
# {'first_name': 'Aisha', 'last_name': 'Tan', 'gender': 'Female', 'age': 25,
#  'country': 'Mauritius', 'is_married': True,
#  'skills': ['Python', 'Swift', 'HTML'], 'city': 'Beau Vallon',
#  'address': {'street': 'Space street', 'zipcode': '02210'}}
```

**7. Get the dictionary keys as a list**
```python
keys = student_dic.keys()
print(keys)
# dict_keys(['first_name', 'last_name', 'gender', 'age', 'country',
#             'is_married', 'skills', 'city', 'address'])
```

**8. Get the dictionary values as a list**
```python
values = student_dic.values()
print(values)
# dict_values(['Aisha', 'Tan', 'Female', 25, 'Mauritius', True,
#               ['Python', 'Swift', 'HTML'], 'Beau Vallon',
#               {'street': 'Space street', 'zipcode': '02210'}])
```

**9. Change the dictionary to a list of tuples using `items()`**
```python
print(student_dic.items())
# dict_items([('first_name', 'Aisha'), ('last_name', 'Tan'), ('gender', 'Female'),
#             ('age', 25), ('country', 'Mauritius'), ('is_married', True),
#             ('skills', ['Python', 'Swift', 'HTML']), ('city', 'Beau Vallon'),
#             ('address', {'street': 'Space street', 'zipcode': '02210'})])
```

---

## Level 3

**10. Delete one of the items in the dictionary**
```python
student_dic.pop('first_name')
```

**11. Delete one of the dictionaries entirely**
```python
del dog
# dog no longer exists — calling it raises NameError
```

---

## 🧠 Cheatsheet

| Operation | Syntax | Notes |
|---|---|---|
| Create | `{}` or `dict()` | |
| Access | `dct['key']` | raises `KeyError` if missing |
| Safe access | `dct.get('key')` | returns `None` if missing |
| Add/Modify | `dct['key'] = value` | adds if new, overwrites if exists |
| Check key exists | `'key' in dct` | returns bool |
| Remove (by key) | `dct.pop('key')` | removes & returns value |
| Remove (last item) | `dct.popitem()` | |
| Remove (by key, no return) | `del dct['key']` | |
| Empty dict, keep variable | `dct.clear()` | dict becomes `{}` |
| Delete variable entirely | `del dct` | variable no longer exists |
| Copy (no mutation) | `dct.copy()` | |
| Length | `len(dct)` | counts key:value pairs |
| Keys as view | `dct.keys()` | |
| Values as view | `dct.values()` | |
| Key-value pairs as view | `dct.items()` | tuples |
| Order | insertion-ordered | guaranteed since Python 3.7 |