# Learn Python

> Learn Python with short lessons, clear explanations, and runnable examples.

Practical Python guide for scripting, web development, AI tooling, and day-to-day backend work.

- Learn the language fundamentals, common standard-library tools, and real-world workflow used in Python projects.
- Use this README as a single long-form guide, or browse the docs site chapter by chapter.

- :page_facing_up: **Documentation site** — the full content is published at **[learn-python-dev.netlify.app](https://learn-python-dev.netlify.app/)** with a sidebar, search, and per-chapter navigation.

- :notebook: **Interactive notebook** — [Open learn-python.ipynb in VS Code](https://vscode.dev/github/meysamhadeli/learn-python/blob/main/learn-python.ipynb) to run and edit every code block inline.

> [!NOTE]
> After editing any file in `docs/`, run this to update the website content:
> ```bash
> python website/scripts/sync_docs.py
> ```

## Table of Contents

- [Getting Started](#getting-started)
- [I — The Basics](#chapter-i-the-basics)
  - [Hello World](#hello-world)
  - [Variables](#variables)
  - [Built-in Data Types](#built-in-data-types)
  - [String Formatting](#string-formatting)
  - [Operators](#operators)
  - [Falsy Values](#falsy-values)
- [II — Data Structures](#chapter-ii-data-structures)
  - [Lists](#lists)
  - [Tuples](#tuples)
  - [Dictionaries](#dictionaries)
  - [Sets](#sets)
  - [Collections Module](#collections-module)
  - [Comprehensions](#comprehensions)
  - [Type Conversion](#type-conversion)
- [III — Control Flow](#chapter-iii-control-flow)
  - [If / Else](#if-else)
  - [Match / Case](#match-case-python-3-10)
  - [Loops](#loops)
- [IV — Functions](#chapter-iv-functions)
  - [Defining Functions](#defining-functions)
  - [Parameters & Arguments](#parameters-arguments)
  - [Lambda Functions](#lambda-functions)
  - [Scoping Rules](#scoping-rules-legb)
  - [Type Hints](#type-hints)
- [V — OOP](#chapter-v-object-oriented-programming)
  - [Classes](#classes)
  - [Inheritance](#inheritance)
  - [Abstract Base Classes](#abstract-base-classes)
  - [Magic Methods](#magic-methods)
  - [Dataclasses](#dataclasses)
- [VI — Advanced Python Techniques](#chapter-vi-advanced-python-techniques)
  - [Iterators & Generators](#iterators-generators)
  - [itertools & functools](#itertools-functools)
  - [Decorators](#decorators)
  - [Context Managers](#context-managers)
  - [Pattern Matching](#pattern-matching-python-3-10)
- [VII — Modules & Packaging](#chapter-vii-modules-packaging)
  - [Modules](#modules)
  - [File I/O & JSON](#file-i-o-json)
  - [Packages](#packages)
  - [Virtual Environments](#virtual-environments)
  - [Useful Commands](#useful-commands)
  - [Build & Packaging](#build-packaging)
- [VIII — Errors & Exceptions](#chapter-viii-errors-exceptions)
- [IX — Concurrency](#chapter-ix-concurrency)
  - [The GIL](#the-gil)
  - [Async / Await](#async-await)
  - [Threading](#threading)
  - [Multiprocessing](#multiprocessing)
  - [Free-Threading](#free-threading-python-3-13)
  - [Decision Matrix](#concurrency-decision-matrix)
- [Appendix](#appendix)
  - [AI & Data Science](#ai-data-science)
  - [Web Development](#web-development)
- [Support](#support)
- [Contribution](#contribution)
- [Project References](#project-references)

---

<a id="getting-started"></a>

## Getting Started

This guide teaches Python through short lessons, runnable examples, and practical concepts that show up in real projects.

### Why Python

- **AI**: most popular SDKs, notebooks, and automation workflows are Python-first
- **Web**: FastAPI and Django are strong backend choices
- **Scripting**: Python is excellent for glue code, CLIs, and data tasks

### Installation and Setup

Install Python from the [official downloads page](https://www.python.org/downloads/).

#### macOS

```bash
python3 --version
```

#### Linux

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
python3 --version
```

#### Windows

1. Open the installer.
2. Check "Add Python to PATH".
3. Click "Install Now".

```bash
python --version
```

#### VS Code

Install VS Code and the Microsoft Python extension for IntelliSense, linting, debugging, and notebook support.

> Use [learn-python.ipynb](https://github.com/meysamhadeli/learn-python/blob/main/learn-python.ipynb) to run examples interactively while reading.

---

<a id="chapter-i-the-basics"></a>

## Chapter I: The Basics

The foundation you need before Python starts feeling natural.

Focus on these first:

- assignment and mutability
- built-in scalar types
- string formatting with `f"..."`
- truthy and falsy values
- basic operators you see in real code

If you are already an experienced developer, do not over-study this chapter. Learn Python's object model and syntax differences, then move on.

### What to read now

- [Variables](./docs/01-the-basics/variables.md)
- [Built-in Data Types](./docs/01-the-basics/built-in-data-types.md)
- [String Formatting](./docs/01-the-basics/string-formatting.md)
- [Operators](./docs/01-the-basics/operators.md)
- [Falsy Values](./docs/01-the-basics/falsy-values.md)

### Can skim

- [Hello World](./docs/01-the-basics/hello-world.md) if you already know how to run a script

### Sections

- [Hello World](./docs/01-the-basics/hello-world.md)
- [Variables](./docs/01-the-basics/variables.md)
- [Built-in Data Types](./docs/01-the-basics/built-in-data-types.md)
- [String Formatting](./docs/01-the-basics/string-formatting.md)
- [Operators](./docs/01-the-basics/operators.md)
- [Falsy Values](./docs/01-the-basics/falsy-values.md)

---

<a id="hello-world"></a>

## Hello World

### Your First Program

The first useful Python program is a single line:

```python
print("Hello, World!")
```

Save this to `main.py` and run it:

```bash
python main.py
## or on Windows
py main.py
```

Output: `Hello, World!`

### Script Mode vs Interactive Mode

You will use Python in two common ways:

- **Script mode**: you run a file like `main.py`.
- **Interactive mode**: you start Python first, then type commands one at a time.

```bash
python
## or on Windows
py
```

You will usually see a prompt like `>>>`. Anything you type after that is executed immediately:

```python
>>> print("Hello, World!")
Hello, World!
```

Use the REPL for quick checks. Use files for scripts and real projects.

### How Python Executes Code

The practical mental model is:

1. Python reads your file.
2. Python checks that the syntax is valid.
3. Python runs the statements in order.

### The `print()` Function

`print()` writes values to standard output:

```python
print("Hello", "World")          # Hello World  (space-separated by default)
print("Hello", "World", sep="-") # Hello-World
print("Hello", end="")           # no newline at the end
print(42, 3.14, True, None)      # 42 3.14 True None
```

It is the fastest way to inspect values while learning.

```python
name = "Maya"
score = 95

print("Student:", name, "Score:", score)
```

### The `__main__` Guard

Use `if __name__ == "__main__":` when a file should act as both an importable module and a runnable script:

```python
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("World"))
```

You do not need it in every tiny example, but you will see it often in real projects.

### Reading Input

`input()` reads text from standard input and always returns a string:

```python
name = input("Enter your name: ")
print(f"Hello, {name}!")
age = int(input("Enter your age: "))
```

Convert explicitly when needed:

```python
age = int(input("Enter your age: "))
print(age + 1)
```

---

<a id="variables"></a>

## Variables

### Assignment and Naming

In Python, a variable is created by assignment. There is no separate declaration step.

```python
name = "Python"
version = 3.13
is_awesome = True
_private = "convention only"
```

Use `snake_case` for variable and function names.

### Variables Are References

Variables are references to objects, not typed boxes.

```python
x = [1, 2, 3]
y = x           # y points to the SAME list object
y.append(4)
print(x)        # [1, 2, 3, 4] — modifying via y also affects x
```

If you need an independent copy of a mutable object, copy it:

```python
y = x.copy()    # or: y = x[:]
y.append(99)
print(x)        # unaffected
```

### Multiple Assignment

Python supports unpacking:

```python
x, y, z = 1, 2.5, "three"  # types can differ
a = b = c = 0               # all three point to the same object

## Swap without a temporary variable — a Python idiom
x, y = y, x
```

### Constants

Python has no hard constants. Use `UPPER_CASE` by convention:

```python
MAX_CONNECTIONS = 100
PI = 3.14159
DATABASE_URL = "postgresql://localhost/mydb"
```

### Deleting Variables

Use `del` to remove a name:

```python
temp = 42
del temp
## print(temp)  # NameError: name 'temp' is not defined
```
Usually you will use it more with container items than simple variables.

---

<a id="built-in-data-types"></a>

## Built-in Data Types

Python's core built-in types cover most day-one work. Python is dynamically typed, so values carry their type at runtime.

```python
value = 10
print(type(value))

value = "ten"
print(type(value))
```

### int

`int` has arbitrary precision.

```python
count = 42
big_number = 10 ** 100        # a googol — no problem
binary = 0b1010               # 10 in binary
hexadecimal = 0xFF            # 255 in hex
```

Use `/` for float division and `//` for floor division:

```python
print(7 // 2)   # 3   (floor division — always int)
print(7 / 2)    # 3.5 (true division — always float)
print(7 % 2)    # 1   (remainder)
```

### float

`float` is fast and common, but it is not exact for decimal fractions.

```python
pi = 3.14159
small = 1.5e-4      # scientific notation: 0.00015
large = 6.022e23    # Avogadro's number
```

Classic gotcha:

```python
print(0.1 + 0.2)        # 0.30000000000000004
print(0.1 + 0.2 == 0.3) # False!
```

For exact decimal arithmetic, use `decimal.Decimal`:

```python
from decimal import Decimal
print(Decimal("0.1") + Decimal("0.2"))  # 0.3 — exact
```

### complex

Python also has native `complex` numbers, mostly useful in scientific code:

```python
c = 3 + 4j
print(c.real)    # 3.0
print(c.imag)    # 4.0
print(abs(c))    # 5.0 — Euclidean magnitude: sqrt(3² + 4²)
print(c * 2)     # (6+8j)
```

### str

Strings are immutable Unicode text.

```python
text = "Python"
print(text[0])       # 'P'       — indexing from 0
print(text[-1])      # 'n'       — negative indexes from the end
print(text[1:4])     # 'yth'     — slicing [start:stop]
print(text[::-1])    # 'nohtyP'  — reverse via step
print(len(text))     # 6
```

Common string methods:

```python
s = "  Hello, World!  "
print(s.strip())            # "Hello, World!"
print(s.lower())            # "  hello, world!  "
print(s.replace("World", "Python"))  # "  Hello, Python!  "
print("Hello, World!".split(", "))   # ['Hello', 'World!']
print("-".join(["a", "b", "c"]))     # "a-b-c"
print("hello".startswith("he"))      # True
```

Useful literal forms:

```python
single = 'Hello'
double = "Hello"              # identical
multiline = """Line 1
Line 2"""
raw = r"C:\Users\Name"        # backslashes are literal — no escape processing
```

Strings cannot be changed in place.

### bool

`bool` has two values: `True` and `False`.

```python
print(True + True)    # 2
print(True * 5)       # 5
print(sum([True, False, True, True]))  # 3  — counts Trues
```

### None

`None` means "no value":

```python
result = None

if result is None:           # always use 'is', not '=='
    print("No result yet")

def find(items, target):
    for item in items:
        if item == target:
            return item
    # implicitly returns None if not found
```
Use `is None`, not `== None`.

---

<a id="string-formatting"></a>

## String Formatting

### f-Strings (Recommended)

Use f-strings for most new code.

```python
name = "Alice"
age = 30

print(f"My name is {name} and I am {age} years old.")
## My name is Alice and I am 30 years old.

## Any expression works inside {}
print(f"In 5 years: {age + 5}")
print(f"Uppercase: {name.upper()}")
print(f"Length: {len(name)}")
print(f"{'even' if age % 2 == 0 else 'odd'}")
```

```python
product = "Keyboard"
price = 49.99

print(f"{product} costs ${price}")
```

### Format Specification Mini-Language

After `:` inside `{}`, specify formatting:

```python
pi = 3.14159265

print(f"{pi:.2f}")      # 3.14
print(f"{pi:.4f}")      # 3.1416

print(f"{42:10d}")      # '        42'  (right-aligned, width 10)
print(f"{42:<10d}")     # '42        '  (left-aligned)
print(f"{42:^10d}")     # '    42    '  (centered)
print(f"{42:010d}")     # '0000000042' (zero-padded)

print(f"{1000000:,}")   # 1,000,000

ratio = 0.756
print(f"{ratio:.1%}")   # 75.6%
```

### Debugging with `=`

Python 3.8+ added `=` for quick debugging:

```python
x = 42
y = [1, 2, 3]
print(f"{x=}")          # x=42
print(f"{y=}")          # y=[1, 2, 3]
print(f"{x * 2 + 1=}")  # x * 2 + 1=85
```

### Other Formatting Approaches

You will still see older styles in existing code:

```python
print("Hello, {}!".format("World"))
print("{name} is {age}".format(name="Alice", age=30))

print("Hello, %s! You are %d years old." % ("Alice", 30))
```

For `logging`, `%` formatting is still common:

```python
import logging
logging.debug("User %s logged in from %s", username, ip_address)
```

Practical rule: use f-strings in everyday code, recognize `.format()` and `%` in older code.

---

<a id="operators"></a>

## Operators

### Arithmetic Operators

Python arithmetic mostly works as expected. The main rules to remember are `/`, `//`, `%`, and `**`.

```python
print(7 + 2)    # 9
print(7 - 2)    # 5
print(7 * 2)    # 14
print(7 / 2)    # 3.5   — always float
print(7 // 2)   # 3     — floor division
print(7 % 2)    # 1     — modulo (remainder)
print(7 ** 2)   # 49    — exponentiation
```

`//` rounds toward negative infinity:

```python
print(-7 // 2)   # -4  (not -3)
print(7 // -2)   # -4
```

### Comparison & Logical Operators

Comparisons return booleans. Python also supports chained comparisons:

```python
x = 7
print(x > 5)          # True
print(x != 10)        # True
print(0 < x < 10)     # True  — equivalent to (0 < x) and (x < 10)
print(1 < 2 < 3 < 4)  # True  — any number of chained comparisons
```

Logical operators use words, not symbols:

```python
print(x > 5 and x < 10)   # True
print(x > 10 or x < 5)    # False
print(not x == 7)          # False
```

`and` and `or` short-circuit and return actual values:

```python
name = ""
result = name or "Anonymous"   # "Anonymous" — name is falsy
items = [1, 2, 3]
first = items and items[0]     # 1 — items is truthy, so evaluates items[0]
```

### Assignment Operators

Augmented assignment is common:

```python
x = 10
x += 5    # x = 15
x -= 3    # x = 12
x *= 2    # x = 24
x /= 4    # x = 6.0  (always float)
x //= 2   # x = 3.0
x **= 3   # x = 27.0
x %= 5    # x = 2.0
```

Lists often update in place:

```python
numbers = [1, 2]
alias = numbers

numbers += [3]
print(alias)  # [1, 2, 3]
```

### Identity and Membership Operators

`is` checks identity. `in` checks membership.

```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)    # True  — equal values
print(a is b)    # False — different objects

## 'is' is appropriate for singletons:
result = None
print(result is None)     # True  (correct)
print(result is not None) # False

## Membership — O(1) for sets and dict keys, O(n) for lists
fruits = {"apple", "banana", "cherry"}
print("banana" in fruits)    # True
print("grape" not in fruits) # True
```

Use `==` for values and `is` for singletons like `None`.

### Walrus Operator `:=` (Python 3.8+)

The walrus operator assigns and returns a value in one expression:

```python
data = [1, 2, 3, 4, 5]

if (n := len(data)) > 3:
    print(f"List has {n} items")
```

Useful in `while` loops:

```python
import sys

while line := sys.stdin.readline():
    process(line)
```
Use it when it improves clarity, not just to be clever.

### Bitwise Operators

Bitwise operators matter in lower-level or protocol-heavy code:

```python
a = 0b1100   # 12
b = 0b1010   # 10

print(a & b)   # 0b1000 = 8   (AND)
print(a | b)   # 0b1110 = 14  (OR)
print(a ^ b)   # 0b0110 = 6   (XOR)
print(~a)      # -13           (NOT — inverts all bits, two's complement)
print(a << 2)  # 48            (left shift by 2)
print(a >> 1)  # 6             (right shift by 1)
```

---

<a id="falsy-values"></a>

## Falsy Values

### What is Truthiness?

In Python, values can be truthy or falsy in `if`, `while`, `and`, and `or` expressions.

```python
items = [1, 2, 3]

if items:
    print("We have data")
```

### The Complete List of Falsy Values

These values are falsy. Most other values are truthy.

| Value | Type |
|-------|------|
| `False` | bool |
| `None` | NoneType |
| `0` | int |
| `0.0` | float |
| `0j` | complex |
| `""` | str (empty) |
| `[]` | list (empty) |
| `()` | tuple (empty) |
| `{}` | dict (empty) |
| `set()` | set (empty) |
| `b""` | bytes (empty) |

```python
## All of these branches are skipped:
if False: ...
if None: ...
if 0: ...
if "": ...
if []: ...
if {}: ...
```

### Practical Patterns

Truthiness leads to short, idiomatic checks:

```python
def process(items):
    if not items:
        print("Nothing to process")
        return
    for item in items:
        ...

name = user_input or "Anonymous"  # if user_input is "", use fallback
port = config.get("port") or 8080
```

Be careful: `x or default` also treats `0`, `""`, and `[]` as missing.

When only `None` means missing, be explicit:

```python
port = config.get("port")
if port is None:
    port = 8080
```

### Custom Truthiness

Custom classes can define truthiness with `__bool__` or `__len__`:

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def __bool__(self):
        return self.balance > 0

account = BankAccount(0)
if not account:
    print("Account is empty")  # This prints

class Queue:
    def __init__(self, items):
        self._items = list(items)

    def __len__(self):
        return len(self._items)  # falsy when empty

q = Queue([])
if not q:
    print("Queue is empty")     # This prints
```

Practical rule: empty containers, zero numbers, and `None` are falsy.

Once that rule feels natural, your conditions become much easier to read.

---

<a id="chapter-ii-data-structures"></a>

## Chapter II: Data Structures

Python's built-in containers and when to reach for each one.

This chapter matters a lot because Python code leans heavily on built-in collections instead of custom classes for many day-one tasks.

- lists when order and mutation matter
- tuples when fixed structure matters
- dictionaries when values need names or keys
- sets when uniqueness and fast membership checks matter

If you want to write useful Python quickly, get comfortable with lists and dictionaries first, then understand sets and comprehensions.

### Priority

- Must read: Lists, Dictionaries, Comprehensions, Type Conversion
- Read if needed: Tuples, Sets
- Optional for now: Collections Module

### Sections

- [Lists](./docs/02-data-structures/lists.md)
- [Tuples](./docs/02-data-structures/tuples.md)
- [Dictionaries](./docs/02-data-structures/dictionaries.md)
- [Sets](./docs/02-data-structures/sets.md)
- [Collections Module](./docs/02-data-structures/collections-module.md)
- [Comprehensions](./docs/02-data-structures/comprehensions.md)
- [Type Conversion](./docs/02-data-structures/type-conversion.md)

---

<a id="lists"></a>

## Lists

Lists are ordered, mutable collections and the default sequence type in Python.

### What is a List?

A list can hold mixed types and can grow or shrink at runtime.

```python
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, None]
nested = [[1, 2], [3, 4], [5, 6]]
empty = []
```

### Indexing and Slicing

Lists are zero-indexed. Negative indexes count from the end. Slicing returns a new list.

```python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

print(fruits[0])     # "apple"
print(fruits[-1])    # "elderberry"
print(fruits[1:3])   # ["banana", "cherry"]  — stop index is exclusive
print(fruits[:2])    # ["apple", "banana"]
print(fruits[2:])    # ["cherry", "date", "elderberry"]
print(fruits[::2])   # ["apple", "cherry", "elderberry"]  — every 2nd
print(fruits[::-1])  # reverse
```

### Modifying Lists

Lists can be changed in place:

```python
fruits = ["apple", "banana", "cherry"]

fruits.append("date")            # add to end: O(1) amortized
fruits.insert(1, "blueberry")    # insert at index: O(n)
fruits.extend(["elderberry", "fig"])  # add multiple: O(k)

fruits.remove("banana")          # remove first occurrence by value: O(n)
popped = fruits.pop()            # remove and return last: O(1)
popped2 = fruits.pop(0)         # remove and return at index: O(n)
del fruits[1]                    # remove at index without returning

fruits[0] = "avocado"            # replace by index
fruits[1:3] = ["kiwi", "mango"] # replace a slice
```

### Sorting

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

numbers.sort()                    # in-place, ascending
numbers.sort(reverse=True)        # in-place, descending

sorted_copy = sorted(numbers)     # returns NEW list, original unchanged

words = ["banana", "apple", "cherry", "date"]
words.sort(key=len)               # sort by string length
words.sort(key=str.lower)         # case-insensitive sort
```

### Useful List Methods

```python
items = [3, 1, 4, 1, 5, 1]

print(len(items))          # 6
print(items.count(1))      # 3  — how many times 1 appears
print(items.index(4))      # 2  — index of first occurrence
items.reverse()            # in-place reverse
items.clear()              # remove all elements
```

### Performance Notes

Indexing and appending are fast. Inserting or removing near the front is slow. For queue-like behavior, use `collections.deque`.

### List Copying

Assignment shares the same list object:

```python
a = [1, 2, 3]
b = a             # b is the SAME list
b.append(4)
print(a)          # [1, 2, 3, 4]

## Shallow copy — new list, but nested objects still shared
c = a.copy()      # or: a[:]  or: list(a)
c.append(99)
print(a)          # [1, 2, 3, 4] — unaffected
```

---

<a id="tuples"></a>

## Tuples

Tuples often look like simpler lists, but their role is different. They are most useful when the shape of the data should stay fixed, such as coordinates, records, return values, and dictionary keys.

The key idea is not just that tuples are immutable. It is that immutability communicates intent to the reader.

### What is a Tuple?

A tuple is an **ordered, immutable** sequence. Once created, its contents cannot change. Tuples are slightly more memory-efficient than lists and can be used as dictionary keys or set members (because they are hashable, provided all their elements are also hashable).

```python
point = (10, 20)
rgb = (255, 128, 0)
single = (42,)        # trailing comma is REQUIRED for single-element tuples
empty = ()
no_parens = 1, 2, 3   # parentheses are optional — this is also a tuple
```

**A common mistake:**

```python
x = (42)    # This is NOT a tuple — just the integer 42 in parentheses
x = (42,)   # This IS a tuple with one element
```

### Immutability

Tuples cannot be modified after creation:

```python
t = (1, 2, 3)
## t[0] = 99       # TypeError: 'tuple' object does not support item assignment
## t.append(4)     # AttributeError: 'tuple' object has no attribute 'append'
```

However, if a tuple contains a mutable object (like a list), that object can still be modified:

```python
t = ([1, 2], [3, 4])
t[0].append(99)
print(t)   # ([1, 2, 99], [3, 4]) — the list inside was mutated
```

### Unpacking

Tuple unpacking is one of Python's most useful features:

```python
point = (10, 20)
x, y = point         # basic unpacking

## Ignore values with _
first, _, third = (1, 2, 3)

## Star unpacking — collect remaining items
head, *tail = (1, 2, 3, 4, 5)    # head=1, tail=[2,3,4,5]
*init, last = (1, 2, 3, 4, 5)    # init=[1,2,3,4], last=5
first, *middle, last = range(10)  # first=0, middle=[1..8], last=9

## Swap without a temp variable
a, b = 10, 20
a, b = b, a   # a=20, b=10
```

### Returning Multiple Values

Functions can return multiple values as a tuple — the most common tuple use case:

```python
def min_max(numbers):
    return min(numbers), max(numbers)   # returns a tuple

low, high = min_max([3, 1, 4, 1, 5, 9])
print(low, high)   # 1 9
```

### Tuples as Dictionary Keys

Because tuples are hashable, they can be used as dictionary keys — lists cannot:

```python
## Coordinate lookup
distances = {
    (0, 0): 0,
    (1, 0): 1,
    (0, 1): 1,
    (1, 1): 1.414,
}

print(distances[(1, 1)])  # 1.414

## This would fail:
## {[1, 2]: "value"}  # TypeError: unhashable type: 'list'
```

### Named Tuples

For tuples with many fields, `namedtuple` or `dataclass` give field names without sacrificing performance:

```python
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(p.x, p.y)    # 10 20
print(p[0])        # 10  — still indexable
print(p)           # Point(x=10, y=20)
```

---

<a id="dictionaries"></a>

## Dictionaries

Dictionaries map keys to values and are one of Python's most important data structures.

### What is a Dictionary?

A dictionary is a mutable mapping of unique keys to values. Lookups are fast, keys must be hashable, and insertion order is preserved.

```python
person = {"name": "Alice", "age": 30, "city": "New York"}
empty = {}
from_pairs = dict([("a", 1), ("b", 2)])
from_kwargs = dict(name="Alice", age=30)
```

### Accessing Values

```python
person = {"name": "Alice", "age": 30}

print(person["name"])          # "Alice"

print(person.get("email"))          # None
print(person.get("email", "N/A"))   # "N/A"

if "age" in person:
    print(person["age"])
```

### Modifying Dictionaries

```python
person = {"name": "Alice", "age": 30}

person["email"] = "alice@example.com"
person["age"] = 31

person |= {"city": "Boston", "lang": "Python"}

person.update({"country": "US"})

del person["lang"]                      # raises KeyError if missing
email = person.pop("email")             # remove and return value
removed = person.pop("missing", None)   # safe remove with default
```

### Iterating

```python
person = {"name": "Alice", "age": 30, "city": "NY"}

for key in person:                 # iterate over keys (default)
    print(key)

for value in person.values():      # values view
    print(value)

for key, value in person.items():  # key-value pairs
    print(f"{key}: {value}")
```

### Dict Comprehensions

```python
squares = {x: x**2 for x in range(6)}

original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}

even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
```

### Merging Dictionaries

```python
defaults = {"color": "blue", "size": 10, "visible": True}
overrides = {"size": 20, "opacity": 0.8}

merged = defaults | overrides
```

### `setdefault` and `defaultdict`

`setdefault()` is useful for grouping:

```python
groups = {}
for word in ["apple", "ant", "banana", "bear"]:
    groups.setdefault(word[0], []).append(word)
```

For heavy grouping code, `collections.defaultdict` is often cleaner.

---

<a id="sets"></a>

## Sets

Sets are for uniqueness and fast membership tests.

### What is a Set?

A set is an unordered collection of unique, hashable objects.

```python
colors = {"red", "green", "blue"}
from_list = set([1, 2, 2, 3, 3])   # {1, 2, 3} — duplicates removed
empty = set()                        # NOT {} — that creates an empty dict!
```

### Adding and Removing Elements

```python
s = {1, 2, 3}

s.add(4)          # add a single element
s.update([5, 6])  # add multiple elements

s.remove(3)       # raises KeyError if not present
s.discard(99)     # safe — no error if not present
s.pop()           # remove and return an arbitrary element (order is undefined)
s.clear()         # remove all elements
```

### Set Operations

Set algebra is built in:

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)         # {1, 2, 3, 4, 5, 6}

print(a & b)              # {3, 4}

print(a - b)              # {1, 2}

print(a ^ b)                        # {1, 2, 5, 6}
```

### Set Comparisons

```python
a = {1, 2, 3}
b = {1, 2, 3, 4, 5}

print(a.issubset(b))     # True  — all of a is in b
print(a <= b)            # True  — same as issubset
print(b.issuperset(a))   # True  — b contains all of a
print(a.isdisjoint({6, 7}))  # True — no elements in common
```

### Practical Uses

```python
def deduplicate(items):
    seen = set()
    return [x for x in items if not (x in seen or seen.add(x))]

VALID_EXTENSIONS = {".py", ".txt", ".json", ".yaml"}
filename = "script.py"
if filename.endswith(tuple(VALID_EXTENSIONS)):
    print("Valid file")
```

### Frozensets

A `frozenset` is an immutable set:

```python
fs = frozenset([1, 2, 3])
d = {fs: "value"}       # works because frozenset is hashable
```

---

<a id="collections-module"></a>

## Collections Module

The `collections` module exists because Python's basic containers are powerful, but some recurring problems deserve more specialized tools. This page introduces those tools so you can choose clearer abstractions instead of forcing every problem into a plain list or dictionary.

Read these types as practical upgrades for common situations, not as features you must memorize all at once.

`collections` provides specialized container types that solve common patterns more cleanly than plain dicts and lists.

### defaultdict

A dict that auto-initializes missing keys — eliminates the need for manual key checks.

```python
from collections import defaultdict

word_count = defaultdict(int)
words = ["apple", "banana", "apple", "cherry"]
for word in words:
    word_count[word] += 1

print(dict(word_count))  # {'apple': 2, 'banana': 1, 'cherry': 1}

## Grouping by first letter
groups = defaultdict(list)
for word in words:
    groups[word[0]].append(word)
```

### Counter

Counts hashable objects and supports arithmetic between counters.

```python
from collections import Counter

text = "hello world"
char_count = Counter(text)
print(char_count.most_common(3))  # [('l', 3), ('o', 2), ('h', 1)]

votes = Counter(["Python", "Python", "Rust", "Go", "Python"])
print(votes["Python"])  # 3

a = Counter("aab")
b = Counter("abb")
print(a + b)  # Counter({'a': 3, 'b': 3})
print(a - b)  # Counter({'a': 1})
```

### deque

A double-ended queue — O(1) appends/pops from both ends (lists are O(n) at the front).

```python
from collections import deque

queue = deque([1, 2, 3])
queue.append(4)      # [1, 2, 3, 4]
queue.appendleft(0)  # [0, 1, 2, 3, 4]
queue.pop()          # returns 4, queue: [0, 1, 2, 3]
queue.popleft()      # returns 0, queue: [1, 2, 3]

history = deque(maxlen=3)
for i in range(5):
    history.append(i)
print(history)  # deque([2, 3, 4], maxlen=3) — auto-evicts oldest
```

---

<a id="comprehensions"></a>

## Comprehensions

Comprehensions are a compact way to build collections from other iterables.

They work best when the transformation stays simple and readable.

### List Comprehensions

General form: `[expression for item in iterable if condition]`

```python
squares = [x**2 for x in range(10)]

evens = [x for x in range(20) if x % 2 == 0]

words = ["hello", "world", "python"]
upper = [w.upper() for w in words]
```

Nested comprehensions are possible, but use them carefully:

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flat = [n for row in matrix for n in row]
```

### Dict Comprehensions

```python
words = ["Python", "is", "great"]
lengths = {word: len(word) for word in words}

prices = {"apple": 1.0, "banana": 0.5, "cherry": 2.0}
expensive = {k: v for k, v in prices.items() if v > 0.8}
```

### Set Comprehensions

```python
unique = {x**2 for x in [-2, -1, 0, 1, 2]}
words = ["apple", "ant", "banana", "avocado"]
first_letters = {w[0] for w in words}  # {"a", "b"}
```

### Generator Expressions

A generator expression uses `()` and produces values lazily:

```python
big_list = [x**2 for x in range(1_000_000)]

gen = (x**2 for x in range(1_000_000))  # barely any memory used

total = sum(x**2 for x in range(1_000_000))
```

### When to Use Comprehensions

Use comprehensions for simple transforms and filters. Use a normal loop when logic becomes hard to read.

```python
doubles = [x * 2 for x in data if x > 0]

result = []
for item in data:
    processed = transform(item)
    if validate(processed):
        log(processed)
        result.append(processed)
```

---

<a id="type-conversion"></a>

## Type Conversion

Type conversion is where many beginner bugs become visible. Input usually arrives as strings, APIs may return one type while your logic expects another, and containers can often be converted from one form to another depending on the operation you need.

This page is really about making type changes explicit, predictable, and easy to reason about.

### Explicit vs Implicit Conversion

Python performs **almost no implicit type coercion**. Unlike JavaScript (where `"5" + 1 = "51"`) or C (where types are silently cast), Python raises a `TypeError` when you mix incompatible types:

```python
## This fails — Python won't silently convert
## print("Age: " + 30)   # TypeError: can only concatenate str (not "int") to str

## You must convert explicitly:
print("Age: " + str(30))  # "Age: 30"
print(f"Age: {30}")       # better — f-strings handle conversion automatically
```

### Numeric Conversions

```python
## String to number
x = int("42")           # 42
y = float("3.14")       # 3.14
z = int("0xFF", 16)     # 255  — parse hex string
b = int("1010", 2)      # 10   — parse binary string

## Number to string
s = str(100)            # "100"
s = str(3.14)           # "3.14"
s = hex(255)            # "0xff"
s = bin(10)             # "0b1010"
s = oct(8)              # "0o10"

## Between numeric types
i = int(3.9)            # 3    — truncates toward zero (not rounds!)
f = float(7)            # 7.0
c = complex(3)          # (3+0j)
```

**`int()` truncates, it does not round:**

```python
print(int(3.9))    # 3  — NOT 4
print(int(-3.9))   # -3 — NOT -4

## To round: use round()
print(round(3.9))  # 4
print(round(3.5))  # 4  — rounds to even (banker's rounding)
```

### Collection Conversions

```python
## To list
from_tuple  = list((1, 2, 3))      # [1, 2, 3]
from_set    = list({3, 1, 2})      # order not guaranteed
from_string = list("hello")        # ['h', 'e', 'l', 'l', 'o']
from_range  = list(range(5))       # [0, 1, 2, 3, 4]
from_dict   = list({"a": 1, "b": 2})  # ['a', 'b']  — keys only!

## To tuple
t = tuple([1, 2, 3])      # (1, 2, 3)

## To set — deduplicates
unique = set([1, 2, 2, 3, 3])  # {1, 2, 3}

## To dict — from key-value pairs
d = dict([("a", 1), ("b", 2)])
d = dict(zip(["a", "b"], [1, 2]))
```

### Boolean Conversion

```python
## Any object can be converted to bool
print(bool(0))       # False
print(bool(1))       # True
print(bool(""))      # False
print(bool("hi"))    # True
print(bool([]))      # False
print(bool([0]))     # True  — a list with one element, even if that element is 0
```

See the [Falsy Values](./docs/01-the-basics/falsy-values.md) page for the full rules.

### `isinstance()` vs Type Conversion

Before converting, you sometimes want to check the type first:

```python
def process(value):
    if isinstance(value, str):
        value = int(value)
    return value * 2

## isinstance() accepts a tuple of types:
def is_numeric(x):
    return isinstance(x, (int, float, complex))
```

Use `isinstance()` rather than `type(x) == int` — it correctly handles subclasses.

---

<a id="chapter-iii-control-flow"></a>

## Chapter III: Control Flow

Conditional logic, iteration, and the small amount of syntax you need to read most Python code.

Nothing exotic here. The main Python-specific part is getting comfortable reading clean indentation-based flow.

- `if` and `elif` choose between paths
- `match` expresses structured branching more clearly in some cases
- loops let you process repeated data without repeating code by hand

`match` is useful, but not a blocker for productive Python. Learn `if`, `for`, and loop patterns first.

### Priority

- Must read: If / Else, Loops
- Optional for now: Match / Case

### Sections

- [If / Else](./docs/03-control-flow/if-else.md)
- [Match / Case](./docs/03-control-flow/match-case.md)
- [Loops](./docs/03-control-flow/loops.md)

---

<a id="if-else"></a>

## If / Else

Conditional logic is how a program starts making decisions. The important skill is not just writing conditions, but reading them clearly and predicting which branch will run for a given input.

This page connects directly to truthiness from Chapter I, because Python conditions often depend on values that are not literally `True` or `False`.

### Basic Conditional

Python uses indentation to delimit blocks — there are no curly braces. The `elif` keyword replaces `else if`:

```python
age = 20

if age < 18:
    print("Minor")
elif age < 65:
    print("Adult")
else:
    print("Senior")
```

Python evaluates each condition in order and executes the first matching block. The `else` block is optional. You can have as many `elif` branches as you need.

### Truthy and Falsy Conditions

Any expression can be used as a condition — Python will evaluate its truthiness:

```python
name = input("Enter name: ")

if name:                     # equivalent to: if name != ""
    print(f"Hello, {name}!")
else:
    print("No name entered")

items = []
if not items:                # equivalent to: if len(items) == 0
    print("List is empty")
```

### Conditional Expression (Ternary)

Python has a one-line conditional expression: `value_if_true if condition else value_if_false`.

```python
age = 20
status = "Adult" if age >= 18 else "Minor"

## Useful in assignments and function arguments
label = "yes" if is_active else "no"
print("on" if enabled else "off")
```

Keep ternary expressions short and readable. If the condition or the values are complex, use a regular `if`/`else` block.

### Nested Conditions

```python
x = 15

if x > 0:
    if x % 2 == 0:
        print("Positive even")
    else:
        print("Positive odd")
else:
    print("Non-positive")
```

Flatten nested conditions with `and` when possible:

```python
if x > 0 and x % 2 == 0:
    print("Positive even")
```

### Multiple Conditions

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
```

For large numbers of discrete values, `match`/`case` (Python 3.10+) or a dictionary lookup is often cleaner:

```python
grade_map = {range(90, 101): "A", range(80, 90): "B", range(70, 80): "C"}
grade = next((g for r, g in grade_map.items() if score in r), "F")
```

---

<a id="match-case-python-3-10"></a>

## Match / Case (Python 3.10+)

`match` is Python's structural pattern matching feature. It is more powerful than a classic switch statement because it can both test values and unpack structure at the same time.

The main question to keep in mind is when `match` makes intent clearer than a chain of `if` and `elif` statements.

### Overview

`match`/`case` is Python's **structural pattern matching** — introduced in PEP 634. It is similar to `switch` in other languages but far more powerful: it can destructure sequences, mappings, and class instances, check types, bind variables, and apply guards — all in a single expression.

```python
command = "quit"

match command:
    case "quit":
        print("Quitting...")
    case "help":
        print("Available: quit, help, start")
    case _:
        print(f"Unknown: {command}")  # _ is the wildcard — always matches
```

### Matching Sequences

```python
def handle(point):
    match point:
        case (0, 0):
            print("Origin")
        case (x, 0):
            print(f"On x-axis at {x}")   # x is bound here
        case (0, y):
            print(f"On y-axis at {y}")
        case (x, y):
            print(f"Point at ({x}, {y})")
```

The variables named in a `case` pattern are **bound** when the pattern matches. They are available in the body of that case.

### Matching Mappings (Dicts)

```python
def handle_event(event):
    match event:
        case {"type": "click", "x": x, "y": y}:
            print(f"Click at ({x}, {y})")
        case {"type": "keypress", "key": k}:
            print(f"Key: {k}")
        case {"type": t}:
            print(f"Unknown event type: {t}")
```

Mapping patterns match if the dict contains **at least** the specified keys — extra keys are ignored.

### Matching Class Instances

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float

@dataclass
class Circle:
    center: Point
    radius: float

def describe(shape):
    match shape:
        case Point(x=0, y=0):
            return "Origin point"
        case Point(x=x, y=y):
            return f"Point at ({x}, {y})"
        case Circle(center=Point(x=cx, y=cy), radius=r):
            return f"Circle at ({cx}, {cy}) r={r}"
```

### OR Patterns and Guards

Use `|` to match multiple alternatives. Add a `if` guard for conditions that cannot be expressed structurally:

```python
def classify(value):
    match value:
        case 0 | False | None:
            return "falsy zero-like"
        case int(n) | float(n) if n < 0:
            return f"negative: {n}"
        case int(n) | float(n):
            return f"positive number: {n}"
        case str(s) if len(s) > 10:
            return "long string"
        case str(s):
            return f"string: {s!r}"
        case _:
            return "unknown"
```

### Matching Command Sequences

A practical pattern for command parsers:

```python
def parse_command(command: str):
    match command.split():
        case ["quit"]:
            return ("quit",)
        case ["go", direction] if direction in ("north", "south", "east", "west"):
            return ("go", direction)
        case ["go", direction]:
            return ("error", f"Invalid direction: {direction}")
        case ["pick", "up", item]:
            return ("pick_up", item)
        case ["drop", *items]:
            return ("drop", items)
        case []:
            return ("noop",)
        case _:
            return ("error", f"Unknown command: {command!r}")
```

### `as` Pattern

Bind a matched value to a name while still matching a pattern:

```python
match data:
    case [first, *rest] as full_list:
        print(f"First: {first}, Total: {len(full_list)}")
```

---

<a id="loops"></a>

## Loops

Python loops are mostly about iterating over values directly, not manually managing indexes.

### `for` Loops

`for` works with any iterable: lists, strings, ranges, dicts, files, and generators.

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

for char in "Python":
    print(char)

for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 10, 2):  # start, stop (exclusive), step
    print(i)               # 2, 4, 6, 8
```

### `enumerate()` — Index + Value

Use `enumerate()` when you need both index and value:

```python
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(i, fruit)

for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")
```

### `zip()` — Parallel Iteration

`zip()` pairs elements from multiple iterables:

```python
names = ["Alice", "Bob", "Charlie"]
scores = [95, 80, 88]

for name, score in zip(names, scores):
    print(f"{name}: {score}")
```

### `while` Loops

`while` repeats while a condition is true:

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

### `break`, `continue`, and `else`

- `break` — immediately exits the innermost loop
- `continue` — skip the rest of the current iteration and go to the next
- `else` on a loop — executes if the loop completed **without** hitting a `break`

```python
for n in range(10):
    if n == 3:
        continue    # skip 3
    if n == 7:
        break       # stop at 7
    print(n)        # prints 0, 1, 2, 4, 5, 6
```

### Iterating Over Dictionaries

```python
person = {"name": "Alice", "age": 30, "city": "NY"}

for key in person:           # keys (default)
    print(key)

for key, value in person.items():
    print(f"{key}: {value}")
```

### `reversed()` and `sorted()`

```python
items = [3, 1, 4, 1, 5, 9]

for x in reversed(items):   # iterate backward — no copy needed
    print(x)

for x in sorted(items):     # iterate in sorted order — returns new list
    print(x)

for x in sorted(items, reverse=True, key=abs):
    print(x)
```

---

<a id="chapter-iv-functions"></a>

## Chapter IV: Functions

Function syntax, arguments, return values, and the Python conventions that appear in almost every codebase.

If you are coming from another language, functions are familiar. What matters here is Python's calling style and a few common features that show up often.

Focus on these ideas:

- a function is a reusable block of behavior
- parameters describe what a function needs
- return values describe what a function produces
- type hints improve readability even in dynamic code

Do not spend much time on `lambda` unless you already use functional-style helpers.

### Priority

- Must read: Defining Functions, Parameters & Arguments, Type Hints
- Read next: Scoping Rules
- Optional for now: Lambda Functions

### Sections

- [Defining Functions](./docs/04-functions/defining-functions.md)
- [Parameters & Arguments](./docs/04-functions/parameters-arguments.md)
- [Lambda Functions](./docs/04-functions/lambda-functions.md)
- [Scoping Rules](./docs/04-functions/scoping-rules.md)
- [Type Hints](./docs/04-functions/type-hints.md)

---

<a id="defining-functions"></a>

## Defining Functions

Function definitions are where Python code starts becoming reusable instead of purely sequential. A function gives a piece of logic a name, a boundary, and a clear interface.

As you read, keep separating three concerns: what goes into the function, what happens inside it, and what comes back out.

### The `def` Statement

Functions are defined with `def`, followed by a name, parentheses for parameters, a colon, and an indented body. They are **first-class objects** — you can assign them to variables, pass them as arguments, and return them from other functions.

```python
def greet(name):
    return f"Hello, {name}!"

message = greet("Alice")    # "Hello, Alice!"
print(message)

## Assigning a function to a variable
say_hi = greet
print(say_hi("Bob"))        # "Hello, Bob!"
```

### Return Values

Every function returns a value. If there is no `return` statement (or `return` with no value), the function returns `None`:

```python
def add(a, b):
    return a + b

def log(message):
    print(message)          # no return → returns None implicitly

result = log("hello")
print(result)               # None
```

A function can return **multiple values** — Python packs them into a tuple:

```python
def min_max(numbers):
    return min(numbers), max(numbers)   # returns (min, max) tuple

low, high = min_max([3, 1, 4, 1, 5, 9])
print(low, high)    # 1 9

## Or capture as a tuple:
result = min_max([3, 1, 4])
print(type(result))  # <class 'tuple'>
```

### Docstrings

Document your function's purpose, parameters, and return value with a docstring — a string literal as the first statement in the body. Tools like `help()`, IDEs, and `pydoc` read these:

```python
def divide(a: float, b: float) -> float:
    """
    Divide a by b and return the result.

    Args:
        a: The dividend.
        b: The divisor. Must not be zero.

    Returns:
        The result of a / b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Divisor cannot be zero")
    return a / b

help(divide)        # prints the docstring
print(divide.__doc__)  # access programmatically
```

### Functions as Objects

Since functions are first-class objects, they can be passed around like any other value:

```python
def apply(func, value):
    return func(value)

def double(x):
    return x * 2

print(apply(double, 5))     # 10
print(apply(str, 42))       # "42"

## Store functions in a list
transformations = [str.upper, str.strip, str.title]
text = "  hello world  "
for fn in transformations:
    print(fn(text))
```

### Nested Functions

Functions can be defined inside other functions. Inner functions have access to the enclosing function's variables (closure):

```python
def make_multiplier(factor):
    def multiply(x):
        return x * factor   # 'factor' is captured from the enclosing scope
    return multiply

triple = make_multiplier(3)
print(triple(10))   # 30
print(triple(5))    # 15
```

---

<a id="parameters-arguments"></a>

## Parameters & Arguments

This page explains one of the most important parts of Python function design: how callers provide data to a function and how the function definition controls that calling style.

The details matter because many real bugs come from argument ordering, mutable defaults, or APIs that are technically valid but hard to call correctly.

### Positional Parameters

The simplest parameters — arguments are matched left to right by position:

```python
def power(base, exponent):
    return base ** exponent

power(2, 10)    # 1024 — base=2, exponent=10
```

### Default Parameter Values

Parameters can have default values, making them optional at the call site:

```python
def greet(name, greeting="Hello", punctuation="!"):
    return f"{greeting}, {name}{punctuation}"

greet("Alice")                    # "Hello, Alice!"
greet("Bob", "Hi")                # "Hi, Bob!"
greet("Carol", punctuation=".")   # "Hello, Carol."
```

**The mutable default trap** — the default value is evaluated **once** when the function is defined, not on each call. Using a mutable object (list, dict) as a default creates a shared state across calls:

```python
## WRONG — the list is shared across all calls
def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item("a"))   # ["a"]
print(add_item("b"))   # ["a", "b"]  — unexpected!

## CORRECT — use None as sentinel, create fresh object inside
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

### Keyword Arguments

At the call site, you can pass any argument by name, which makes the code more readable and lets you pass arguments out of order:

```python
def connect(host, port, timeout=30, ssl=True):
    ...

connect("db.example.com", 5432)
connect(port=5432, host="db.example.com", ssl=False)
connect("db.example.com", 5432, timeout=60)
```

### `*args` — Variable Positional Arguments

Prefix a parameter with `*` to collect any number of positional arguments into a **tuple**:

```python
def total(*numbers):
    return sum(numbers)

total(1, 2, 3)          # 6
total(10, 20, 30, 40)   # 100

## Spread a sequence with *
nums = [1, 2, 3, 4, 5]
print(total(*nums))     # 15
```

### `**kwargs` — Variable Keyword Arguments

Prefix a parameter with `**` to collect any number of keyword arguments into a **dict**:

```python
def describe(**attributes):
    for key, value in attributes.items():
        print(f"  {key}: {value}")

describe(name="Alice", age=30, city="New York")
## name: Alice
## age: 30
## city: New York

## Spread a dict with **
config = {"host": "localhost", "port": 8080}
connect(**config)   # equivalent to connect(host="localhost", port=8080)
```

### Keyword-Only and Positional-Only Parameters

Python lets you enforce how arguments must be passed:

```python
## Parameters after * must be passed by keyword
def fetch(url, *, timeout=30, retries=3):
    ...

fetch("https://api.example.com")              # OK
fetch("https://api.example.com", timeout=60)  # OK
## fetch("https://api.example.com", 60)        # TypeError

## Parameters before / must be passed positionally (Python 3.8+)
def normalize(x, y, /, *, precision=2):
    ...

normalize(3.0, 4.0)                    # OK
## normalize(x=3.0, y=4.0)             # TypeError — positional-only
normalize(3.0, 4.0, precision=4)      # OK
```

### Full Signature

The complete parameter order is:

```python
def func(pos_only, /, standard, *, kw_only):
    ...

## Or with variadic:
def full(pos_only, /, positional, *args, kw_only, **kwargs):
    ...
```

---

<a id="lambda-functions"></a>

## Lambda Functions

Lambda functions are small anonymous functions used mostly where a short function is needed temporarily. They are convenient, but they are intentionally limited, and Python style guides expect you to prefer named functions once logic becomes substantial.

The real lesson here is not "use lambda everywhere." It is learning when a one-line function improves clarity and when it hides meaning.

### What is a Lambda?

A **lambda** is an anonymous, single-expression function. It is written `lambda parameters: expression` and can be defined inline wherever a function object is expected. The expression is evaluated and returned automatically — no `return` keyword.

```python
square = lambda x: x ** 2
print(square(5))   # 25

add = lambda a, b: a + b
print(add(3, 4))   # 7
```

Lambdas are syntactically limited to a **single expression** — no assignments, no `if`/`else` blocks (though the ternary conditional works), no loops.

### When to Use Lambdas

Lambdas shine as short **callback functions** passed to higher-order functions. The most common use case is a `key` argument for sorting:

```python
## Sort by string length
words = ["banana", "apple", "cherry", "date"]
words.sort(key=lambda w: len(w))
print(words)   # ['date', 'apple', 'banana', 'cherry']

## Sort by the second element of each tuple
pairs = [(1, 3), (2, 1), (4, 2)]
pairs.sort(key=lambda pair: pair[1])
print(pairs)   # [(2, 1), (4, 2), (1, 3)]

## Sort by multiple fields (last name, then first name)
people = [("Alice", "Smith"), ("Bob", "Jones"), ("Carol", "Smith")]
people.sort(key=lambda p: (p[1], p[0]))
```

### Lambdas with `map()` and `filter()`

```python
numbers = [1, 2, 3, 4, 5, 6]

doubled = list(map(lambda x: x * 2, numbers))
## [2, 4, 6, 8, 10, 12]

evens = list(filter(lambda x: x % 2 == 0, numbers))
## [2, 4, 6]
```

In modern Python, **list comprehensions are usually preferred** over `map`/`filter` with lambdas:

```python
doubled = [x * 2 for x in numbers]
evens = [x for x in numbers if x % 2 == 0]
```

### Lambdas vs Named Functions

Use a named function when:
- You need more than one expression
- The function will be reused
- Readability matters more than brevity

```python
## Lambda — fine for one-off sort key
items.sort(key=lambda x: x.priority)

## Named function — better when the logic is complex or reused
def sort_key(item):
    return (item.priority, item.created_at, item.name)

items.sort(key=sort_key)
```

PEP 8 advises **against** assigning a lambda to a variable (use `def` instead), because `def` gives the function a proper name, which makes stack traces and `repr()` outputs clearer:

```python
## Discouraged by PEP 8:
square = lambda x: x ** 2

## Preferred:
def square(x):
    return x ** 2
```

---

<a id="scoping-rules-legb"></a>

## Scoping Rules (LEGB)

LEGB explains where Python looks up names.

### The LEGB Rule

Python searches in this order:

1. **L — Local** — names defined inside the current function
2. **E — Enclosing** — names in any enclosing functions (for nested functions)
3. **G — Global** — names defined at the module level
4. **B — Built-in** — names in Python's built-in namespace (`len`, `print`, `range`, etc.)

```python
x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)    # "local"   — L wins

    inner()
    print(x)        # "enclosing" — E wins

outer()
print(x)            # "global"  — G
```

### The `global` Keyword

Assignment inside a function creates a local variable unless you declare `global`:

```python
counter = 0

def increment():
    global counter      # without this, we'd create a local 'counter'
    counter += 1

increment()
increment()
print(counter)  # 2
```

### The `nonlocal` Keyword

`nonlocal` lets an inner function modify a variable from an enclosing function:

```python
def make_counter(start=0):
    count = start

    def increment(step=1):
        nonlocal count      # modify the enclosing 'count'
        count += step
        return count

    def reset():
        nonlocal count
        count = start

    return increment, reset

inc, reset = make_counter(10)
print(inc())    # 11
print(inc())    # 12
print(inc(5))   # 17
reset()
print(inc())    # 11
```

### Closures

A closure keeps access to variables from an outer function even after that function returns:

```python
def make_multiplier(factor):
    def multiply(x):
        return x * factor   # 'factor' is captured in the closure
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))   # 10
print(triple(5))   # 15
```

### A Common Closure Gotcha — Late Binding

Closures in loops use late binding unless you capture values explicitly:

```python
funcs = [lambda: i for i in range(5)]
for f in funcs:
    print(f())   # 4, 4, 4, 4, 4

funcs = [lambda i=i: i for i in range(5)]
for f in funcs:
    print(f())   # 0, 1, 2, 3, 4
```

### Variable Scope and the `UnboundLocalError`

If a function assigns to a name, Python treats that name as local throughout the function:

```python
x = 10

def bad():
    print(x)    # UnboundLocalError — x is treated as local because of the line below
    x = 20

## Fix: declare global, or avoid the re-assignment
def good():
    global x
    print(x)    # 10
    x = 20
```

---

<a id="type-hints"></a>

### Type Hints

Type hints document expected types. Python does not enforce them at runtime, but editors and type checkers use them.

#### Basic Syntax

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a + b

def log(message: str) -> None:  # Returns nothing
    print(message)
```

#### Common Types

```python
def process(value: int | str) -> str:  # Python 3.10+ union syntax
    return str(value)

def find_user(id: int) -> dict | None:  # Or Optional[dict]
    return {"id": id} if id > 0 else None

def first(items: list[int]) -> int:
    return items[0]

def get_config() -> dict[str, str]:
    return {"host": "localhost", "port": "8080"}

def coordinates() -> tuple[float, float]:
    return (10.5, 20.3)
```

#### Generics

Use generics when the return type depends on the input type:

```python
from typing import TypeVar

T = TypeVar('T')

def first(items: list[T]) -> T | None:
    return items[0] if items else None

## Type is preserved
value = first([1, 2, 3])     # value is int | None
text = first(["a", "b"])     # text is str | None
```

#### Generic Classes

```python
from typing import Generic, TypeVar

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []
    
    def push(self, item: T) -> None:
        self._items.append(item)
    
    def pop(self) -> T | None:
        return self._items.pop() if self._items else None

## Usage - type is preserved
int_stack = Stack[int]()
int_stack.push(1)
value = int_stack.pop()  # value is int

str_stack = Stack[str]()
str_stack.push("hello")
text = str_stack.pop()   # text is str
```

#### Type Aliases

Use aliases to simplify repeated types:

```python
from typing import TypeAlias

UserID: TypeAlias = int
Vector: TypeAlias = list[float]
JSONValue: TypeAlias = str | int | float | bool | None | dict | list

def get_user(id: UserID) -> dict:
    return {"id": id}

def dot_product(a: Vector, b: Vector) -> float:
    return sum(x * y for x, y in zip(a, b))
```

#### Function Types (Callable)

Use `Callable` when a parameter accepts a function:

```python
from collections.abc import Callable

def apply(func: Callable[[int], int], value: int) -> int:
    return func(value)

## Callable that takes two strings and returns a string
def combine(func: Callable[[str, str], str], a: str, b: str) -> str:
    return func(a, b)

apply(lambda x: x * 2, 5)        # 10
combine(lambda a, b: a + b, "Hello", "World")  # "HelloWorld"
```

#### Type Checking with mypy

Validate hints with `mypy`:

```bash
pip install mypy
mypy your_script.py
```

This catches type errors before runtime:
```python
def add(a: int, b: int) -> int:
    return a + b

add("1", "2")  # mypy will complain: Argument 1 to "add" has incompatible type "str"
```

For API clients, AI agents, and backend code, type hints pay off quickly because function boundaries stay clearer.

---

<a id="chapter-v-object-oriented-programming"></a>

## Chapter V: Object-Oriented Programming

Classes, dataclasses, and enough OOP to read framework and application code confidently.

Python supports OOP well, but many Python programs stay simpler than typical Java or C# designs. Use classes when they clarify state and behavior, not by default.

Keep these ideas in mind:

- classes define behavior and data together
- instances represent concrete objects created from those class definitions
- inheritance and composition are tools, not goals
- `dataclass` often replaces a lot of boilerplate

For a fast Python ramp-up, prioritize plain classes and dataclasses. Leave deeper inheritance patterns for later.

### Priority

- Read if you build services or framework code: Classes, Dataclasses
- Optional for now: Inheritance, Abstract Base Classes, Magic Methods

### Sections

- [Classes](./docs/05-oop/classes.md)
- [Inheritance](./docs/05-oop/inheritance.md)
- [Abstract Base Classes](./docs/05-oop/abstract-base-classes.md)
- [Magic Methods](./docs/05-oop/magic-methods.md)
- [Dataclasses](./docs/05-oop/dataclasses.md)

---

<a id="classes"></a>

## Classes

Classes bundle related data and behavior.

### Defining a Class

The class defines the structure. The instance is a concrete object.

```python
class Dog:
    species = "Canis familiaris"

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def speak(self, sound: str = "Woof") -> str:
        return f"{self.name} says {sound}!"

    def __repr__(self) -> str:
        return f"Dog(name={self.name!r}, age={self.age})"

rex = Dog("Rex", 3)
buddy = Dog("Buddy", 5)

print(rex.speak())          # Rex says Woof!
print(buddy.speak("Bark"))  # Buddy says Bark!
print(rex.species)          # Canis familiaris  — from class attribute
print(rex)                  # Dog(name='Rex', age=3)
```

### `self` — The Instance Reference

`self` refers to the current instance.

```python
class Counter:
    def __init__(self):
        self.value = 0      # instance attribute

    def increment(self):
        self.value += 1

    def reset(self):
        self.value = 0

c = Counter()
c.increment()
c.increment()
print(c.value)   # 2
c.reset()
print(c.value)   # 0
```

### Class vs Instance Attributes

Class attributes are shared. Instance attributes belong to one object.

```python
class Config:
    debug = False       # class attribute

c1 = Config()
c2 = Config()

Config.debug = True     # changes it for ALL instances (via class)
print(c1.debug)         # True
print(c2.debug)         # True

c1.debug = False        # creates an INSTANCE attribute on c1 — does not affect Config
print(c1.debug)         # False  — instance attribute wins
print(c2.debug)         # True   — still uses class attribute
print(Config.debug)     # True   — unchanged
```

### Class Methods and Static Methods

```python
class Temperature:
    def __init__(self, celsius: float):
        self.celsius = celsius

    def to_fahrenheit(self) -> float:
        return self.celsius * 9 / 5 + 32

    @classmethod
    def from_fahrenheit(cls, fahrenheit: float) -> "Temperature":
        return cls((fahrenheit - 32) * 5 / 9)

    @staticmethod
    def is_freezing(celsius: float) -> bool:
        return celsius <= 0

t = Temperature(100)
print(t.to_fahrenheit())                    # 212.0
t2 = Temperature.from_fahrenheit(32)        # factory
print(t2.celsius)                           # 0.0
print(Temperature.is_freezing(-5))          # True
```

### Properties

Use `@property` for computed values or validation:

```python
class Circle:
    def __init__(self, radius: float):
        self._radius = radius

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def area(self) -> float:
        import math
        return math.pi * self._radius ** 2

c = Circle(5)
print(c.area)       # 78.53...  — looks like attribute, runs computation
c.radius = 10       # calls the setter
```

For many real projects, classes plus dataclasses are enough. You do not need deep inheritance to write good Python.

---

<a id="inheritance"></a>

## Inheritance

Inheritance lets one class reuse and extend another, but it is most helpful when the relationship is genuinely conceptual and not just a way to share code mechanically.

This page is best read with a design question in mind: does the subtype really represent a specialized form of the parent type?

### Basic Inheritance

A subclass inherits all attributes and methods from its parent. Use `super()` to call the parent's implementation from within an override:

```python
class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        raise NotImplementedError(f"{type(self).__name__} must implement speak()")

    def __repr__(self) -> str:
        return f"{type(self).__name__}(name={self.name!r})"


class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name} says Woof!"


class Cat(Animal):
    def speak(self) -> str:
        return f"{self.name} says Meow!"


animals: list[Animal] = [Dog("Rex"), Cat("Whiskers"), Dog("Buddy")]
for animal in animals:
    print(animal.speak())   # polymorphism — each uses its own speak()
```

### `super()` and `__init__` Chaining

When a subclass defines `__init__`, it must explicitly call `super().__init__()` to initialize the parent's attributes:

```python
class Vehicle:
    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year

    def description(self) -> str:
        return f"{self.year} {self.make} {self.model}"


class ElectricVehicle(Vehicle):
    def __init__(self, make: str, model: str, year: int, range_km: int):
        super().__init__(make, model, year)   # initialize parent attributes
        self.range_km = range_km              # add new attribute

    def description(self) -> str:
        base = super().description()           # reuse parent method
        return f"{base} — EV ({self.range_km} km range)"


tesla = ElectricVehicle("Tesla", "Model 3", 2024, 570)
print(tesla.description())
## 2024 Tesla Model 3 — EV (570 km range)
```

### `isinstance()` and `issubclass()`

```python
print(isinstance(tesla, ElectricVehicle))   # True
print(isinstance(tesla, Vehicle))           # True — also an instance of the parent
print(isinstance(tesla, Animal))            # False

print(issubclass(ElectricVehicle, Vehicle)) # True
print(issubclass(Dog, Animal))              # True
```

### Multiple Inheritance and MRO

Python supports multiple inheritance. The **Method Resolution Order (MRO)** defines the order in which Python searches for a method. It uses the C3 linearization algorithm and is accessible via `ClassName.__mro__`:

```python
class Flyable:
    def move(self):
        return "Flying"

class Swimmable:
    def move(self):
        return "Swimming"

class Duck(Flyable, Swimmable):
    pass

d = Duck()
print(d.move())            # "Flying" — Flyable comes first in MRO
print(Duck.__mro__)        # (Duck, Flyable, Swimmable, object)
```

### Composition vs Inheritance

Inheritance models **is-a** relationships. Composition (holding a reference to another object) models **has-a** relationships, and is often more flexible:

```python
## Inheritance: Duck IS-A Bird
class Bird:
    def fly(self): ...

class Duck(Bird):
    pass

## Composition: Car HAS-A Engine
class Engine:
    def start(self): ...

class Car:
    def __init__(self):
        self.engine = Engine()   # has-a, not is-a

    def start(self):
        self.engine.start()
```

Prefer composition when the relationship is not a strict "is-a", or when you want to swap components at runtime.

---

<a id="abstract-base-classes"></a>

## Abstract Base Classes

Abstract base classes are about defining contracts. They let you say "any concrete subclass must provide this behavior" before you care about the exact implementation details.

That makes them useful when multiple classes should behave consistently, especially in larger designs or library code.

### What is an ABC?

An **Abstract Base Class (ABC)** is a class that cannot be instantiated directly — it defines a contract that subclasses must fulfill. Any method marked with `@abstractmethod` must be overridden in concrete subclasses, or instantiation of that subclass also fails.

ABCs enforce interface contracts at class-creation time rather than at method-call time, which catches missing implementations early.

```python
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        """Return the area of the shape."""

    @abstractmethod
    def perimeter(self) -> float:
        """Return the perimeter of the shape."""

    # Concrete method — available to all subclasses
    def describe(self) -> str:
        return f"{type(self).__name__}: area={self.area():.2f}, perimeter={self.perimeter():.2f}"


## Shape()   # TypeError: Can't instantiate abstract class Shape
## Missing: area, perimeter
```

### Implementing Concrete Subclasses

```python
class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


shapes: list[Shape] = [Circle(5), Rectangle(4, 6)]
for s in shapes:
    print(s.describe())
## Circle: area=78.54, perimeter=31.42
## Rectangle: area=24.00, perimeter=20.00
```

### Abstract Properties

Use `@property` and `@abstractmethod` together to require subclasses to implement computed attributes:

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @property
    @abstractmethod
    def sound(self) -> str:
        """The sound this animal makes."""

    def speak(self) -> str:
        return f"I say: {self.sound}"


class Dog(Animal):
    @property
    def sound(self) -> str:
        return "Woof"


class Cat(Animal):
    @property
    def sound(self) -> str:
        return "Meow"

print(Dog().speak())   # I say: Woof
```

### ABCs from `collections.abc`

The standard library defines ABCs for Python's built-in protocols in `collections.abc`. These are useful both for implementing and for type-checking:

```python
from collections.abc import Mapping, Sequence, Iterable, Callable

def process(data: Iterable[int]) -> int:
    return sum(data)

process([1, 2, 3])          # ✅ list is Iterable
process((1, 2, 3))          # ✅ tuple is Iterable
process(range(10))          # ✅ range is Iterable

## isinstance checks with ABCs
print(isinstance([], Sequence))   # True — list implements Sequence
print(isinstance({}, Mapping))    # True — dict implements Mapping
print(isinstance("hi", Sequence)) # True — str implements Sequence
```

### `register()` — Virtual Subclasses

You can declare an existing class as a "virtual subclass" of an ABC without modifying it:

```python
from collections.abc import Hashable

class MyClass:
    def __hash__(self):
        return 42

Hashable.register(MyClass)
print(isinstance(MyClass(), Hashable))   # True
```

This is useful for integrating third-party code with your ABC hierarchy.

---

<a id="magic-methods"></a>

## Magic Methods

Magic methods let custom classes work with Python syntax such as `print()`, `len()`, operators, iteration, and context managers.

### What Are Magic Methods?

Magic methods, or dunder methods, are special methods that Python calls automatically.

### String Representation

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Point({self.x!r}, {self.y!r})"

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

p = Point(3, 4)
print(repr(p))   # Point(3, 4)
print(str(p))    # (3, 4)
print(p)         # (3, 4)  — print() calls __str__
```

### Arithmetic Operators

```python
class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float) -> "Vector":
        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar: float) -> "Vector":
        return self.__mul__(scalar)

    def __neg__(self) -> "Vector":
        return Vector(-self.x, -self.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)    # Vector(4, 6)
print(v1 * 3)     # Vector(3, 6)
print(3 * v1)     # Vector(3, 6)  — uses __rmul__
print(-v1)        # Vector(-1, -2)
```

### Comparison Operators

```python
from functools import total_ordering

@total_ordering
class Temperature:
    def __init__(self, celsius: float):
        self.celsius = celsius

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Temperature):
            return NotImplemented
        return self.celsius == other.celsius

    def __lt__(self, other: "Temperature") -> bool:
        return self.celsius < other.celsius

t1 = Temperature(20)
t2 = Temperature(30)
print(t1 < t2)    # True
print(t2 >= t1)   # True
```

### Container Protocol

```python
class Playlist:
    def __init__(self, songs: list):
        self._songs = songs

    def __len__(self) -> int:
        return len(self._songs)

    def __getitem__(self, index):
        return self._songs[index]

    def __contains__(self, song) -> bool:
        return song in self._songs

    def __iter__(self):
        return iter(self._songs)

pl = Playlist(["Song A", "Song B", "Song C"])
print(len(pl))               # 3
print(pl[0])                 # "Song A"
print("Song B" in pl)        # True
for song in pl:
    print(song)
```

### `__call__` — Making Instances Callable

```python
class Multiplier:
    def __init__(self, factor: float):
        self.factor = factor

    def __call__(self, value: float) -> float:
        return value * self.factor

double = Multiplier(2)
print(double(5))    # 10.0
print(double(7))    # 14.0
print(callable(double))  # True
```

### `__enter__` and `__exit__` — Context Manager Protocol

These power the `with` statement.

```python
class Timer:
    def __enter__(self):
        import time
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.elapsed = time.time() - self.start
        return False

with Timer() as t:
    sum(range(1_000_000))
print(f"Elapsed: {t.elapsed:.4f}s")
```

You do not need to memorize every magic method. Focus on the common ones: `__init__`, `__repr__`, `__str__`, comparison methods, iterator methods, and context-manager methods.

---

<a id="dataclasses"></a>

## Dataclasses

Dataclasses reduce the boilerplate that often makes simple classes feel heavier than the data they hold. They are especially useful for records, configuration objects, and other classes whose main job is storing structured data.

Think of them as a way to keep object-oriented code concise when full manual class definitions would add noise instead of clarity.

### What is a Dataclass?

The `@dataclass` decorator (Python 3.7+) automatically generates boilerplate methods from annotated fields:
- `__init__` — with a parameter for each field
- `__repr__` — `ClassName(field=value, ...)`
- `__eq__` — compares all fields

This removes the repetitive `self.x = x` pattern entirely.

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float

p1 = Point(1.0, 2.0)
p2 = Point(1.0, 2.0)
print(p1)            # Point(x=1.0, y=2.0)
print(p1 == p2)      # True  — field-by-field comparison
```

### Default Values and `field()`

Provide defaults as literals for immutable types. For mutable defaults (lists, dicts), use `field(default_factory=...)`:

```python
from dataclasses import dataclass, field

@dataclass
class Employee:
    name: str
    department: str
    salary: float = 0.0
    # WRONG: skills: list = []   — mutable default is not allowed
    skills: list[str] = field(default_factory=list)
    metadata: dict = field(default_factory=dict)

emp = Employee("Alice", "Engineering", 90_000.0, ["Python", "SQL"])
print(emp)
```

`field()` also supports:
- `repr=False` — exclude from `__repr__`
- `compare=False` — exclude from `__eq__` and ordering
- `init=False` — don't include in `__init__` (initialize in `__post_init__`)

### `__post_init__`

Runs after `__init__` — use it for derived fields or validation:

```python
@dataclass
class Rectangle:
    width: float
    height: float
    area: float = field(init=False, repr=False)

    def __post_init__(self):
        if self.width <= 0 or self.height <= 0:
            raise ValueError("Dimensions must be positive")
        self.area = self.width * self.height

r = Rectangle(3.0, 4.0)
print(r.area)   # 12.0
```

### Ordering

Set `order=True` to generate `<`, `>`, `<=`, `>=` based on field order:

```python
@dataclass(order=True)
class Version:
    major: int
    minor: int
    patch: int

versions = [Version(1, 10, 0), Version(2, 0, 0), Version(1, 9, 5)]
print(sorted(versions))
## [Version(major=1, minor=9, patch=5), Version(major=1, minor=10, patch=0), Version(major=2, minor=0, patch=0)]
```

### Frozen Dataclasses

Set `frozen=True` to make instances immutable — enabling use as dict keys and set members:

```python
@dataclass(frozen=True)
class Config:
    host: str
    port: int

c = Config("localhost", 5432)
## c.port = 5433   # FrozenInstanceError
cache = {c: "connection"}  # works — frozen dataclasses are hashable
```

### Dataclass vs `namedtuple` vs Regular Class

| | `dataclass` | `namedtuple` | regular class |
|--|-------------|--------------|---------------|
| Mutable | ✅ (default) | ❌ | ✅ |
| `__repr__` auto | ✅ | ✅ | ❌ |
| Ordering | opt-in | ✅ | ❌ |
| Hashable | frozen only | ✅ | with `__hash__` |
| Inheritance | ✅ | limited | ✅ |
| Type hints | ✅ | ✅ | ✅ |

Use `@dataclass` for most new code. Use `namedtuple` for lightweight read-only records. Use a regular class when you need heavy customization.

---

<a id="chapter-vi-advanced-python-techniques"></a>

## Chapter VI: Advanced Python Techniques

Useful Python features that appear in real codebases, but are not all required on day one.

Treat this chapter as selective reading. Learn the parts that unblock framework code or make common patterns clearer.

Start with:

- context managers because `with` is everywhere
- decorators because frameworks use them heavily
- generators because they explain lazy iteration

You do not need every helper in `itertools` or every functional pattern before writing useful Python.

### Priority

- Must know soon: Context Managers, Decorators
- Read when useful: Iterators & Generators, Pattern Matching
- Optional for now: itertools & functools

### Sections

- [Iterators & Generators](./docs/06-advanced-python-techniques/iterators-generators.md)
- [itertools & functools](./docs/06-advanced-python-techniques/itertools-functools.md)
- [Decorators](./docs/06-advanced-python-techniques/decorators.md)
- [Context Managers](./docs/06-advanced-python-techniques/context-managers.md)
- [Pattern Matching](./docs/06-advanced-python-techniques/pattern-matching.md)

---

<a id="iterators-generators"></a>

## Iterators & Generators

Iterators and generators explain how Python processes data lazily instead of building everything in memory first.

### The Iterator Protocol

An iterable can be looped over. An iterator produces one item at a time.

```python
lst = [1, 2, 3]
it = iter(lst)
print(next(it))   # 1
print(next(it))   # 2
print(next(it))   # 3
## next(it)        # StopIteration
```

### Implementing a Custom Iterator

```python
class Countdown:
    def __init__(self, start: int):
        self.current = start

    def __iter__(self):
        return self   # the iterator IS the object

    def __next__(self) -> int:
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

for n in Countdown(3):
    print(n)    # 3, 2, 1, 0
```

### Generator Functions

Generator functions use `yield` and are usually easier than writing iterator classes:

```python
def countdown(start: int):
    while start >= 0:
        yield start
        start -= 1

for n in countdown(3):
    print(n)    # 3, 2, 1, 0
```

### Generators are Lazy

Generators produce values on demand, which is useful for large or infinite sequences:

```python
def fibonacci():
    a, b = 0, 1
    while True:            # infinite sequence!
        yield a
        a, b = b, a + b

fib = fibonacci()
for _ in range(8):
    print(next(fib), end=" ")   # 0 1 1 2 3 5 8 13
```

### Generator Expressions

A generator expression is the lazy version of a list comprehension:

```python
numbers = range(1_000_000)

squares_list = [x**2 for x in numbers]

squares_gen = (x**2 for x in numbers)

total = sum(x**2 for x in range(1_000))
```

### `yield from`

`yield from` delegates to another iterable:

```python
def chain(*iterables):
    for it in iterables:
        yield from it

list(chain([1, 2], "abc", range(3)))
## [1, 2, 'a', 'b', 'c', 0, 1, 2]
```

In practice, generators matter most for streaming data, reading files, paging API results, and memory-efficient pipelines.

---

<a id="itertools-functools"></a>

## itertools & functools

These modules are small toolboxes for iteration, caching, and function composition.

### `itertools` — Efficient Iteration

`itertools` gives you lazy iterator helpers.

#### Common Helpers

```python
import itertools

list(itertools.chain([1, 2], [3, 4], [5]))   # [1, 2, 3, 4, 5]

nested = [[1, 2], [3, 4], [5]]
list(itertools.chain.from_iterable(nested))  # [1, 2, 3, 4, 5]

list(itertools.zip_longest([1, 2, 3], ["a", "b"], fillvalue="-"))
first_five = list(itertools.islice(range(1_000_000), 5))   # [0, 1, 2, 3, 4]

list(itertools.takewhile(lambda x: x < 5, range(10)))  # [0, 1, 2, 3, 4]
list(itertools.dropwhile(lambda x: x < 5, range(10)))  # [5, 6, 7, 8, 9]

list(itertools.product([1, 2], ["a", "b"]))

list(itertools.combinations([1, 2, 3], 2))
for batch in itertools.batched(range(10), 3):
    print(batch)
```

### `functools` — Higher-Order Functions

#### Caching

```python
import functools

@functools.cache                  # unlimited cache — Python 3.9+
def fib(n: int) -> int:
    return n if n < 2 else fib(n-1) + fib(n-2)

@functools.lru_cache(maxsize=128) # bounded LRU cache
def expensive(x: int) -> int:
    return sum(range(x))

## cached_property — computed once per instance, then stored
class Circle:
    def __init__(self, r): self.r = r

    @functools.cached_property
    def area(self):
        import math
        return math.pi * self.r ** 2
```

#### `partial` — Partial Application

```python
from functools import partial

def power(base: float, exponent: float) -> float:
    return base ** exponent

square = partial(power, exponent=2)
cube   = partial(power, exponent=3)

print(square(5))    # 25.0
print(cube(3))      # 27.0
```

#### `reduce` — Fold Over a Sequence

```python
from functools import reduce
import operator

## Sum — same as sum([1,2,3,4,5])
reduce(operator.add, [1, 2, 3, 4, 5])    # 15

reduce(operator.mul, [1, 2, 3, 4, 5])    # 120
```

Prefer built-in `sum()`, `max()`, `min()` where possible — `reduce` is for custom fold operations.

---

<a id="decorators"></a>

### Decorators

Decorators wrap functions to add behavior without changing the original function body.

#### What is a Decorator?

A decorator is a function that takes a function and returns another function.

```python
@log_time
def process_data(data):
    return [x * 2 for x in data]
```

This is equivalent to:

```python
def process_data(data):
    return [x * 2 for x in data]
process_data = log_time(process_data)
```

#### Basic Decorator

```python
import time

def log_time(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper

@log_time
def get_users():
    time.sleep(0.5)
    return ["Alice", "Bob"]

users = get_users()  # Output: get_users took 0.5012s
```

#### Decorators with Parameters

When a decorator takes arguments like `@retry(times=3)`, it is a decorator factory:

```python
def retry(times=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == times:
                        raise
                    print(f"Attempt {attempt} failed: {e}. Retrying...")
        return wrapper
    return decorator

@retry(times=3)
def fetch_user_data(user_id):
    import random
    if random.random() < 0.7:
        raise ConnectionError("API timeout")
    return {"id": user_id, "name": f"User{user_id}"}
```

#### Multiple Decorators

Decorators can be stacked — they apply from bottom to top:

```python
@log_time
@retry(times=2)
def fetch_data():
    # Runs: retry first, then log_time wraps the result
    pass

## Equivalent to:
## fetch_data = log_time(retry(times=2)(fetch_data))
```

#### Common Use Cases

The most common production use cases are logging, auth, caching, retry logic, and framework hooks.

##### Logging

```python
import logging

def log_call(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Called {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_call
def process_order(order_id, customer_id):
    print(f"Processing order {order_id} for customer {customer_id}")
    return {"order_id": order_id, "status": "processed"}

result = process_order(123, 456)
```

##### Auth

```python
def require_role(required_role):
    def decorator(func):
        def wrapper(*args, **kwargs):
            current_user = get_current_user()  # hypothetical function
            if current_user.get("role") != required_role:
                raise PermissionError(f"Requires {required_role} role")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@require_role("admin")
def delete_user(user_id):
    print(f"Deleting user {user_id} from database")
    return {"status": "deleted", "user_id": user_id}
```

##### Caching

```python
from functools import cache

@cache
def expensive_calculation(n):
    print(f"Calculating for {n}...")
    result = sum(i * i for i in range(n))
    return result
```

##### Retry

```python
def retry_with_backoff(max_attempts=3, base_delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts:
                        raise
                    delay = base_delay * (2 ** (attempt - 1))  # Exponential backoff
                    print(f"Attempt {attempt} failed: {e}. Retrying in {delay}s...")
                    time.sleep(delay)
        return wrapper
    return decorator

@retry_with_backoff(max_attempts=3, base_delay=0.5)
def call_external_api(endpoint):
    import random
    if random.random() < 0.6:
        raise TimeoutError("External service timeout")
    return {"data": "successful response"}
```

Use `@functools.wraps` in production so wrapped functions keep their original name and metadata.

---

<a id="context-managers"></a>

## Context Managers

Context managers give Python a clean, explicit way to manage setup and cleanup. They are one of the clearest examples of Python turning a common error-prone pattern into readable syntax.

Whenever code needs paired actions like open and close, acquire and release, or start and cleanup, this page explains the preferred model.

### What is a Context Manager?

A context manager is an object that defines `__enter__` and `__exit__` methods. The `with` statement calls `__enter__` on entry and guarantees that `__exit__` is called on exit — even if an exception occurs. This makes resource management safe and explicit.

```python
## Classic example: file handling
with open("data.txt", "w", encoding="utf-8") as f:
    f.write("Hello!")
## File is closed here — guaranteed, even if write() raised
```

### Implementing with a Class

```python
class DatabaseConnection:
    def __init__(self, url: str):
        self.url = url
        self.conn = None

    def __enter__(self):
        print(f"Connecting to {self.url}")
        self.conn = self._connect(self.url)
        return self.conn    # bound to the 'as' variable

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing connection")
        if self.conn:
            self.conn.close()
        # Return True to suppress the exception; False (or None) to propagate it
        return False

with DatabaseConnection("postgresql://localhost/mydb") as conn:
    conn.execute("SELECT 1")
```

The `__exit__` method receives `(exc_type, exc_val, exc_tb)` — all `None` if no exception occurred. Return `True` to suppress the exception; return `False` or `None` to let it propagate.

### Implementing with `@contextmanager`

`contextlib.contextmanager` lets you write a context manager as a generator — usually much shorter than a class:

```python
from contextlib import contextmanager
import time

@contextmanager
def timer(label: str = ""):
    start = time.perf_counter()
    try:
        yield   # code inside the 'with' block runs here
    finally:
        elapsed = time.perf_counter() - start
        print(f"{label or 'Elapsed'}: {elapsed:.4f}s")

with timer("Sum"):
    total = sum(range(1_000_000))
## Sum: 0.0234s
```

Everything before `yield` is `__enter__`; everything in `finally` after `yield` is `__exit__`. Use `try/finally` to guarantee cleanup even when the `with` block raises.

### Yielding a Value

The `yield` expression can return a value that is bound to the `as` variable:

```python
from contextlib import contextmanager

@contextmanager
def temp_file(name: str):
    from pathlib import Path
    p = Path(name)
    try:
        yield p         # bound to the 'as' variable
    finally:
        p.unlink(missing_ok=True)   # always delete on exit

with temp_file("scratch.txt") as path:
    path.write_text("temporary data")
    # file is deleted after this block
```

### Useful Context Managers from the Standard Library

```python
import contextlib

## Suppress specific exceptions
with contextlib.suppress(FileNotFoundError):
    Path("nonexistent.txt").unlink()   # no exception raised

## Redirect stdout to a string
import io
with contextlib.redirect_stdout(io.StringIO()) as buf:
    print("captured")
print(buf.getvalue())   # "captured\n"

## Manage multiple context managers at once
with contextlib.ExitStack() as stack:
    files = [stack.enter_context(open(f)) for f in ["a.txt", "b.txt"]]
    # all files closed on exit
```

### Threading Lock Example

A common use of `with` for safe concurrent access:

```python
import threading

lock = threading.Lock()

shared_data = []

def append_safely(value):
    with lock:           # __enter__ acquires, __exit__ releases
        shared_data.append(value)
```

---

<a id="pattern-matching-python-3-10"></a>

## Pattern Matching (Python 3.10+)

This page focuses on pattern matching as a Pythonic technique rather than just as syntax. The value of `match` is not only branching on values, but also expressing shape, structure, and extraction in one place.

It overlaps with Chapter III's `match` introduction, but the emphasis here is on writing patterns idiomatically once the basic syntax already makes sense.

`match`/`case` goes beyond `switch` — it can destructure objects, sequences, and mappings.

```python
## Match on class instances
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float

def classify(point):
    match point:
        case Point(x=0, y=0):
            return "Origin"
        case Point(x=0, y=y):
            return f"Y-axis at {y}"
        case Point(x=x, y=0):
            return f"X-axis at {x}"
        case Point(x=x, y=y) if x == y:
            return f"Diagonal at {x}"
        case Point(x=x, y=y):
            return f"Point ({x}, {y})"

print(classify(Point(0, 0)))    # Origin
print(classify(Point(3, 3)))    # Diagonal at 3
print(classify(Point(1, 2)))    # Point (1, 2)

## Match on sequences
def handle_command(command):
    match command.split():
        case ["quit"]:
            return "Quitting"
        case ["go", direction]:
            return f"Going {direction}"
        case ["go", direction, speed]:
            return f"Going {direction} at {speed}"
        case _:
            return "Unknown command"

print(handle_command("go north"))        # Going north
print(handle_command("go south fast"))   # Going south at fast
```

---

<a id="chapter-vii-modules-packaging"></a>

## Chapter VII: Modules & Packaging

How Python projects are structured in practice: files, imports, packages, environments, and basic tooling.

This chapter matters early because productive Python is not only syntax. You also need to know how imports work, how to isolate dependencies, and where code should live.

The main progression is:

- one file becomes many modules
- related modules become packages
- projects gain virtual environments and dependency management
- reusable code can be built and distributed

For a fast start, focus on modules, file I/O, virtual environments, and a small set of useful commands. Packaging can wait unless you are publishing a library.

### Priority

- Must read: Modules, File I/O & JSON, Virtual Environments, Useful Commands
- Read if needed: Packages
- Optional for now: Build & Packaging

### Sections

- [Modules](./docs/07-modules/modules.md)
- [File I/O & JSON](./docs/07-modules/file-io-json.md)
- [Packages](./docs/07-modules/packages.md)
- [Virtual Environments](./docs/07-modules/virtual-environments.md)
- [Useful Commands](./docs/07-modules/useful-commands.md)
- [Build & Packaging](./docs/07-modules/build-packaging.md)

---

<a id="modules"></a>

## Modules

Modules are how Python code is organized into files and reusable namespaces.

### What is a Module?

A module is any `.py` file. Importing it runs the file once and makes its names available.

### Importing Modules

```python
import math
import os
import sys

print(math.sqrt(16))    # 4.0
print(math.pi)          # 3.14159...
print(os.getcwd())      # current directory
print(sys.version)      # Python version string
```

### Selective Imports

```python
from math import pi, sqrt, ceil
print(pi)          # 3.14159...
print(sqrt(25))    # 5.0

from math import *
```

Avoid `from module import *` in real code.

### Aliases

```python
import numpy as np         # de facto standard
import pandas as pd
import matplotlib.pyplot as plt

from datetime import datetime as dt
now = dt.now()
```

### Module Search Path

Python looks for imports in `sys.modules`, built-ins, and directories from `sys.path`.

```python
import sys
print(sys.path)   # list of directories Python searches
```

### The Standard Library

Python ships with a large standard library. Useful modules include:

| Module | Purpose |
|--------|---------|
| `os` | OS interaction, file system |
| `sys` | Interpreter internals, exit, argv |
| `pathlib` | Modern path manipulation |
| `json` | JSON encoding/decoding |
| `re` | Regular expressions |
| `datetime` | Dates and times |
| `collections` | Specialized containers |
| `itertools` | Iterator utilities |
| `functools` | Higher-order functions |
| `logging` | Structured logging |
| `threading` | Thread-based concurrency |
| `asyncio` | Async/await event loop |

### Writing Your Own Module

Use the `__name__ == "__main__"` guard when a file should be both importable and runnable:

```python
## greetings.py
def hello(name: str) -> str:
    return f"Hello, {name}!"

def goodbye(name: str) -> str:
    return f"Goodbye, {name}!"

if __name__ == "__main__":
    # Only runs when executed directly: python3 greetings.py
    print(hello("World"))
```

```python
## main.py
from greetings import hello
print(hello("Alice"))
```

### `__all__` — Controlling Public API

`__all__` controls what `from module import *` exports:

```python
## utils.py
__all__ = ["public_func", "PublicClass"]

def public_func():
    ...

def _internal():    # _ prefix also signals non-public, but __all__ is authoritative
    ...
```

---

<a id="file-i-o-json"></a>

## File I/O & JSON

File I/O and JSON are core tools for scripts, APIs, configs, and AI workflows.

### Opening Files

Use `with open(...)` so the file always closes:

```python
with open("data.txt", "r") as f:
    content = f.read()
```

Common mode strings:

| Mode | Meaning |
|------|---------|
| `"r"` | Read text (default) |
| `"w"` | Write text — **truncates** the file if it exists |
| `"a"` | Append text |
| `"x"` | Exclusive creation — fails if file exists |
| `"rb"` | Read binary |
| `"wb"` | Write binary |

For text files, specify UTF-8:

```python
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
```

### Reading Files

```python
with open("data.txt", encoding="utf-8") as f:
    content = f.read()

with open("data.txt", encoding="utf-8") as f:
    lines = f.readlines()

with open("data.txt", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
```

### Writing Files

```python
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello, World!\n")

lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("output.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)

with open("log.txt", "a", encoding="utf-8") as f:
    f.write("New log entry\n")
```

### Working with Paths — `pathlib`

`pathlib.Path` is the modern way to handle paths:

```python
from pathlib import Path

p = Path("data") / "config.json"   # path joining with /
print(p.exists())
print(p.suffix)      # ".json"
print(p.stem)        # "config"
print(p.parent)      # Path("data")

text = p.read_text(encoding="utf-8")
p.write_text("new content", encoding="utf-8")
```

### JSON

Python's `json` module maps Python data to JSON and back:

| Python | JSON |
|--------|------|
| `dict` | object `{}` |
| `list`, `tuple` | array `[]` |
| `str` | string |
| `int`, `float` | number |
| `True`/`False` | `true`/`false` |
| `None` | `null` |

```python
import json

data = {
    "name": "Alice",
    "age": 30,
    "scores": [95, 87, 92],
    "active": True,
    "address": None,
}

## Serialize to JSON string
json_str = json.dumps(data)                # compact
json_pretty = json.dumps(data, indent=2)   # readable

## Deserialize from JSON string
parsed = json.loads(json_str)
print(parsed["name"])   # "Alice"

## Write to file
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

## Read from file
with open("data.json", encoding="utf-8") as f:
    loaded = json.load(f)
```

`json.dumps()` writes to a string. `json.dump()` writes to a file.

### Handling Missing Files Gracefully

```python
from pathlib import Path
import json

config_file = Path("config.json")

try:
    data = json.loads(config_file.read_text(encoding="utf-8"))
except FileNotFoundError:
    data = {}   # use defaults
except json.JSONDecodeError as e:
    print(f"Invalid JSON in config: {e}")
    data = {}
```

This pattern matters a lot for config files, cached model outputs, prompts, and API payloads.

---

<a id="packages"></a>

## Packages

Packages are how Python scales module organization from a few files to larger codebases. They give related modules a shared namespace and let projects grow without collapsing into import chaos.

If modules organize code by file, packages organize it by folder and public API.

### What is a Package?

A **package** is a directory that contains a special file called `__init__.py`. This file (which can be empty) marks the directory as a Python package, allowing its modules to be imported with dot notation.

```
my_package/
├── __init__.py        # makes this directory a package
├── auth.py
├── database.py
└── utils/
    ├── __init__.py    # nested package
    └── helpers.py
```

### Importing from a Package

```python
## Import a module from the package
import my_package.auth

## Import a specific name
from my_package.auth import login, logout

## Import from a nested package
from my_package.utils.helpers import format_date
```

### `__init__.py` — Defining the Public API

The `__init__.py` runs when the package is first imported. Use it to expose a clean public API and hide internal structure:

```python
## my_package/__init__.py
from .auth import login, logout, User
from .database import connect, disconnect
from .utils.helpers import format_date

__version__ = "1.2.0"
__all__ = ["login", "logout", "User", "connect", "disconnect"]
```

With this setup, users can write `from my_package import login` instead of `from my_package.auth import login`.

### Relative Imports

Inside a package, use **relative imports** (prefixed with `.`) to import from sibling modules:

```python
## my_package/auth.py
from .database import connect      # sibling module
from .utils.helpers import hash_pw # subpackage
from . import config               # the package itself
```

Relative imports only work inside packages — not in scripts run directly.

### Namespace Packages (Python 3.3+)

Python 3.3+ supports **namespace packages** — directories without `__init__.py` that still act as packages. This is useful for splitting a package across multiple directories or repositories, but regular packages with `__init__.py` are still the norm for most projects.

### Practical Package Layout

A typical small project:

```
myproject/
├── pyproject.toml          # project metadata and build config
├── README.md
├── src/
│   └── mypackage/
│       ├── __init__.py
│       ├── core.py
│       └── utils.py
└── tests/
    ├── __init__.py
    ├── test_core.py
    └── test_utils.py
```

Placing the package under `src/` (the "src layout") prevents accidental imports of the development version instead of the installed version, which makes testing more reliable.

---

<a id="virtual-environments"></a>

## Virtual Environments

Virtual environments solve one of the most practical Python problems: dependency isolation. Without them, package versions from one project can leak into another and make behavior hard to reproduce.

Treat a virtual environment as part of the project setup, not as an optional advanced tool.

### Why Virtual Environments?

Without a virtual environment, every package you install with `pip` goes into the global Python installation. This causes problems:
- **Version conflicts** — project A needs `requests==2.28`, project B needs `requests==2.31`
- **Pollution** — unrelated packages from one project clutter another
- **Reproducibility** — "it works on my machine" problems when deploying

A **virtual environment** is an isolated directory containing its own Python interpreter copy, its own `pip`, and its own site-packages. Each project gets its own environment.

### Creating and Activating

```bash
## Create a virtual environment in a folder called 'venv'
python3 -m venv venv

## Activate (macOS / Linux)
source venv/bin/activate

## Activate (Windows CMD)
venv\Scripts\activate.bat

## Activate (Windows PowerShell)
venv\Scripts\Activate.ps1

## Deactivate — return to global Python
deactivate
```

When a virtual environment is active, your shell prompt shows its name: `(venv) $`. All `python` and `pip` commands now use the isolated environment.

### Managing Dependencies

```bash
## Install packages into the active venv
pip install requests fastapi

## Install a specific version
pip install "django==5.0"

## Install from a requirements file
pip install -r requirements.txt

## Freeze current environment to a file
pip freeze > requirements.txt

## Show installed packages
pip list
pip show requests
```

### `requirements.txt`

A `requirements.txt` pins exact versions for reproducible installs:

```
requests==2.31.0
fastapi==0.110.0
pydantic==2.6.0
uvicorn==0.27.0
```

Generate it with `pip freeze > requirements.txt` and commit it to source control. Teammates and CI systems can reproduce the exact environment with `pip install -r requirements.txt`.

### `.gitignore`

Always add the `venv/` directory to `.gitignore` — it should not be committed:

```
venv/
__pycache__/
*.pyc
.env
```

### Modern Alternatives

| Tool | Description |
|------|-------------|
| `uv` | Very fast Rust-based pip + venv replacement |
| `poetry` | Dependency management + packaging in one |
| `pipenv` | Combines pip + virtualenv with a `Pipfile` |
| `conda` | Manages Python versions + packages (popular in data science) |

---

<a id="useful-commands"></a>

## Useful Commands

This page is a working reference rather than a concept-first lesson. The main goal is to help you recognize which command solves which packaging or interpreter task without needing to search every time.

Over time, these commands become part of normal Python workflow, especially when combined with virtual environments and module-based execution.

### pip — Package Installer

```bash
## Install a package
pip install requests

## Install a specific version
pip install "requests==2.31.0"

## Install minimum version
pip install "requests>=2.28"

## Install from a requirements file
pip install -r requirements.txt

## Upgrade a package
pip install --upgrade requests

## Upgrade pip itself
pip install --upgrade pip

## Uninstall a package
pip uninstall requests

## List installed packages
pip list

## Show details for a package (version, location, dependencies)
pip show requests

## Freeze current environment to a file (exact versions)
pip freeze > requirements.txt

## Search PyPI (deprecated in pip 21+; use https://pypi.org instead)
## pip search requests
```

### Python Interpreter Commands

```bash
## Start the interactive REPL
python3

## Run a script
python3 script.py

## Run a module as a script (e.g., the built-in http server)
python3 -m http.server 8000

## Execute a one-liner
python3 -c "print('Hello')"

## Check Python version
python3 --version

## Show where Python is installed
which python3     # macOS / Linux
where python3     # Windows
```

### Virtual Environment Commands

```bash
## Create a virtual environment
python3 -m venv venv

## Activate (macOS / Linux)
source venv/bin/activate

## Activate (Windows CMD)
venv\Scripts\activate.bat

## Activate (Windows PowerShell)
venv\Scripts\Activate.ps1

## Deactivate
deactivate

## Install all project dependencies
pip install -r requirements.txt
```

### Checking Installed Package Info

```bash
## Show package version and location
pip show numpy

## List outdated packages
pip list --outdated

## Verify installed packages against requirements
pip check
```

---

<a id="build-packaging"></a>

## Build & Packaging

Building and packaging are about turning Python code into something other people, tools, or deployment systems can install and use reliably. This is where project metadata, dependencies, and distribution formats come together.

The details can feel operational at first, but they matter because good packaging is what makes code reusable beyond your own machine.

### `pyproject.toml` — The Modern Standard

`pyproject.toml` is the single file that defines a Python project's metadata, dependencies, and build configuration. It replaced the older `setup.py` / `setup.cfg` approach.

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.backends.legacy:build"

[project]
name = "my-package"
version = "1.0.0"
description = "A sample Python package"
readme = "README.md"
license = { text = "MIT" }
requires-python = ">=3.9"
authors = [{ name = "Alice", email = "alice@example.com" }]
keywords = ["python", "example"]
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]
dependencies = [
    "requests>=2.28",
    "pydantic>=2.0",
]

[project.optional-dependencies]
dev = ["pytest", "mypy", "ruff"]
docs = ["mkdocs", "mkdocs-material"]

[project.urls]
Homepage = "https://github.com/user/my-package"
Issues = "https://github.com/user/my-package/issues"

[project.scripts]
my-tool = "my_package.cli:main"   # creates a command-line entry point
```

### Building a Distribution

A **wheel** (`.whl`) is a binary distribution — fast to install. A **source distribution** (`.tar.gz`, sdist) contains raw source files.

```bash
## Install the build frontend
pip install build

## Build both wheel and sdist
python -m build
## Creates: dist/my_package-1.0.0-py3-none-any.whl
##          dist/my_package-1.0.0.tar.gz
```

### Publishing to PyPI

```bash
## Install twine (the upload tool)
pip install twine

## Check the distribution files for errors
twine check dist/*

## Upload to the test PyPI (safe to experiment)
twine upload --repository testpypi dist/*

## Upload to the real PyPI
twine upload dist/*
```

You will need a PyPI account and an API token. Set the token as an environment variable or store it in `~/.pypirc`.

### Development Install

During development, install your package in **editable mode** so changes take effect immediately without reinstalling:

```bash
pip install -e .            # installs in editable mode
pip install -e ".[dev]"     # also installs optional dev dependencies
```

### Project Layout Reference

```
my-package/
├── pyproject.toml
├── README.md
├── LICENSE
├── src/
│   └── my_package/
│       ├── __init__.py
│       ├── core.py
│       └── cli.py
└── tests/
    ├── test_core.py
    └── conftest.py
```

---

<a id="chapter-viii-errors-exceptions"></a>

## Chapter VIII: Errors & Exceptions

This chapter is about writing Python that fails clearly and handles expected problems without hiding bugs.

For a 1-2 hour ramp-up, focus on these ideas:

- bugs you should fix
- runtime problems your code should handle deliberately
- catch specific exceptions, not everything
- use `raise` when invalid input or state should stop execution

You do not need the full exception hierarchy memorized. You need a clean mental model for `try`, `except`, `else`, `finally`, and custom exceptions.

### Priority

- Must read now: Basic `try` / `except`, Raising Exceptions
- Read next: `else` and `finally`, Custom Exceptions
- Optional for now: Exception Chaining

### Basic `try` / `except`

```python
try:
    result = 10 / 0
except ZeroDivisionError as exc:
    print(f"Error: {exc}")
```

Handle the most specific exception type you expect. Catching `Exception` too early can hide real bugs.

### `else` and `finally`

```python
try:
    result = compute(data)
except ValueError as exc:
    print(f"Bad input: {exc}")
else:
    save_result(result)
finally:
    cleanup()
```

### Raising Exceptions

```python
def set_age(age: int):
    if not isinstance(age, int):
        raise TypeError("age must be int")
    if age < 0:
        raise ValueError("age must be non-negative")
```

### Custom Exceptions

```python
class AppError(Exception):
    pass


class AccountLockedError(AppError):
    pass
```

Create custom exceptions when your app or library has domain-specific failure cases that callers may want to handle explicitly.

### Related Topic

Many cleanup scenarios are better expressed with a `with` statement than with `try`/`finally`. See the [Context Managers](./docs/06-advanced-python-techniques/context-managers.md) page when you continue into advanced topics.

---

<a id="chapter-ix-concurrency"></a>

## Chapter IX: Concurrency

Python concurrency choices and when they actually matter.

Do not spend your first hour here unless your immediate work depends on it. Most Python learners need only one idea at the start: choose concurrency based on workload, not fashion.

### Decision rules

- are you waiting on I/O or doing CPU-heavy work?
- async is usually for high-concurrency I/O
- threads are fine for blocking I/O and integration code
- processes are for CPU-heavy work

By the end of the chapter, you should be able to choose an approach for a problem instead of guessing between `asyncio`, threads, and processes.

### Sections

- [The GIL](./docs/09-concurrency/the-gil.md)
- [Async / Await](./docs/09-concurrency/async-await.md)
- [Threading](./docs/09-concurrency/threading.md)
- [Multiprocessing](./docs/09-concurrency/multiprocessing.md)
- [Free-Threading](./docs/09-concurrency/free-threading.md)
- [Decision Matrix](./docs/09-concurrency/decision-matrix.md)

---

<a id="the-gil"></a>

## The GIL

The GIL matters mainly when choosing between threads, processes, and async code.

### What is the GIL?

The **Global Interpreter Lock (GIL)** in CPython allows only one thread to execute Python bytecode at a time.

### What the GIL Prevents

```python
import threading

counter = 0

def increment():
    global counter
    for _ in range(1_000_000):
        counter += 1   # read-modify-write, but GIL makes each bytecode step atomic

threads = [threading.Thread(target=increment) for _ in range(4)]
for t in threads:
    t.start()
for t in threads:
    t.join()

## counter may not be 4_000_000
```

### The GIL is Released During I/O

CPython releases the GIL during I/O, so threads work well for network and file operations.

```python
from concurrent.futures import ThreadPoolExecutor
import urllib.request

def fetch(url):
    with urllib.request.urlopen(url) as r:
        return len(r.read())

with ThreadPoolExecutor(max_workers=10) as pool:
    sizes = list(pool.map(fetch, ["https://python.org"] * 10))
```

### The GIL Does Not Help CPU-Bound Code

For CPU-heavy Python code, threads do not give true parallelism:

```python
def cpu_task():
    total = 0
    for i in range(10_000_000):
        total += i
    return total

from concurrent.futures import ProcessPoolExecutor

with ProcessPoolExecutor() as pool:
    results = list(pool.map(lambda _: cpu_task(), range(4)))
```

### Python 3.13 — Free-Threading (Experimental)

Python 3.13 introduced an experimental free-threaded build, but the normal CPython build still uses the GIL.

### C Extensions and the GIL

Some C extensions such as NumPy release the GIL during heavy work:

```python
import numpy as np
import threading

def matmul():
    a = np.random.rand(1000, 1000)
    b = np.random.rand(1000, 1000)
    return np.dot(a, b)   # GIL is released here

threads = [threading.Thread(target=matmul) for _ in range(4)]
for t in threads:
    t.start()
for t in threads:
    t.join()
```

### Summary

| Workload | Best Tool | Why |
|----------|-----------|-----|
| I/O-bound (network, files) | `asyncio` or `threading` | GIL released during I/O |
| CPU-bound (computation) | `multiprocessing` | Each process has own GIL |
| Mixed | `asyncio` + executor | Run blocking code in thread pool |
| NumPy/C extensions | `threading` | C code can release the GIL |

---

<a id="async-await"></a>

## Async / Await

`async` and `await` are mainly for I/O-heavy concurrency, not CPU-heavy speedups.

### How asyncio Works

`asyncio` uses a single-threaded event loop. Coroutines pause at `await` so other work can run.

### Basic Coroutine

```python
import asyncio

async def greet(name: str) -> str:
    await asyncio.sleep(1)   # non-blocking wait (simulates I/O)
    return f"Hello, {name}!"

async def main():
    result = await greet("Alice")
    print(result)

asyncio.run(main())   # Entry point — creates and runs the event loop
```

Use `asyncio.run()` at top level. In notebooks, usually use `await` directly.

### Concurrency with `asyncio.gather()`

Use `asyncio.gather()` to run multiple coroutines concurrently:

```python
import asyncio
import time

async def fetch(url: str) -> str:
    await asyncio.sleep(1)    # simulate network request
    return f"Data from {url}"

async def main():
    start = time.perf_counter()
    r1, r2 = await asyncio.gather(
        fetch("https://api.example.com/users"),
        fetch("https://api.example.com/posts"),
    )
    print(f"Done in {time.perf_counter() - start:.2f}s")

asyncio.run(main())
```

### Tasks

`asyncio.create_task()` schedules a coroutine immediately:

```python
async def main():
    task1 = asyncio.create_task(fetch("url1"))
    task2 = asyncio.create_task(fetch("url2"))
    result1 = await task1
    result2 = await task2
```

### Real HTTP with `httpx`

```python
import asyncio
import httpx

async def get_post(client: httpx.AsyncClient, post_id: int) -> dict:
    response = await client.get(
        f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    )
    response.raise_for_status()
    return response.json()

async def main():
    async with httpx.AsyncClient() as client:
        posts = await asyncio.gather(
            *[get_post(client, i) for i in range(1, 6)]
        )
    for post in posts:
        print(post["title"])

asyncio.run(main())
```

### Common Pitfalls

- **Blocking calls inside coroutines** — `time.sleep()`, file reads, CPU work block the entire event loop. Use `await asyncio.sleep()`, async libraries, or `loop.run_in_executor()` to offload.
- **Not awaiting a coroutine** — calling `fetch(url)` without `await` creates the coroutine object but never runs it.
- **Shared mutable state** — coroutines share memory; protect shared state with `asyncio.Lock()` when needed.

---

<a id="threading"></a>

### Threading

Threads are useful when a program spends much of its time waiting on external work such as network I/O, file I/O, or blocking library calls. They are less useful when pure Python code is trying to saturate CPU cores.

This page should be read together with the GIL page, because thread behavior makes the most sense once that runtime constraint is clear.

#### When to Use Threads

Python threads are best for **I/O-bound** work — network requests, database queries, file reads — where the program spends most of its time waiting. Because of the GIL, threads do **not** parallelize CPU-bound computation; use `multiprocessing` for that.

#### `ThreadPoolExecutor` — Recommended

`concurrent.futures.ThreadPoolExecutor` is the high-level API. Prefer it over manual `threading.Thread` management:

```python
from concurrent.futures import ThreadPoolExecutor, as_completed
import urllib.request

def fetch(url: str) -> str:
    with urllib.request.urlopen(url, timeout=5) as response:
        return response.read(200).decode()

urls = [
    "https://www.python.org",
    "https://www.github.com",
    "https://www.stackoverflow.com",
]

with ThreadPoolExecutor(max_workers=3) as executor:
    # map — preserves order, blocks until all done
    for result in executor.map(fetch, urls):
        print(result[:50])

    # submit + as_completed — returns results as they finish
    futures = {executor.submit(fetch, url): url for url in urls}
    for future in as_completed(futures):
        url = futures[future]
        try:
            data = future.result()
            print(f"{url}: {len(data)} bytes")
        except Exception as e:
            print(f"{url} failed: {e}")
```

#### Manual Threads

Use `threading.Thread` when you need fine-grained control:

```python
import threading
import time

results = {}

def worker(name: str, duration: float):
    time.sleep(duration)
    results[name] = f"{name} finished after {duration}s"

threads = [
    threading.Thread(target=worker, args=(f"T{i}", 0.1 * i))
    for i in range(1, 4)
]
for t in threads:
    t.start()
for t in threads:
    t.join()    # wait for all to finish

print(results)
```

#### Thread Safety with Locks

When multiple threads write to shared data, use a `Lock` to prevent race conditions:

```python
import threading

counter = 0
lock = threading.Lock()

def increment(n: int):
    global counter
    for _ in range(n):
        with lock:
            counter += 1   # only one thread at a time

threads = [threading.Thread(target=increment, args=(10_000,)) for _ in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(counter)   # Always 50000 — safe with lock
```

Without the lock, threads would read and write `counter` simultaneously, causing lost updates (the count would be unpredictably less than 50000).

#### Thread-Safe Queues

`queue.Queue` is the recommended way to communicate between threads — it is internally thread-safe:

```python
import queue
import threading

task_queue: queue.Queue = queue.Queue()

def producer():
    for i in range(5):
        task_queue.put(i)
    task_queue.put(None)   # sentinel to signal done

def consumer():
    while True:
        item = task_queue.get()
        if item is None:
            break
        print(f"Processing {item}")
        task_queue.task_done()

t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)
t1.start(); t2.start()
t1.join(); t2.join()
```

#### `threading.local()` — Thread-Local Storage

`threading.local()` creates an object where each thread has its own isolated attribute values:

```python
import threading

local_data = threading.local()

def worker():
    local_data.value = threading.current_thread().name
    print(local_data.value)

threads = [threading.Thread(target=worker) for _ in range(3)]
for t in threads:
    t.start()
for t in threads:
    t.join()
```

---

<a id="multiprocessing"></a>

### Multiprocessing

Multiprocessing trades simplicity of shared memory for real parallel execution across CPU cores. That tradeoff matters because it changes both performance and program design.

The main lesson here is when the extra process overhead is justified by CPU-bound workloads.

#### When to Use Multiprocessing

`multiprocessing` creates separate OS processes — each has its own Python interpreter and its own GIL. This enables **true CPU parallelism** across multiple cores, which is impossible with threads due to the GIL.

Use `multiprocessing` for **CPU-bound** tasks: numerical computation, image processing, data parsing, compression.

#### `ProcessPoolExecutor` — Recommended

```python
from concurrent.futures import ProcessPoolExecutor
import time

def cpu_task(n: int) -> int:
    return sum(i * i for i in range(n))

if __name__ == "__main__":   # Required on Windows — guards against infinite spawning
    numbers = [10_000_000] * 4

    start = time.perf_counter()
    with ProcessPoolExecutor() as executor:
        # By default uses cpu_count() workers
        results = list(executor.map(cpu_task, numbers))
    print(f"Done in {time.perf_counter() - start:.2f}s")
    print(results)
```

The `if __name__ == "__main__":` guard is **mandatory** on Windows. Without it, each spawned process re-imports the main module and recursively spawns more processes.

#### Low-Level `multiprocessing.Pool`

```python
from multiprocessing import Pool

def process_chunk(chunk: list[int]) -> int:
    return sum(chunk)

if __name__ == "__main__":
    data = list(range(1_000_000))
    chunk_size = len(data) // 4
    chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]

    with Pool(processes=4) as pool:
        partial_sums = pool.map(process_chunk, chunks)
    print(sum(partial_sums))   # 499999500000
```

#### Sharing State Between Processes

Processes do **not** share memory by default — data is pickled and copied when passed to workers. Avoid shared state; prefer returning results. When you truly need shared state, use `multiprocessing.Value` and `multiprocessing.Array`:

```python
from multiprocessing import Process, Value, Lock

def increment(counter, lock, n):
    for _ in range(n):
        with lock:
            counter.value += 1

if __name__ == "__main__":
    counter = Value("i", 0)    # shared integer (typecode "i")
    lock = Lock()

    processes = [Process(target=increment, args=(counter, lock, 10_000)) for _ in range(4)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()

    print(counter.value)   # 40000
```

#### `multiprocessing.Queue` for Communication

For producer-consumer patterns between processes:

```python
from multiprocessing import Process, Queue

def producer(q: Queue):
    for i in range(5):
        q.put(i)
    q.put(None)   # sentinel

def consumer(q: Queue):
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Processing {item}")

if __name__ == "__main__":
    q = Queue()
    p1 = Process(target=producer, args=(q,))
    p2 = Process(target=consumer, args=(q,))
    p1.start(); p2.start()
    p1.join(); p2.join()
```

#### Performance Considerations

- **Startup cost** — spawning a process is expensive (tens of milliseconds). Only worth it for tasks that take seconds, not microseconds.
- **Serialization cost** — all arguments and results are pickled. Large data (big NumPy arrays) can negate the parallelism benefit. Use `shared_memory` (Python 3.8+) for large arrays.
- **Rule of thumb** — pool size = `os.cpu_count()` for CPU-bound; I/O-bound tasks don't benefit from more processes.

---

<a id="free-threading-python-3-13"></a>

### Free-Threading (Python 3.13+)

Free-threading is one of the biggest recent changes in CPython, but it should be approached as an evolving runtime option, not as a blanket replacement for every concurrency strategy. The model is promising, but the ecosystem is still adapting.

This page is meant to help you understand what changes conceptually once the GIL is removed and what practical cautions still remain.

#### The Experimental GIL-Free Build

Python 3.13 ships with an **experimental free-threaded build** that removes the GIL, allowing Python threads to execute genuinely in parallel on multiple CPU cores. This is the most significant change to CPython's threading model in its history.

The free-threaded build is opt-in: download `python3.13t` (the `t` suffix means free-threaded). The standard `python3.13` still has the GIL.

```bash
### Check if running in free-threaded mode
python3.13t -c "import sys; print(sys._is_gil_enabled())"   # False
python3.13  -c "import sys; print(sys._is_gil_enabled())"   # True
```

#### CPU Parallelism with Threads

Without the GIL, CPU-bound threads genuinely run in parallel:

```python
import threading
import time

def cpu_task(n: int) -> int:
    return sum(i * i for i in range(n))

### In standard CPython: ~4x slower than single thread (GIL overhead)
### In free-threaded 3.13t: ~4x faster than single thread (true parallelism)
start = time.perf_counter()
results = []
lock = threading.Lock()

def run(n):
    value = cpu_task(n)
    with lock:
        results.append(value)

threads = [threading.Thread(target=run, args=(10_000_000,)) for _ in range(4)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"{time.perf_counter() - start:.2f}s")
```

#### Thread Safety Implications

Removing the GIL does **not** make Python thread-safe. It means you must now be more careful about concurrent access to shared data structures, because the GIL previously provided implicit synchronization for many operations.

```python
### UNSAFE in free-threaded mode — concurrent list mutation
shared = []

def appender():
    for i in range(10_000):
        shared.append(i)   # not atomic without GIL

### SAFE — use a lock
lock = threading.Lock()

def safe_appender():
    for i in range(10_000):
        with lock:
            shared.append(i)
```

Python's built-in types (`dict`, `list`, `set`) are being made internally thread-safe for 3.13+, but complex compound operations (read-modify-write) still require explicit synchronization.

#### Compatibility Status

- **Pure Python code** works as-is in free-threaded mode.
- **C extensions** must be explicitly marked as supporting free-threading (`Py_TPFLAGS_DEFAULT` → `Py_GIL_DISABLED`). Many popular packages (NumPy, Cython) are working on compatibility.
- Check https://py-free-threading.github.io/ for a compatibility matrix of popular packages.

#### When to Use Free-Threading

Free-threading is experimental in 3.13 and will stabilize over the 3.14-3.15 cycle. For production workloads now, prefer `multiprocessing` for CPU parallelism. Follow free-threading for projects targeting future Python versions where it becomes stable.

> **Note**: Free-threading is experimental in 3.13. Extension modules must be updated to be thread-safe. Performance characteristics are still evolving.

---

<a id="concurrency-decision-matrix"></a>

### Concurrency Decision Matrix

This page helps you choose the right concurrency tool based on your workload.

#### Which Tool for Which Problem?

| Workload Type | Recommended Tool | Reason |
|---------------|-----------------|--------|
| Many I/O operations, high concurrency | `asyncio` | Single thread, no OS overhead, scales to thousands of connections |
| I/O-bound, existing sync code | `threading` / `ThreadPoolExecutor` | GIL released during I/O, simpler than rewriting async |
| CPU-bound computation | `multiprocessing` / `ProcessPoolExecutor` | Each process bypasses the GIL |
| CPU-bound, Python 3.13+ | free-threading (`python3.13t`) | True parallelism without process overhead |
| Mixed: async event loop + CPU work | `asyncio` + `run_in_executor` | Offloads blocking code without freezing the event loop |

#### The `run_in_executor` Pattern

The most common pattern for mixing `asyncio` with blocking code:

```python
import asyncio
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time

def blocking_io(url: str) -> str:
    time.sleep(1)   # simulates blocking I/O (legacy library)
    return f"Data from {url}"

def cpu_heavy(n: int) -> int:
    return sum(i * i for i in range(n))

async def main():
    loop = asyncio.get_running_loop()

    # Run blocking I/O in a thread pool — doesn't block the event loop
    with ThreadPoolExecutor(max_workers=5) as thread_pool:
        result = await loop.run_in_executor(thread_pool, blocking_io, "https://api.example.com")
        print(result)

    # Run CPU-bound work in a process pool — true parallelism
    with ProcessPoolExecutor() as process_pool:
        result = await loop.run_in_executor(process_pool, cpu_heavy, 10_000_000)
        print(result)

asyncio.run(main())
```

#### Flow Chart

Use this decision flow when choosing a concurrency strategy:

1. **Is the task I/O-bound or CPU-bound?**
   - If **I/O-bound** → continue to step 2
   - If **CPU-bound** → use `ProcessPoolExecutor` (or free-threading on 3.13t)

2. **Is the codebase async-first or sync-first?**
   - If **async** → use `asyncio` with `await`
   - If **sync** → use `ThreadPoolExecutor`

3. **Do you need to mix async with CPU work?**
   - Use `loop.run_in_executor(ProcessPoolExecutor(), ...)` to offload from the event loop

#### Quick Reference

```python
### asyncio — 1000 concurrent I/O tasks
import asyncio, httpx

async def main():
    async with httpx.AsyncClient() as client:
        responses = await asyncio.gather(
            *[client.get(url) for url in urls]
        )

### ThreadPoolExecutor — blocking I/O
from concurrent.futures import ThreadPoolExecutor
import requests

with ThreadPoolExecutor(max_workers=10) as pool:
    results = list(pool.map(requests.get, urls))

### ProcessPoolExecutor — CPU
from concurrent.futures import ProcessPoolExecutor

with ProcessPoolExecutor() as pool:
    results = list(pool.map(compute, data_chunks))
```

#### Performance Expectations

| Approach | Overhead | Scales to |
|----------|---------|-----------|
| `asyncio` | Very low (coroutine switch ~μs) | Tens of thousands of connections |
| `threading` | Low (OS thread switch ~μs) | Hundreds of threads |
| `multiprocessing` | High (process spawn ~50ms) | CPU count processes |

---

<a id="appendix"></a>

## Appendix

Short pointers for the two domains most readers of this repo care about.

Use this chapter after the core path when you want to map Python concepts to actual work.

### Priority

- Must read after core path: AI & Data Science, Web Development

### Sections

- [AI & Data Science](./docs/appendix/ai-data-science.md)
- [Web Development](./docs/appendix/web-development.md)

---

<a id="ai-data-science"></a>

## AI & Data Science

### The Ecosystem

Python dominates AI and data tooling. A few libraries matter most early:

| Library | Purpose |
|---------|---------|
| `numpy` | Fast multi-dimensional arrays and math |
| `pandas` | Tabular data manipulation (DataFrames) |
| `pytorch` | Deep learning (Meta) — research and production |
| `tensorflow` | Deep learning (Google) — production-focused |
| `langchain` | Build LLM workflows, retrieval pipelines, and agent-style applications |
| `pydantic-ai` | Build AI agents with typed inputs, outputs, and validation |

Install only what you need:

```bash
pip install numpy pandas langchain pydantic-ai
```

### NumPy — Fast Arrays

NumPy arrays are the foundation of scientific Python and vectorized math.

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
matrix = np.zeros((3, 4))          # 3x4 matrix of zeros

print(arr * 2)          # array([2, 4, 6, 8, 10])
print(arr ** 2)         # array([ 1,  4,  9, 16, 25])
print(arr[arr > 2])     # array([3, 4, 5])  — boolean indexing

print(arr.mean())       # 3.0
print(arr.sum())        # 15

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(a @ b)            # matrix multiply: [[19, 22], [43, 50]]
```

### Pandas — DataFrames

Pandas is the default tool for tabular data:

```python
import pandas as pd

df = pd.DataFrame({
    "name":   ["Alice", "Bob", "Carol", "Dave"],
    "dept":   ["Eng",   "HR",  "Eng",   "HR"],
    "salary": [90_000,  60_000, 95_000, 65_000],
    "years":  [3, 7, 5, 2],
})

print(df.head())            # first 5 rows
print(df["name"])           # column → Series
print(df[["name", "salary"]])  # multiple columns → DataFrame
print(df[df["salary"] > 70_000])  # filter rows

df["bonus"] = df["salary"] * 0.1     # new column
dept_stats = df.groupby("dept")["salary"].agg(["mean", "max", "count"])
print(dept_stats)
```

### LangChain — LLM Workflows

LangChain helps connect prompts, models, tools, and retrieval into larger LLM workflows.

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a concise Python tutor."),
    ("human", "Explain {topic} in 3 short bullet points."),
])

model = ChatOpenAI(model="gpt-4o-mini")
chain = prompt | model

response = chain.invoke({"topic": "Python decorators"})
print(response.content)
```

### PydanticAI — Typed AI Agents

PydanticAI is useful when you want model output to match a Python schema.

```python
from dataclasses import dataclass

from pydantic_ai import Agent

@dataclass
class StudyPlan:
    topic: str
    difficulty: str
    next_step: str

agent = Agent(
    "openai:gpt-4o-mini",
    output_type=StudyPlan,
    system_prompt="You create short Python study plans.",
)

result = agent.run_sync("Create a beginner study plan for list comprehensions.")
print(result.output)
```

For AI work, the practical Python stack is usually: JSON, HTTP clients, type hints, async basics, and one or two AI libraries rather than every data-science tool at once.

---

<a id="web-development"></a>

## Web Development

### The Landscape

Python has mature frameworks for APIs and full web apps:

| Framework | Best For |
|-----------|---------|
| `FastAPI` | Modern async REST APIs with auto-generated docs |
| `Flask` | Simple web apps and APIs, minimal overhead |
| `Django` | Full-stack web apps — ORM, admin, auth, templates |
| `Starlette` | Lightweight async framework (FastAPI is built on it) |
| `aiohttp` | Async web server and client |

### FastAPI — Modern APIs

FastAPI is a strong default for new APIs because it uses type hints, validates data, and generates docs automatically.

```bash
pip install fastapi uvicorn[standard]
uvicorn main:app --reload   # auto-reloads on file save
```

```python
## main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="My API", version="1.0.0")

users: dict[int, dict] = {}
next_id = 1

class UserCreate(BaseModel):
    name: str
    email: str
    age: Optional[int] = None

class UserResponse(UserCreate):
    id: int

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return users[user_id]

@app.post("/users", response_model=UserResponse, status_code=201)
def create_user(user: UserCreate):
    global next_id
    new_user = {"id": next_id, **user.model_dump()}
    users[next_id] = new_user
    next_id += 1
    return new_user

@app.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    del users[user_id]
```

Open `/docs` to use the generated API explorer.

### Flask — Minimal Web

Flask is minimal and easy to start with:

```bash
pip install flask
```

```python
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

tasks = [{"id": 1, "title": "Buy groceries", "done": False}]

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task is None:
        abort(404)
    return jsonify(task)

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json(force=True)
    task = {"id": len(tasks) + 1, "title": data["title"], "done": False}
    tasks.append(task)
    return jsonify(task), 201

if __name__ == "__main__":
    app.run(debug=True)
```

### Django — Full Stack

Django is full-stack and includes an ORM, admin panel, auth, and templating.

```bash
pip install django
django-admin startproject mysite
python manage.py startapp blog
python manage.py runserver
```

```python
## blog/models.py
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    published = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-published"]

    def __str__(self):
        return self.title

## blog/views.py
from django.http import JsonResponse
from .models import Post

def post_list(request):
    posts = list(Post.objects.values("id", "title", "published"))
    return JsonResponse(posts, safe=False)
```

### Choosing a Framework

- **New REST API** → FastAPI (async, type-safe, auto-docs)
- **Simple script/prototype** → Flask (minimal setup)
- **Complex web application** → Django (ORM, admin, auth, form validation all included)

---

<a id="support"></a>

## Support

If you like my work, feel free to:

- ⭐ this repository. And we will be happy together :)

Thanks a bunch for supporting me!

<a id="contribution"></a>

## Contribution

Thanks to all [contributors](https://github.com/meysamhadeli/learn-python/graphs/contributors), you're awesome and this wouldn't be possible without you!

Please follow this [contribution guideline](./CONTRIBUTION.md) to submit a pull request or create the issue.

<a id="project-references"></a>

## Project References

- [Official Python Docs](https://docs.python.org/3/)
- [FastAPI Tutorial](https://fastapi.tiangolo.com/)
- [Python Type Hints Cheat Sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)
