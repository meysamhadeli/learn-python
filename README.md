# Learn Python

> Learn Python from scratch with short lessons, clear explanations, and runnable examples.

- :page_facing_up: **Documentation site** — the full content is published at **[https://learn-python-dev.netlify.app](https://learn-python-dev.netlify.app/)** with a sidebar, search, and per-chapter navigation.

- :notebook: **Interactive notebook** — Open **[learn-python.ipynb](https://vscode.dev/github/meysamhadeli/learn-python/blob/main/learn-python.ipynb)** in VS Code, to run and edit every code block inline.

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

---

<a id="getting-started"></a>

## Getting Started

### What is Python?

Python is a high-level, interpreted language created by Guido van Rossum in 1991. It reads like plain English, runs everywhere, and is the #1 language for AI, data science, and backend web development.

### Why learn Python?

**Short answer:** Python is the language of AI — and it's also great for web backends.

- **AI/ML**: PyTorch, TensorFlow, Hugging Face, LangChain, OpenAI SDK — all Python-first.
- **Web**: FastAPI (async, high-performance), Django (batteries-included), powers Instagram & Spotify.
- **Ecosystem**: 300,000+ packages on PyPI for everything from scraping to DevOps.
- **Jobs**: Python skills are in massive demand and only growing with the AI boom.

### Installation and Setup

#### Download

Install Python from the [official downloads page](https://www.python.org/downloads/).

#### macOS

```bash
## Verify installation
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
2. **Check "Add Python to PATH"**.
3. Click "Install Now".

```bash
python --version
```

#### VS Code

Download from [code.visualstudio.com](https://code.visualstudio.com/) and install the **Python extension** by Microsoft for IntelliSense, linting, and debugging.

> 💡 Use [learn-python.ipynb](https://github.com/meysamhadeli/learn-python/blob/main/learn-python.ipynb) in VS Code to run and debug code interactively!

---

<a id="chapter-i-the-basics"></a>

## Chapter I: The Basics

The foundation — types, variables, strings, operators, and truthiness.

This chapter is where Python starts to feel concrete. You are not only learning syntax here; you are building the mental model that the rest of the language depends on:

- how Python stores values
- how names point to objects
- how expressions are evaluated
- how text and numbers behave differently
- how conditions decide whether code runs

If any page in this chapter feels slower than expected, that is a good sign. These topics look simple, but they explain a large share of beginner mistakes later in the course.

### Sections

- [Hello World](./hello-world)
- [Variables](./variables)
- [Built-in Data Types](./built-in-data-types)
- [String Formatting](./string-formatting)
- [Operators](./operators)
- [Falsy Values](./falsy-values)

---

<a id="hello-world"></a>

## Hello World

### Your First Program

The traditional starting point for any language is printing "Hello, World!" to the screen. In Python this is a single line:

```python
print("Hello, World!")
```

This small example already shows two core ideas from the official Python tutorial:

- Python code is designed to be read almost like plain English.
- You can write a useful program before learning classes, build steps, or type declarations.

Save this to `main.py` and run it:

```bash
python main.py
## or on Windows
py main.py
```

Output:
```
Hello, World!
```

If Python is installed correctly, the interpreter reads the file from top to bottom and executes each statement in order. Right now there is only one statement, so the behavior is easy to predict: Python calls `print()`, and the text appears in your terminal.

### Script Mode vs Interactive Mode

Python can be used in two common ways:

- **Script mode**: you run a file like `main.py`.
- **Interactive mode**: you start Python first, then type commands one at a time.

For example, this opens the interactive interpreter:

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

Interactive mode is useful for quick experiments. Script mode is better when you want to save, rerun, and share your code.

### How Python Executes Code

When you run `python main.py`, the CPython interpreter reads your source file, compiles it to **bytecode** (a low-level, platform-independent instruction set), and executes that bytecode on the Python Virtual Machine (PVM). You never see the bytecode directly — it is cached in `__pycache__/` as `.pyc` files to speed up future runs.

Unlike compiled languages (C, Go, Rust), there is no separate compilation step you must run manually. The compile-and-run happens transparently each time you invoke the interpreter.

For beginners, the important mental model is simpler than the implementation details:

1. Python reads your file.
2. Python checks that the syntax is valid.
3. Python runs the statements in order.

That mental model will stay useful throughout the course.

### The `print()` Function

`print()` is a built-in function that writes its arguments to **standard output** (`stdout`), followed by a newline by default. It accepts multiple arguments and several keyword parameters:

```python
print("Hello", "World")          # Hello World  (space-separated by default)
print("Hello", "World", sep="-") # Hello-World
print("Hello", end="")           # no newline at the end
print(42, 3.14, True, None)      # 42 3.14 True None
```

The `sep` parameter controls what goes between arguments (default: `" "`). The `end` parameter controls what is appended after the last argument (default: `"\n"`).

This matters because beginners often try to build a long string manually with `+`. In many cases, `print()` can already format simple output cleanly for you:

```python
name = "Maya"
score = 95

print("Student:", name, "Score:", score)
```

Use `print()` to inspect values while learning. It is the fastest way to answer questions like "What is in this variable right now?" or "Did this branch actually run?"

### The `__main__` Guard

When Python imports a file as a module, it sets the special variable `__name__` to the file's module name. When you run a file directly, Python sets `__name__` to the string `"__main__"`.

This lets you write code that only runs when the file is the entry point — not when it is imported by another module:

```python
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    # This block runs only when the script is executed directly.
    # It is skipped when the file is imported as a module.
    print(greet("World"))
```

This pattern is standard practice for any Python script that also exposes reusable functions.

If you are just starting out, you do not need this guard in every tiny example. It becomes useful once a file starts doing two jobs at once:

- defining reusable functions
- acting as a runnable program

That is why you will see it more often in larger examples than in one-line demos.

### Reading Input

The built-in `input()` function reads a line from standard input and returns it as a string:

```python
name = input("Enter your name: ")
print(f"Hello, {name}!")
```

`input()` **always returns a string**, even if the user types a number. Convert explicitly when needed:

```python
age = int(input("Enter your age: "))
```

That explicit conversion step is important. Python does not guess whether the user meant an integer, a float, or plain text.

```python
age_text = input("Enter your age: ")
print(age_text, type(age_text))  # always a str
```

One common beginner mistake is mixing input text with numbers too early:

```python
age = input("Enter your age: ")
## print(age + 1)  # TypeError: can't add str and int
print(int(age) + 1)
```

As a rule:

- `input()` gets text from the user.
- conversion functions like `int()` and `float()` turn that text into other types.
- `print()` shows results back to the user.

---

<a id="variables"></a>

## Variables

### Assignment and Naming

In Python you create a variable simply by assigning a value to a name — no type declaration is needed. A variable name must start with a letter or underscore, can contain letters, digits, and underscores, and is case-sensitive (`count` and `Count` are different variables).

```python
name = "Python"
version = 3.13
is_awesome = True
_private = "convention only"
```

Python follows **snake_case** for variable and function names (e.g. `user_name`, `total_price`), as specified in [PEP 8](https://peps.python.org/pep-0008/).

The official tutorial introduces assignment very early because it is one of the main differences beginners notice when coming from other languages: you do not write a declaration like `string name;` or `let name;` first. You simply bind a name to a value.

```python
language = "Python"
year = 1991
```

After that assignment, the names `language` and `year` can be reused anywhere in the current scope.

### Variables Are References

This is one of Python's most important concepts: a variable is **not a box that holds a value** — it is a **label that points to an object** in memory. When you write `x = 42`, Python creates the integer object `42` in memory and makes `x` point to it.

```python
x = [1, 2, 3]
y = x           # y points to the SAME list object
y.append(4)
print(x)        # [1, 2, 3, 4] — modifying via y also affects x
```

Use `id()` to see the memory address an object lives at:

```python
a = "hello"
b = "hello"
print(id(a) == id(b))  # Often True — Python interns short strings
```

If you want an independent copy of a mutable object, use `copy()` or slicing:

```python
y = x.copy()    # or: y = x[:]
y.append(99)
print(x)        # unaffected
```

This reference model explains a lot of Python behavior:

- assigning one list to another name does **not** make a copy
- changing a mutable object through one name is visible through every name pointing to it
- rebinding a name does not change the old object; it only changes what the name points to

```python
items = [1, 2, 3]
other = items
items = [10, 20, 30]

print(other)  # [1, 2, 3]
```

Here, `other` still points to the original list. Reassigning `items` did not rewrite that old list.

### Multiple Assignment

Python lets you assign multiple variables in one line using **tuple unpacking**:

```python
x, y, z = 1, 2.5, "three"  # types can differ
a = b = c = 0               # all three point to the same object

## Swap without a temporary variable — a Python idiom
x, y = y, x
```

This works because Python evaluates the full right-hand side first, then performs the assignments. That is why swapping values is safe and does not overwrite one side too early.

### Constants

Python has no built-in constant mechanism. The convention is to name constants in **UPPER_CASE** to signal they should not be reassigned:

```python
MAX_CONNECTIONS = 100
PI = 3.14159
DATABASE_URL = "postgresql://localhost/mydb"
```

Nothing prevents another part of the code from reassigning these — it is a social convention, not a language feature. For stricter enforcement, use `typing.Final`:

```python
from typing import Final
MAX_RETRIES: Final = 3
```

For course code and small scripts, the naming convention is usually enough. In larger codebases, `Final` helps readers and type checkers understand your intent.

### Deleting Variables

Use `del` to remove a variable name from the current scope:

```python
temp = 42
del temp
## print(temp)  # NameError: name 'temp' is not defined
```

This does not necessarily destroy the object — Python's garbage collector reclaims memory when an object has no more references pointing to it.

Most beginners do not need `del` often. It appears more in cases like:

- removing items from containers
- cleaning up names in a narrow scope
- demonstrating how references work

The main lesson is that names and objects are related, but they are not the same thing.

---

<a id="built-in-data-types"></a>

## Built-in Data Types

Python has a small set of built-in types that cover almost every need. They are all objects — even `int` and `bool` — and every value carries its type with it at runtime.

That last point is important: Python is **dynamically typed**, which means values know their own type while the variable name does not permanently lock to one type.

```python
value = 10
print(type(value))

value = "ten"
print(type(value))
```

This flexibility is convenient, but it also means you need to pay attention to what kind of value a variable holds at a given moment.

### int

Python integers have **arbitrary precision** — they grow as large as your memory allows, with no overflow and no need to choose between `int` and `long` as in languages like Java or C.

```python
count = 42
big_number = 10 ** 100        # a googol — no problem
binary = 0b1010               # 10 in binary
hexadecimal = 0xFF            # 255 in hex
```

Arithmetic on integers is exact. For floating-point results, use `/`:

```python
print(7 // 2)   # 3   (floor division — always int)
print(7 / 2)    # 3.5 (true division — always float)
print(7 % 2)    # 1   (remainder)
```

If you are learning from calculator examples, remember this rule from the Python tutorial: `/` means real division, while `//` means floor division. Mixing them up is a very common source of off-by-one style mistakes.

### float

Floats are **IEEE 754 double-precision** numbers (64-bit). They can represent an enormous range of values but with limited precision — about 15–17 significant decimal digits.

```python
pi = 3.14159
small = 1.5e-4      # scientific notation: 0.00015
large = 6.022e23    # Avogadro's number
```

**The classic gotcha:**

```python
print(0.1 + 0.2)        # 0.30000000000000004
print(0.1 + 0.2 == 0.3) # False!
```

This is a consequence of binary floating-point, not a Python bug. For exact decimal arithmetic use `decimal.Decimal`:

```python
from decimal import Decimal
print(Decimal("0.1") + Decimal("0.2"))  # 0.3 — exact
```

This is why equality comparisons with floats should be treated carefully. For many real-world tasks, you compare within a tolerance instead of expecting perfect decimal precision.

### complex

Python has **native complex number support** — useful in signal processing, scientific computing, and some mathematical algorithms.

```python
c = 3 + 4j
print(c.real)    # 3.0
print(c.imag)    # 4.0
print(abs(c))    # 5.0 — Euclidean magnitude: sqrt(3² + 4²)
print(c * 2)     # (6+8j)
```

The `j` suffix (not `i`) denotes the imaginary part. Complex arithmetic follows standard mathematical rules.

If you are not doing math-heavy work, you may rarely use `complex` directly. It is still useful to know that Python includes it natively instead of treating it as a special library-only feature.

### str

Strings are **immutable sequences of Unicode characters**. "Immutable" means once created, their content cannot change — any operation that appears to modify a string actually creates a new one.

```python
text = "Python"
print(text[0])       # 'P'       — indexing from 0
print(text[-1])      # 'n'       — negative indexes from the end
print(text[1:4])     # 'yth'     — slicing [start:stop]
print(text[::-1])    # 'nohtyP'  — reverse via step
print(len(text))     # 6
```

Strings support many built-in methods:

```python
s = "  Hello, World!  "
print(s.strip())            # "Hello, World!"
print(s.lower())            # "  hello, world!  "
print(s.replace("World", "Python"))  # "  Hello, Python!  "
print("Hello, World!".split(", "))   # ['Hello', 'World!']
print("-".join(["a", "b", "c"]))     # "a-b-c"
print("hello".startswith("he"))      # True
```

String literals can be written in several ways:

```python
single = 'Hello'
double = "Hello"              # identical
multiline = """Line 1
Line 2"""
raw = r"C:\Users\Name"        # backslashes are literal — no escape processing
byte_str = b"binary data"     # bytes object, not str
```

Two details from the Python tutorial matter a lot here:

- strings are sequences, so indexing and slicing work naturally
- strings are immutable, so operations create new strings instead of changing the old one in place

```python
word = "Python"
new_word = "J" + word[1:]

print(word)      # Python
print(new_word)  # Jython
```

Beginners often expect `word[0] = "J"` to work, but it fails because strings cannot be modified character by character.

### bool

`bool` is a **subclass of `int`** — `True` equals `1` and `False` equals `0`. This means booleans work in arithmetic:

```python
print(True + True)    # 2
print(True * 5)       # 5
print(sum([True, False, True, True]))  # 3  — counts Trues

is_adult = age >= 18  # comparison returns a bool
```

Boolean values are created by comparisons, `not`, membership tests (`in`), and truthiness checks (`bool(value)`).

In practice, `bool` appears everywhere because `if`, `while`, and logical expressions all depend on it. Even when you do not write `True` or `False` yourself, Python is constantly producing boolean results behind the scenes.

### None

`None` is Python's null value — the sole instance of `NoneType`. It represents the absence of a value and is what functions return when they have no explicit `return` statement.

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

`None` is a **singleton** — there is only one `None` object in any Python process. That is why `is None` is correct and `== None` is discouraged (a custom class could override `__eq__` to return `True` when compared to `None`).

Treat `None` as "no value yet" or "nothing was found". That makes it easier to read functions and conditionals:

```python
user = None

if user is None:
    print("Please log in first")
```

---

<a id="string-formatting"></a>

## String Formatting

### f-Strings (Recommended)

Introduced in Python 3.6, **f-strings** (formatted string literals) are the recommended way to embed expressions inside strings. Prefix the string with `f` or `F` and place any valid Python expression inside `{}`:

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

This style is usually the clearest because the variable names stay close to the text they belong to. You read the final sentence almost the same way the user will see it.

```python
product = "Keyboard"
price = 49.99

print(f"{product} costs ${price}")
```

Any valid expression can go inside the braces, but do not overdo it. Short expressions are helpful; long expressions can make the string hard to read. When formatting becomes complex, compute values first and format second.

### Format Specification Mini-Language

After a colon inside `{}` you can specify how the value should be formatted:

```python
pi = 3.14159265

## Decimal places
print(f"{pi:.2f}")      # 3.14
print(f"{pi:.4f}")      # 3.1416

## Width and padding
print(f"{42:10d}")      # '        42'  (right-aligned, width 10)
print(f"{42:<10d}")     # '42        '  (left-aligned)
print(f"{42:^10d}")     # '    42    '  (centered)
print(f"{42:010d}")     # '0000000042' (zero-padded)

## Thousands separator
print(f"{1000000:,}")   # 1,000,000

## Percentage
ratio = 0.756
print(f"{ratio:.1%}")   # 75.6%

## Scientific notation
print(f"{0.000123:.2e}")  # 1.23e-04
```

This formatting system is especially useful when output should look aligned or predictable, such as tables, reports, prices, percentages, or scientific values.

```python
item = "Book"
price = 12.5

print(f"{item:<10} ${price:>6.2f}")
```

### Debugging with `=`

Python 3.8+ added a handy `=` specifier that prints the expression and its value — great for quick debugging:

```python
x = 42
y = [1, 2, 3]
print(f"{x=}")          # x=42
print(f"{y=}")          # y=[1, 2, 3]
print(f"{x * 2 + 1=}")  # x * 2 + 1=85
```

This is excellent for short investigations because you see both the expression and the result in one place. It reduces the guesswork when debugging small programs.

### Other Formatting Approaches

While f-strings are preferred for new code, you may encounter older styles in existing codebases:

```python
## str.format() — Python 2.6+
print("Hello, {}!".format("World"))
print("{name} is {age}".format(name="Alice", age=30))

## % formatting — oldest style, still common in logging
print("Hello, %s! You are %d years old." % ("Alice", 30))
```

You will still see these older styles in tutorials, libraries, and legacy code. Knowing them helps you read existing Python even if you choose f-strings for new work.

For **logging**, the `%`-style is intentionally used because `logging` can skip the formatting entirely when the log level is disabled:

```python
import logging
logging.debug("User %s logged in from %s", username, ip_address)
## String is only formatted if DEBUG level is active
```

Practical rule:

- use f-strings for everyday output
- recognize `.format()` when reading older code
- keep `%` formatting in mind for logging APIs

---

<a id="operators"></a>

## Operators

### Arithmetic Operators

Python's arithmetic operators work as expected, with a few worth noting: `/` always produces a float (true division), `//` performs floor division (rounds toward negative infinity), and `**` is the power operator.

```python
print(7 + 2)    # 9
print(7 - 2)    # 5
print(7 * 2)    # 14
print(7 / 2)    # 3.5   — always float
print(7 // 2)   # 3     — floor division
print(7 % 2)    # 1     — modulo (remainder)
print(7 ** 2)   # 49    — exponentiation
```

Floor division rounds toward **negative infinity**, not zero:

```python
print(-7 // 2)   # -4  (not -3)
print(7 // -2)   # -4
```

That "rounds toward negative infinity" detail is easy to miss. If you expected truncation toward zero, negative examples can look surprising at first.

### Comparison & Logical Operators

Comparison operators return `True` or `False`. Python supports **chained comparisons**, which read naturally and are more efficient than separate `and` comparisons:

```python
x = 7
print(x > 5)          # True
print(x != 10)        # True
print(0 < x < 10)     # True  — equivalent to (0 < x) and (x < 10)
print(1 < 2 < 3 < 4)  # True  — any number of chained comparisons
```

Logical operators use English words, not symbols:

```python
print(x > 5 and x < 10)   # True
print(x > 10 or x < 5)    # False
print(not x == 7)          # False
```

**Short-circuit evaluation:** `and` stops at the first falsy value; `or` stops at the first truthy value. They return the actual value that determined the outcome (not just `True`/`False`):

```python
name = ""
result = name or "Anonymous"   # "Anonymous" — name is falsy
items = [1, 2, 3]
first = items and items[0]     # 1 — items is truthy, so evaluates items[0]
```

This "return the actual value" behavior is why expressions like `user_name or "Anonymous"` are so common in Python. The operators are not limited to plain booleans; they also help choose between real values.

### Assignment Operators

Augmented assignment operators update a variable in place. Under the hood, `x += 5` calls `x.__iadd__(5)` if available (which modifies the object in-place for mutable types like lists) or falls back to `x = x + 5`:

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

For immutable types like integers and strings, this usually means rebinding the name to a new value. For mutable types like lists, the operation may update the existing object in place.

```python
numbers = [1, 2]
alias = numbers

numbers += [3]
print(alias)  # [1, 2, 3]
```

That behavior connects directly to the reference model explained in the Variables page.

### Identity and Membership Operators

`is` tests whether two variables refer to the **same object** in memory (not just equal values). `in` tests for membership in a sequence, set, or dict:

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

Use `==` when you care about value equality, and `is` when you care about object identity. Beginners often write `x is 5` or `name is "Alice"`, but value comparisons should normally use `==`.

### Walrus Operator `:=` (Python 3.8+)

The walrus operator assigns a value **and** returns it as an expression. This is useful for avoiding redundant calls or extra temporary variables:

```python
data = [1, 2, 3, 4, 5]

## Without walrus: len() called twice or needs a temp variable
if len(data) > 3:
    print(f"List has {len(data)} items")

## With walrus: computed once, used twice
if (n := len(data)) > 3:
    print(f"List has {n} items")
```

It is especially useful in `while` loops that read until a sentinel value:

```python
import sys

while line := sys.stdin.readline():
    process(line)

## Reading file in chunks without while True + break:
with open("large_file.bin", "rb") as f:
    while chunk := f.read(8192):
        process(chunk)
```

And in comprehensions where you want to compute a value once and filter by it:

```python
results = [y for x in range(20) if (y := x ** 2) > 50]
```

Use this operator with restraint. It is most helpful when it removes repeated work and keeps the code easier to read. If it makes the condition harder to understand, a normal assignment is better.

### Bitwise Operators

Python integers support bitwise operations, which operate on the binary representation:

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

These operators are less common in beginner application code, but they appear in low-level programming, flags, permissions, binary protocols, and performance-sensitive logic.

---

<a id="falsy-values"></a>

## Falsy Values

### What is Truthiness?

Python's `if` statement and boolean operators do not require an explicit `True` or `False`. Instead, every object has a **truthiness** — it can be evaluated in a boolean context. An object is either **truthy** (behaves like `True`) or **falsy** (behaves like `False`).

This is one of the most Pythonic ideas for beginners to learn early. Instead of writing verbose checks such as `if len(items) > 0`, Python often lets you write the shorter and more natural `if items`.

```python
items = [1, 2, 3]

if items:
    print("We have data")
```

If `items` were empty, that condition would evaluate to `False`.

### The Complete List of Falsy Values

The following values evaluate to `False` in any boolean context. Everything else is truthy.

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

This explains why the same `if value:` pattern works across many types. Python is not asking "is this literally `True`?" It is asking "should this value count as true in a boolean context?"

### Practical Patterns

Truthiness enables clean, idiomatic code:

```python
## Guard against empty collections
def process(items):
    if not items:
        print("Nothing to process")
        return
    for item in items:
        ...

## Default values with 'or'
name = user_input or "Anonymous"  # if user_input is "", use fallback
port = config.get("port") or 8080

## Count truthy values in a list
flags = [True, False, True, None, 1, 0, "yes", ""]
print(sum(bool(f) for f in flags))  # 4
```

These patterns are concise, but they must still match your intent. For example, `port = config.get("port") or 8080` treats `0` as missing because `0` is falsy. That may be correct, or it may hide a real value.

When `None` specifically means "missing", be explicit:

```python
port = config.get("port")
if port is None:
    port = 8080
```

### Custom Truthiness

You can control how your own classes behave in boolean context by implementing `__bool__` (or `__len__` as a fallback — Python calls `len(obj) != 0` if `__bool__` is not defined):

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

This works because Python first looks for `__bool__()`. If that method is not defined, it falls back to `__len__()` and treats zero length as falsy.

The practical takeaway is simple:

- empty containers are falsy
- zero numeric values are falsy
- `None` is falsy
- most other values are truthy

Once that rule feels natural, your conditions become much easier to read.

---

<a id="chapter-ii-data-structures"></a>

## Chapter II: Data Structures

Python's core data structures and when to use each.

This chapter moves from single values to collections of values. The key shift is not just learning new syntax, but learning to choose the right container for the job:

- lists when order and mutation matter
- tuples when fixed structure matters
- dictionaries when values need names or keys
- sets when uniqueness and fast membership checks matter

If Chapter I taught you what Python values are, this chapter teaches you how Python groups and organizes them.

### Sections

- [Lists](./lists)
- [Tuples](./tuples)
- [Dictionaries](./dictionaries)
- [Sets](./sets)
- [Collections Module](./collections-module)
- [Comprehensions](./comprehensions)
- [Type Conversion](./type-conversion)

---

<a id="lists"></a>

## Lists

Lists are usually the first real collection Python learners rely on heavily. They are flexible, easy to read, and useful in everyday code, but they also introduce important ideas like mutation, shared references, and performance tradeoffs.

As you read this page, focus on when a list is the right default choice and when another container would express your intent more clearly.

### What is a List?

A list is an **ordered, mutable** sequence of objects. Lists can hold any mix of types and can grow or shrink at runtime. They are Python's most versatile built-in collection.

```python
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, None]
nested = [[1, 2], [3, 4], [5, 6]]
empty = []
```

### Indexing and Slicing

Python lists are zero-indexed. Negative indexes count from the end. Slicing returns a **new** list — it does not modify the original.

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

Because lists are mutable, you can change them in place:

```python
fruits = ["apple", "banana", "cherry"]

## Add elements
fruits.append("date")            # add to end: O(1) amortized
fruits.insert(1, "blueberry")    # insert at index: O(n)
fruits.extend(["elderberry", "fig"])  # add multiple: O(k)

## Remove elements
fruits.remove("banana")          # remove first occurrence by value: O(n)
popped = fruits.pop()            # remove and return last: O(1)
popped2 = fruits.pop(0)         # remove and return at index: O(n)
del fruits[1]                    # remove at index without returning

## In-place modification
fruits[0] = "avocado"            # replace by index
fruits[1:3] = ["kiwi", "mango"] # replace a slice
```

### Sorting

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

numbers.sort()                    # in-place, ascending
numbers.sort(reverse=True)        # in-place, descending

sorted_copy = sorted(numbers)     # returns NEW list, original unchanged

## Sort with a custom key
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

## Check membership: O(n) — use a set if you need fast lookups
print(5 in items)          # True/False
```

### Performance Notes

Lists are backed by a dynamic array. This means:
- **Indexing** and **appending** are O(1) amortized.
- **Inserting or removing** at the front or middle is O(n) — all elements after the point must shift.
- For frequent front operations, use `collections.deque` instead.

### List Copying

Assignment creates a new reference to the **same** list, not a copy:

```python
a = [1, 2, 3]
b = a             # b is the SAME list
b.append(4)
print(a)          # [1, 2, 3, 4]

## Shallow copy — new list, but nested objects still shared
c = a.copy()      # or: a[:]  or: list(a)
c.append(99)
print(a)          # [1, 2, 3, 4] — unaffected

## Deep copy — recursively copies all nested objects
import copy
d = copy.deepcopy(a)
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

Dictionaries are one of Python's most important data structures because they let you attach meaning to values through keys. When you need lookup by name, ID, or label, a dictionary is often the most natural fit.

This page is easiest to understand if you think of a dictionary as a mapping from keys to values rather than as a sequence with positions.

### What is a Dictionary?

A dictionary is a **mutable mapping** of unique keys to values. As of Python 3.7+, dictionaries preserve **insertion order**. Lookup by key is O(1) on average (backed by a hash table). Keys must be hashable — strings, numbers, and tuples of hashables all work; lists and dicts cannot be keys.

```python
person = {"name": "Alice", "age": 30, "city": "New York"}
empty = {}
from_pairs = dict([("a", 1), ("b", 2)])
from_kwargs = dict(name="Alice", age=30)
```

### Accessing Values

```python
person = {"name": "Alice", "age": 30}

## Direct access — raises KeyError if the key doesn't exist
print(person["name"])          # "Alice"

## Safe access with a default
print(person.get("email"))          # None
print(person.get("email", "N/A"))   # "N/A"

## Check if a key exists before accessing
if "age" in person:
    print(person["age"])
```

### Modifying Dictionaries

```python
person = {"name": "Alice", "age": 30}

## Add or update a key
person["email"] = "alice@example.com"
person["age"] = 31

## Merge another dict (Python 3.9+ syntax)
person |= {"city": "Boston", "lang": "Python"}

## update() works in all versions
person.update({"country": "US"})

## Remove a key
del person["lang"]                      # raises KeyError if missing
email = person.pop("email")             # remove and return value
removed = person.pop("missing", None)   # safe remove with default

## Remove last inserted item (Python 3.7+ order is guaranteed)
last_key, last_val = person.popitem()
```

### Iterating

```python
person = {"name": "Alice", "age": 30, "city": "NY"}

for key in person:                 # iterate over keys (default)
    print(key)

for key in person.keys():          # explicit keys view
    print(key)

for value in person.values():      # values view
    print(value)

for key, value in person.items():  # key-value pairs
    print(f"{key}: {value}")
```

The views returned by `.keys()`, `.values()`, and `.items()` are **live views** — they reflect changes to the dict without creating a copy.

### Dict Comprehensions

```python
squares = {x: x**2 for x in range(6)}
## {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

## Invert a dictionary (assuming unique values)
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
## {1: "a", 2: "b", 3: "c"}

## Filter while building
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
```

### Merging Dictionaries

```python
defaults = {"color": "blue", "size": 10, "visible": True}
overrides = {"size": 20, "opacity": 0.8}

## Python 3.9+ — | operator
merged = defaults | overrides
## {"color": "blue", "size": 20, "visible": True, "opacity": 0.8}

## Older style
merged = {**defaults, **overrides}   # right side wins on conflict
```

### `setdefault` and `defaultdict`

`setdefault` is useful for grouping — it inserts a default value only if the key is missing, then returns the value:

```python
groups = {}
for word in ["apple", "ant", "banana", "bear"]:
    groups.setdefault(word[0], []).append(word)
## {"a": ["apple", "ant"], "b": ["banana", "bear"]}
```

For this pattern, `collections.defaultdict` is even cleaner — see the [Collections Module](./collections-module) page.

---

<a id="sets"></a>

## Sets

Sets are designed for uniqueness and fast membership testing. They are less about storing values in order and more about answering questions like "have I seen this before?" or "what values overlap between these groups?"

That is why sets become especially useful in validation, deduplication, and comparison tasks.

### What is a Set?

A set is an **unordered collection of unique, hashable objects**. Sets are backed by a hash table, giving O(1) average-case performance for membership tests, insertion, and deletion. Because sets are unordered, they do not support indexing or slicing.

The primary use cases for sets are:
- **Deduplication** — removing duplicates from any sequence
- **Membership testing** — `x in my_set` is O(1) vs O(n) for a list
- **Set operations** — unions, intersections, and differences

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

Set algebra is built directly into Python:

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

## Union — all elements from both
print(a | b)         # {1, 2, 3, 4, 5, 6}
print(a.union(b))    # same

## Intersection — only elements in both
print(a & b)              # {3, 4}
print(a.intersection(b))  # same

## Difference — in a but not in b
print(a - b)              # {1, 2}
print(a.difference(b))    # same

## Symmetric difference — in either, but not both
print(a ^ b)                        # {1, 2, 5, 6}
print(a.symmetric_difference(b))    # same
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
## Deduplication while preserving order (Python 3.7+)
def deduplicate(items):
    seen = set()
    return [x for x in items if not (x in seen or seen.add(x))]

## Fast membership test
VALID_EXTENSIONS = {".py", ".txt", ".json", ".yaml"}
filename = "script.py"
if filename.endswith(tuple(VALID_EXTENSIONS)):
    print("Valid file")

## Find common elements between two lists efficiently
list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 6, 7]
common = set(list_a) & set(list_b)  # {3, 4, 5}
only_in_a = set(list_a) - set(list_b)  # {1, 2}
```

### Frozensets

A `frozenset` is an **immutable** set — it can be used as a dictionary key or stored in another set:

```python
fs = frozenset([1, 2, 3])
d = {fs: "value"}       # works because frozenset is hashable
## fs.add(4)             # AttributeError — frozensets are immutable
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

Comprehensions are a compact way to build collections from other iterables. They are one of Python's most recognizable idioms, but they work best when they stay readable and focused on a single transformation.

The goal here is to understand why comprehensions feel natural in Python, and also where a normal loop is the better choice.

### What Are Comprehensions?

Comprehensions are concise expressions for building new collections by transforming and filtering existing iterables. They replace verbose `for` loops and are generally faster because they are optimized at the bytecode level.

### List Comprehensions

The general form is `[expression for item in iterable if condition]`. The `if` clause is optional.

```python
## Basic — square each number
squares = [x**2 for x in range(10)]
## [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

## With filter — only even numbers
evens = [x for x in range(20) if x % 2 == 0]

## Transform strings
words = ["hello", "world", "python"]
upper = [w.upper() for w in words]

## Equivalent for-loop (less idiomatic):
result = []
for x in range(10):
    result.append(x**2)
```

**Nested comprehensions** — process 2D data:

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

## Flatten
flat = [n for row in matrix for n in row]
## [1, 2, 3, 4, 5, 6, 7, 8, 9]

## Transpose
transposed = [[row[i] for row in matrix] for i in range(3)]
```

### Dict Comprehensions

```python
## Map word → length
words = ["Python", "is", "great"]
lengths = {word: len(word) for word in words}
## {"Python": 6, "is": 2, "great": 5}

## Filter a dict
prices = {"apple": 1.0, "banana": 0.5, "cherry": 2.0}
expensive = {k: v for k, v in prices.items() if v > 0.8}
## {"apple": 1.0, "cherry": 2.0}
```

### Set Comprehensions

```python
## Unique squares — duplicates automatically removed
unique = {x**2 for x in [-2, -1, 0, 1, 2]}
## {0, 1, 4}

## All unique first letters
words = ["apple", "ant", "banana", "avocado"]
first_letters = {w[0] for w in words}  # {"a", "b"}
```

### Generator Expressions

A **generator expression** looks like a list comprehension but uses parentheses `()`. It does **not** build the collection in memory — it produces values lazily, one at a time. Use these when you only need to iterate once or when the collection would be very large.

```python
## List comprehension — builds all 1M items in memory immediately
big_list = [x**2 for x in range(1_000_000)]

## Generator expression — computes each value on demand
gen = (x**2 for x in range(1_000_000))  # barely any memory used

## Works with any function that accepts an iterable
total = sum(x**2 for x in range(1_000_000))
maximum = max(len(line) for line in open("file.txt"))
any_even = any(x % 2 == 0 for x in range(100))
```

When you pass a generator expression as the only argument to a function, you can omit the extra parentheses: `sum(x**2 for x in range(10))`.

### When to Use Comprehensions

Use comprehensions when the logic is simple and readable. If you need side effects (like printing), multiple conditions, or complex logic, a regular `for` loop is clearer:

```python
## Fine as a comprehension
doubles = [x * 2 for x in data if x > 0]

## Too complex — use a loop instead
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

See the [Falsy Values](../01-the-basics/falsy-values) page for the full rules.

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

Conditional logic and loops.

This chapter is about deciding what code runs and how many times it runs. These tools look simple, but they are the foundation of almost every real program:

- `if` and `elif` choose between paths
- `match` expresses structured branching more clearly in some cases
- loops let you process repeated data without repeating code by hand

The main skill here is learning to read code as execution flow: what happens first, what gets skipped, and what repeats.

### Sections

- [If / Else](./if-else)
- [Match / Case](./match-case)
- [Loops](./loops)

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

Loops let you express repetition without duplicating code. In Python, the biggest shift for many learners is understanding that `for` usually means "loop over items" rather than "manually control an index."

That design makes Python loops read more directly, but it also means you should pay attention to what object is being iterated and whether the loop is mutating data along the way.

### `for` Loops

Python's `for` loop iterates over any **iterable** — lists, strings, ranges, dicts, files, generators, and anything that implements the iterator protocol:

```python
## Iterate over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

## Iterate over a string
for char in "Python":
    print(char)

## Iterate over a range
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 10, 2):  # start, stop (exclusive), step
    print(i)               # 2, 4, 6, 8
```

### `enumerate()` — Index + Value

When you need both the index and the value, use `enumerate()` instead of indexing manually:

```python
fruits = ["apple", "banana", "cherry"]

## Don't do this:
for i in range(len(fruits)):
    print(i, fruits[i])

## Do this:
for i, fruit in enumerate(fruits):
    print(i, fruit)

## Start the counter at a different value
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")
```

### `zip()` — Parallel Iteration

`zip()` pairs elements from multiple iterables and stops when the shortest is exhausted:

```python
names = ["Alice", "Bob", "Charlie"]
scores = [95, 80, 88]

for name, score in zip(names, scores):
    print(f"{name}: {score}")

## Unzip (transpose)
pairs = [(1, "a"), (2, "b"), (3, "c")]
numbers, letters = zip(*pairs)  # (1, 2, 3), ('a', 'b', 'c')
```

### `while` Loops

`while` repeats as long as its condition is truthy:

```python
count = 0
while count < 5:
    print(count)
    count += 1

## Reading until a condition
total = 0
while True:
    value = int(input("Enter number (0 to stop): "))
    if value == 0:
        break
    total += value
print(f"Total: {total}")
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

## Loop else: useful for search patterns
def find_prime(numbers):
    for n in numbers:
        if n < 2:
            continue
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                break       # n is not prime
        else:
            print(f"{n} is prime")  # only runs if inner loop didn't break
```

### Iterating Over Dictionaries

```python
person = {"name": "Alice", "age": 30, "city": "NY"}

for key in person:           # keys (default)
    print(key)

for key, value in person.items():
    print(f"{key}: {value}")

## Modify values (never add/remove keys during iteration)
person = {k: v * 2 if isinstance(v, int) else v for k, v in person.items()}
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

Defining and calling functions in Python.

Functions are where small scripts start becoming reusable programs. This chapter teaches you how to package logic into named units, control inputs and outputs, and keep code manageable as it grows.

Focus on three ideas as you read:

- a function is a reusable block of behavior
- parameters describe what a function needs
- return values describe what a function produces

Once these ideas feel natural, later topics like modules, classes, and decorators become much easier.

### Sections

- [Defining Functions](./defining-functions)
- [Parameters & Arguments](./parameters-arguments)
- [Lambda Functions](./lambda-functions)
- [Scoping Rules](./scoping-rules)
- [Type Hints](./type-hints)

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

Scoping rules explain where Python looks for names and why some assignments behave differently than beginners expect. This is one of the most important mental models in the language because it affects functions, closures, imports, and debugging.

If a name lookup or reassignment has ever felt surprising, LEGB is usually the reason.

### The LEGB Rule

When Python encounters a name (variable, function, class), it searches four scopes in order until it finds the name or raises a `NameError`:

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

By default, assignment inside a function creates a **new local variable** — it does not modify the global. To modify a global variable, you must declare it with `global`:

```python
counter = 0

def increment():
    global counter      # without this, we'd create a local 'counter'
    counter += 1

increment()
increment()
print(counter)  # 2
```

Use `global` sparingly. Shared mutable global state makes code harder to test and reason about. Prefer passing values as arguments and returning updated values.

### The `nonlocal` Keyword

`nonlocal` allows an inner function to modify a variable in an **enclosing** (but not global) scope. This is the key mechanism behind closures with state:

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

A **closure** is a function that "closes over" variables from its enclosing scope — those variables continue to exist even after the outer function returns:

```python
def make_multiplier(factor):
    def multiply(x):
        return x * factor   # 'factor' is captured in the closure
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))   # 10
print(triple(5))   # 15

## Inspect captured variables
print(double.__closure__[0].cell_contents)  # 2
```

### A Common Closure Gotcha — Late Binding

Variables in closures are looked up at **call time**, not at definition time. This catches many developers off guard in loops:

```python
## BUG — all functions print 4
funcs = [lambda: i for i in range(5)]
for f in funcs:
    print(f())   # 4, 4, 4, 4, 4

## FIX — capture the current value of i with a default argument
funcs = [lambda i=i: i for i in range(5)]
for f in funcs:
    print(f())   # 0, 1, 2, 3, 4
```

### Variable Scope and the `UnboundLocalError`

If you assign to a name anywhere in a function, Python treats it as local **everywhere** in that function — even before the assignment:

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

## Type Hints

Type hints add structure to Python code without changing Python into a statically typed language. They are best understood as communication tools for readers, editors, and type checkers rather than runtime enforcement.

This page is about learning what hints express well, where they help maintainability, and why they remain optional in normal Python execution.

### What Are Type Hints?

Introduced in PEP 484, **type hints** are optional annotations that document the expected types of function parameters and return values. Python **does not enforce them at runtime** — they are purely informational for developers and static analysis tools like `mypy`, `pyright`, and IDEs.

```python
def add(a: int, b: int) -> int:
    return a + b

def greet(name: str) -> str:
    return f"Hello, {name}!"
```

The `->` annotation on the function signature declares the return type. Both annotations are accessible via `add.__annotations__`.

### Common Annotations

```python
from typing import Optional, Union, Any

## Optional — the value can be the type or None
def find(items: list, target: int) -> Optional[int]:
    for i, item in enumerate(items):
        if item == target:
            return i
    return None

## Python 3.10+ shorthand (preferred for new code)
def find2(items: list, target: int) -> int | None:
    ...

## Union — multiple possible types
def process(value: int | str | None) -> str:
    return str(value) if value is not None else ""

## Any — opt out of checking (use sparingly)
def debug(value: Any) -> None:
    print(repr(value))
```

### Generic Collections (Python 3.9+)

Before Python 3.9, you had to import generics from `typing`. Since 3.9, built-in types support subscripting directly:

```python
## Python 3.9+
def first(items: list[int]) -> int:
    return items[0]

def merge(a: dict[str, int], b: dict[str, int]) -> dict[str, int]:
    return {**a, **b}

def flatten(matrix: list[list[float]]) -> list[float]:
    return [x for row in matrix for x in row]

## Tuple with specific element types
def stats(data: list[float]) -> tuple[float, float, float]:
    return min(data), max(data), sum(data) / len(data)
```

### Type Aliases

Give a meaningful name to a complex type to improve readability:

```python
from typing import TypeAlias

Vector: TypeAlias = list[float]
Matrix: TypeAlias = list[list[float]]
JSONValue: TypeAlias = str | int | float | bool | None | dict | list

def dot_product(a: Vector, b: Vector) -> float:
    return sum(x * y for x, y in zip(a, b))
```

### Callable Types

When a parameter is a function, annotate it with `Callable`:

```python
from collections.abc import Callable

def apply(func: Callable[[int], int], value: int) -> int:
    return func(value)

def apply_all(
    funcs: list[Callable[[str], str]],
    text: str,
) -> str:
    for fn in funcs:
        text = fn(text)
    return text
```

### Running `mypy`

Type hints are most useful when checked with a static type checker:

```bash
pip install mypy
mypy my_script.py
```

`mypy` will report type errors — arguments passed with the wrong type, return values that don't match, and missing annotations — before you even run the code.

---

<a id="chapter-v-object-oriented-programming"></a>

## Chapter V: Object-Oriented Programming

Classes, inheritance, and Python's OOP toolset.

Object-oriented programming in Python is best understood as a way to model state and behavior together. This chapter is not about using classes everywhere; it is about knowing when objects help code become clearer and more maintainable.

Keep these ideas in mind:

- classes define behavior and data together
- instances represent concrete objects created from those class definitions
- inheritance and composition are tools, not goals

Python supports OOP well, but it also stays flexible, so the real skill is learning where OOP improves design and where simpler code is better.

### Sections

- [Classes](./classes)
- [Inheritance](./inheritance)
- [Abstract Base Classes](./abstract-base-classes)
- [Magic Methods](./magic-methods)
- [Dataclasses](./dataclasses)

---

<a id="classes"></a>

## Classes

Classes are Python's main tool for bundling related data and behavior into a single abstraction. They are useful when values need associated operations or when many objects share the same structure.

The key beginner shift is to see a class as a definition and an instance as a concrete object created from that definition.

### Defining a Class

A class is a blueprint for creating objects. It bundles **data** (attributes) and **behavior** (methods) together. The `__init__` method is the initializer — it runs automatically when a new instance is created.

```python
class Dog:
    # Class attribute — shared by ALL instances
    species = "Canis familiaris"

    # __init__ is the initializer (not the constructor — __new__ creates the object)
    def __init__(self, name: str, age: int):
        # Instance attributes — unique to each object
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

`self` is a reference to the current instance. It is passed automatically when you call a method on an object. The name `self` is a convention — Python does not enforce it — but you should always use it.

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

Class attributes are defined on the class and shared by all instances. Instance attributes are defined on `self` and unique to each instance. **Assigning to an instance attribute always shadows the class attribute** — it does not modify it:

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

    # Regular method — receives instance as first arg
    def to_fahrenheit(self) -> float:
        return self.celsius * 9 / 5 + 32

    # Class method — receives the CLASS as first arg (useful for factory methods)
    @classmethod
    def from_fahrenheit(cls, fahrenheit: float) -> "Temperature":
        return cls((fahrenheit - 32) * 5 / 9)

    # Static method — no implicit first argument; a plain function scoped to the class
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

Use `@property` to make a method callable like an attribute — great for computed values or adding validation:

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
## c.radius = -1     # ValueError
```

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
        return 2 * (self.width + self.height)

## Shape()  # TypeError: can't instantiate abstract class
c = Circle(5)
print(c.describe())  # Area: 78.54, Perimeter: 31.42
```

---

<a id="magic-methods"></a>

## Magic Methods

Magic methods are what let custom classes participate naturally in Python syntax. They are the reason your own objects can work with `print()`, `len()`, operators, iteration, comparisons, and context managers.

The important idea is not memorizing every dunder method. It is understanding that Python syntax often dispatches to these methods under the hood.

### What Are Magic Methods?

**Magic methods** (also called dunder methods — "double underscore") are special methods that Python calls automatically in response to built-in operations. By implementing them, your classes integrate seamlessly with Python's syntax and built-in functions.

### String Representation

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        # Unambiguous representation — for developers and debugging
        # Ideally: eval(repr(obj)) == obj
        return f"Point({self.x!r}, {self.y!r})"

    def __str__(self) -> str:
        # Human-readable representation — for print() and str()
        return f"({self.x}, {self.y})"

p = Point(3, 4)
print(repr(p))   # Point(3, 4)
print(str(p))    # (3, 4)
print(p)         # (3, 4)  — print() calls __str__
```

If only `__repr__` is defined, `str(obj)` falls back to it.

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
        return self.__mul__(scalar)    # supports 3 * vector (reversed)

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

@total_ordering   # auto-generates <, <=, >=, > from __eq__ and __lt__
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
print(t2 >= t1)   # True  — generated by @total_ordering
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

See the [Context Managers](../06-advanced-python-techniques/context-managers) page for a full explanation.

```python
class Timer:
    def __enter__(self):
        import time
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.elapsed = time.time() - self.start
        return False   # don't suppress exceptions

with Timer() as t:
    sum(range(1_000_000))
print(f"Elapsed: {t.elapsed:.4f}s")
```

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

Language features and standard-library techniques that make Python code more expressive and efficient.

This chapter focuses on advanced techniques that show up across the Python language and standard library. These topics are not just about style. They are practical tools for iteration, abstraction, resource management, and cleaner control over how code behaves.

As you read, ask two questions:

- what problem does this pattern solve?
- when is it clearer than a more explicit alternative?

Advanced Python is not about writing the shortest code possible. It is about choosing features and tools that fit the language naturally and make the design clearer.

### Sections

- [Iterators & Generators](./iterators-generators)
- [itertools & functools](./itertools-functools)
- [Decorators](./decorators)
- [Context Managers](./context-managers)
- [Pattern Matching](./pattern-matching)

---

<a id="iterators-generators"></a>

## Iterators & Generators

Iterators and generators explain why Python can process data lazily instead of building every result in memory upfront. They are central to how loops, comprehensions, files, and many library tools work.

If you understand this page well, a lot of Python's "it just works in a for loop" behavior becomes much less magical.

### The Iterator Protocol

An **iterable** is any object you can loop over — lists, tuples, strings, files, ranges. An **iterator** is an object with a `__next__()` method that returns the next value and raises `StopIteration` when exhausted.

`iter()` converts an iterable into an iterator; `next()` retrieves the next value:

```python
lst = [1, 2, 3]
it = iter(lst)
print(next(it))   # 1
print(next(it))   # 2
print(next(it))   # 3
## next(it)        # StopIteration

## A for loop is just:
## it = iter(lst)
## while True:
##     try: value = next(it)
##     except StopIteration: break
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

Writing the full iterator class above is verbose. A **generator function** using `yield` does the same in far fewer lines:

```python
def countdown(start: int):
    while start >= 0:
        yield start   # suspends here, returns value; resumes on next()
        start -= 1

for n in countdown(3):
    print(n)    # 3, 2, 1, 0
```

When Python sees `yield` in a function, calling that function returns a **generator object** — it does not execute the body immediately. The body runs step-by-step as `next()` is called on the generator.

### Generators are Lazy

Generators produce values on demand. They do not compute the whole sequence upfront, making them ideal for large or infinite sequences:

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

A generator expression is the lazy equivalent of a list comprehension. Use `()` instead of `[]`:

```python
numbers = range(1_000_000)

## List comprehension — creates full list in memory immediately
squares_list = [x**2 for x in numbers]

## Generator expression — lazy, one value at a time
squares_gen = (x**2 for x in numbers)

## Useful in function calls — no double parentheses needed in sum()
total = sum(x**2 for x in range(1_000))
```

### `yield from`

`yield from` delegates to another iterable or generator — flattening or chaining:

```python
def chain(*iterables):
    for it in iterables:
        yield from it    # same as: for item in it: yield item

list(chain([1, 2], "abc", range(3)))
## [1, 2, 'a', 'b', 'c', 0, 1, 2]

def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)   # recursive
        else:
            yield item

list(flatten([1, [2, [3, 4]], 5]))
## [1, 2, 3, 4, 5]
```

### `send()` — Coroutines

Generators can receive values via `send()`. This enables cooperative coroutines (though `async`/`await` is now preferred for that):

```python
def running_average():
    total = 0.0
    count = 0
    while True:
        value = yield (total / count if count else None)
        total += value
        count += 1

avg = running_average()
next(avg)               # prime the generator (advance to first yield)
avg.send(10)            # total=10, count=1
avg.send(20)            # total=30, count=2
print(avg.send(30))     # 20.0  — (10+20+30)/3
```

---

<a id="itertools-functools"></a>

## itertools & functools

These two modules are full of tools that make existing Python code more composable. They are not required for everyday beginner code, but they become extremely valuable once you start combining iterables, caching results, or passing functions around.

The best way to read this page is as a toolbox: learn the shape of the problems these modules solve, then revisit the specific functions when needed.

### `itertools` — Efficient Iteration

`itertools` provides composable, lazy iterators for common looping patterns. All functions return iterators — they produce values on demand without creating intermediate lists.

#### Combining Iterables

```python
import itertools

## chain — concatenate multiple iterables
list(itertools.chain([1, 2], [3, 4], [5]))   # [1, 2, 3, 4, 5]

## chain.from_iterable — flatten one level of nesting
nested = [[1, 2], [3, 4], [5]]
list(itertools.chain.from_iterable(nested))  # [1, 2, 3, 4, 5]

## zip_longest — zip but pad shorter iterables
list(itertools.zip_longest([1, 2, 3], ["a", "b"], fillvalue="-"))
## [(1, 'a'), (2, 'b'), (3, '-')]
```

#### Slicing and Filtering

```python
## islice — lazy slice of any iterable (no index required)
first_five = list(itertools.islice(range(1_000_000), 5))   # [0, 1, 2, 3, 4]

## takewhile / dropwhile
list(itertools.takewhile(lambda x: x < 5, range(10)))  # [0, 1, 2, 3, 4]
list(itertools.dropwhile(lambda x: x < 5, range(10)))  # [5, 6, 7, 8, 9]

## filterfalse — opposite of filter()
list(itertools.filterfalse(str.isdigit, "a1b2c3"))  # ['a', 'b', 'c']
```

#### Combinatorics

```python
## product — Cartesian product
list(itertools.product([1, 2], ["a", "b"]))
## [(1,'a'), (1,'b'), (2,'a'), (2,'b')]

## combinations — unique pairs without repetition
list(itertools.combinations([1, 2, 3], 2))
## [(1, 2), (1, 3), (2, 3)]

## permutations — ordered arrangements
list(itertools.permutations([1, 2, 3], 2))
## [(1,2), (1,3), (2,1), (2,3), (3,1), (3,2)]

## combinations_with_replacement
list(itertools.combinations_with_replacement("AB", 2))
## [('A','A'), ('A','B'), ('B','B')]
```

#### Grouping

```python
## groupby — groups consecutive items with the same key (sort first!)
data = [("Alice", "Eng"), ("Bob", "Eng"), ("Carol", "HR"), ("Dave", "HR")]
data.sort(key=lambda x: x[1])

for dept, members in itertools.groupby(data, key=lambda x: x[1]):
    print(dept, [m[0] for m in members])
## Eng ['Alice', 'Bob']
## HR  ['Carol', 'Dave']
```

#### Batching (Python 3.12+)

```python
## batched — split iterable into fixed-size chunks
for batch in itertools.batched(range(10), 3):
    print(batch)   # (0,1,2) then (3,4,5) then (6,7,8) then (9,)
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

## Useful with map/sorted
from functools import partial
import operator

multiply_by_3 = partial(operator.mul, 3)
list(map(multiply_by_3, [1, 2, 3, 4]))   # [3, 6, 9, 12]
```

#### `reduce` — Fold Over a Sequence

```python
from functools import reduce
import operator

## Sum — same as sum([1,2,3,4,5])
reduce(operator.add, [1, 2, 3, 4, 5])    # 15

## Product of list
reduce(operator.mul, [1, 2, 3, 4, 5])    # 120

## Max — same as max([3,1,4,1,5,9])
reduce(lambda a, b: a if a > b else b, [3, 1, 4, 1, 5, 9])  # 9
```

Prefer built-in `sum()`, `max()`, `min()` where possible — `reduce` is for custom fold operations.

#### `total_ordering`

See the [Magic Methods](../05-oop/magic-methods) page — `@total_ordering` generates comparison methods from `__eq__` and `__lt__`.
```

```python
import functools

## lru_cache — memoize function results
@functools.lru_cache(maxsize=128)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

## cache (Python 3.9+) — unbounded lru_cache
@functools.cache
def expensive(x):
    return x ** 2

## reduce — fold a sequence into a single value
from functools import reduce
product = reduce(lambda acc, x: acc * x, [1, 2, 3, 4, 5])  # 120

## partial — pre-fill arguments
from functools import partial
power_of_two = partial(pow, 2)
print(power_of_two(10))  # 1024
```

---

<a id="decorators"></a>

## Decorators

Decorators are a Python way to wrap behavior around functions or classes without editing their core logic directly. They are powerful, but they also introduce an extra layer of indirection, so clarity matters.

The main goal here is to understand what the decoration step actually does to the original callable.

### What is a Decorator?

A decorator is a function that takes another function as input and returns a new function that wraps the original — adding behavior before or after it runs without modifying the original source. The `@decorator` syntax is just syntactic sugar for `func = decorator(func)`.

### A Basic Decorator

```python
import functools

def log_calls(func):
    @functools.wraps(func)   # preserves __name__, __doc__, etc.
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}({args}, {kwargs})")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result!r}")
        return result
    return wrapper

