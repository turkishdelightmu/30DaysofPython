# Day 5 - Lists

A list is an ordered, mutable collection that holds mixed types and allows duplicates. The four collection types: **list** (ordered, mutable, dupes ok), **tuple** (ordered, immutable), **set** (unordered, un-indexed, mutable, no dupes), **dict** (insertion-ordered since 3.7, keyed, no dupe keys).


## Level 1

```python
empty_list = list()                          # → []  — list() and [] both make an empty list
web_techs = ['HTML','CSS','JS','React','Python']
len(web_techs)                               # → 5

web_techs[0]                                 # → 'HTML'   — index starts at 0
web_techs[2]                                 # → 'JS'     — middle of a 5-item list
web_techs[-1]                                # → 'Python' — negative index counts from the end

it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
len(it_companies)                            # → 7
it_companies[0]                              # → 'Facebook'  (first)
it_companies[len(it_companies)//2]           # → 'Apple'     — middle COMPUTED, not hardcoded
it_companies[-1]                             # → 'Amazon'    (last)

it_companies[0] = 'Meta'                     # lists are mutable — reassign by index
it_companies.append('Tesla')                 # adds one item to the END
it_companies.insert(len(it_companies)//2, 'Reddit')  # inserts at index, shifts rest right
it_companies[3] = it_companies[3].upper()    # → 'APPLE'  — IBM untouched
'#;  '.join(it_companies)                     # → 'Meta#;  Google#;  ...' — joins into ONE string
'Google' in it_companies                     # → True  — membership test
it_companies.sort()                          # ascending, IN PLACE
it_companies.reverse()                       # flips current order (NOT a descending sort)
it_companies[:3]                             # first 3   (stop is exclusive)
it_companies[-3:]                            # last 3
it_companies.pop(0)                          # removes & returns by index
it_companies.clear()                         # → []  empties the list (variable still exists)
del it_companies                             # destroys the variable entirely
```

```python
front_end = ['HTML','CSS','JS','React','Redux']
back_end  = ['Node','Express','MongoDB']
full_stack = front_end + back_end            # + concatenates two lists
redux_index = full_stack.index('Redux')      # find position, don't hardcode
full_stack[redux_index+1:redux_index+1] = ['Python','SQL']  # slice-insert AFTER Redux
# → [...,'Redux','Python','SQL','Node',...]  — NOT extend(), which appends to the end
```

## Level 2

```python
ages = [19,22,19,24,20,25,26,24,25,24]
ages.sort()                                  # → [19,19,20,22,24,24,24,25,25,26]
min_age, max_age = ages[0], ages[-1]         # → 19, 26
ages.append(min_age); ages.append(max_age)   # appends land at the END → list now unsorted
ages.sort()                                  # MUST re-sort before taking the middle
mid = len(ages)//2
median_age = (ages[mid] + ages[mid-1]) / 2   # → 24.0  (avg of the two middle items)
sum(ages)/len(ages)                          # → 22.75 average
max_age - min_age                            # → 7 range
abs(min_age-average), abs(max_age-average)   # → 3.75, 3.25  — abs() drops the sign
```

```python
n = len(countries)                           # → 195
countries[(n-1)//2 : (n+2)//2]               # → ['Lesotho'] — single middle for an ODD list
# the slice self-adjusts: odd n → 1 item, even n → 2 items

half = len(countries)//2 + len(countries)%2  # → 98  (one extra to the first half if odd)
first_half  = countries[:half]               # 98 items
second_half = countries[half:]               # 97 items

c = ['China','Russia','USA','Finland','Sweden','Norway','Denmark']
first_three, scandic = c[:3], c[3:]          # → ['China','Russia','USA'] | rest
# (star form: a, b, c, *scandic = c  — one name = one item, star collects the rest)
```

---

## Day 5 — Lists Cheatsheet

| Task | Syntax | Notes |
| --- | --- | --- |
| Create | `list()` or `[]` | both make empty |
| Length | `len(lst)` | item count |
| Access | `lst[0]` / `lst[-1]` / `lst[i]` | index from 0; negatives from end |
| Middle | `lst[len(lst)//2]` | compute, don't hardcode |
| Slice | `lst[start:stop:step]` | stop **exclusive**; defaults `0 : len(lst) : 1` |
| Reverse copy | `lst[::-1]` | new list, doesn't modify original |
| Add one | `lst.append(x)` | to the end |
| Add at index | `lst.insert(i, x)` | shifts rest right |
| Insert after item | `lst[i+1:i+1] = [x, y]` | slice-insert (not `extend`) |
| Join lists | `a + b` or `a.extend(b)` | both add to the end |
| Join to string | `'sep'.join(lst)` | items must be strings |
| Membership | `x in lst` | → `True` / `False` |
| Find / count | `lst.index(x)` / `lst.count(x)` | index = first match |
| Remove value | `lst.remove(x)` | first match only |
| Remove by index | `lst.pop(i)` / `lst.pop()` | returns the item; `pop()` = last |
| Delete | `del lst[i]` / `del lst[i:j]` / `del lst` | last form destroys the variable |
| Empty | `lst.clear()` | → `[]`, variable survives |
| Sort | `lst.sort()` / `lst.sort(reverse=True)` | in place |
| Sort (new list) | `sorted(lst)` | original untouched |
| Reverse order | `lst.reverse()` | flips current order, **not** a sort |
| Copy | `lst.copy()` | `b = a` shares the same list |
| Unpack | `a, b, *rest = lst` | one name = one item; `*` collects remainder |