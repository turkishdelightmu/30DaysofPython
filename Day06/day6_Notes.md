# Day 6 - Tuples

A tuple is an ordered, immutable collection. Written with `()`. Once created, values cannot be changed — no `add`, `insert`, or `remove`. Unlike lists, tuples have very few methods.

Key tuple methods: `tuple()`, `count()`, `index()`, `+` (concatenation)

> 📝 **Watch out** `("Fatima")` is NOT a tuple — it's just a string in parentheses. A single-element tuple requires a trailing comma: `("Fatima",)`. Without it, Python treats the parentheses as grouping, not a tuple constructor.

## Level 1

```python
empty_tuple = ()           # or tuple()

sisters = ("Sana", "Hana", "Rina")
brothers = ("Ahmad", "Uthman", "Omar")

siblings = brothers + sisters          # + concatenates tuples into a new tuple
len(siblings)                          # → 6

mother = ("Fatima",)                   # trailing comma = single-element tuple
father = ("Kamal",)
family_members = siblings + mother + father   # → 8-item flat tuple
```

## Level 2

```python
bro1, bro2, bro3, sis1, sis2, sis3, mother, father = family_members   # unpack all 8

fruits = ("apple", "banana", "strawberry")
veggies = ("carrot", "lettuce", "cucumber")
animal_products = ("milk", "cheese", "yogurt")
food_stuff_tp = fruits + veggies + animal_products    # 9-item tuple

food_stuff_lt = list(food_stuff_tp)    # convert tuple → list (tuples are immutable)

mid = len(food_stuff_tp) // 2
food_stuff_tp[mid]                     # → 'lettuce'  — middle item (index 4 of 9)
# ⚠️ (food_stuff_tp[mid] + food_stuff_tp[mid-1]) / 2 → TypeError: can't divide strings
# // 2 gives the INDEX, not a numeric average — only works for numbers

food_stuff_lt[:3]                      # → ['apple', 'banana', 'strawberry']
food_stuff_lt[-3:]                     # → ['milk', 'cheese', 'yogurt']

del food_stuff_tp                      # deletes the variable entirely (can't remove single items)

nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
'Estonia' in nordic_countries          # → False
'Iceland' in nordic_countries          # → True
```

---

## Day 6 — Tuples Cheatsheet

| Task | Syntax | Notes |
|---|---|---|
| Create empty | `()` or `tuple()` | both work |
| Single-element | `(x,)` | trailing comma is mandatory |
| Length | `len(tpl)` | item count |
| Access | `tpl[0]` / `tpl[-1]` | same indexing as lists |
| Middle item | `tpl[len(tpl)//2]` | `//2` = index, not numeric average |
| Slice | `tpl[start:stop]` | same rules as lists, stop exclusive |
| Concatenate | `tpl1 + tpl2` | returns a new tuple |
| Membership | `x in tpl` | → `True` / `False` |
| Convert to list | `list(tpl)` | needed to mutate |
| Convert to tuple | `tuple(lst)` | back from list |
| Count | `tpl.count(x)` | occurrences of x |
| Find index | `tpl.index(x)` | first match |
| Unpack | `a, b, c = tpl` | must match length exactly |
| Delete tuple | `del tpl` | can't delete single items |