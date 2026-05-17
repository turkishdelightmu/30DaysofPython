# Day 03 — Operators

## Key Takeaways
- Python has three number types: `int` (whole), `float` (decimal), and `complex` (e.g. `1 + 4j`)
- `input()` always returns a `str` — always wrap with `float()` or `int()` before doing maths
- `**` is the exponentiation operator; `**0.5` is a clean way to compute square roots
- `//` is floor division (drops the decimal); `%` gives the remainder — together they're useful for divisibility checks (`n % 2 == 0` → even number)
- `in` checks substring membership in strings: `'on' in 'python'` → `True`
- `and` / `not in` let you combine membership checks across multiple strings
- Type conversion chain: `int` → `float()` → `str()` — you can cast in steps
- `int()` truncates toward zero: `int(2.7)` → `2`, same as `7 // 3`
- `int('9.8')` raises an error; you must go through `float` first: `int(float('9.8'))`
- Quadratic `y = x² + 6x + 9` equals `(x + 3)²` — it hits zero at `x = -3`
- Slope formula: `m = (y2 - y1) / (x2 - x1)`; Euclidean distance: `((Δx)² + (Δy)²) ** 0.5`
