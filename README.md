# Learn Python

Hey, welcome to the course, and thanks for learning Python. I hope this course provides a great learning experience.

# Table of Contents

- [Getting Started](#getting-started)
    - [What is Python?](#what-is-python)
    - [Why learn Python?](#why-learn-python)
    - [Installation and Setup](#installation-and-setup)
    - [Docusaurus Docs Site](#docusaurus-docs-site)
- [Chapter I: Core Python](#chapter-i-core-python)
    - [Hello World](#hello-world)
    - [Variables](#variables)
    - [Built-in Data Types](#built-in-data-types)
    - [Data Structures](#data-structures)
    - [Type Conversion](#type-conversion)
    - [Operators](#operators)
    - [Falsy Values](#falsy-values)
    - [String Formatting](#string-formatting)
    - [Flow Control](#flow-control)
        - [If/Else](#ifelse)
        - [Match/Case](#matchcase-python-310)
        - [Loops](#loops)
    - [Functions](#functions)
    - [Modules](#modules)
    - [Packages](#packages)
    - [Virtual Environments](#virtual-environments)
    - [Useful Commands](#useful-commands)
    - [Build & Packaging](#build--packaging)
- [Chapter II: Advanced Features](#chapter-ii-advanced-features)
    - [List Comprehensions](#list-comprehensions)
    - [Type Hints](#type-hints)
    - [Classes & Magic Methods](#classes--magic-methods)
    - [Errors and Exceptions](#errors-and-exceptions)
    - [Iterators & Generators](#iterators--generators)
    - [Decorators](#decorators)
    - [Context Managers](#context-managers)
    - [Pattern Matching](#pattern-matching-python-310)
- [Chapter III: Concurrency](#chapter-iii-concurrency)
    - [The GIL](#the-gil-global-interpreter-lock)
    - [Threading](#threading-for-io-bound-tasks)
    - [Async/Await](#asyncawait)
    - [Multiprocessing](#multiprocessing-for-cpu-bound-work)
    - [Free-Threading](#free-threading-python-313)
    - [Decision Matrix](#decision-matrix-for-2026)
- [Appendix](#appendix)
    - [Next Steps (AI & Web)](#next-steps-ai--web)
- [Support](#support)
- [Contribution](#contribution)
- [Project References](#project-references)

---

# Getting Started

## What is Python?

Python is a high-level, interpreted programming language created by Guido van Rossum and first released in 1991. Its design philosophy emphasizes code readability with notable use of significant whitespace.

It supports multiple programming paradigms, including structured, object-oriented, and functional programming.

## Why learn Python?

Before we start this course, let us talk about why we should learn Python.

### 1. The Language of AI and the Future

Python is **the undisputed language of Artificial Intelligence**. If you want to work with AI in 2026 and beyond, Python is not optional—it's essential.

- **TensorFlow** and **PyTorch** (the two dominant deep learning frameworks) are written in Python.
- **LangChain**, **LlamaIndex**, and other LLM orchestration tools are Python-first.
- **Hugging Face** ecosystem (transformers, diffusers, datasets) is built on Python.
- **OpenAI**, **Anthropic**, **Google Gemini** — all provide Python SDKs as their primary interface.

Whether you're building AI agents, fine-tuning LLMs, or working with embeddings, Python is the language you'll use.

### 2. Web Development Powerhouse

Python isn't just for AI. It's also a serious backend language:

- **FastAPI** (async, auto-docs, high performance) is revolutionizing API development.
- **Django** (batteries-included) powers Instagram, Pinterest, and Spotify.
- **Starlette** and **Litestar** provide modern async frameworks.

### 3. Easy to learn, powerful to master

Python is quite easy to learn and has a supportive and active community. The syntax reads like plain English, which means less time fighting the language and more time solving problems.

### 4. Huge Ecosystem

With over **300,000 packages** on PyPI (Python Package Index), there's a library for almost everything:

- **Data Science**: NumPy, Pandas, Polars
- **Web Scraping**: BeautifulSoup, Scrapy
- **DevOps**: Ansible, SaltStack

### 5. Career opportunities

Python developers are in extremely high demand. From AI startups to Fortune 500 companies, Python skills command top salaries. And with the AI boom, this demand is only growing.

I hope this made you excited about Python. Let's start this course.

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

## Docusaurus Docs Site

This repository also includes a [Docusaurus](https://docusaurus.io/) documentation site so the course can be read as a searchable, navigable learning website.

### Run locally

Install the JavaScript dependencies once:

```bash
npm install
```

Start the local documentation server:

```bash
npm run docs:start
```

Build the static site:

```bash
npm run docs:build
```

Preview the production build:

```bash
npm run docs:serve
```

The Docusaurus content lives in the `docs/` folder. The docs pages are generated from this `README.md`, split into nested course sections, and displayed with a Microsoft Docs-style left sidebar so learners can move through the course topic by topic.

This site also enables Docusaurus' official `@docusaurus/theme-live-codeblock` theme. It is most useful for interactive JavaScript/React examples, while Python examples continue to use syntax-highlighted code blocks for readability.

If you edit the course in `README.md`, refresh the generated Docusaurus page with:

```bash
npm run docs:sync
```

---

# Chapter I: Core Python

## Hello World

Let's write our first hello world program.

Create a new file called `main.py`:

```python
print("Hello World!")
```

Now, to run our code, we can simply use the `python` command:

```bash
python main.py
```

```
Hello World!
```

Congratulations, you just wrote your first Python program!

### Structure of a Python program

Unlike some languages, Python doesn't require a `main` function, but it's a good practice to use one:

```python
def main():
    print("Hello World!")

if __name__ == "__main__":
    main()
```

- `def main():` defines a function named `main`.
- `if __name__ == "__main__":` ensures the code runs only when the script is executed directly (not imported as a module).

## Variables

Python is dynamically typed, meaning you don't need to declare the type of a variable.

```python
# Simple assignment
name = "Python"
version = 3.13
is_awesome = True

# Multiple assignment - assign multiple variables in one line
x, y, z = 1, 2.5, "three"

# Constants (by convention, use UPPER_CASE - Python doesn't enforce this)
MAX_CONNECTIONS = 100
```

## Built-in Data Types

Python has several built-in types that are fundamental to the language. These represent single values.

### int

Integer of arbitrary precision (no overflow! Python can handle huge numbers).

```python
count = 42
big_number = 10 ** 100  # Googol, Python handles it effortlessly
negative = -15
```

### float

Double-precision floating-point.

```python
pi = 3.14159
small = 1.5e-4  # 0.00015
negative_float = -0.5
```

### complex

Complex numbers with real and imaginary parts. Uses `j` for the imaginary unit.

```python
c1 = 3 + 4j
c2 = complex(2, -3)  # 2 - 3j
print(c1.real)  # 3.0 (real part)
print(c1.imag)  # 4.0 (imaginary part)
```

### str (String)

Strings are sequences of Unicode characters. They can be created with single, double, or triple quotes.

```python
single = 'Hello'
double = "World"
multiline = """This is
a multiline
string"""

# Escape sequences
escaped = "Line1\nLine2\tTabbed"
raw = r"C:\Users\Name"  # Raw string (backslashes are literal)

# Strings support indexing
text = "Python"
print(text[0])  # 'P'
print(text[-1]) # 'n'
print(len(text)) # 6
```
### bool

Boolean values: `True` or `False`.

```python
is_ready = True
is_done = False

# Boolean from comparison
is_adult = age >= 18
```

### None

`None` represents the absence of a value.

```python
result = None

# Common pattern: check if value exists
if result is None:
    print("No result")
```

## Data Structures

Data structures are collections that hold multiple values.

### Lists

A list is an ordered, **mutable** collection. You can change, add, or remove elements after creation.

```python
# Creating lists
empty = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
nested = [[1, 2], [3, 4]]  # List of lists

# Accessing elements (zero-based indexing)
fruits = ["apple", "banana", "cherry"]
print(fruits[0])     # apple (first element)
print(fruits[-1])    # cherry (last element)
print(fruits[1:3])   # ['banana', 'cherry'] (slicing)

# Modifying lists
fruits.append("date")           # Add to end
fruits.insert(1, "blueberry")   # Insert at index
fruits[0] = "apricot"           # Change element
fruits.remove("banana")         # Remove by value
popped = fruits.pop()           # Remove and return last element

# Useful methods
fruits.sort()        # Sort in-place
fruits.reverse()     # Reverse in-place
```

### Tuples

A tuple is an ordered, **immutable** collection. Once created, it cannot be changed.

```python
# Creating tuples
point = (10, 20)
single = (42,)      # Comma is required for single-item tuple
coords = 10, 20, 30  # Parentheses are optional

# Unpacking
x, y = point        # x=10, y=20
a, b, c = coords    # a=10, b=20, c=30

# Accessing
print(point[0])     # 10
print(point[-1])    # 20

# Tuple as dictionary key (lists cannot do this!)
locations = {(40.7128, -74.0060): "New York"}
```

### Dictionaries

A dictionary is an unordered collection of key-value pairs.

```python
# Creating dictionaries
empty = {}
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Using dict constructor
person = dict(name="Alice", age=30)

# Accessing values
print(person["name"])                    # Alice (raises KeyError if missing)
print(person.get("city", "Unknown"))    # Unknown (no error)

# Modifying
person["age"] = 31                       # Update existing
person["email"] = "alice@example.com"    # Add new
person.update({"city": "Boston", "age": 32})

# Removing
del person["city"]
age = person.pop("age")

# Loop through dictionaries
for key, value in person.items():
    print(f"{key}: {value}")
```

### Sets

A set is an unordered collection of **unique** elements.

```python
# Creating sets
fruits = {"apple", "banana", "cherry"}
unique = set([1, 2, 2, 3, 3, 4])  # {1, 2, 3, 4}

# Adding and removing
fruits.add("date")
fruits.remove("banana")    # Raises KeyError if missing
fruits.discard("grape")    # No error if missing

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a | b   # Union: {1, 2, 3, 4, 5, 6}
a & b   # Intersection: {3, 4}
a - b   # Difference: {1, 2}
a ^ b   # Symmetric difference: {1, 2, 5, 6}

# Remove duplicates from a list
nums = [1, 2, 2, 3, 3, 4, 5, 5]
unique_nums = list(set(nums))  # [1, 2, 3, 4, 5]
```

## Type Conversion

Python provides built-in functions for converting between types.

```python
# Converting between built-in types
int("123")           # 123
float("3.14")        # 3.14
str(42)              # "42"
bool(1)              # True
bool(0)              # False
int(3.99)            # 3 (truncates, not rounds!)

# Converting between data structures
list((1, 2, 3))      # Tuple to list: [1, 2, 3]
tuple([1, 2, 3])     # List to tuple: (1, 2, 3)
set([1, 2, 2, 3])    # List to set: {1, 2, 3}

# Mixed type operations (automatic conversion)
result = 5 + 2.5     # 7.5 (int becomes float)
result = 5 + True    # 6 (True becomes 1)

# Manual conversion needed for strings
message = "Count: " + str(42)
```

## Operators

Operators perform operations on values. Here are the most common ones:

### Arithmetic Operators

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `5 - 3` | `2` |
| `*` | Multiplication | `5 * 3` | `15` |
| `/` | Division | `5 / 2` | `2.5` |
| `//` | Floor Division | `5 // 2` | `2` |
| `%` | Modulo (remainder) | `5 % 2` | `1` |
| `**` | Exponentiation | `5 ** 2` | `25` |

```python
print(10 + 3)    # 13
print(10 - 3)    # 7
print(10 * 3)    # 30
print(10 / 3)    # 3.333...
print(10 // 3)   # 3
print(10 % 3)    # 1
print(10 ** 3)   # 1000
```

### Comparison Operators

Compare values and return `True` or `False`.

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal | `5 != 3` | `True` |
| `<` | Less than | `3 < 5` | `True` |
| `>` | Greater than | `5 > 3` | `True` |
| `<=` | Less than or equal | `3 <= 3` | `True` |
| `>=` | Greater than or equal | `5 >= 3` | `True` |

### Logical Operators

Combine boolean values.

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `and` | Both true | `True and True` | `True` |
| `or` | At least one true | `True or False` | `True` |
| `not` | Opposite | `not True` | `False` |

```python
x = 7
print(x > 5 and x < 10)   # True (both true)
print(x > 10 or x < 5)    # False (neither true)
print(not x == 7)         # False
```

### Assignment Operators

Shorthand for updating variables.

| Operator | Example | Equivalent to |
|----------|---------|---------------|
| `=` | `x = 5` | `x = 5` |
| `+=` | `x += 3` | `x = x + 3` |
| `-=` | `x -= 3` | `x = x - 3` |
| `*=` | `x *= 3` | `x = x * 3` |
| `/=` | `x /= 3` | `x = x / 3` |

```python
x = 10
x += 5   # x = 15
x -= 3   # x = 12
x *= 2   # x = 24
x /= 4   # x = 6.0
```

### Membership Operators

Check if a value exists in a collection.

| Operator | Example | Result |
|----------|---------|--------|
| `in` | `"apple" in ["apple", "banana"]` | `True` |
| `not in` | `"grape" not in ["apple", "banana"]` | `True` |

```python
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)     # True
print("grape" in fruits)      # False

text = "Hello, World!"
print("World" in text)        # True

person = {"name": "Alice", "age": 30}
print("name" in person)       # True (checks keys)
```

### Operator Precedence

Use parentheses `()` to control the order of operations:

```python
# Without parentheses (multiplication first)
result = 5 + 3 * 2    # 11

# With parentheses (addition first)
result = (5 + 3) * 2  # 16
```

When in doubt, use parentheses to make your intention clear.

## Falsy Values

In Python, these values evaluate to `False` in a boolean context (everything else is `True`):

- `None`
- `False`
- `0`, `0.0`
- `""` (empty string)
- `[]` (empty list)
- `()` (empty tuple)
- `{}` (empty dict)
- `set()` (empty set)

```python
# All of these are False in conditions
if not "":
    print("Empty string is falsy")

if not []:
    print("Empty list is falsy")

# Check if list is empty
my_list = []
if my_list:  # Equivalent to: if len(my_list) > 0
    print("List has items")
else:
    print("List is empty")  # This prints
```

## String Formatting

f-strings are the recommended way to format strings. Prefix the string with `f` and put variables inside `{}`.

```python
name = "Python"
year = 2026

msg = f"Hello {name}, version {year}"
print(msg)  # Hello Python, version 2026

# Expressions inside {}
print(f"Result: {10 + 20}")
print(f"List length: {len([1, 2, 3])}")

# Formatting numbers
pi = 3.14159
print(f"Pi to 2 decimals: {pi:.2f}")  # Pi to 2 decimals: 3.14

# Formatting with padding
for i in range(1, 4):
    print(f"Number: {i:03d}")  # 001, 002, 003

# Dictionaries inside f-strings
person = {"name": "Alice", "age": 30}
print(f"{person['name']} is {person['age']} years old")
```

## Flow Control

### If/Else

Python uses **indentation** (4 spaces is the convention) to define blocks.

```python
x = 10

if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x equals 5")
else:
    print("x is less than 5")
```

#### Ternary operator (conditional expression)

A compact way to write simple if-else:

```python
age = 18
status = "Adult" if age >= 18 else "Minor"  # status = "Adult"

# With collections
items = []
message = "Has items" if items else "Empty"  # "Empty"
```

### Match/Case (Python 3.10+)

The `match` statement is like a `switch` on steroids.

```python
def check_status(code):
    match code:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500 | 502 | 503:  # Multiple values
            return "Server Error"
        case _:  # Default case
            return "Unknown"

print(check_status(404))  # Not Found
```

**Pattern matching with collections:**

```python
def process_collection(data):
    match data:
        case []:
            print("Empty list")
        case [x]:
            print(f"Single item: {x}")
        case [x, y]:
            print(f"Two items: {x} and {y}")
        case {"name": name, "age": age}:
            print(f"Person: {name}, {age} years old")
        case _:
            print("Unknown structure")
```

### Loops

#### For loop

Iterates over any iterable (list, tuple, string, dictionary).

```python
# Iterate over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Range loop
for i in range(5):      # 0,1,2,3,4
    print(i)

for i in range(2, 10, 2):  # start, stop, step -> 2,4,6,8
    print(i)

# Enumerate to get index and value
for index, value in enumerate(fruits):
    print(f"{index}: {value}")

# Loop through dictionary
person = {"name": "Alice", "age": 30}
for key, value in person.items():
    print(f"{key}: {value}")
```

#### While loop

Runs as long as the condition is true.

```python
count = 0
while count < 3:
    print(count)
    count += 1
```

#### Break and Continue

- `break` exits the loop entirely
- `continue` skips the rest of the current iteration

```python
for i in range(10):
    if i % 2 == 0:
        continue  # skip even numbers
    if i > 7:
        break     # stop at 9
    print(i)      # prints 1,3,5,7
```

#### Else with loops

The `else` block runs if the loop completes without `break`.

```python
fruits = ["apple", "banana", "cherry"]
search = "orange"

for fruit in fruits:
    if fruit == search:
        print("Found!")
        break
else:
    print("Not found")  # This runs because break wasn't hit
```

## Functions

### Simple declaration

```python
def my_function():
    pass  # placeholder

my_function()
```

### Parameters and arguments

```python
def greet(name):
    print(f"Hello, {name}")

greet("Alice")  # Hello, Alice
```

### Default arguments

```python
def power(base, exp=2):
    return base ** exp

print(power(5))      # 25 (uses default exp=2)
print(power(2, 3))   # 8

# Don't use mutable defaults like [] or {}
def add_item(item, items=None):  # Correct way
    if items is None:
        items = []
    items.append(item)
    return items
```

### Keyword arguments

```python
def describe(name, age, city):
    print(f"{name} is {age} years old and lives in {city}")

describe(city="Paris", name="Alice", age=30)  # Order doesn't matter
```

### Variable arguments (`*args` and `**kwargs`)

```python
# *args collects positional arguments as a tuple
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3))        # 6
print(sum_all(1, 2, 3, 4, 5))  # 15

# **kwargs collects keyword arguments as a dictionary
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="Paris")
```

### Return values

```python
def add(a, b):
    return a + b

result = add(3, 5)  # 8
```

#### Multiple returns

```python
def get_user():
    return "Alice", 30  # Returns a tuple

name, age = get_user()  # Tuple unpacking
print(name, age)  # Alice 30
```

### Lambda functions

Anonymous, single-expression functions.

```python
# Basic lambda
square = lambda x: x ** 2
print(square(5))  # 25

# Used with sorting
points = [(1, 2), (3, 1), (5, -1)]
points.sort(key=lambda p: p[1])  # Sort by y-coordinate
print(points)  # [(5, -1), (3, 1), (1, 2)]

# With map and filter
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))  # [1, 4, 9, 16, 25]
evens = list(filter(lambda x: x % 2 == 0, numbers))  # [2, 4]
```

### Docstrings

Documentation strings explain what a function does.

```python
def greet(name):
    """Return a friendly greeting.
    
    Args:
        name: The name of the person to greet
        
    Returns:
        A greeting string
    """
    return f"Hello, {name}"

help(greet)
```

## Modules

### What are modules?

A module is simply a file containing Python code.

### Creating a module

Create `mymodule.py`:

```python
# mymodule.py
def helper():
    return "Help from module"

PI = 3.14159
```

### Importing modules

```python
# Import entire module
import mymodule
print(mymodule.helper())
print(mymodule.PI)

# Import specific items
from mymodule import helper, PI
print(helper())

# Import with alias
import mymodule as mm
print(mm.helper())
```

### The `__name__` variable

```python
# This code runs only when executing directly
if __name__ == "__main__":
    print("This runs only when executed directly")
```

### Standard library modules

```python
import math
import random
import datetime
import os
import sys

print(math.sqrt(16))                 # 4.0
print(random.randint(1, 10))         # random number
print(datetime.datetime.now())       # current date and time
print(os.getcwd())                   # current directory
print(sys.version)                   # Python version
```

## Packages

### What are packages?

A package is a directory containing modules and a special `__init__.py` file.

### Creating a package

Create this structure:

```
mypackage/
    __init__.py
    module1.py
    module2.py
```

`module1.py`:

```python
def hello():
    return "Hello from module1"
```

`__init__.py`:

```python
from .module1 import hello
```

### Using a package

```python
from mypackage import hello
print(hello())

# Or
from mypackage import module1
print(module1.hello())
```

## Virtual Environments

### What are virtual environments?

A virtual environment is an isolated Python environment for managing dependencies per project. Every professional Python developer uses them.

### Creating a virtual environment

```bash
python -m venv .venv
```

### Activating

- **Windows**:
  ```bash
  .venv\Scripts\activate
  ```
- **macOS/Linux**:
  ```bash
  source .venv/bin/activate
  ```

You'll see `(.venv)` at the beginning of your terminal prompt when activated.

### Deactivating

```bash
deactivate
```

### Managing dependencies

```bash
# Install a package
pip install requests

# Save dependencies
pip freeze > requirements.txt

# Install from file
pip install -r requirements.txt
```

## Useful Commands

### Running scripts

```bash
python script.py       # Run script
python -m module_name  # Run module as script
```

### Virtual environments

```bash
python -m venv .venv              # Create
source .venv/bin/activate         # Activate (macOS/Linux)
.venv\Scripts\activate            # Activate (Windows)
deactivate                        # Deactivate
```

### Package management

```bash
pip install package               # Install
pip uninstall package             # Uninstall
pip list                          # List installed
pip freeze > requirements.txt     # Save dependencies
pip install -r requirements.txt   # Install from file
```

### Code formatting and linting

```bash
# Black (code formatter)
pip install black
black script.py

# Ruff (fast linter)
pip install ruff
ruff check script.py

# mypy (type checker)
pip install mypy
mypy script.py
```

## Build & Packaging

### The `pyproject.toml` file

The modern way to define a Python package.

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "myapp"
version = "0.1.0"
description = "A sample Python project"
requires-python = ">=3.10"
dependencies = [
    "fastapi>=0.100.0",
]

[project.scripts]
myapp-cli = "myapp.cli:main"
```

### Building packages

```bash
pip install build
python -m build
```

### Project structure

```
myproject/
├── pyproject.toml
├── README.md
├── src/
│   └── mypackage/
│       ├── __init__.py
│       └── main.py
└── tests/
    └── test_main.py
```

---

# Chapter II: Advanced Features

## List Comprehensions

A concise way to create lists.

### Basic syntax

```python
# Traditional loop
squares = []
for x in range(10):
    squares.append(x**2)

# List comprehension (same result)
squares = [x**2 for x in range(10)]
```

### With condition

```python
even_squares = [x**2 for x in range(10) if x % 2 == 0]
# [0, 4, 16, 36, 64]
```

### With conditional expression

```python
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
# ['even', 'odd', 'even', 'odd', 'even']
```

### Nested comprehensions

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### Set and dict comprehensions

```python
# Set comprehension
unique_lens = {len(word) for word in ["hi", "hello", "hi"]}
# {2, 5}

# Dict comprehension
word_lens = {word: len(word) for word in ["hi", "hello"]}
# {'hi': 2, 'hello': 5}
```

## Type Hints

Type hints allow you to annotate your code with type information (Python 3.5+).

### Basic type hints

```python
def greet(name: str) -> str:
    return f"Hello, {name}"

age: int = 30
names: list[str] = ["Alice", "Bob"]
```

### Union types (Python 3.10+)

```python
def parse(value: int | str) -> float:
    return float(value)
```

### Optional types

```python
def find_user(id: int) -> dict | None:
    if id == 1:
        return {"name": "Alice"}
    return None
```

### TypedDict

```python
from typing import TypedDict

class User(TypedDict):
    name: str
    age: int

def process_user(user: User) -> None:
    print(f"Processing {user['name']}")
```

### Generics (Python 3.12+)

```python
def first[T](items: list[T]) -> T:
    return items[0]

result = first([1, 2, 3])     # result is int
```

## Classes & Magic Methods

### Defining a class

```python
class Person:
    # Class variable
    species = "Homo sapiens"
    
    # Constructor
    def __init__(self, name: str, age: int):
        self.name = name
        self._internal = 0         # protected by convention
    
    # Regular method
    def greet(self) -> str:
        return f"Hi, I'm {self.name}"
    
    # Property
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value
    
    # Static method
    @staticmethod
    def is_adult(age: int) -> bool:
        return age >= 18
    
    # Class method
    @classmethod
    def from_birth_year(cls, name: str, year: int):
        age = 2026 - year
        return cls(name, age)
```

### Magic methods

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
print(p1 + p2)  # (4, 6)
```

### Data classes (Python 3.7+)

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    email: str = ""

p = Person("Alice", 30)
print(p)  # Person(name='Alice', age=30, email='')
```

## Errors and Exceptions

### Try-Except

```python
try:
    value = int(input("Enter number: "))
    result = 100 / value
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"Unexpected error: {e}")
else:
    print(f"Result: {result}")
finally:
    print("Cleanup")
```

### Raising exceptions

```python
def validate_age(age: int):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age
```

### Custom exceptions

```python
class PaymentError(Exception):
    pass

def process_payment(amount):
    if amount <= 0:
        raise PaymentError("Amount must be positive")
```

## Iterators & Generators

### Iterators

```python
class Counter:
    def __init__(self, limit):
        self.limit = limit
        self.count = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count >= self.limit:
            raise StopIteration
        self.count += 1
        return self.count

for num in Counter(5):
    print(num)  # 1,2,3,4,5
```

### Generators

```python
def fibonacci(limit: int):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

for num in fibonacci(100):
    print(num)  # 0,1,1,2,3,5,8,13,21,34,55,89
```

### Generator expressions

```python
# Lazy evaluation - values created on demand
squares_gen = (x**2 for x in range(1000000))

# Get values one at a time
first = next(squares_gen)   # 0
second = next(squares_gen)  # 1
```

### Reading large files

```python
def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

# Process line by line (only one line in memory at a time)
for line in read_large_file("huge_file.log"):
    process_line(line)
```

## Decorators

### Basic decorator

```python
def timer(func):
    import time
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
```

### Decorators with arguments

```python
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(times):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    return f"Hello, {name}"

print(greet("Alice"))  # ['Hello, Alice', 'Hello, Alice', 'Hello, Alice']
```

### Authentication decorator

```python
from functools import wraps

def login_required(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if not user.get("logged_in", False):
            raise PermissionError("Login required")
        return func(user, *args, **kwargs)
    return wrapper

@login_required
def view_dashboard(user):
    return "Welcome to your dashboard"

current_user = {"name": "Alice", "logged_in": True}
print(view_dashboard(current_user))  # Works
```

## Context Managers

### Using context managers

```python
# Without context manager
f = open("file.txt", "w")
f.write("Hello")
f.close()  # Easy to forget!

# With context manager (auto-closes)
with open("file.txt", "w") as f:
    f.write("Hello")
# File automatically closed here
```

### Custom context manager

```python
class DatabaseConnection:
    def __enter__(self):
        print("Connecting...")
        self.connection = "fake_connection"
        return self.connection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing...")
        self.connection = None

with DatabaseConnection() as conn:
    print(f"Using {conn}")
```

### Function-based context manager

```python
from contextlib import contextmanager

@contextmanager
def timer(block_name):
    import time
    print(f"Starting {block_name}...")
    start = time.time()
    try:
        yield
    finally:
        elapsed = time.time() - start
        print(f"{block_name} took {elapsed:.4f}s")

with timer("data processing"):
    sum(range(10_000_000))
```

## Pattern Matching (Python 3.10+)

### Matching with guards

```python
def classify(number):
    match number:
        case n if n < 0:
            return "Negative"
        case 0:
            return "Zero"
        case n if n > 0:
            return "Positive"
```

### Matching classes

```python
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
```

### Matching JSON-like data

```python
def handle_api_response(response):
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

---

# Chapter III: Concurrency

## The GIL (Global Interpreter Lock)

The GIL prevents multiple threads from executing Python bytecode simultaneously. This means **threads are not useful for CPU-bound work** in standard Python.

Python 3.13+ offers **free-threading** (no GIL) as an option.

## Threading (for I/O-bound tasks)

Use threads for I/O-bound tasks (network, disk, database). The GIL is released during I/O operations.

```python
import threading
import time

def download(url: str):
    print(f"Downloading {url}")
    time.sleep(1)  # Simulates I/O (GIL is released)
    print(f"Finished {url}")

threads = []
for url in ["a.com", "b.com", "c.com"]:
    t = threading.Thread(target=download, args=(url,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()
```

### Thread pool

```python
from concurrent.futures import ThreadPoolExecutor

def download(url):
    time.sleep(1)
    return f"Data from {url}"

urls = ["a.com", "b.com", "c.com", "d.com", "e.com"]

with ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(download, urls))
```

## Async/Await

Async is **single-threaded** but can handle thousands of concurrent connections.

### Basic async example

```python
import asyncio

async def say_after(delay, msg):
    await asyncio.sleep(delay)
    print(msg)

async def main():
    task1 = asyncio.create_task(say_after(1, "Hello"))
    task2 = asyncio.create_task(say_after(2, "World"))
    await task1
    await task2

asyncio.run(main())
```

### Running multiple tasks

```python
async def main():
    await asyncio.gather(
        say_after(1, "Hello"),
        say_after(2, "World")
    )
```

### Async HTTP requests

```python
import aiohttp
import asyncio

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        return results

urls = ["https://api.example.com/1", "https://api.example.com/2"]
results = asyncio.run(fetch_all(urls))
```

### Async vs Threads

| Use Threads | Use Async |
|-------------|-----------|
| Simple I/O tasks | 1000+ concurrent connections |
| Blocking libraries | Web servers (FastAPI) |
| Easier to understand | Better performance at scale |

## Multiprocessing (for CPU-bound work)

Use multiprocessing to bypass the GIL and use multiple cores.

```python
from multiprocessing import Pool
import time

def cpu_intensive(n: int) -> int:
    return sum(i * i for i in range(n))

def run_parallel():
    start = time.time()
    with Pool(processes=4) as pool:
        results = pool.map(cpu_intensive, [10_000_000] * 4)
    print(f"Parallel: {time.time() - start:.2f}s")
```

### Sharing data between processes

```python
from multiprocessing import Process, Queue, Value

def worker(queue, counter):
    counter.value += 1
    queue.put("Done")

queue = Queue()
counter = Value('i', 0)

processes = [Process(target=worker, args=(queue, counter)) for _ in range(4)]
for p in processes: p.start()
for p in processes: p.join()
```

## Free-Threading (Python 3.13+)

Free-threading makes the GIL optional, allowing threads to run truly in parallel.

```python
# Run with free-threaded Python (--disable-gil build)
import threading

def cpu_work():
    total = 0
    for i in range(50_000_000):
        total += i
    return total

threads = [threading.Thread(target=cpu_work) for _ in range(4)]
for t in threads: t.start()
for t in threads: t.join()
```

**Note:** Free-threading is optional. Most Python installations still enable the GIL by default.

## Decision Matrix for 2026

| Workload | Standard Python | Free-Threading (3.13+) |
|----------|----------------|------------------------|
| I/O (high concurrency) | `asyncio` | `asyncio` |
| I/O (moderate) | `ThreadPoolExecutor` | `ThreadPoolExecutor` |
| CPU bound | `multiprocessing` | `threading` |
| Mixed CPU + I/O | `asyncio` + `run_in_executor()` | `threading` |

---

# Appendix

## Next Steps (AI & Web)

### Web Development

**FastAPI** - Build async APIs
```python
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

**Django** - Full-featured web framework

**SQLModel** - Async ORM

### AI & Data Science

**LangChain** - Build LLM applications
```python
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-4")
response = llm.invoke("Hello!")
```

**Hugging Face Transformers** - Use pre-trained models
```python
from transformers import pipeline
classifier = pipeline("sentiment-analysis")
result = classifier("I love Python!")
```

**Polars** - Fast dataframes
```python
import polars as pl
df = pl.DataFrame({"name": ["Alice", "Bob"], "age": [30, 25]})
```

**PyTorch** or **TensorFlow** - Deep learning frameworks

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
