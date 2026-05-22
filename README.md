# Learn Python

Hey, welcome to the course, and thanks for learning Python. I hope this course provides a great learning experience.

# Table of Contents

- [Getting Started](#getting-started)
    - [What is Python?](#what-is-python)
    - [Why learn Python?](#why-learn-python)
    - [Installation and Setup](#installation-and-setup)
- [Chapter I: Basics](#chapter-i-basics)
    - [Hello World](#hello-world)
    - [Variables and Data Types](#variables-and-data-types)
    - [String Formatting](#string-formatting)
    - [Flow Control](#flow-control)
    - [Functions](#functions)
    - [Modules](#modules)
    - [Packages](#packages)
    - [Virtual Environments](#virtual-environments)
    - [Useful Commands](#useful-commands)
    - [Build & Packaging](#build--packaging)
- [Chapter II: Data Structures](#chapter-ii-data-structures)
    - [Lists and Tuples](#lists-and-tuples)
    - [Dictionaries and Sets](#dictionaries-and-sets)
    - [List Comprehensions](#list-comprehensions)
- [Chapter III: Features](#chapter-iii-features)
    - [Type Hints](#type-hints)
    - [Classes & Magic Methods](#classes--magic-methods)
    - [Errors and Exceptions](#errors-and-exceptions)
    - [Iterators & Generators](#iterators--generators)
    - [Decorators](#decorators)
    - [Context Managers](#context-managers)
    - [Pattern Matching](#pattern-matching-python-310)
- [Chapter IV: Concurrency](#chapter-iv-concurrency)
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

# Chapter I: Basics

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

## Variables and Data Types

In this tutorial, we will learn about variables and the different data types that Python provides.

### Variables

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

### Data Types

Let's look at the basic data types available in Python.

#### None

`None` represents the absence of a value (similar to `null` in other languages).

```python
result = None
```

#### bool

Boolean values: `True` or `False` (note the capitalization - Python is case-sensitive).

```python
is_ready = True
is_done = False
```

**Operators:**

| Type | Syntax |
|------|--------|
| Logical | `and`, `or`, `not` |
| Comparison | `==`, `!=`, `<`, `>`, `<=`, `>=` |

#### Numeric Types

**int** – Integer of arbitrary precision (no overflow! Python can handle huge numbers).

```python
count = 42
big_number = 10 ** 100  # Googol, Python handles it effortlessly
```

**float** – Double-precision floating-point (follows IEEE-754 standard).

```python
pi = 3.14159
small = 1.5e-4  # 0.00015 (scientific notation)
```

**complex** – Complex numbers with real and imaginary parts.

```python
c = 3 + 4j  # j represents the imaginary unit
```

**Operators:**

| Type | Syntax |
|------|--------|
| Arithmetic | `+`, `-`, `*`, `/`, `//` (floor division), `%` (modulo), `**` (power) |
| Comparison | `==`, `!=`, `<`, `>`, `<=`, `>=` |

#### str (String)

Strings are sequences of Unicode characters. They can be created with single, double, or triple quotes.

```python
single = 'Hello'
double = "World"
multiline = """This is
a multiline
string"""  # Triple quotes preserve line breaks
```

### Type Conversion

Python provides built-in functions for converting between types.

```python
# int to float
i = 42
f = float(i)  # 42.0

# float to int (truncates toward zero, not rounds)
i2 = int(3.99)  # 3 (not 4!)

# number to string
s = str(42)  # "42"

# string to number (raises ValueError if invalid)
num = int("123")  # 123
pi = float("3.14")  # 3.14
```

### Falsy values

In Python, these values evaluate to `False` in a boolean context (everything else is `True`):

- `None`
- `False`
- `0`, `0.0`
- `""` (empty string)
- `[]` (empty list)
- `{}` (empty dict)
- `set()` (empty set)

```python
if not "":
    print("Empty string is falsy")  # This prints
```

## String Formatting

In this tutorial, we will learn about string formatting in Python.

### f-strings (Python 3.6+)

f-strings are the recommended way to format strings. They are readable, fast, and intuitive. Simply prefix the string with `f` and put variables or expressions inside `{}`.

```python
name = "Python"
year = 2026

msg = f"Hello {name}, version {year}"
print(msg)  # Hello Python, version 2026

# Expressions inside {} - you can put any valid Python expression
print(f"Result: {10 + 20}")

# Formatting numbers - use colon followed by format specifier
pi = 3.14159
print(f"Pi to 2 decimals: {pi:.2f}")  # Pi to 2 decimals: 3.14

# Formatting with padding - zero-pad to 3 digits
for i in range(1, 4):
    print(f"Number: {i:03d}")  # 001, 002, 003
```

### Raw strings

Raw strings treat backslashes as literal characters. Useful for file paths and regular expressions where backslashes would otherwise be escape characters.

```python
# Without raw string, \n would become a newline
path = r"C:\Users\Name\Documents"
print(path)  # C:\Users\Name\Documents (backslashes preserved)
```

## Flow Control

Let's talk about flow control in Python.

### If/Else

Python uses **indentation** (4 spaces is the convention) to define blocks, not braces. This makes the code cleaner and enforces readability.

```python
x = 10

if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x equals 5")
else:
    print("x is less than 5")
```

#### Ternary operator

A compact way to write simple if-else expressions.

```python
age = 18
status = "Adult" if age >= 18 else "Minor"  # status = "Adult"
```

### Match/Case (Python 3.10+)

The `match` statement is like a `switch` on steroids with pattern matching. It's more powerful than traditional switch statements.

```python
def check_status(code):
    match code:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500 | 502 | 503:  # OR pattern - multiple values
            return "Server Error"
        case _:  # underscore is the default/wildcard pattern
            return "Unknown"

print(check_status(404))  # Not Found
```

Pattern matching with sequences - you can unpack values:

```python
def process(point):
    match point:
        case (0, 0):
            print("Origin")
        case (x, 0):
            print(f"On X-axis at {x}")
        case (0, y):
            print(f"On Y-axis at {y}")
        case (x, y):
            print(f"Point at ({x}, {y})")

process((10, 0))  # On X-axis at 10
```

### Loops

#### For loop

The `for` loop iterates over any iterable (list, tuple, string, range, etc.).

```python
# Iterate over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Range loop - generates numbers from start to stop-1
for i in range(5):      # 0,1,2,3,4
    print(i)

for i in range(2, 10, 2):  # start, stop, step -> 2,4,6,8
    print(i)

# Enumerate to get both index and value
for index, value in enumerate(fruits):
    print(f"{index}: {value}")
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
        break     # stop when i reaches 9
    print(i)      # prints 1,3,5,7
```

## Functions

In this tutorial, we will discuss how to work with functions in Python.

### Simple declaration

```python
def my_function():
    pass  # 'pass' is a placeholder that does nothing

my_function()  # call the function
```

### Parameters and arguments

```python
def greet(name):
    print(f"Hello, {name}")

greet("Alice")  # Hello, Alice
```

### Default arguments

You can provide default values for parameters. These are used when the caller doesn't provide a value.

```python
def power(base, exp=2):
    return base ** exp

print(power(5))      # 25 (uses default exp=2)
print(power(2, 3))   # 8
```

**Important note:** Default arguments are evaluated only once when the function is defined. Don't use mutable defaults (like `[]` or `{}`) unless you understand the implications.

```python
# This works as expected
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

### Keyword arguments

You can pass arguments by name, regardless of their position.

```python
def describe(name, age, city):
    print(f"{name} is {age} years old and lives in {city}")

describe(city="Paris", name="Alice", age=30)  # Order doesn't matter
```

### Variable arguments (`*args` and `**kwargs`)

Sometimes you don't know how many arguments will be passed. Python handles this with `*args` and `**kwargs`.

```python
# *args collects extra positional arguments as a tuple
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3))  # 6
print(sum_all(1, 2, 3, 4, 5))  # 15

# **kwargs collects extra keyword arguments as a dictionary
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="Paris")
# name: Alice
# age: 30
# city: Paris
```

### Return values

Functions can return values using the `return` keyword.

```python
def add(a, b):
    return a + b

result = add(3, 5)  # 8
```

#### Multiple returns

Python can return multiple values as a tuple (which can be unpacked).

```python
def get_user():
    return "Alice", 30  # Returns a tuple

name, age = get_user()  # Tuple unpacking
print(name, age)  # Alice 30
```

### Lambda functions

Lambdas are anonymous, single-expression functions. They're great for short, throwaway functions where a full `def` would be overkill.

```python
# Basic lambda - takes x, returns x squared
square = lambda x: x ** 2
print(square(5))  # 25

# Often used with sorting - sort by the second element (index 1)
points = [(1, 2), (3, 1), (5, -1)]
points.sort(key=lambda p: p[1])  # lambda extracts the y-coordinate
print(points)  # [(5, -1), (3, 1), (1, 2)]

# With map and filter - functional programming style
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))  # [1, 4, 9, 16, 25]
evens = list(filter(lambda x: x % 2 == 0, numbers))  # [2, 4]
```

### Docstrings

Documentation strings explain what a function does. They're accessible via `help()` or `.__doc__`.

```python
def greet(name):
    """Return a friendly greeting."""
    return f"Hello, {name}"

print(greet.__doc__)  # Return a friendly greeting.
help(greet)  # Shows the docstring in an interactive viewer
```

## Modules

In this tutorial, we will learn about modules.

### What are modules?

A module is simply a file containing Python code. Modules allow you to organize your code into reusable pieces. The filename (without `.py`) is the module name.

### Creating a module

Create `mymodule.py`:

```python
# mymodule.py
def helper():
    return "Help from module"

PI = 3.14159
```

### Importing modules

There are several ways to import modules:

```python
# Import entire module (access with dot notation)
import mymodule
print(mymodule.helper())

# Import specific items directly into your namespace
from mymodule import helper, PI
print(helper())

# Import with alias (useful for long module names or conflicts)
import mymodule as mm
print(mm.helper())
```

### The `__name__` variable

When a module is run directly, `__name__` is set to `"__main__"`. When imported, it's set to the module's name. This allows code to run only when the script is executed directly.

```python
# mymodule.py
def helper():
    return "help"

# This code only runs when executing mymodule.py directly
if __name__ == "__main__":
    print("This runs only when executed directly")
    print(helper())
```

### Standard library modules

Python comes with a rich standard library - no installation needed.

```python
import math
import random
import datetime
import json
import re

print(math.sqrt(16))           # 4.0
print(random.randint(1, 10))   # random number between 1 and 10
print(datetime.datetime.now()) # current date and time
```

## Packages

In this tutorial, we will talk about packages.

### What are packages?

A package is a directory containing modules and a special `__init__.py` file. Packages help organize related modules into a hierarchy.

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

`__init__.py` (can be empty, or define what gets imported with `from package import *`):

```python
from .module1 import hello
```

### Using a package

```python
# Import the function directly (if defined in __init__.py)
from mypackage import hello
print(hello())

# Or import the module directly
from mypackage import module1
print(module1.hello())
```

### Import rules

Names starting with an underscore (`_`) are considered "private" by convention. They won't be imported with `from module import *`.

```python
public_var = "I am public"
_private_var = "I am private by convention"  # Won't be imported with *
```

## Virtual Environments

In this tutorial, we will learn about virtual environments.

### What are virtual environments?

A virtual environment is an isolated Python environment that allows you to manage dependencies for different projects separately. Without them, different projects would share the same global packages, leading to version conflicts.

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

When activated, you'll see `(.venv)` at the beginning of your terminal prompt.

### Deactivating

```bash
deactivate
```

### Managing dependencies

```bash
# Install a package (only affects this environment)
pip install requests

# Freeze dependencies to a file (share with others)
pip freeze > requirements.txt

# Install all dependencies from a file
pip install -r requirements.txt
```

## Useful Commands

Let's discuss some important Python commands.

### Running scripts

```bash
python script.py       # Run script
python -m module_name  # Run module as script (handles relative imports correctly)
```

### Virtual environments

```bash
python -m venv .venv              # Create
source .venv/bin/activate         # Activate (macOS/Linux)
.venv\Scripts\activate            # Activate (Windows)
```

### Package management

```bash
pip install package               # Install
pip uninstall package             # Uninstall
pip list                          # List installed packages
pip freeze > requirements.txt     # Save dependencies
```

### Code formatting and linting

```bash
# Black (opinionated code formatter)
pip install black
black script.py

# Ruff (fast linter and formatter, written in Rust)
pip install ruff
ruff check script.py

# mypy (static type checker)
pip install mypy
mypy script.py
```

## Build & Packaging

In this tutorial, we will learn how to package and distribute Python code.

### The `pyproject.toml` file (modern standard)

The modern way to define a Python package is with `pyproject.toml`. This single file replaces `setup.py`, `setup.cfg`, and `requirements.txt`.

```toml
# pyproject.toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "myapp"
version = "0.1.0"
description = "A sample Python project"
authors = [{name = "Your Name", email = "you@example.com"}]
license = {text = "MIT"}
readme = "README.md"
requires-python = ">=3.10"
dependencies = [
    "fastapi>=0.100.0",
    "httpx"
]

[project.optional-dependencies]
dev = ["pytest", "black", "ruff"]

[project.scripts]
myapp-cli = "myapp.cli:main"
```

### Building packages

```bash
# Install build tools
pip install build

# Build source distribution and wheel
python -m build

# The built packages will be in dist/ directory
```

### Project structure

A typical Python project looks like this:

```
myproject/
├── pyproject.toml
├── README.md
├── LICENSE
├── src/
│   └── mypackage/
│       ├── __init__.py
│       └── main.py
└── tests/
    ├── __init__.py
    └── test_main.py
```

# Chapter II: Data Structures

## Lists and Tuples

In this tutorial, we will learn about lists and tuples.

### Lists

A list is an ordered, **mutable** collection. You can change, add, or remove elements after creation.

#### Creating lists

```python
# Empty list
empty = []

# List with items (can mix types)
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

# List comprehension (we'll cover this in detail later)
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
```

#### Accessing elements

Python uses zero-based indexing. Negative indices count from the end.

```python
fruits = ["apple", "banana", "cherry", "date"]

print(fruits[0])    # apple (first element)
print(fruits[-1])   # date (last element)
print(fruits[1:3])  # ['banana', 'cherry'] (slicing: start inclusive, end exclusive)
```

#### Modifying lists

```python
fruits = ["apple", "banana"]

fruits.append("cherry")        # add to end: ['apple', 'banana', 'cherry']
fruits.insert(1, "blueberry")  # insert at index: ['apple', 'blueberry', 'banana', 'cherry']
fruits[0] = "apricot"          # change element by index: ['apricot', 'blueberry', 'banana', 'cherry']
fruits.remove("banana")        # remove by value (first occurrence)
popped = fruits.pop()          # remove and return last element
```

#### List methods

| Method | Description |
|--------|-------------|
| `append(x)` | Add x to the end |
| `extend(iterable)` | Add all items from iterable |
| `insert(i, x)` | Insert x at index i |
| `remove(x)` | Remove first occurrence of x |
| `pop([i])` | Remove and return item at i (default last) |
| `sort()` | Sort the list in-place |
| `reverse()` | Reverse the list in-place |

#### Slicing

Slicing syntax: `[start:end:step]`. All parameters are optional.

```python
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

nums[2:5]    # [2, 3, 4] (indices 2,3,4)
nums[:4]     # [0, 1, 2, 3] (start defaults to 0)
nums[6:]     # [6, 7, 8, 9] (end defaults to length)
nums[::2]    # [0, 2, 4, 6, 8] (step 2 - every other element)
nums[::-1]   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (reverse)
```

### Tuples

A tuple is an ordered, **immutable** collection. Once created, it cannot be changed. Use tuples when you want to ensure data isn't modified.

```python
# Creating tuples
point = (10, 20)
single = (42,)  # comma is required for single-item tuple

# Without parentheses (tuple packing)
coords = 10, 20, 30  # This is still a tuple

# Unpacking - assign tuple elements to variables
x, y = point  # x=10, y=20
```

**Why use tuples?** They are:
- **Immutable** - safe from accidental changes
- **Hashable** - can be used as dictionary keys (lists cannot)
- **Slightly faster** than lists

```python
# Tuple as dictionary key (works because tuples are hashable)
locations = {(40.7128, -74.0060): "New York"}
```

## Dictionaries and Sets

In this tutorial, we will learn about dictionaries and sets.

### Dictionaries

A dictionary is an unordered collection of key-value pairs. Keys must be unique and hashable (immutable). Dictionaries are optimized for fast lookups.

#### Creating dictionaries

```python
# Empty dict
empty = {}

# With items
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Using dict constructor
person = dict(name="Alice", age=30)
```

#### Accessing values

```python
person = {"name": "Alice", "age": 30}

# Using square brackets (raises KeyError if key doesn't exist)
print(person["name"])  # Alice

# Using get() (returns None or default value if key doesn't exist)
print(person.get("city", "Unknown"))  # Unknown (no error)

# Get all keys, values, or items (key-value pairs)
person.keys()    # dict_keys(['name', 'age'])
person.values()  # dict_values(['Alice', 30])
person.items()   # dict_items([('name', 'Alice'), ('age', 30)])
```

#### Modifying dictionaries

```python
person = {"name": "Alice"}

person["age"] = 30           # add new key-value pair
person["name"] = "Bob"       # update existing key
person.update({"city": "Boston", "age": 31})  # merge another dictionary

del person["age"]            # delete key
age = person.pop("age")      # remove and return value
```

#### Dictionary comprehensions

Just like list comprehensions, but for dictionaries.

```python
squares = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

#### Merging dictionaries (Python 3.9+)

```python
defaults = {"theme": "dark", "lang": "en"}
overrides = {"lang": "fr"}

settings = defaults | overrides  # {'theme': 'dark', 'lang': 'fr'}
```

### Sets

A set is an unordered collection of **unique** elements. Great for removing duplicates and mathematical set operations.

#### Creating sets

```python
# Creating sets - note the curly braces without colons
fruits = {"apple", "banana", "cherry"}

# From list (automatically removes duplicates)
unique = set([1, 2, 2, 3])  # {1, 2, 3}

# Set comprehension
evens = {x for x in range(10) if x % 2 == 0}  # {0, 2, 4, 6, 8}
```

#### Set operations

Sets support mathematical operations like union, intersection, etc.

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a | b   # union: {1,2,3,4,5,6}  (all elements from both)
a & b   # intersection: {3,4}    (elements in both)
a - b   # difference: {1,2}      (in a but not in b)
a ^ b   # symmetric difference: {1,2,5,6} (in either but not both)
```

#### Common use case: removing duplicates

```python
nums = [1, 2, 2, 3, 3, 4]
unique = list(set(nums))  # [1, 2, 3, 4] (order not preserved)
```

## List Comprehensions

List comprehensions provide a concise way to create lists. This is a very Pythonic feature that you'll see everywhere. Instead of writing a multi-line loop, you can create lists in one line.

### Basic syntax

```python
# Traditional loop (3 lines)
squares = []
for x in range(10):
    squares.append(x**2)

# List comprehension (1 line) - same result
squares = [x**2 for x in range(10)]
```

The pattern is `[expression for item in iterable]`.

### With condition

Add an `if` at the end to filter items.

```python
even_squares = [x**2 for x in range(10) if x % 2 == 0]
# [0, 4, 16, 36, 64]
```

### With conditional expression

Use a ternary expression inside for different values based on condition.

```python
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
# ['even', 'odd', 'even', 'odd', 'even']
```

### Nested comprehensions

You can nest loops inside the comprehension.

```python
# Flatten a matrix (2D list to 1D list)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### Set and dict comprehensions

The same idea works for sets and dictionaries.

```python
# Set comprehension (curly braces, no colons)
unique_lens = {len(word) for word in ["hi", "hello", "hi"]}
# {2, 5}  (unique lengths only)

# Dict comprehension (curly braces with colon)
word_lens = {word: len(word) for word in ["hi", "hello"]}
# {'hi': 2, 'hello': 5}
```

# Chapter III: Features

## Type Hints

Type hints (introduced in Python 3.5, improved in later versions) allow you to annotate your code with type information. They don't affect runtime but help with IDE autocomplete, static checking, and code readability. In 2026, type hints are considered best practice for any serious project.

### Basic type hints

```python
def greet(name: str) -> str:
    """name: string parameter, returns a string"""
    return f"Hello, {name}"

age: int = 30  # variable with type hint
names: list[str] = ["Alice", "Bob"]  # Python 3.9+ allows list[str]
```

### Union types (Python 3.10+)

When a value can be one of several types, use `|` (the union operator).

```python
def parse(value: int | str) -> float:
    """Works with both int and string inputs"""
    return float(value)
```

### Optional types

`Optional[T]` means the value can be either `T` or `None`. In Python 3.10+, you can write `T | None`.

```python
def find_user(id: int) -> dict | None:
    """Returns a user dict or None if not found"""
    if id == 1:
        return {"name": "Alice"}
    return None
```

### Literals (specific values)

Use `Literal` when a parameter can only accept specific values.

```python
from typing import Literal

def set_mode(mode: Literal["auto", "manual"]) -> None:
    """mode must be exactly 'auto' or 'manual'"""
    print(f"Mode set to {mode}")

set_mode("auto")   # OK
set_mode("invalid")  # Type checker will complain
```

### TypedDict (structured dicts)

Define the expected structure of a dictionary.

```python
from typing import TypedDict

class User(TypedDict):
    name: str
    age: int
    email: str  # optional fields require total=False

def process_user(user: User) -> None:
    print(f"Processing {user['name']}")
```

### Generics (Python 3.12+)

Write functions that work with any type while preserving type information.

```python
def first[T](items: list[T]) -> T:
    """Return the first element of a list, preserving the element type"""
    return items[0]

# T becomes int here
result1 = first([1, 2, 3])  # result1 is int

# T becomes str here
result2 = first(["a", "b", "c"])  # result2 is str
```

## Classes & Magic Methods

In this tutorial, we will learn about classes in Python.

### Defining a class

```python
class Person:
    # Class variable (shared by all instances) - like a static field
    species = "Homo sapiens"
    
    # Constructor - called when creating an instance
    def __init__(self, name: str, age: int):
        self.name = name      # instance variable
        self._internal = 0    # protected by convention (single underscore)
        self.__private = 0    # name mangling (double underscore) - truly private
    
    # Regular method - receives instance as first parameter (self)
    def greet(self) -> str:
        return f"Hi, I'm {self.name}"
    
    # Property - getter/setter for controlled attribute access
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value
    
    # Static method - no self or cls, like a regular function in the class namespace
    @staticmethod
    def is_adult(age: int) -> bool:
        return age >= 18
    
    # Class method - receives class as first parameter (cls)
    @classmethod
    def from_birth_year(cls, name: str, year: int):
        """Alternative constructor - creates Person from birth year"""
        age = 2026 - year
        return cls(name, age)
```

### Magic methods

Magic methods (also called dunder methods for "double underscore") allow you to define how objects behave with built-in operations. They're what makes Python objects work with operators, built-in functions, and language features.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):      # Called by str() and print()
        return f"({self.x}, {self.y})"
    
    def __repr__(self):     # Called by repr() - developer-friendly representation
        return f"Point({self.x}, {self.y})"
    
    def __add__(self, other):  # Called by + operator
        return Point(self.x + other.x, self.y + other.y)
    
    def __eq__(self, other):   # Called by == operator
        return self.x == other.x and self.y == other.y
    
    def __len__(self):         # Called by len() function
        return 2
    
    def __getitem__(self, key):  # Called by indexing []
        if key == 0:
            return self.x
        elif key == 1:
            return self.y
        else:
            raise IndexError()

p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1 + p2)  # (4, 6) - uses __add__
print(p1 == p2)  # False - uses __eq__
print(len(p1))   # 2 - uses __len__
```

### Data classes (Python 3.7+)

Data classes reduce boilerplate for simple data containers. Instead of writing `__init__`, `__repr__`, `__eq__`, etc., you just declare the fields.

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    email: str = ""  # default value

p = Person("Alice", 30)
print(p)  # Person(name='Alice', age=30, email='') - auto-generated __repr__
```

## Errors and Exceptions

In this tutorial, we will learn about error handling.

### Try-Except

Python uses `try-except` blocks for exception handling. This is similar to `try-catch` in other languages.

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
    print(f"Result: {result}")  # Runs if no exception occurred
finally:
    print("Cleanup")  # Always runs, whether exception or not
```

### Raising exceptions

Use `raise` to trigger an exception.

```python
def validate_age(age: int):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age
```

### Custom exceptions

Create your own exception classes by inheriting from `Exception`.

```python
class PaymentError(Exception):
    """Raised when payment processing fails"""
    pass

def process_payment(amount):
    if amount <= 0:
        raise PaymentError("Amount must be positive")
```

### Exception chaining (Python 3.11+)

When handling an exception and raising a new one, you can preserve the original exception for debugging.

```python
try:
    process_payment(-10)
except PaymentError as e:
    raise RuntimeError("Payment system failed") from e
```

## Iterators & Generators

In this tutorial, we will learn about iterators and generators—powerful tools for working with sequences of data efficiently.

### Iterators

Any object that implements `__iter__()` and `__next__()` can be iterated with a `for` loop. This is how Python internally implements iteration.

```python
class Counter:
    def __init__(self, limit):
        self.limit = limit
        self.count = 0
    
    def __iter__(self):
        return self  # Return the iterator object itself
    
    def __next__(self):
        if self.count >= self.limit:
            raise StopIteration  # Signals end of iteration
        self.count += 1
        return self.count

for num in Counter(5):
    print(num)  # 1,2,3,4,5
```

### Generators

Generators are a simpler way to create iterators. Instead of implementing `__iter__` and `__next__`, you write a function with `yield`. Each `yield` pauses the function and returns a value. The next call resumes from where it left off.

```python
def fibonacci(limit: int):
    """Generate Fibonacci numbers up to limit."""
    a, b = 0, 1
    while a < limit:
        yield a  # Return a value and pause
        a, b = b, a + b  # Resume here next time

# Use it in a loop - values generated on demand
for num in fibonacci(100):
    print(num)  # 0,1,1,2,3,5,8,13,21,34,55,89

# Convert to list (consumes the generator)
fib_list = list(fibonacci(100))
```

### Generator expressions (lazy)

Generator expressions are like list comprehensions but with parentheses instead of brackets. They produce values lazily (one at a time) instead of creating the entire list in memory.

```python
# List comprehension (eager - creates entire list in memory)
squares_list = [x**2 for x in range(1000000)]  # Uses ~32MB memory

# Generator expression (lazy - creates values on demand)
squares_gen = (x**2 for x in range(1000000))  # Uses minimal memory

# Get values one at a time
first = next(squares_gen)  # 0
second = next(squares_gen)  # 1
```

### Real-world example: reading large files

This pattern is essential when working with large files that don't fit in memory.

```python
def read_large_file(file_path):
    """Read a file line by line without loading everything into memory."""
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

# Process a 10GB file line by line
for line in read_large_file("huge_file.log"):
    process_line(line)  # Only one line in memory at a time
```

## Decorators

Decorators are one of Python's most powerful features. They allow you to modify or enhance functions without changing their code. A decorator is a function that takes another function and returns a new function.

### How decorators work

```python
def timer(func):
    """Decorator that measures execution time."""
    import time
    def wrapper(*args, **kwargs):  # *args and **kwargs capture any arguments
        start = time.time()
        result = func(*args, **kwargs)  # Call the original function
        print(f"{func.__name__} took {time.time() - start:.4f}s")
        return result
    return wrapper

@timer  # This is equivalent to: slow_function = timer(slow_function)
def slow_function():
    return sum(range(10_000_000))

slow_function()  # slow_function took 0.2345s
```

### Decorators with arguments

Sometimes you need to pass arguments to the decorator itself.

```python
def repeat(times):
    """Decorator that repeats a function multiple times."""
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

### Multiple decorators

Decorators are applied from bottom to top (closest to function first).

```python
@timer
@repeat(3)
def say_hello():
    return "Hello"

# Equivalent to:
# say_hello = timer(repeat(3)(say_hello))
```

### Real-world example: authentication decorator

This is a common pattern in web frameworks like Flask and FastAPI.

```python
from functools import wraps

def login_required(func):
    """Decorator to check if user is logged in."""
    @wraps(func)  # Preserves original function's name and docstring
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

bad_user = {"name": "Bob", "logged_in": False}
print(view_dashboard(bad_user))  # Raises PermissionError
```

## Context Managers

Context managers handle setup and cleanup automatically using the `with` statement. They ensure resources are properly released even if an error occurs.

### Using context managers

The most common example is file handling:

```python
# Without context manager (need manual close)
f = open("file.txt", "w")
f.write("Hello")
f.close()  # Easy to forget, especially if an error occurs!

# With context manager (auto-closes even if error occurs)
with open("file.txt", "w") as f:
    f.write("Hello")
# File is automatically closed here, even if write() had an error
```

### Creating custom context managers

#### Class-based approach

```python
class DatabaseConnection:
    def __enter__(self):
        print("Connecting to database...")
        self.connection = "fake_connection"
        return self.connection  # This gets assigned to the 'as' variable
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing database connection...")
        self.connection = None
        # Return True to suppress exceptions, False to propagate
        return False

with DatabaseConnection() as conn:
    print(f"Using {conn}")
# Output:
# Connecting to database...
# Using fake_connection
# Closing database connection...
```

#### Function-based approach (using `contextlib`)

```python
from contextlib import contextmanager

@contextmanager
def database_connection():
    print("Connecting...")
    conn = "fake_connection"
    try:
        yield conn  # This is where the 'with' block runs
    finally:
        print("Closing...")

with database_connection() as conn:
    print(f"Using {conn}")
```

### Real-world example: timing code blocks

```python
import time
from contextlib import contextmanager

@contextmanager
def timer(block_name):
    """Context manager to time code blocks."""
    print(f"Starting {block_name}...")
    start = time.time()
    try:
        yield
    finally:
        elapsed = time.time() - start
        print(f"{block_name} took {elapsed:.4f}s")

with timer("data processing"):
    sum(range(10_000_000))
# Output:
# Starting data processing...
# data processing took 0.2345s
```

## Pattern Matching (Python 3.10+)

We covered basic pattern matching earlier. Here are more advanced examples:

### Matching with guards (conditions)

Guards add extra conditions using `if` after the pattern.

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

Pattern matching works with class instances too.

```python
from dataclasses import dataclass

@dataclass
class Circle:
    radius: float

@dataclass
class Rectangle:
    width: float
    height: float

@dataclass
class Point:
    x: float
    y: float

def area(shape):
    match shape:
        case Circle(radius=r):
            return 3.14159 * r ** 2
        case Rectangle(width=w, height=h):
            return w * h
        case Point():
            return 0
        case _:
            raise ValueError("Unknown shape")
```

### Matching JSON-like data

Pattern matching is great for handling API responses and configuration data.

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

# Chapter IV: Concurrency

In this tutorial, we will learn about concurrency in Python. This is one of the most important topics for building high-performance applications.

### The GIL (Global Interpreter Lock)

The GIL is a mutex that prevents multiple threads from executing Python bytecode simultaneously. This means **threads are not useful for CPU-bound work** in standard Python.

However, Python 3.13+ offers **free-threading** (no GIL) as an option, which changes everything.

### Threading (for I/O-bound tasks)

Use threads when your code spends time waiting for I/O (network, disk, database). The GIL is released during I/O operations, so multiple threads can make progress concurrently.

```python
import threading
import time

def download(url: str):
    print(f"Downloading {url}")
    time.sleep(1)  # Simulate I/O wait (GIL is released here)
    print(f"Finished {url}")

# Create and start threads
threads = []
for url in ["a.com", "b.com", "c.com"]:
    t = threading.Thread(target=download, args=(url,))
    t.start()
    threads.append(t)

# Wait for all to complete
for t in threads:
    t.join()
```

#### Thread pool (recommended for many tasks)

Managing threads manually becomes messy with many tasks. `ThreadPoolExecutor` handles this for you.

```python
from concurrent.futures import ThreadPoolExecutor

def download(url):
    time.sleep(1)
    return f"Data from {url}"

urls = ["a.com", "b.com", "c.com", "d.com", "e.com"]

# Using map - simpler when results order matches input order
with ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(download, urls))
    print(results)

# Using futures - more control, results available as they complete
with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(download, url) for url in urls]
    for future in futures:
        print(future.result())
```

### Async/Await

Async is **single-threaded** but can handle thousands of concurrent connections efficiently. It's the preferred choice for web servers and high-concurrency APIs. The event loop switches between tasks at `await` points.

#### Basic async example

```python
import asyncio

async def say_after(delay, msg):
    await asyncio.sleep(delay)  # Non-blocking - yields control to event loop
    print(msg)

async def main():
    print("Start")
    await say_after(1, "Hello")   # Wait for completion (blocks this task)
    await say_after(2, "World")
    print("Done")

asyncio.run(main())
```

#### Running multiple tasks concurrently

```python
async def main():
    # Create tasks (don't await immediately - they start running)
    task1 = asyncio.create_task(say_after(1, "Hello"))
    task2 = asyncio.create_task(say_after(2, "World"))
    
    # Wait for both to complete
    await task1
    await task2

# Or use gather for multiple tasks - more concise
async def main():
    await asyncio.gather(
        say_after(1, "Hello"),
        say_after(2, "World")
    )
```

#### Real-world async HTTP requests

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

# Run it
urls = ["https://api.example.com/1", "https://api.example.com/2"]
results = asyncio.run(fetch_all(urls))
```

#### Async vs Threads: Which to use?

| Use Threads | Use Async |
|-------------|-----------|
| Simple I/O tasks | 1000+ concurrent connections |
| Blocking libraries (e.g., requests) | Web servers (FastAPI) |
| CPU + I/O mixed (pre-3.13) | Streaming data |
| Easier to understand | Better performance at scale |

### Multiprocessing (for CPU-bound work)

For CPU-intensive work (calculations, data processing), use multiprocessing to bypass the GIL and use multiple cores. Each process has its own Python interpreter and its own GIL.

```python
from multiprocessing import Pool
import time

def cpu_intensive(n: int) -> int:
    """Calculate sum of squares (CPU heavy - no I/O)."""
    return sum(i * i for i in range(n))

def run_sequential():
    start = time.time()
    results = [cpu_intensive(10_000_000) for _ in range(4)]
    print(f"Sequential: {time.time() - start:.2f}s")

def run_parallel():
    start = time.time()
    with Pool(processes=4) as pool:  # Uses 4 CPU cores
        results = pool.map(cpu_intensive, [10_000_000] * 4)
    print(f"Parallel (4 processes): {time.time() - start:.2f}s")

# For Python <3.13, parallel will be ~4x faster than sequential
```

#### Sharing data between processes

Since processes don't share memory, you need special mechanisms for communication.

```python
from multiprocessing import Process, Queue, Value

def worker(queue, counter):
    counter.value += 1
    queue.put("Done")

queue = Queue()
counter = Value('i', 0)  # 'i' means signed integer

processes = [Process(target=worker, args=(queue, counter)) for _ in range(4)]
for p in processes: p.start()
for p in processes: p.join()

print(queue.qsize())  # 4
print(counter.value)  # 4
```

### Free-Threading (Python 3.13+)

**This is the game changer for 2026.** Free-threading makes the GIL optional, allowing threads to run truly in parallel on multiple cores. This means you can finally use threads for CPU-bound work!

```python
# Run with free-threaded Python (--disable-gil build)
import threading
import time

def cpu_work():
    total = 0
    for i in range(50_000_000):
        total += i
    return total

# These threads NOW run truly in parallel on multiple cores
threads = [threading.Thread(target=cpu_work) for _ in range(4)]
start = time.time()
for t in threads: t.start()
for t in threads: t.join()
print(f"Time with free-threading: {time.time() - start:.2f}s")
# ~4x faster than GIL build (on a 4-core machine)
```

**Note:** Free-threading is optional. Most Python installations still enable the GIL by default for compatibility. You'll need a special build (e.g., `python-nogil`) to use this feature.

### Decision Matrix for 2026

| Workload | Standard Python (with GIL) | Free-Threading Python (3.13+) |
|----------|---------------------------|-------------------------------|
| I/O (high concurrency) | `asyncio` | `asyncio` (same) |
| I/O (moderate) | `ThreadPoolExecutor` | `ThreadPoolExecutor` |
| CPU bound | `multiprocessing` | `threading` (finally!) |
| Mixed CPU + I/O | `asyncio` + `run_in_executor()` | `threading` |

# Appendix

### Next Steps (AI & Web)

Congratulations on completing the course! Here's where to go next:

#### Web Development

1. **FastAPI** - Build async APIs with automatic documentation
   - [FastAPI Official Tutorial](https://fastapi.tiangolo.com/)
   ```python
   from fastapi import FastAPI
   app = FastAPI()
   
   @app.get("/")
   async def root():
       return {"message": "Hello World"}
   ```

2. **Django** - Full-featured web framework with admin panel, ORM, and authentication
   - [Django Tutorial](https://docs.djangoproject.com/en/stable/intro/tutorial01/)

3. **SQLModel** - Async ORM by the same author as FastAPI

#### AI & Data Science

1. **LangChain** - Build LLM applications and AI Agents
   ```bash
   pip install langchain langchain-openai
   ```
   ```python
   from langchain_openai import ChatOpenAI
   llm = ChatOpenAI(model="gpt-4")
   response = llm.invoke("Hello!")
   ```

2. **Hugging Face Transformers** - Use pre-trained models
   ```python
   from transformers import pipeline
   classifier = pipeline("sentiment-analysis")
   result = classifier("I love Python!")
   print(result)  # [{'label': 'POSITIVE', 'score': 0.999}]
   ```

3. **Polars** - Fast dataframes (better than Pandas for large datasets)
   ```python
   import polars as pl
   df = pl.DataFrame({"name": ["Alice", "Bob"], "age": [30, 25]})
   ```

4. **PyTorch** or **TensorFlow** - Deep learning frameworks

# Support

If you like my work, feel free to:

- ⭐ this repository. And we will be happy together :)

Thanks a bunch for supporting me!

# Contribution

Thanks to all [contributors](https://github.com/meysamhadeli/learn-python/graphs/contributors), you're awesome and this wouldn't be possible without you! The goal is to build a categorized, community-driven collection of very well-known resources.

Please follow this [contribution guideline](./CONTRIBUTION.md) to submit a pull request or create the issue.

# Project References

- [Official Python Docs](https://docs.python.org/3/)
- [Awesome Python](https://github.com/vinta/awesome-python)
- [FastAPI Tutorial](https://fastapi.tiangolo.com/)
- [Real Python Tutorials](https://realpython.com/)
- [Python Type Hints Cheat Sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)
