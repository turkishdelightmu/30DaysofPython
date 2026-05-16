# Day 02 — Variables and Built-in Functions

## 1. Variables

A variable is a named container that stores a value. Python assigns the type automatically based on what you put in it.

```python
first_name = 'Aisha'   # str
age = 25               # int
is_married = False     # bool
```

> **Note:** Variable names should be lowercase with underscores (`snake_case`). They cannot start with a number.

---

## 2. Variable Assignment — Multiple at Once

You can declare and assign multiple variables on a single line:

```python
first_name, last_name, country, age, is_married = 'Aisha', 'Taneri', 'Turkey', 25, False
```

Order matters — values are assigned left to right.

---

## 3. Data Types Covered

| Type | Example | Notes |
|------|---------|-------|
| `str` | `'Aisha'` | Text, always in quotes |
| `int` | `25` | Whole numbers |
| `float` | `1.25` | Decimal numbers |
| `bool` | `True` / `False` | Exactly two values, capitalised |

---

## 4. Checking Types with `type()`

```python
print(type(first_name))   # <class 'str'>
print(type(age))          # <class 'int'>
print(type(is_married))   # <class 'bool'>
```

Useful whenever you're unsure what Python is treating a value as.

---

## 5. Useful Built-in Functions

| Function | What it does | Example |
|----------|-------------|---------|
| `type()` | Returns the data type | `type('hi')` → `<class 'str'>` |
| `len()` | Returns the length | `len('Aisha')` → `5` |
| `input()` | Gets text from the user | `input('Enter name: ')` |
| `float()` | Converts to decimal | `float('3.14')` → `3.14` |
| `help()` | Opens built-in docs | `help('keywords')` |

---

## 6. Arithmetic — All Seven Operators

```python
num_one = 5
num_two = 4

total    = num_one + num_two   # 9   — addition
diff     = num_one - num_two   # 1   — subtraction
times    = num_one * num_two   # 20  — multiplication
divi     = num_one / num_two   # 1.25 — division (always float)
per      = num_one % num_two   # 1   — modulus (remainder)
power    = num_one ** num_two  # 625 — exponentiation
flo_divi = num_one // num_two  # 1   — floor division (drops decimal)
```

---

## 7. Practical — Circle Area and Circumference

```python
rad = float(input('Enter radius of a circle: '))
area_of_circle  = 3.14 * rad ** 2
circum_of_circle = 2 * 3.14 * rad
```

`input()` always returns a string — wrap it in `float()` before doing maths with it.

---

## Key Takeaways
- Python is **dynamically typed** — you never declare a type, Python figures it out
- `bool` only has two values: `True` and `False` (capital first letter)
- `input()` always returns a `str` — convert it with `int()` or `float()` before arithmetic
- `len()` works on strings and counts characters, including spaces
- `//` gives the whole-number part of a division; `%` gives the leftover remainder
- `help('keywords')` lists all reserved words Python won't let you use as variable names