@log_calls
def add(a, b):
    return a + b

add(3, 4)
## Calling add((3, 4), {})
## add returned 7
```

Always use `@functools.wraps(func)` in the wrapper — without it, the wrapped function loses its name, docstring, and signature, which breaks introspection tools like `help()`.

### Decorator with Arguments

To add parameters, add another layer of nesting:

```python
def retry(times: int = 3, exceptions=(Exception,)):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == times:
                        raise
                    print(f"Attempt {attempt} failed: {e}. Retrying...")
        return wrapper
    return decorator

@retry(times=3, exceptions=(ConnectionError,))
def fetch_data(url: str) -> str:
    # Might raise ConnectionError
    ...
```

### Stacking Decorators

Multiple decorators are applied bottom-up — the one closest to `def` is applied first:

```python
@log_calls
@retry(times=2)
def risky_operation():
    ...

## Equivalent to:
## risky_operation = log_calls(retry(times=2)(risky_operation))
```

### Class-Based Decorator

A class can be a decorator by implementing `__call__`:

```python
class Memoize:
    """Cache the return value of expensive function calls."""
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.cache: dict = {}

    def __call__(self, *args):
        if args not in self.cache:
            self.cache[args] = self.func(*args)
        return self.cache[args]

@Memoize
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(35))   # Fast — results are cached
```

Note: Python's standard library already provides `@functools.lru_cache` and `@functools.cache` for memoization.

### Practical Decorators from the Standard Library

```python
import functools

