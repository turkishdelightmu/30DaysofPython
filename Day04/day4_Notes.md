# Day 4 — Strings Cheatsheet

---

## String Basics

```python
company = 'Coding For All'
print(len(company))        # 14 — length of string
```

---

## Concatenation

```python
# Join with + and add spaces manually
str1, str2, str3, str4 = 'Thirty', 'Days', 'Of', 'Python'
result = str1 + ' ' + str2 + ' ' + str3 + ' ' + str4
# → 'Thirty Days Of Python'
```

---

## Case Methods

```python
company = 'Coding For All'

company.upper()       # → 'CODING FOR ALL'
company.lower()       # → 'coding for all'
company.capitalize()  # → 'Coding for all'  (only first letter of whole string)
company.title()       # → 'Coding For All'  (first letter of each word)
company.swapcase()    # → 'cODING fOR aLL'
```

---

## Slicing

```python
company = 'Coding For All'

company[:6]           # → 'Coding'   (first word)
company[0]            # → 'C'        (index 0)
company[10]           # → ' '        (space — careful, spaces count!)
company[-1]           # → 'l'        (last character)
len(company) - 1      # → 13         (last index)
```

---

## Search & Check

```python
company = 'Coding For All'

'Coding' in company           # → True   (membership check)
company.startswith('Coding')  # → True
company.endswith('coding')    # → False  (case-sensitive!)

company.index('C')            # → 0      (first 'C'; raises error if not found)
company.index('F')            # → 7      (first 'F')

sentence = 'You cannot end a sentence with because because because is a conjunction'
sentence.find('because')      # → 31     (first occurrence; returns -1 if not found)
sentence.rindex('because')    # → 47     (last occurrence)

'Coding For All People'.rfind('l')   # → 19  (last 'l')
```

---

## Replace & Split

```python
company = 'Coding For All'

company.replace('Coding', 'Python')   # → 'Python For All'

'Python for Everyone'.replace('Everyone', 'All')  # → 'Python for All'

company.split(' ')   # → ['Coding', 'For', 'All']

'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'.split(', ')
# → ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
# ⚠️ separator must match exactly — 'split(" , ")' won't work here
```

---

## Strip (Remove Whitespace)

```python
'   Coding For All   '.strip()   # → 'Coding For All'
```

---

## Slicing a Phrase

```python
sentence = 'You cannot end a sentence with because because because is a conjunction'
sentence[31:54]   # → 'because because because'
# Tip: use sentence.find('because') to get the start index → 31
```

---

## Acronym (Generator Expression)

```python
phrase = 'Python For Everyone'
''.join(word[0] for word in phrase.split())   # → 'PFE'

phrase2 = 'Coding For All'
''.join(word[0] for word in phrase2.split())  # → 'CFA'
```

---

## isidentifier()

```python
'30DaysOfPython'.isidentifier()      # → False  (starts with a number)
'thirty_days_of_python'.isidentifier()  # → True
```

---

## Join

```python
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
' # '.join(libraries)
# → 'Django # Flask # Bottle # Pyramid # Falcon'
```

---

## Escape Sequences

```python
print('Line one.\nLine two.')    # \n → new line
print('Name\tAge\tCity')         # \t → tab
```

---

## String Formatting

### `.format()` method

```python
radius = 10
area = 3.14 * radius ** 2
'The area of a circle with radius {} is {} meters square.'.format(radius, int(area))
# → 'The area of a circle with radius 10 is 314 meters square.'
# ⚠️ Use int(area) to avoid getting 314.0

num1, num2 = 8, 6
'{} + {} = {}'.format(num1, num2, num1 + num2)    # → '8 + 6 = 14'
'{} / {} = {:.2f}'.format(num1, num2, num1 / num2) # → '8 / 6 = 1.33'
# ⚠️ Use {:.2f} for 2 decimal places — plain {} gives 1.3333...
```

---

## ⚠️ Common Traps

| Trap                             | What happens                                                      | Fix                               |
| -------------------------------- | ----------------------------------------------------------------- | --------------------------------- |
| `split(' , ')` on `'word, word'` | Returns whole string as one item                                  | Use `split(', ')` — match exactly |
| `int(area)` vs `area` in format  | `314.0` instead of `314`                                          | Wrap with `int()`                 |
| `endswith('coding')`             | Case-sensitive → `False`                                          | Match exact case                  |
| Spaces count as characters       | `company[10]` is `' '` not `'A'`                                  | Count carefully                   |
| `index()` vs `find()`            | `index()` raises `ValueError` if not found; `find()` returns `-1` | Use `find()` when unsure          |

---

## 🔑 Key Takeaways

- Strings are **zero-indexed** — the first character is at index `0`, last is at `len(string) - 1`
- **Spaces are characters** — they take up an index position just like letters
- String methods **don't modify the original** — they return a new string; you must store or print the result
- `capitalize()` ≠ `title()` — `capitalize()` lowercases everything except the very first letter; `title()` capitalises each word
- `find()` is safer than `index()` — use `index()` only when you're certain the substring exists
- `split()` separator must **match exactly** — `', '` and `' , '` are different
- `{:.2f}` in `.format()` controls decimal places — without it, division gives long floats
- Wrap float results in `int()` when the expected output is a whole number
- `endswith()` and `startswith()` are **case-sensitive**
- `isidentifier()` follows Python variable naming rules — no leading digits, no spaces
