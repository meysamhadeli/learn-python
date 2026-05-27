# Learn Python

> Welcome! This repo will take you from zero to confident in Python, with step-by-step lessons, plain‑language explanations, and real code examples that you can run right away.


- **Documentation site** — the full content is published at **[learn-python-dev.netlify.app](https://learn-python-dev.netlify.app/)** with a sidebar, search, and per-chapter navigation.

- **Interactive notebook** — [learn-python.ipynb](learn-python.ipynb) in VS Code lets you run and edit every code block inline.

# Table of Contents

- [Getting Started](#getting-started)
    - [What is Python?](#what-is-python)
    - [Why learn Python?](#why-learn-python)
    - [Installation and Setup](#installation-and-setup)
- [Chapter I: The Basics](#chapter-i-the-basics)
    - [Hello World](#hello-world)
    - [Variables](#variables)
    - [Built-in Data Types](#built-in-data-types)
    - [String Formatting](#string-formatting)
    - [Operators](#operators)
    - [Falsy Values](#falsy-values)
- [Chapter II: Data Structures](#chapter-ii-data-structures)
    - [Lists](#lists)
    - [Tuples](#tuples)
    - [Dictionaries](#dictionaries)
    - [Sets](#sets)
    - [Collections Module](#collections-module)
    - [Comprehensions](#comprehensions)
    - [Type Conversion](#type-conversion)
- [Chapter III: Control Flow](#chapter-iii-control-flow)
    - [If/Else](#ifelse)
    - [Match/Case](#matchcase-python-310)
    - [Loops](#loops)
- [Chapter IV: Functions](#chapter-iv-functions)
    - [Defining Functions](#defining-functions)
    - [Parameters & Arguments](#parameters--arguments)
    - [Lambda Functions](#lambda-functions)
    - [Scoping Rules](#scoping-rules-legb)
    - [Type Hints](#type-hints)
- [Chapter V: Modules, Packages & Environment](#chapter-v-modules-packages--environment)
    - [Modules](#modules)
    - [Packages](#packages)
    - [Virtual Environments](#virtual-environments)
    - [File I/O & JSON](#file-io--json)
    - [Useful Commands](#useful-commands)
    - [Build & Packaging](#build--packaging)
- [Chapter VI: Object-Oriented Python](#chapter-vi-object-oriented-python)
    - [Classes](#classes)
    - [Inheritance](#inheritance)
    - [Abstract Base Classes](#abstract-base-classes)
    - [Magic Methods](#magic-methods)
    - [Dataclasses](#dataclasses)
- [Chapter VII: Errors & Exceptions](#chapter-vii-errors--exceptions)
- [Chapter VIII: Pythonic Patterns](#chapter-viii-pythonic-patterns)
    - [Iterators & Generators](#iterators--generators)
    - [itertools & functools](#itertools--functools)
    - [Decorators](#decorators)
    - [Context Managers](#context-managers)
    - [Pattern Matching](#pattern-matching-python-310)
- [Chapter IX: Concurrency](#chapter-ix-concurrency)
    - [The GIL](#the-gil-global-interpreter-lock)
    - [Async/Await](#asyncawait)
    - [Threading](#threading-for-io-bound-tasks)
    - [Multiprocessing](#multiprocessing-for-cpu-bound-work)
    - [Free-Threading](#free-threading-python-313)
    - [Decision Matrix](#decision-matrix-for-2026)
- [Appendix: What's Next](#appendix-whats-next)
    - [AI & Data Science](#ai--data-science)
    - [Web Development](#web-development)
- [Support](#support)
- [Contribution](#contribution)
- [Project References](#project-references)

---

# Getting Started

## What is Python?

Python is a high-level, interpreted language created by Guido van Rossum in 1991. It reads like plain English, runs everywhere, and is the #1 language for AI, data science, and backend web development.

## Why learn Python?

**Short answer:** Python is the language of AI — and it's also great for web backends.

- **AI/ML**: PyTorch, TensorFlow, Hugging Face, LangChain, OpenAI SDK — all Python-first.
- **Web**: FastAPI (async, high-performance), Django (batteries-included), powers Instagram & Spotify.
- **Ecosystem**: 300,000+ packages on PyPI for everything from scraping to DevOps.
- **Jobs**: Python skills are in massive demand and only growing with the AI boom.

Let's get into it.

## Installation and Setup

In this tutorial, we will install Python and set up our code editor.

### Download

We can install Python from the [official downloads section](https://www.python.org/downloads/).

### Installation

_These instructions are from the official website._

#### macOS

1. Open the package file you downloaded and follow the prompts to install Python.
2. Verify that you've installed Python by opening a terminal and typing:

```bash
python3 --version
```

3. Confirm that the command prints the installed version of Python (e.g., `Python 3.13.0`).

#### Linux

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

Verify:

```bash
python3 --version
```

#### Windows

1. Open the executable file you downloaded.
2. **Important:** Check the box that says "Add Python to PATH".
3. Click "Install Now".
4. Verify by opening Command Prompt:

```bash
python --version
```

### VS Code

In this course, I will be using VS Code. You can download it from [code.visualstudio.com](https://code.visualstudio.com/).

_Feel free to use any other code editor you prefer._

### Extension

Make sure to install the **Python extension** by Microsoft. It provides IntelliSense, linting, debugging, and more.

This is it for the installation and setup of Python. Let's start the course and write our first hello world!


---

# Chapter I: The Basics

## Hello World

Let's write our first hello world program.

Create a new file called `main.py`:

```python
print("Hello World!")
```

Run it:

```bash
python main.py
```

```
Hello World!
```

### Structure of a Python program

```python
def main():
    print("Hello World!")

if __name__ == "__main__":
    main()
```

- `def main():` defines a function named `main`.
- `if __name__ == "__main__":` ensures this runs only when executed directly, not when imported.

## Variables

Python is dynamically typed — no need to declare types.

```python
# Simple assignment
name = "Python"
version = 3.13
is_awesome = True

# Multiple assignment
x, y, z = 1, 2.5, "three"

# Constants (UPPER_CASE by convention — Python doesn't enforce this)
MAX_CONNECTIONS = 100
```

## Built-in Data Types

### int

Python integers have arbitrary precision — no overflow, no size limit, no casting to `long`.

```python
count = 42
big_number = 10 ** 100  # Python handles arbitrarily large integers
```

### float

Double-precision float — watch out for imprecision: `0.1 + 0.2 != 0.3`.

```python
pi = 3.14159
small = 1.5e-4  # 0.00015
```

### complex

Built-in support for complex numbers — used in signal processing, scientific computing, and some AI/ML math.

```python
c = 3 + 4j
print(c.real)  # 3.0
print(c.imag)  # 4.0
print(abs(c))  # 5.0 (magnitude)
```

### str (String)

Strings are immutable sequences of Unicode characters — indexable, sliceable, and packed with built-in methods.

```python
single = 'Hello'
double = "World"
multiline = """This is
a multiline string"""

raw = r"C:\Users\Name"  # Raw string — backslashes are literal

text = "Python"
print(text[0])   # 'P'
print(text[-1])  # 'n'
print(len(text)) # 6
```

### bool

A subclass of `int` — `True == 1` and `False == 0`, so booleans work in arithmetic and can be summed.

```python
is_ready = True
is_done = False
is_adult = age >= 18  # Boolean from comparison
```

### None

Python's null value — always compare with `is None`, not `== None`.

```python
result = None

if result is None:
    print("No result")
```

## String Formatting

f-strings are the recommended way to format strings in Python.

```python
name = "Python"
year = 2026

print(f"Hello {name}, version {year}")  # Hello Python, version 2026

# Expressions inside {}
print(f"Result: {10 + 20}")
print(f"Length: {len([1, 2, 3])}")

# Formatting numbers
pi = 3.14159
print(f"Pi: {pi:.2f}")          # Pi: 3.14
print(f"Padded: {42:05d}")      # Padded: 00042

# Dict values in f-strings
person = {"name": "Alice", "age": 30}
print(f"{person['name']} is {person['age']} years old")
```

## Operators

Python's operator set is mostly familiar, with a few useful additions: floor division `//`, power `**`, membership `in`, and the walrus `:=`.

### Arithmetic

| Operator | Example | Result |
|----------|---------|--------|
| `+` `-` `*` | `5 + 3` | `8` |
| `/` | `5 / 2` | `2.5` |
| `//` | `5 // 2` | `2` (floor) |
| `%` | `5 % 2` | `1` (remainder) |
| `**` | `5 ** 2` | `25` (power) |

### Comparison & Logical

Python uses `and`, `or`, `not` instead of `&&`, `||`, `!` — and supports chained comparisons like `0 < x < 10`.

```python
x = 7
print(x > 5 and x < 10)   # True
print(x > 10 or x < 5)    # False
print(not x == 7)          # False
```

### Assignment Shortcuts

Shorthand for updating a variable in place — `x += 5` is equivalent to `x = x + 5`.

```python
x = 10
x += 5   # x = 15
x -= 3   # x = 12
x *= 2   # x = 24
x /= 4   # x = 6.0
```

### Membership

Tests presence in a sequence, dict (by key), or set — O(1) for dicts and sets, O(n) for lists.

```python
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)   # True
print("grape" not in fruits) # True

person = {"name": "Alice"}
print("name" in person)     # True (checks keys)
```

### Walrus Operator `:=` (Python 3.8+)

Assigns a value and returns it in the same expression — removes redundant calls.

```python
# Avoid computing len() twice
data = [1, 2, 3, 4, 5]
if (n := len(data)) > 3:
    print(f"List is long: {n} items")  # List is long: 5 items

# Cleaner while loops (e.g. reading chunks from a file)
with open("file.txt", "rb") as f:
    while chunk := f.read(8192):
        process(chunk)

# In comprehensions — compute once, filter and use
results = [y for x in data if (y := x * 2) > 4]
```

## Falsy Values

These values evaluate to `False` in a boolean context — everything else is `True`:

- `None`, `False`, `0`, `0.0`
- `""` (empty string), `[]` (empty list), `()` (empty tuple), `{}` (empty dict), `set()`

```python
my_list = []
if my_list:
    print("Has items")
else:
    print("Empty")  # This prints

# Useful for checking optional values
response = None
data = response or "default"  # "default"
```

---

# Chapter II: Data Structures

## Lists

An ordered, **mutable** collection.

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])    # apple
print(fruits[-1])   # cherry
print(fruits[1:3])  # ['banana', 'cherry']

fruits.append("date")         # Add to end
fruits.insert(1, "blueberry") # Insert at index
fruits.remove("banana")       # Remove by value
popped = fruits.pop()         # Remove and return last

fruits.sort()    # Sort in-place
fruits.reverse() # Reverse in-place
```

## Tuples

An ordered, **immutable** collection. Great for fixed data and dictionary keys.

```python
point = (10, 20)
x, y = point        # Unpacking: x=10, y=20

# Tuple as dict key (lists cannot do this)
locations = {(40.7128, -74.0060): "New York"}
```

## Dictionaries

Key-value pairs — the workhorse of Python data handling.

```python
person = {"name": "Alice", "age": 30, "city": "New York"}

print(person["name"])                 # Alice (raises KeyError if missing)
print(person.get("email", "N/A"))     # N/A (safe access)

person["age"] = 31                    # Update
person["email"] = "alice@example.com" # Add new key
person.update({"city": "Boston"})

del person["city"]
age = person.pop("age")

for key, value in person.items():
    print(f"{key}: {value}")
```

## Sets

An unordered collection of **unique** elements.

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a | b   # Union: {1, 2, 3, 4, 5, 6}
a & b   # Intersection: {3, 4}
a - b   # Difference: {1, 2}
a ^ b   # Symmetric difference: {1, 2, 5, 6}

# Remove duplicates from a list
nums = [1, 2, 2, 3, 3, 4]
unique = list(set(nums))  # [1, 2, 3, 4]
```

## Collections Module

The `collections` module extends Python's built-in data structures with specialized containers that solve common problems more cleanly.

```python
from collections import defaultdict, Counter, deque

# defaultdict — like a regular dict but never raises KeyError;
# the factory function provides a default value on first access
word_count = defaultdict(int)
for word in ["apple", "banana", "apple", "cherry", "apple"]:
    word_count[word] += 1
# defaultdict(<class 'int'>, {'apple': 3, 'banana': 1, 'cherry': 1})

grouped = defaultdict(list)
for name, dept in [("Alice", "Eng"), ("Bob", "Eng"), ("Carol", "HR")]:
    grouped[dept].append(name)
# {'Eng': ['Alice', 'Bob'], 'HR': ['Carol']}

# Counter — counts occurrences and supports arithmetic between counts
votes = Counter(["alice", "bob", "alice", "alice", "bob"])
print(votes.most_common(2))   # [('alice', 3), ('bob', 2)]
print(votes["alice"])         # 3
print(votes["unknown"])       # 0 (no KeyError)

letters = Counter("mississippi")
print(letters)  # Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})

# deque — doubly-linked list; O(1) appends and pops from both ends
# (list.insert(0, x) is O(n) — deque fixes that)
queue = deque([1, 2, 3])
queue.appendleft(0)   # [0, 1, 2, 3]
queue.append(4)        # [0, 1, 2, 3, 4]
queue.popleft()        # 0  → queue is now [1, 2, 3, 4]
queue.rotate(1)        # [4, 1, 2, 3]  (rotate right by 1)

# Bounded deque — automatically discards oldest items
recent = deque(maxlen=3)
for i in range(5):
    recent.append(i)
print(recent)  # deque([2, 3, 4], maxlen=3)
```

## Comprehensions

A concise and Pythonic way to build collections.

```python
# List comprehension
squares = [x**2 for x in range(10)]
even_squares = [x**2 for x in range(10) if x % 2 == 0]

# Conditional expression
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]

# Flatten a matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]

# Set comprehension
unique_lens = {len(word) for word in ["hi", "hello", "hi"]}
# {2, 5}

# Dict comprehension
word_lens = {word: len(word) for word in ["hi", "hello"]}
# {'hi': 2, 'hello': 5}
```

## Type Conversion

Explicit conversion with built-in functions — `int + float` auto-promotes, but `"text" + 42` raises a `TypeError`.

```python
int("123")        # 123
float("3.14")     # 3.14
str(42)           # "42"
bool(1)           # True
int(3.99)         # 3 (truncates, not rounds!)

list((1, 2, 3))   # [1, 2, 3]
tuple([1, 2, 3])  # (1, 2, 3)
set([1, 2, 2, 3]) # {1, 2, 3}

result = 5 + 2.5  # 7.5 (int auto-converts to float)
message = "Count: " + str(42)
```

---

# Chapter III: Control Flow

## If/Else

Python uses **indentation** (4 spaces) to define blocks.

```python
x = 10

if x > 5:
    print("greater than 5")
elif x == 5:
    print("equals 5")
else:
    print("less than 5")

# Ternary (one-liner)
status = "Adult" if x >= 18 else "Minor"
```

## Match/Case (Python 3.10+)

The modern `switch` — especially useful for handling API responses or commands.

```python
def check_status(code):
    match code:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500 | 502 | 503:
            return "Server Error"
        case _:
            return "Unknown"
```

Match also works on dicts — great for JSON payloads:

```python
def handle_response(response):
    match response:
        case {"status": 200, "data": data}:
            return f"Success: {data}"
        case {"status": 404}:
            return "Not found"
        case {"status": 500, "error": err}:
            return f"Server error: {err}"
        case _:
            return "Unknown response"
```

## Loops

Python has `for` and `while` loops — both support an `else` clause that runs only if no `break` occurred.

```python
# For loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

for i in range(2, 10, 2):  # 2, 4, 6, 8
    print(i)

for index, value in enumerate(fruits):
    print(f"{index}: {value}")

# While loop
count = 0
while count < 3:
    print(count)
    count += 1

# break / continue
for i in range(10):
    if i % 2 == 0:
        continue   # skip evens
    if i > 7:
        break      # stop loop
    print(i)       # 1, 3, 5, 7

# else on a loop — runs if no break occurred
for fruit in fruits:
    if fruit == "orange":
        break
else:
    print("Not found")
```

---

# Chapter IV: Functions

## Defining Functions

Defined with `def`, returning values with `return` — functions are first-class objects you can pass and store like any other value.

```python
def greet(name):
    print(f"Hello, {name}")

greet("Alice")  # Hello, Alice
```

## Parameters & Arguments

Default values, keyword args, and `*args`/`**kwargs` cover every calling convention — no function overloading needed.

```python
# Default arguments
def power(base, exp=2):
    return base ** exp

print(power(5))      # 25
print(power(2, 3))   # 8

# Avoid mutable defaults — use None instead
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

# Keyword arguments (order doesn't matter)
def describe(name, age, city):
    print(f"{name}, {age}, {city}")

describe(city="Paris", name="Alice", age=30)

# *args and **kwargs
def sum_all(*args):
    return sum(args)

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30)

# Multiple return values (returned as a tuple)
def get_user():
    return "Alice", 30

name, age = get_user()
```

## Lambda Functions

Anonymous single-expression functions — great for sorting and callbacks.

```python
square = lambda x: x ** 2
print(square(5))  # 25

points = [(1, 2), (3, 1), (5, -1)]
points.sort(key=lambda p: p[1])  # Sort by y-coordinate

numbers = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, numbers))  # [2, 4]
```

## Scoping Rules (LEGB)

Python resolves names by searching four scopes in order: **L**ocal → **E**nclosing → **G**lobal → **B**uilt-in.

```python
x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)   # local   ← found in Local scope first

    inner()
    print(x)       # enclosing

outer()
print(x)           # global
```

```python
# global — modify a module-level variable from inside a function
count = 0

def increment():
    global count   # without this, count += 1 raises UnboundLocalError
    count += 1

increment()
print(count)  # 1

# nonlocal — modify an enclosing (but non-global) variable
def make_counter():
    n = 0

    def step():
        nonlocal n  # binds to the enclosing n, not a new local
        n += 1
        return n

    return step

counter = make_counter()
print(counter())  # 1
print(counter())  # 2
print(counter())  # 3
```

> **Rule of thumb:** Avoid `global` in real code — prefer returning values or using classes to hold state. `nonlocal` is fine inside closures and factory functions.

## Type Hints

Type hints make code self-documenting and enable IDE autocompletion and tools like `mypy`.

```python
def greet(name: str) -> str:
    return f"Hello, {name}"

age: int = 30
names: list[str] = ["Alice", "Bob"]

# Union types (Python 3.10+)
def parse(value: int | str) -> float:
    return float(value)

# Optional return
def find_user(id: int) -> dict | None:
    if id == 1:
        return {"name": "Alice"}
    return None

# TypedDict for structured dicts
from typing import TypedDict

class User(TypedDict):
    name: str
    age: int

def process_user(user: User) -> None:
    print(f"Processing {user['name']}")

# Generics (Python 3.12+)
def first[T](items: list[T]) -> T:
    return items[0]
```

---

# Chapter V: Modules, Packages & Environment

## Modules

A module is simply a Python file.

```python
# mymodule.py
def helper():
    return "Help from module"

PI = 3.14159
```

```python
import mymodule
print(mymodule.helper())

from mymodule import helper, PI
import mymodule as mm

# Runs only when executed directly
if __name__ == "__main__":
    print("Running as script")
```

### Standard Library Highlights

Python ships with an extensive standard library — these are the modules you'll reach for constantly without installing anything.

```python
import math, random, datetime, os, sys

print(math.sqrt(16))           # 4.0
print(random.randint(1, 10))   # random int
print(datetime.datetime.now()) # current datetime
print(os.getcwd())             # current directory
print(sys.version)             # Python version
```

## File I/O & JSON

File I/O and JSON are from Python docs chapter 7 — essential for any backend or data work.

```python
# Writing a file
with open("data.txt", "w", encoding="utf-8") as f:
    f.write("Hello, Python!\n")

# Reading a file
with open("data.txt", encoding="utf-8") as f:
    content = f.read()       # entire file as string

# Reading line by line (memory-efficient)
with open("data.txt", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
```

JSON is the universal data format for APIs — use the built-in `json` module:

```python
import json

# Python dict → JSON string
user = {"name": "Alice", "age": 30, "roles": ["admin", "user"]}
json_str = json.dumps(user, indent=2)
print(json_str)

# JSON string → Python dict
parsed = json.loads(json_str)
print(parsed["name"])  # Alice

# Write JSON to file
with open("user.json", "w", encoding="utf-8") as f:
    json.dump(user, f, indent=2)

# Read JSON from file
with open("user.json", encoding="utf-8") as f:
    data = json.load(f)
```

> **Note:** Prefer `json` over `pickle` for interoperability. `pickle` is Python-only and unsafe with untrusted data.

## Packages

A package is a directory with an `__init__.py` file.

```
mypackage/
    __init__.py
    module1.py
    module2.py
```

```python
# __init__.py
from .module1 import hello
```

```python
from mypackage import hello
print(hello())
```

## Virtual Environments

Every Python project should have its own virtual environment to isolate dependencies.

```bash
python -m venv .venv
```

Activate:
- **Windows**: `.venv\Scripts\activate`
- **macOS/Linux**: `source .venv/bin/activate`

You'll see `(.venv)` in your terminal prompt. Run `deactivate` to exit.

```bash
pip install requests
pip freeze > requirements.txt    # Save
pip install -r requirements.txt  # Restore
```

## Useful Commands

A quick reference for running scripts, managing packages, and checking code quality from the terminal.

```bash
# Run
python script.py
python -m module_name

# Packages
pip install package
pip uninstall package
pip list

# Code quality
pip install ruff mypy
ruff check script.py   # Fast linter
mypy script.py         # Type checker
```

## Build & Packaging

`pyproject.toml` is the modern standard for defining a Python package — replacing `setup.py` and `setup.cfg`. It declares metadata, dependencies, build backend, and CLI entry points in one file.

```toml
# pyproject.toml — the modern way to define a Python package
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "myapp"
version = "0.1.0"
requires-python = ">=3.10"
dependencies = ["fastapi>=0.100.0"]

[project.scripts]
myapp-cli = "myapp.cli:main"
```

```
myproject/
├── pyproject.toml
├── src/
│   └── mypackage/
│       ├── __init__.py
│       └── main.py
└── tests/
    └── test_main.py
```

---

# Chapter VI: Object-Oriented Python

## Classes

Classes bundle data and behavior — `__init__` is the constructor, `self` is the explicit reference to the current instance.

```python
class Person:
    species = "Homo sapiens"  # Class variable

    def __init__(self, name: str, age: int):
        self.name = name
        self._age = age        # Protected by convention

    def greet(self) -> str:
        return f"Hi, I'm {self.name}"

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

    @staticmethod
    def is_adult(age: int) -> bool:
        return age >= 18

    @classmethod
    def from_birth_year(cls, name: str, year: int):
        return cls(name, 2026 - year)

alice = Person("Alice", 30)
print(alice.greet())           # Hi, I'm Alice
print(Person.is_adult(20))     # True
bob = Person.from_birth_year("Bob", 1995)
```

## Inheritance

Inheritance lets you build on existing classes, keeping your code DRY.

```python
class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        raise NotImplementedError

class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self) -> str:
        return f"{self.name} says Meow!"

animals = [Dog("Rex"), Cat("Whiskers")]
for animal in animals:
    print(animal.speak())
# Rex says Woof!
# Whiskers says Meow!

# Use super() to call the parent constructor
class Employee(Person):
    def __init__(self, name: str, age: int, role: str):
        super().__init__(name, age)
        self.role = role
```

## Abstract Base Classes

ABCs define a required interface — any subclass that doesn't implement all `@abstractmethod` methods raises a `TypeError` at instantiation time, catching missing implementations early.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    """Any shape must know its area and perimeter."""

    @abstractmethod
    def area(self) -> float: ...

    @abstractmethod
    def perimeter(self) -> float: ...

    # Concrete method shared by all subclasses
    def describe(self) -> str:
        return f"{type(self).__name__}: area={self.area():.2f}"

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return 3.14159 * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * 3.14159 * self.radius

class Rectangle(Shape):
    def __init__(self, w: float, h: float):
        self.w, self.h = w, h

    def area(self) -> float:
        return self.w * self.h

    def perimeter(self) -> float:
        return 2 * (self.w + self.h)

# Shape()  →  TypeError: Can't instantiate abstract class
circle = Circle(5)
print(circle.describe())     # Circle: area=78.54
print(circle.perimeter())    # 31.4159

shapes: list[Shape] = [Circle(3), Rectangle(4, 5)]
for s in shapes:
    print(s.area())          # polymorphic — each shape uses its own formula
```

> ABCs are the Python equivalent of interfaces in Java/C#. They're common in larger codebases and libraries where you define a plugin or strategy contract.

## Magic Methods

Magic methods let your objects behave like built-in types.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1 + p2)   # (4, 6)
print(p1 == p2)  # False
```

## Dataclasses

Dataclasses auto-generate `__init__`, `__repr__`, and `__eq__` — less boilerplate.

```python
from dataclasses import dataclass, field

@dataclass
class Person:
    name: str
    age: int
    tags: list[str] = field(default_factory=list)

p = Person("Alice", 30)
print(p)  # Person(name='Alice', age=30, tags=[])
```

---

# Chapter VII: Errors & Exceptions

## Exception Hierarchy

All exceptions inherit from `BaseException`. The ones you normally handle inherit from `Exception`:

```
BaseException
├── SystemExit
├── KeyboardInterrupt
├── GeneratorExit
└── Exception
    ├── TypeError
    ├── ValueError
    ├── NameError
    ├── AttributeError
    ├── IndexError
    ├── KeyError
    ├── FileNotFoundError
    ├── ZeroDivisionError
    ├── RuntimeError
    └── ...
```

Handle the **most specific** exception type you expect; catching bare `Exception` broadly can hide bugs.

## try / except / else / finally

```python
try:
    value = int(input("Enter number: "))
    result = 100 / value
except ValueError:
    print("Not a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"Unexpected error: {e}")
else:
    print(f"Result: {result}")   # Runs only if no exception was raised
finally:
    print("Cleanup")              # Always runs — even if an exception escapes
```

To catch multiple types in one clause, use a tuple:

```python
try:
    value = int(user_input)
except (ValueError, TypeError) as e:
    print(f"Conversion error: {e}")
```

## Raising Exceptions

```python
def set_age(age: int):
    if not isinstance(age, int):
        raise TypeError(f"age must be int, got {type(age).__name__}")
    if age < 0 or age > 150:
        raise ValueError(f"age must be 0–150, got {age}")
    return age

# Re-raise the current exception (preserve original traceback)
try:
    risky()
except ValueError:
    log_error()
    raise   # re-raises the same ValueError
```

## Exception Chaining

When you raise inside an `except` block, Python links the exceptions with `__cause__`:

```python
try:
    data = json.loads(raw)
except json.JSONDecodeError as e:
    raise ValueError("Could not parse response") from e
    # "The above exception was the direct cause of the following exception"
```

Use `raise ... from None` to suppress chaining and hide the original exception.

## Custom Exceptions

Define custom exception classes to provide richer error information:

```python
class AppError(Exception):
    """Base class for all application errors."""

class InsufficientFundsError(AppError):
    def __init__(self, requested: float, available: float):
        self.requested = requested
        self.available = available
        super().__init__(
            f"Requested {requested:.2f} but only {available:.2f} available"
        )

class AccountLockedError(AppError):
    pass


class BankAccount:
    def __init__(self, balance: float):
        self.balance = balance
        self.locked = False

    def withdraw(self, amount: float) -> float:
        if self.locked:
            raise AccountLockedError("Account is locked")
        if amount > self.balance:
            raise InsufficientFundsError(amount, self.balance)
        self.balance -= amount
        return amount


account = BankAccount(100.0)
try:
    account.withdraw(150.0)
except InsufficientFundsError as e:
    print(e)                      # Requested 150.00 but only 100.00 available
    print(f"Short by: {e.requested - e.available:.2f}")
except AppError as e:
    print(f"App error: {e}")
```

---

# Chapter VIII: Pythonic Patterns

## Iterators & Generators

Generators produce values on demand — memory-efficient for large data.

```python
def fibonacci(limit: int):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

for num in fibonacci(100):
    print(num)  # 0,1,1,2,3,5,8,13,21,34,55,89

# Generator expression (lazy evaluation)
squares_gen = (x**2 for x in range(1_000_000))
print(next(squares_gen))  # 0
print(next(squares_gen))  # 1

# Reading large files line by line
def read_large_file(file_path):
    with open(file_path) as f:
        for line in f:
            yield line.strip()
```

## itertools & functools

`itertools` provides memory-efficient tools for working with iterables. `functools` provides higher-order function utilities. Both are from the standard library — no install needed.

```python
import itertools

# chain — flatten multiple iterables into one stream
combined = list(itertools.chain([1, 2], [3, 4], [5]))
# [1, 2, 3, 4, 5]

# islice — take the first N items from any iterable (including infinite ones)
first_five_evens = list(itertools.islice(itertools.count(0, 2), 5))
# [0, 2, 4, 6, 8]

# product — Cartesian product (nested loops without nesting)
pairs = list(itertools.product("AB", [1, 2]))
# [('A', 1), ('A', 2), ('B', 1), ('B', 2)]

# groupby — group consecutive elements by a key
data = [("Eng", "Alice"), ("Eng", "Bob"), ("HR", "Carol")]
for dept, members in itertools.groupby(data, key=lambda x: x[0]):
    print(dept, [m[1] for m in members])
# Eng ['Alice', 'Bob']
# HR  ['Carol']

# batched (Python 3.12+) — split an iterable into fixed-size chunks
pages = list(itertools.batched(range(10), 3))
# [(0, 1, 2), (3, 4, 5), (6, 7, 8), (9,)]
```

```python
from functools import lru_cache, partial, reduce

# lru_cache — memoize expensive or recursive functions automatically
@lru_cache(maxsize=128)
def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(50))         # instant — results are cached
print(fibonacci.cache_info()) # CacheInfo(hits=48, misses=51, ...)

# partial — freeze some arguments of a function to create a simpler callable
def power(base: float, exp: float) -> float:
    return base ** exp

square = partial(power, exp=2)
cube   = partial(power, exp=3)
print(square(5))  # 25
print(cube(3))    # 27

# reduce — fold a sequence into a single value (left-to-right)
product = reduce(lambda acc, x: acc * x, [1, 2, 3, 4, 5])
print(product)  # 120
```

## Decorators

Decorators wrap functions to add behavior — used everywhere in web frameworks.

```python
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.4f}s")
        return result
    return wrapper

@timer
def slow_function():
    return sum(range(10_000_000))

slow_function()  # slow_function took 0.2345s

# Decorator with arguments
def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return [func(*args, **kwargs) for _ in range(times)]
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    return f"Hello, {name}"

# Real-world example: login guard
def login_required(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if not user.get("logged_in", False):
            raise PermissionError("Login required")
        return func(user, *args, **kwargs)
    return wrapper

@login_required
def view_dashboard(user):
    return "Welcome!"
```

## Context Managers

Context managers handle setup and teardown automatically — no leaking resources.

```python
# Built-in: files
with open("file.txt", "w") as f:
    f.write("Hello")
# File is automatically closed here

# Custom class-based
class DatabaseConnection:
    def __enter__(self):
        self.connection = "connected"
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection = None

with DatabaseConnection() as conn:
    print(f"Using {conn}")

# Function-based with contextlib
from contextlib import contextmanager

@contextmanager
def timer(label):
    import time
    start = time.time()
    try:
        yield
    finally:
        print(f"{label} took {time.time() - start:.4f}s")

with timer("data processing"):
    sum(range(10_000_000))
```

## Pattern Matching (Python 3.10+)

Beyond the basic `match/case` shown in Chapter III — guards add conditional logic to cases, structural matching on dataclasses lets you destructure objects, and sequence patterns match lists or tuples by structure.

```python
# Guards
def classify(n):
    match n:
        case n if n < 0: return "Negative"
        case 0:          return "Zero"
        case _:          return "Positive"

# Matching dataclasses
from dataclasses import dataclass

@dataclass
class Circle:
    radius: float

@dataclass
class Rectangle:
    width: float
    height: float

def area(shape):
    match shape:
        case Circle(radius=r):
            return 3.14159 * r ** 2
        case Rectangle(width=w, height=h):
            return w * h
        case _:
            raise ValueError("Unknown shape")

# Sequence patterns — match lists/tuples by structure
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

print(handle_command("go north"))       # Going north
print(handle_command("go south fast"))  # Going south at fast
```

---

# Chapter IX: Concurrency

## The GIL (Global Interpreter Lock)

The GIL prevents true thread parallelism — for CPU-bound work use multiprocessing, or Python 3.13+ free-threading.

## Async/Await

Async is **single-threaded** but handles thousands of concurrent connections — the right choice for web servers and I/O-heavy apps.

```python
import asyncio

async def say_after(delay, msg):
    await asyncio.sleep(delay)
    print(msg)

async def main():
    # Run concurrently
    await asyncio.gather(
        say_after(1, "Hello"),
        say_after(2, "World")
    )

asyncio.run(main())
```

### Async HTTP (aiohttp)

For HTTP requests inside async code, use `aiohttp` — the standard `urllib`/`requests` libraries are blocking and will stall the event loop.

```python
import aiohttp
import asyncio

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        return await asyncio.gather(*[fetch(session, url) for url in urls])

results = asyncio.run(fetch_all(["https://api.example.com/1", "https://api.example.com/2"]))
```

## Threading (for I/O-bound tasks)

The GIL is released during I/O, so threads work well for moderate I/O workloads with blocking libraries.

```python
from concurrent.futures import ThreadPoolExecutor
import time

def download(url):
    time.sleep(1)
    return f"Data from {url}"

urls = ["a.com", "b.com", "c.com"]
with ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(download, urls))
```

## Multiprocessing (for CPU-bound work)

Bypass the GIL and use all cores for CPU-intensive tasks.

```python
from multiprocessing import Pool

def cpu_intensive(n: int) -> int:
    return sum(i * i for i in range(n))

with Pool(processes=4) as pool:
    results = pool.map(cpu_intensive, [10_000_000] * 4)
```

## Free-Threading (Python 3.13+)

Free-threading makes the GIL optional, allowing threads to run truly in parallel for CPU work.

```python
# Run with a free-threaded Python build
import threading

def cpu_work():
    return sum(range(50_000_000))

threads = [threading.Thread(target=cpu_work) for _ in range(4)]
for t in threads: t.start()
for t in threads: t.join()
```

> **Note:** Free-threading is optional. Most Python installs still use the GIL by default.

## Decision Matrix for 2026

| Workload | Best Tool |
|----------|-----------|
| I/O — high concurrency (web servers) | `asyncio` |
| I/O — moderate, blocking libraries | `ThreadPoolExecutor` |
| CPU-bound (standard Python) | `multiprocessing` |
| CPU-bound (Python 3.13+ free-threading) | `threading` |
| Mixed CPU + I/O | `asyncio` + `run_in_executor()` |

---

# Appendix: What's Next

## AI & Data Science

**LangChain** — Build LLM-powered applications
```python
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-4")
response = llm.invoke("Explain Python in one sentence.")
```

**Hugging Face Transformers** — Use pre-trained models
```python
from transformers import pipeline
classifier = pipeline("sentiment-analysis")
result = classifier("I love Python!")
```

**Polars** — Fast, modern dataframes
```python
import polars as pl
df = pl.DataFrame({"name": ["Alice", "Bob"], "score": [95, 87]})
print(df.filter(pl.col("score") > 90))
```

**PyTorch / TensorFlow** — Deep learning

## Web Development

**FastAPI** — Async APIs with automatic docs
```python
from fastapi import FastAPI
app = FastAPI()

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return {"id": user_id, "name": "Alice"}
```

**Django** — Full-featured framework (Instagram, Spotify)

**SQLModel** — Type-safe async ORM (built on SQLAlchemy + Pydantic)

---

# Support

If you like my work, feel free to:

- ⭐ this repository. And we will be happy together :)

Thanks a bunch for supporting me!

# Contribution

Thanks to all [contributors](https://github.com/meysamhadeli/learn-python/graphs/contributors), you're awesome and this wouldn't be possible without you!

Please follow this [contribution guideline](./CONTRIBUTION.md) to submit a pull request or create the issue.

# Project References

- [Official Python Docs](https://docs.python.org/3/)
- [Awesome Python](https://github.com/vinta/awesome-python)
- [FastAPI Tutorial](https://fastapi.tiangolo.com/)
- [Python Type Hints Cheat Sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)