## Cache all calls indefinitely
@functools.cache
def expensive(n: int) -> int:
    return sum(range(n))

## Cache with a maximum size (LRU eviction)
@functools.lru_cache(maxsize=128)
def fib(n: int) -> int:
    return n if n < 2 else fib(n-1) + fib(n-2)

## Mark a method as a property (computed once, then cached)
class Circle:
    def __init__(self, r): self._r = r

    @functools.cached_property
    def area(self):
        import math
        return math.pi * self._r ** 2

c = Circle(5)
print(c.area)   # computed
print(c.area)   # returned from cache
```

    def __call__(self, *args):
        if args not in self.cache:
            self.cache[args] = self.func(*args)
        return self.cache[args]

@Memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

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

    def __enter__(self):
        print(f"Connecting to {self.url}")
        self.conn = "connection"
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing connection")
        self.conn = None
        return False  # Re-raise any exceptions

with DatabaseConnection("db://localhost") as conn:
    print(f"Using {conn}")
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

Organizing code into modules, packages, and distributable projects.

This chapter explains how Python code grows beyond a single file. It covers both the practical side of splitting code into modules and the ecosystem side of installing, structuring, and shipping Python projects.

The main progression is:

- one file becomes many modules
- related modules become packages
- projects gain virtual environments and dependency management
- reusable code can be built and distributed

That structure matters because maintainable Python is not just about syntax; it is also about layout, imports, and clear boundaries between parts of a project.

### Sections

- [Modules](./modules)
- [File I/O & JSON](./file-io-json)
- [Packages](./packages)
- [Virtual Environments](./virtual-environments)
- [Useful Commands](./useful-commands)
- [Build & Packaging](./build-packaging)

---

<a id="modules"></a>

## Modules

Modules are how Python code stops being a single long file and starts becoming a structured program. They let you group related names together, separate concerns, and reuse logic without copying code.

The core mental model is simple: importing a module runs it once, then gives you access to the names it defines.

### What is a Module?

A **module** is any Python file (`.py`). When you `import` a module, Python executes its code once and makes its names available under the module's namespace. Subsequent imports of the same module reuse the cached version from `sys.modules` — the code is not re-executed.

### Importing Modules

```python
## Import the whole module — access names via dot notation
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
## Import specific names into the current namespace
from math import pi, sqrt, ceil
print(pi)          # 3.14159...
print(sqrt(25))    # 5.0

