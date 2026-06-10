# Day 7 - Sets

A set is an unordered, un-indexed collection of **distinct** (unique) elements. Sets automatically remove duplicates and support mathematical operations: union, intersection, difference, symmetric difference, subset, superset, and disjoint checks.

Key set methods: `add()`, `update()`, `remove()`, `discard()`, `pop()`, `clear()`, `union()`, `intersection()`, `issubset()`, `issuperset()`, `difference()`, `symmetric_difference()`, `isdisjoint()`

> 📝 **Watch out** — `{}` creates an empty **dict**, not a set. Use `set()` for an empty set.
> 

> 📝 **Watch out** — `remove()` raises a `KeyError` if the item is not found. `discard()` is silent — use it when you're not sure if the item exists.
> 

> 📝 **Watch out** — the method is `isdisjoint()`, NOT `disjoint()`. Calling `A.disjoint(B)` raises an `AttributeError`.
> 

## Level 1

```python
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

len(it_companies)                              # -> 7

# membership check
'Apple' in it_companies                        # -> True
'Tesla' in it_companies                        # -> False

it_companies.add('Twitter')                    # add one item

it_companies.update(['Meta', 'LinkedIn', 'Netflix'])   # add multiple items at once

it_companies.remove('Facebook')               # removes Facebook; raises KeyError if not found

# remove() vs discard()
it_companies.remove('IBM')     # KeyError if 'IBM' not present
it_companies.discard('IBM')    # no error if 'IBM' not present — does nothing silently

it_companies.pop()             # removes and returns a random item

it_companies.clear()           # empties the set -> set()  (variable still exists)
```

## Level 2

```python
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# membership
19 in A                           # -> True
99 in A                           # -> False

# join
A.union(B)                        # -> {19, 20, 22, 24, 25, 26, 27, 28}  (same as A | B)
A.union(B) == B.union(A)          # -> True  (union is commutative)
A.update(B)                       # modifies A in place — adds B's items into A

# intersection
A.intersection(B)                 # -> {19, 20, 22, 24, 25, 26}  (same as A & B)

# subset / superset
A.issubset(B)                     # -> True  (every element of A is in B)
B.issuperset(A)                   # -> True  (B contains all elements of A — same relationship, opposite angle)

# disjoint
A.isdisjoint(B)                   # -> False  (A and B share 6 elements)

# difference
B.difference(A)                   # -> {27, 28}  (in B but NOT in A — same as B - A)
A.difference(B)                   # -> set()    (nothing in A that isn't already in B)

# symmetric difference
A.symmetric_difference(B)         # -> {27, 28}  (in either but NOT in both — same as A ^ B)

del A
del B
```

## Level 3

```python
age = [22, 19, 24, 25, 26, 24, 25, 24]
age_set = set(age)
len(age)        # -> 8
len(age_set)    # -> 5  (24 appears 3x, 25 appears 2x — duplicates removed)
len(age) > len(age_set)   # -> True — the list is bigger

# String vs List vs Tuple vs Set
# String:  ordered, immutable, allows duplicates     "hello"
# List:    ordered, mutable,   allows duplicates     [1, 2, 3]
# Tuple:   ordered, immutable, allows duplicates     (1, 2, 3)
# Set:     unordered, mutable, NO duplicates         {1, 2, 3}

sentence = "I am a teacher and I love to inspire and teach people"
unique_words = set(sentence.split())
len(unique_words)   # -> 10  ('I' and 'and' each appear twice → removed as duplicates)
```

---

## Day 7 - Sets Cheatsheet

| Task | Syntax | Notes |
| --- | --- | --- |
| Create empty set | `set()` | `{}` creates a dict, not a set |
| Create with items | `{1, 2, 3}` | unordered, duplicates ignored |
| Length | `len(st)` | number of unique items |
| Membership check | `x in st` | O(1) lookup |
| Add one item | `st.add(x)` | no effect if x already in set |
| Add multiple items | `st.update(iterable)` | accepts list, tuple, set, etc. |
| Remove (strict) | `st.remove(x)` | KeyError if x not found |
| Remove (safe) | `st.discard(x)` | silent if x not found |
| Remove random item | `st.pop()` | returns the removed item |
| Empty the set | `st.clear()` | variable still exists as set() |
| Delete the set | `del st` | variable is gone entirely |
| List → Set | `set(lst)` | removes duplicates |
| Union | `A.union(B)` or `A | B` | new set, originals unchanged |
| Intersection | `A.intersection(B)` or `A & B` | items in both A and B |
| Difference | `A.difference(B)` or `A - B` | items in A but not in B |
| Symmetric difference | `A.symmetric_difference(B)` or `A ^ B` | items in either but not both |
| Subset | `A.issubset(B)` | True if all of A is in B |
| Superset | `A.issuperset(B)` | True if A contains all of B |
| Disjoint | `A.isdisjoint(B)` | True if no common elements |