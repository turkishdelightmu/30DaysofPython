# 30 Days of Python 🐍

![30 Days of Python](banner.png)

Working through [@Asabeneh](https://github.com/Asabeneh)'s [30-Days-Of-Python](https://github.com/Asabeneh/30-Days-Of-Python) challenge at my own pace.

I'm a finance professional transitioning toward data and AI. Python is the foundation. This repo is my honest, unfiltered learning log — no skipping, no faking progress.

---

## Progress

| Day | Topic | Status |
|-----|-------|--------|
| Day 01 | Introduction — Syntax, Data Types, Arithmetic | ✅ Done |
| Day 02 | Variables, Built-in Functions | ✅ Done |
| Day 03 | Operators | ✅ Done |
| Day 04 | Strings | ✅ Done |
| Day 05 | Lists | ✅ Done |
| Day 06 | Tuples | ✅ Done |
| Day 07 | Sets | ✅ Done |
| Day 08 | Dictionaries | ✅ Done |
| Day 09 | Conditionals | ✅ Done |
| ... | ... | ... |

---

## Day 01 — Introduction

**What I covered:**
- Basic arithmetic operators: `+`, `-`, `*`, `/`, `**`, `%`, `//`
- Data types: int, float, complex, string, list, dict, set, tuple, bool
- Used `type()` to inspect values
- Calculated Euclidean distance using pure arithmetic

**File:** `Day01/Day1.py`

## Day 02 — Variables and Built-in Functions

**What I covered:**
- Declaring variables and assigning values (str, int, float, bool)
- Multiple assignment on a single line
- Built-in functions: `type()`, `len()`, `input()`, `float()`, `help()`
- All seven arithmetic operators applied to variables
- Calculated circle area and circumference from user input

**Files:** `Day02/Day2.py` · `Day02/Day02_Notes.md`

## Day 03 — Operators

**What I covered:**
- Number types: int, float, complex
- Geometry calculations: triangle area/perimeter, rectangle area/perimeter, circle area/circumference
- Slope and Euclidean distance between two points
- Solving `y = x² + 6x + 9` by testing x values
- String membership with `in` and `not in`
- Type conversion chain: `int` → `float()` → `str()`
- Divisibility check with modulus: `n % 2 == 0`

**Files:** `Day03/day3.py` · `Day03/Day3_Notes.md`

## Day 04 — Strings

**What I covered:**
- String length with `len()`, concatenation with `+`
- Case methods: `upper()`, `lower()`, `capitalize()`, `title()`, `swapcase()`
- Slicing: index access, negative indexing, range slices
- Search methods: `in`, `startswith()`, `endswith()`, `index()`, `find()`, `rindex()`, `rfind()`
- `replace()`, `split()`, `strip()`
- Acronym generation with a generator expression and `join()`
- `isidentifier()`, escape sequences (`\n`, `\t`)
- String formatting with `.format()` and `{:.2f}` for decimal control

**Files:** `Day04/day4.py` · `Day04/day4_Notes.md`

## Day 05 — Lists

**What I covered:**
- List creation with `list()` and `[]`; ordered, mutable, duplicates allowed
- Indexing, negative indexing, and computed middle index (`len(lst)//2`)
- Slicing: `lst[start:stop]`, `lst[-3:]`, `lst[::-1]` for a reversed copy
- Mutating: `append()`, `insert()`, slice-insert `lst[i:i] = [x, y]`
- List concatenation with `+`; joining to a string with `'sep'.join(lst)`
- `sort()` / `sort(reverse=True)` in place vs `sorted()` (new list)
- `reverse()`, `pop()`, `remove()`, `clear()`, `del`
- Median from a sorted list; `abs()` for unsigned deviation
- Splitting a list into halves; star unpacking `a, b, *rest = lst`
- Four collection types compared: list, tuple, set, dict

**Files:** `Day05/day5.py` · `Day05/day5_Notes.md`

## Day 06 — Tuples

**What I covered:**
- Tuples are ordered and immutable — no `add`, `insert`, or `remove`
- Single-element tuple requires a trailing comma: `("Fatima",)` not `("Fatima")`
- Concatenation with `+` returns a new tuple
- `len()`, indexing, negative indexing, and slicing work the same as lists
- Unpacking: `a, b, c = tpl` — must match length exactly
- `tpl[len(tpl)//2]` gives the middle item index, not a numeric average
- Convert to list with `list()` when mutation is needed
- `del tpl` removes the whole tuple — can't delete individual items
- Membership check with `in`

**Files:** `Day06/day6.py` · `Day06/day6_Notes.md`

## Day 07 — Sets

**What I covered:**

- Sets are unordered, un-indexed, and hold only unique elements — duplicates are removed automatically
- `{}` creates an empty dict, not a set — use `set()` for an empty set
- `add()` for one item, `update()` for multiple; `remove()` raises `KeyError`, `discard()` is silent
- `pop()` removes a random item; `clear()` empties the set; `del` destroys the variable entirely
- Set math: `union()`, `intersection()`, `difference()`, `symmetric_difference()`
- Relationship checks: `issubset()`, `issuperset()`, `isdisjoint()`
- Used `set()` on a list to count unique elements and deduplicate words in a sentence

**Files:** `Day07/day7.py` · `Day07/day7_Notes.md`

## Day 08 — Dictionaries

**What I covered:**

- Dictionaries are key:value pairs — accessed by key, not index; mutable and insertion-ordered since Python 3.7
- `dct['key']` raises `KeyError` if missing; `dct.get('key')` returns `None` safely
- `pop()` removes and returns a value; `del dct['key']` removes without returning
- `clear()` empties the dict but keeps the variable; `del dct` destroys it entirely
- `keys()`, `values()`, `items()` return live views of the dictionary
- Nested dictionaries: a value can itself be a dict (e.g. `address` with `street` and `zipcode`)
- Skills value is a list — modified in place with `append()`

**Files:** `Day08/day8.py` · `Day08/day8_Notes.md`

## Day 09 — Conditionals

**What I covered:**

- `if`, `elif`, `else` control flow — Python executes the first matching block; indentation is required
- Comparison operators: `>`, `<`, `>=`, `<=`, `==`, `!=` — all return `True`/`False`
- Logical operators: `and`, `or` — combining multiple conditions in one expression
- Membership with `in` — checking presence in a list or dict
- `abs()` for unsigned age/value differences; chained comparisons like `90 <= score <= 100`
- Season detection using `in` with a list of month names + `.capitalize()` for input normalisation
- Conditional dictionary access: checking key existence before reading nested values
- Developer-type classification by inspecting a `skills` list with combined `and`/`or` logic

**Files:** `Day09/day9.py` · `Day09/day9_Notes.md`

---

*Following the curriculum from [Asabeneh/30-Days-Of-Python](https://github.com/Asabeneh/30-Days-Of-Python). All solutions are my own work.*