## Import all public names (avoid — pollutes namespace, hides where names come from)
from math import *
```

### Aliases

```python
## Give a module a shorter alias
import numpy as np         # de facto standard
import pandas as pd
import matplotlib.pyplot as plt

## Alias an imported name
from datetime import datetime as dt
now = dt.now()
```

### Module Search Path

When you `import foo`, Python looks for `foo` in this order:

1. `sys.modules` (already-imported modules)
2. Built-in modules (compiled into the interpreter)
3. Directories in `sys.path` — which includes the script's directory, `PYTHONPATH`, and site-packages

```python
import sys
print(sys.path)   # list of directories Python searches
```

### The Standard Library

Python ships with an extensive standard library. Key modules:

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

Any `.py` file is a module. Use the `__name__ == "__main__"` guard to separate code that runs when the file is a script from code that runs when imported:

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

Define `__all__` in a module to specify which names are exported when someone does `from module import *`:

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

File handling is where Python programs start interacting with the outside world. That also means mistakes matter more here: wrong paths, wrong modes, wrong encodings, and missing files are all common real-world issues.

This page is easiest to read if you keep two concerns separate: how to read and write files safely, and how JSON turns Python data into a portable text format.

### Opening Files

Use the built-in `open()` function to open a file. The `with` statement is the correct way to do so — it guarantees the file is closed when the block exits, even if an exception is raised:

```python
with open("data.txt", "r") as f:
    content = f.read()
