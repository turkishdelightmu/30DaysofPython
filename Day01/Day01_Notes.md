# Day 01 — Introduction to Python

## 1. Arithmetic Operators

| Operator | Symbol | Example | Result |
|----------|--------|---------|--------|
| Addition | `+` | `3 + 4` | `7` |
| Subtraction | `-` | `4 - 3` | `1` |
| Multiplication | `*` | `3 * 4` | `12` |
| Division | `/` | `3 / 4` | `0.75` |
| Exponentiation | `**` | `3 ** 4` | `81` |
| Modulus | `%` | `3 % 4` | `3` |
| Floor Division | `//` | `3 // 4` | `0` |

> **Note:** Floor division drops the decimal and rounds down. Modulus returns the remainder.

---

## 2. Data Types

| Type | Example |
|------|---------|
| Integer | `29` |
| Float | `2.14` |
| Complex | `4 + 3j` |
| String | `'Hello'` |
| List | `[11, 12, 13]` |
| Dictionary | `{'name': 'Aisha'}` |
| Set | `{1.8, 4.14, 8.7}` |
| Tuple | `(1.8, 4.14, 8.7)` |
| Boolean | `True` / `False` |

---

## 3. Checking Data Types
```python
print(type(10))        # <class 'int'>
print(type(9.8))       # <class 'float'>
print(type(4 - 4j))   # <class 'complex'>
print(type('Aisha'))   # <class 'str'>
```
Use `type()` to inspect what type a value is. Useful for debugging.

---

## 4. Practical Exercise — Euclidean Distance

Formula: `√((x2 - x1)² + (y2 - y1)²)`

```python
# Distance between (2, 3) and (10, 8)
print(((10 - 2) ** 2 + (8 - 3) ** 2) ** 0.5)  # 9.433981...
```

Pure arithmetic — no libraries needed for this. Shows how Python handles math naturally.

---

## Key Takeaways
- Python executes top to bottom, line by line
- Everything has a type — Python assigns it automatically
- `type()` is your friend when you're unsure what you're working with
- Floor division `//` and modulus `%` are more useful than they look — you'll see them constantly in data work