## File is automatically closed here
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

Always specify `encoding="utf-8"` explicitly on text files to avoid platform-dependent behavior:

```python
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
```

### Reading Files

```python
## Read entire file as a single string
with open("data.txt", encoding="utf-8") as f:
    content = f.read()

## Read all lines into a list (includes newline characters)
with open("data.txt", encoding="utf-8") as f:
    lines = f.readlines()

## Iterate line by line — best for large files (no memory spike)
with open("data.txt", encoding="utf-8") as f:
    for line in f:
        print(line.strip())   # strip() removes the trailing newline

## Read a fixed number of characters
with open("data.txt", encoding="utf-8") as f:
    chunk = f.read(1024)
```

### Writing Files

```python
## Write a single string ("w" truncates if file exists)
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello, World!\n")

## Write multiple lines
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("output.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)

## Append without overwriting
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("New log entry\n")
```

### Working with Paths — `pathlib`

The modern way to handle file paths is `pathlib.Path` — it is cross-platform and object-oriented:

```python
from pathlib import Path

p = Path("data") / "config.json"   # path joining with /
print(p.exists())
print(p.suffix)      # ".json"
print(p.stem)        # "config"
print(p.parent)      # Path("data")

## Read and write directly
text = p.read_text(encoding="utf-8")
p.write_text("new content", encoding="utf-8")

## Iterate over directory contents
for file in Path(".").glob("*.py"):
    print(file)
```

### JSON

Python's `json` module serializes Python objects to JSON strings and back. The mapping is:

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

**`json.dumps()`** = "dump to string", **`json.dump()`** = "dump to file". Same distinction for `json.loads()` / `json.load()`.

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

Errors are part of normal Python programming, not just something that happens when code is "bad." This chapter explains how Python reports problems, how you can handle expected failures, and how to raise clear exceptions of your own.

The big goal is to separate two ideas:

- bugs you should fix
- runtime problems your code should handle deliberately

Good exception handling makes programs more predictable, easier to debug, and safer to use.

### The Exception Hierarchy

Python's exceptions are classes organized in a hierarchy. All exceptions inherit from `BaseException`. The ones you normally handle inherit from `Exception`:

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

### Basic `try` / `except`

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")    # Error: division by zero
```

The `as e` clause binds the exception object — it has a `args` attribute and a string representation. Handle the **most specific** exception type you expect; catching `Exception` broadly can hide bugs.

### Multiple Except Clauses

```python
def parse_config(path: str) -> dict:
    try:
        with open(path) as f:
            import json
            return json.load(f)
    except FileNotFoundError:
        print(f"Config file not found: {path}")
        return {}
    except json.JSONDecodeError as e:
        print(f"Invalid JSON at line {e.lineno}: {e.msg}")
        return {}
    except PermissionError:
        print(f"Permission denied: {path}")
        raise   # re-raise — we can't recover from this
```

To catch multiple types in one clause, use a tuple:

```python
try:
    value = int(user_input)
except (ValueError, TypeError) as e:
    print(f"Conversion error: {e}")
```

### `else` and `finally`

```python
try:
    result = compute(data)
except ValueError as e:
    print(f"Bad input: {e}")
else:
    # Runs only if NO exception was raised in the try block
    save_result(result)
finally:
    # ALWAYS runs — even if an exception was raised and not caught
    cleanup()
```

Use `finally` for cleanup that must happen regardless: closing connections, releasing locks, writing logs.

### Raising Exceptions

Use `raise` to signal an error condition:

```python
def set_age(age: int):
    if not isinstance(age, int):
        raise TypeError(f"age must be int, got {type(age).__name__}")
    if age < 0 or age > 150:
        raise ValueError(f"age must be 0-150, got {age}")
    return age

## Re-raise the current exception (preserve original traceback)
try:
    risky()
except ValueError:
    log_error()
    raise   # re-raises the same ValueError with original traceback
```

### Exception Chaining

When you raise an exception inside an `except` block, Python links them together with `__cause__` or `__context__`:

```python
try:
    data = json.loads(raw)
except json.JSONDecodeError as e:
    raise ValueError("Could not parse response") from e
    # "The above exception was the direct cause of the following exception"
```

Use `raise ... from None` to suppress the chaining (hide the original exception from the traceback).

### Custom Exceptions

Define custom exception classes to provide richer error information and allow callers to catch specific errors from your library:

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
    print(f"App error: {e}")      # catches any other AppError subclass
```

### Context Managers for Safe Cleanup

Many cleanup scenarios are better expressed with a `with` statement than with `try`/`finally`. See the [Context Managers](../06-advanced-python-techniques/context-managers) page.

```python
## Instead of:
lock.acquire()
try:
    critical_section()
finally:
    lock.release()

## Do this:
with lock:
    critical_section()
```

---

<a id="chapter-ix-concurrency"></a>

## Chapter IX: Concurrency

Python's concurrency model and when to use each tool.

Concurrency is where Python learners often need a decision framework, not just syntax. This chapter explains the major tools Python offers and, more importantly, the tradeoffs between them.

The central questions are:

- are you waiting on I/O or doing CPU-heavy work?
- do you need shared memory, isolation, or simple coordination?
- does the Global Interpreter Lock matter for this workload?

By the end of the chapter, you should be able to choose an approach for a problem instead of guessing between `asyncio`, threads, and processes.

### Sections

- [The GIL](./the-gil)
- [Async / Await](./async-await)
- [Threading](./threading)
- [Multiprocessing](./multiprocessing)
- [Free-Threading](./free-threading)
- [Decision Matrix](./decision-matrix)

---

<a id="the-gil"></a>

## The GIL

The GIL is one of the most discussed parts of Python concurrency, but it is often explained too vaguely. The important question is not simply whether the GIL exists, but what kinds of workloads it limits and what kinds it does not.

Read this page as a decision aid: it helps explain why threads behave differently for CPU-bound work and I/O-bound work in CPython.

### What is the GIL?

The **Global Interpreter Lock (GIL)** is a mutex in CPython — the standard Python interpreter — that allows only one thread to execute Python bytecode at a time. It exists to protect CPython's internal data structures (reference counts, memory allocator) from concurrent modification, which would otherwise cause crashes and memory corruption.

The GIL is a **CPython implementation detail**, not a language requirement. Other implementations — Jython (JVM), IronPython (.NET), PyPy-STM — do not have a GIL.

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

## counter may not be 4_000_000 — the GIL does NOT make compound operations atomic!
## counter += 1 is three bytecodes: LOAD, ADD, STORE — threads can interleave between them
```

### The GIL is Released During I/O

CPython releases the GIL whenever a thread performs I/O — network reads, file reads, `time.sleep()`. This is why threading works well for I/O-bound tasks: while one thread waits for a network response, other threads can execute Python code.

```python
## Threads work well here — GIL is released during urlopen
from concurrent.futures import ThreadPoolExecutor
import urllib.request

def fetch(url):
    with urllib.request.urlopen(url) as r:
        return len(r.read())

with ThreadPoolExecutor(max_workers=10) as pool:
    sizes = list(pool.map(fetch, ["https://python.org"] * 10))
```

### The GIL Does Not Help CPU-Bound Code

For CPU-intensive work, threads do not run in parallel — only one thread runs at a time even on multi-core systems:

```python
## This is NOT parallelized — 4 threads, but still uses 1 core
def cpu_task():
    total = 0
    for i in range(10_000_000):
        total += i
    return total

## Use multiprocessing instead — each process has its own GIL
from concurrent.futures import ProcessPoolExecutor

with ProcessPoolExecutor() as pool:
    results = list(pool.map(lambda _: cpu_task(), range(4)))
```

### Python 3.13 — Free-Threading (Experimental)

Python 3.13 introduced an experimental **free-threaded build** (`python3.13t`) with the GIL disabled. See the [Free-Threading](./free-threading) page for details. This is opt-in for now; the standard CPython 3.13 still has the GIL.

### C Extensions and the GIL

Many C extensions — notably NumPy — release the GIL during heavy computation, allowing genuine parallelism with Python threads:

```python
import numpy as np
import threading

## NumPy releases the GIL during C-level operations
def matmul():
    a = np.random.rand(1000, 1000)
    b = np.random.rand(1000, 1000)
    return np.dot(a, b)   # GIL is released here

threads = [threading.Thread(target=matmul) for _ in range(4)]
for t in threads:
    t.start()
for t in threads:
    t.join()
## These DO run in parallel — NumPy bypasses the GIL
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

`async` and `await` are best understood as a model for cooperative I/O concurrency, not as a universal speed feature. They help when many tasks spend time waiting, but they do not automatically improve CPU-heavy work.

This page is mainly about learning the event-loop mental model so that coroutine behavior feels predictable instead of mysterious.

### How asyncio Works

Python's `asyncio` library provides a single-threaded **event loop** that runs cooperative coroutines. A **coroutine** is a function defined with `async def` — it can `await` other coroutines, pausing execution without blocking the thread. When a coroutine awaits I/O, the event loop runs other ready coroutines instead of sitting idle.

This makes `asyncio` ideal for **I/O-bound** workloads: thousands of simultaneous HTTP requests, database queries, WebSocket connections — all in a single thread.

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

`asyncio.run()` is the correct entry point for top-level code. Never call it from inside a running event loop (e.g., in Jupyter use `await main()` instead).

### Concurrency with `asyncio.gather()`

To run multiple coroutines **concurrently**, use `asyncio.gather()` — it starts all of them and waits until all complete:

```python
import asyncio
import time

async def fetch(url: str) -> str:
    await asyncio.sleep(1)    # simulate network request
    return f"Data from {url}"

async def main():
    start = time.perf_counter()

    # Sequential — total ~2s
    r1 = await fetch("https://api.example.com/users")
    r2 = await fetch("https://api.example.com/posts")

    # Concurrent — total ~1s
    r1, r2 = await asyncio.gather(
        fetch("https://api.example.com/users"),
        fetch("https://api.example.com/posts"),
    )
    print(f"Done in {time.perf_counter() - start:.2f}s")

asyncio.run(main())
```

### Tasks

`asyncio.create_task()` schedules a coroutine to run on the event loop immediately — it does not block until the `await`:

```python
async def main():
    task1 = asyncio.create_task(fetch("url1"))
    task2 = asyncio.create_task(fetch("url2"))
    # Both are now scheduled. Do other work...
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

### Async Generators and Context Managers

```python
async def async_range(n: int):
    for i in range(n):
        await asyncio.sleep(0)   # yield control to event loop
        yield i

async def main():
    async for value in async_range(5):
        print(value)

    # Async context manager
    async with httpx.AsyncClient() as client:
        ...
```

### Common Pitfalls

- **Blocking calls inside coroutines** — `time.sleep()`, file reads, CPU work block the entire event loop. Use `await asyncio.sleep()`, async libraries, or `loop.run_in_executor()` to offload.
- **Not awaiting a coroutine** — calling `fetch(url)` without `await` creates the coroutine object but never runs it.
- **Shared mutable state** — coroutines share memory; protect shared state with `asyncio.Lock()` when needed.

---

<a id="threading"></a>

## Threading

Threads are useful when a program spends much of its time waiting on external work such as network I/O, file I/O, or blocking library calls. They are less useful when pure Python code is trying to saturate CPU cores.

This page should be read together with the GIL page, because thread behavior makes the most sense once that runtime constraint is clear.

### When to Use Threads

Python threads are best for **I/O-bound** work — network requests, database queries, file reads — where the program spends most of its time waiting. Because of the GIL, threads do **not** parallelize CPU-bound computation; use `multiprocessing` for that.

### `ThreadPoolExecutor` — Recommended

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

### Manual Threads

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

### Thread Safety with Locks

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

### Thread-Safe Queues

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

### `threading.local()` — Thread-Local Storage

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

## Multiprocessing

Multiprocessing trades simplicity of shared memory for real parallel execution across CPU cores. That tradeoff matters because it changes both performance and program design.

The main lesson here is when the extra process overhead is justified by CPU-bound workloads.

### When to Use Multiprocessing

`multiprocessing` creates separate OS processes — each has its own Python interpreter and its own GIL. This enables **true CPU parallelism** across multiple cores, which is impossible with threads due to the GIL.

Use `multiprocessing` for **CPU-bound** tasks: numerical computation, image processing, data parsing, compression.

### `ProcessPoolExecutor` — Recommended

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

### Low-Level `multiprocessing.Pool`

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

### Sharing State Between Processes

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

### `multiprocessing.Queue` for Communication

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

### Performance Considerations

- **Startup cost** — spawning a process is expensive (tens of milliseconds). Only worth it for tasks that take seconds, not microseconds.
- **Serialization cost** — all arguments and results are pickled. Large data (big NumPy arrays) can negate the parallelism benefit. Use `shared_memory` (Python 3.8+) for large arrays.
- **Rule of thumb** — pool size = `os.cpu_count()` for CPU-bound; I/O-bound tasks don't benefit from more processes.

---

<a id="free-threading-python-3-13"></a>

## Free-Threading (Python 3.13+)

Free-threading is one of the biggest recent changes in CPython, but it should be approached as an evolving runtime option, not as a blanket replacement for every concurrency strategy. The model is promising, but the ecosystem is still adapting.

This page is meant to help you understand what changes conceptually once the GIL is removed and what practical cautions still remain.

### The Experimental GIL-Free Build

Python 3.13 ships with an **experimental free-threaded build** that removes the GIL, allowing Python threads to execute genuinely in parallel on multiple CPU cores. This is the most significant change to CPython's threading model in its history.

The free-threaded build is opt-in: download `python3.13t` (the `t` suffix means free-threaded). The standard `python3.13` still has the GIL.

```bash
## Check if running in free-threaded mode
python3.13t -c "import sys; print(sys._is_gil_enabled())"   # False
python3.13  -c "import sys; print(sys._is_gil_enabled())"   # True
```

### CPU Parallelism with Threads

Without the GIL, CPU-bound threads genuinely run in parallel:

```python
import threading
import time

def cpu_task(n: int) -> int:
    return sum(i * i for i in range(n))

## In standard CPython: ~4x slower than single thread (GIL overhead)
## In free-threaded 3.13t: ~4x faster than single thread (true parallelism)
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

### Thread Safety Implications

Removing the GIL does **not** make Python thread-safe. It means you must now be more careful about concurrent access to shared data structures, because the GIL previously provided implicit synchronization for many operations.

```python
## UNSAFE in free-threaded mode — concurrent list mutation
shared = []

def appender():
    for i in range(10_000):
        shared.append(i)   # not atomic without GIL

## SAFE — use a lock
lock = threading.Lock()

def safe_appender():
    for i in range(10_000):
        with lock:
            shared.append(i)
```

Python's built-in types (`dict`, `list`, `set`) are being made internally thread-safe for 3.13+, but complex compound operations (read-modify-write) still require explicit synchronization.

### Compatibility Status

- **Pure Python code** works as-is in free-threaded mode.
- **C extensions** must be explicitly marked as supporting free-threading (`Py_TPFLAGS_DEFAULT` → `Py_GIL_DISABLED`). Many popular packages (NumPy, Cython) are working on compatibility.
- Check https://py-free-threading.github.io/ for a compatibility matrix of popular packages.

### When to Use Free-Threading

Free-threading is experimental in 3.13 and will stabilize over the 3.14-3.15 cycle. For production workloads now, prefer `multiprocessing` for CPU parallelism. Follow free-threading for projects targeting future Python versions where it becomes stable.

print(results)
```

> **Note**: Free-threading is experimental in 3.13. Extension modules must be updated to be thread-safe. Performance characteristics are still evolving.

---

<a id="concurrency-decision-matrix"></a>

## Concurrency Decision Matrix

This page is the synthesis step for the chapter. Instead of learning one tool in isolation, you use it to choose an approach based on workload, coordination needs, and runtime constraints.

If the earlier concurrency pages explain how each tool works, this page explains how to decide between them in practice.

### Which Tool for Which Problem?

| Workload Type | Recommended Tool | Reason |
|---------------|-----------------|--------|
| Many I/O operations, high concurrency | `asyncio` | Single thread, no OS overhead, scales to thousands of connections |
| I/O-bound, existing sync code | `threading` / `ThreadPoolExecutor` | GIL released during I/O, simpler than rewriting async |
| CPU-bound computation | `multiprocessing` / `ProcessPoolExecutor` | Each process bypasses the GIL |
| CPU-bound, Python 3.13+ | free-threading (`python3.13t`) | True parallelism without process overhead |
| Mixed: async event loop + CPU work | `asyncio` + `run_in_executor` | Offloads blocking code without freezing the event loop |

### The `run_in_executor` Pattern

The most common pattern for mixing `asyncio` with blocking code (CPU-bound or legacy sync libraries):

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

### Flow Chart

Use this decision flow when choosing a concurrency strategy:

1. **Is the task I/O-bound or CPU-bound?**
   - If **I/O-bound** → continue to step 2
   - If **CPU-bound** → use `ProcessPoolExecutor` (or free-threading on 3.13t)

2. **Is the codebase async-first or sync-first?**
   - If **async** → use `asyncio` with `await`
   - If **sync** → use `ThreadPoolExecutor`

3. **Do you need to mix async with CPU work?**
   - Use `loop.run_in_executor(ProcessPoolExecutor(), ...)` to offload from the event loop

### Quick Reference

```python
## asyncio — 1000 concurrent I/O tasks
import asyncio, httpx

async def main():
    async with httpx.AsyncClient() as client:
        responses = await asyncio.gather(
            *[client.get(url) for url in urls]
        )

## ThreadPoolExecutor — blocking I/O
from concurrent.futures import ThreadPoolExecutor
import requests

with ThreadPoolExecutor(max_workers=10) as pool:
    results = list(pool.map(requests.get, urls))

## ProcessPoolExecutor — CPU
from concurrent.futures import ProcessPoolExecutor

with ProcessPoolExecutor() as pool:
    results = list(pool.map(compute, data_chunks))
```

### Performance Expectations

| Approach | Overhead | Scales to |
|----------|---------|-----------|
| `asyncio` | Very low (coroutine switch ~μs) | Tens of thousands of connections |
| `threading` | Low (OS thread switch ~μs) | Hundreds of threads |
| `multiprocessing` | High (process spawn ~50ms) | CPU count processes |

---

<a id="appendix"></a>

## Appendix

Additional Python ecosystems for specialized domains.

### Sections

- [AI & Data Science](./ai-data-science)
- [Web Development](./web-development)

---

<a id="ai-data-science"></a>

## AI & Data Science

### The Ecosystem

Python dominates AI, machine learning, and data science. The core libraries are:

| Library | Purpose |
|---------|---------|
| `numpy` | Fast multi-dimensional arrays and math |
| `pandas` | Tabular data manipulation (DataFrames) |
| `matplotlib` | 2D plotting |
| `scikit-learn` | Classical machine learning |
| `pytorch` | Deep learning (Meta) — research and production |
| `tensorflow` | Deep learning (Google) — production-focused |
| `xgboost` | Gradient boosting for structured data |

Install the essentials:

```bash
pip install numpy pandas matplotlib scikit-learn
```

### NumPy — Fast Arrays

NumPy's `ndarray` is the foundation of scientific Python. Operations run in C, making them orders of magnitude faster than Python loops:

```python
import numpy as np

## Create arrays
arr = np.array([1, 2, 3, 4, 5])
matrix = np.zeros((3, 4))          # 3x4 matrix of zeros
identity = np.eye(3)               # 3x3 identity matrix
rand = np.random.rand(100, 100)    # random floats

## Vectorized operations — no loop needed
print(arr * 2)          # array([2, 4, 6, 8, 10])
print(arr ** 2)         # array([ 1,  4,  9, 16, 25])
print(arr[arr > 2])     # array([3, 4, 5])  — boolean indexing

## Statistics
print(arr.mean())       # 3.0
print(arr.std())        # 1.4142...
print(arr.sum())        # 15

## Matrix operations
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(a @ b)            # matrix multiply: [[19, 22], [43, 50]]
print(a.T)              # transpose

## Reshape
flat = np.arange(12)
grid = flat.reshape(3, 4)   # shape (3, 4) — same data, different view
```

### Pandas — DataFrames

Pandas provides the `DataFrame` — a table with labeled rows and columns:

```python
import pandas as pd

## Create a DataFrame
df = pd.DataFrame({
    "name":   ["Alice", "Bob", "Carol", "Dave"],
    "dept":   ["Eng",   "HR",  "Eng",   "HR"],
    "salary": [90_000,  60_000, 95_000, 65_000],
    "years":  [3, 7, 5, 2],
})

## Inspect
print(df.head())            # first 5 rows
print(df.dtypes)            # column types
print(df.describe())        # summary statistics

## Selecting
print(df["name"])           # column → Series
print(df[["name", "salary"]])  # multiple columns → DataFrame
print(df[df["salary"] > 70_000])  # filter rows

## Transforming
df["bonus"] = df["salary"] * 0.1     # new column
df["salary_k"] = df["salary"] / 1000

## Grouping
dept_stats = df.groupby("dept")["salary"].agg(["mean", "max", "count"])
print(dept_stats)

## Sorting
print(df.sort_values("salary", ascending=False))

## Reading / writing data
df.to_csv("employees.csv", index=False)
df2 = pd.read_csv("employees.csv")

df.to_json("employees.json", orient="records")
df3 = pd.read_json("employees.json")
```

### Matplotlib — Plotting

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 100)

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

axes[0].plot(x, np.sin(x), label="sin(x)")
axes[0].plot(x, np.cos(x), label="cos(x)")
axes[0].set_title("Trigonometric Functions")
axes[0].legend()
axes[0].grid(True)

data = np.random.randn(1000)
axes[1].hist(data, bins=30, color="steelblue", edgecolor="white")
axes[1].set_title("Normal Distribution")

plt.tight_layout()
plt.savefig("plot.png", dpi=150)
plt.show()
```

### scikit-learn — Machine Learning

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

## Load a dataset
X, y = load_iris(return_X_y=True)

## Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

## Train a model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

## Evaluate
predictions = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, predictions):.2%}")
print(classification_report(y_test, predictions))
```

All scikit-learn estimators follow the same API: `fit()`, `predict()`, `score()` — making it easy to swap algorithms.

---

<a id="web-development"></a>

## Web Development

### The Landscape

Python has mature web frameworks for every use case:

| Framework | Best For |
|-----------|---------|
| `FastAPI` | Modern async REST APIs with auto-generated docs |
| `Flask` | Simple web apps and APIs, minimal overhead |
| `Django` | Full-stack web apps — ORM, admin, auth, templates |
| `Starlette` | Lightweight async framework (FastAPI is built on it) |
| `aiohttp` | Async web server and client |

### FastAPI — Modern APIs

FastAPI is the recommended choice for new REST APIs. It uses Python type annotations to:
- Validate request/response data automatically (via Pydantic)
- Generate interactive API docs at `/docs` (Swagger UI) and `/redoc`
- Run async handlers natively

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

## In-memory store (use a real database in production)
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

Visit `http://localhost:8000/docs` for an interactive browser-based API explorer.

### Flask — Minimal Web

Flask is a micro-framework — it gives you routing and request/response handling, and leaves everything else (database, auth) up to you:

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

Django follows the "batteries included" philosophy — it ships with an ORM, admin panel, auth, form handling, and templating out of the box:

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

Django's admin panel (`/admin/`) provides a full CRUD UI for your models with zero extra code.

### Choosing a Framework

- **New REST API** → FastAPI (async, type-safe, auto-docs)
- **Simple script/prototype** → Flask (minimal setup)
- **Complex web application** → Django (ORM, admin, auth, form validation all included)

## Run: flask run
```

---

