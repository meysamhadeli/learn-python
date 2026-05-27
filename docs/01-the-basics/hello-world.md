# Hello World

## Your First Program

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
# or on Windows
py main.py
```

Output:
```
Hello, World!
```

If Python is installed correctly, the interpreter reads the file from top to bottom and executes each statement in order. Right now there is only one statement, so the behavior is easy to predict: Python calls `print()`, and the text appears in your terminal.

## Script Mode vs Interactive Mode

Python can be used in two common ways:

- **Script mode**: you run a file like `main.py`.
- **Interactive mode**: you start Python first, then type commands one at a time.

For example, this opens the interactive interpreter:

```bash
python
# or on Windows
py
```

You will usually see a prompt like `>>>`. Anything you type after that is executed immediately:

```python
>>> print("Hello, World!")
Hello, World!
```

Interactive mode is useful for quick experiments. Script mode is better when you want to save, rerun, and share your code.

## How Python Executes Code

When you run `python main.py`, the CPython interpreter reads your source file, compiles it to **bytecode** (a low-level, platform-independent instruction set), and executes that bytecode on the Python Virtual Machine (PVM). You never see the bytecode directly — it is cached in `__pycache__/` as `.pyc` files to speed up future runs.

Unlike compiled languages (C, Go, Rust), there is no separate compilation step you must run manually. The compile-and-run happens transparently each time you invoke the interpreter.

For beginners, the important mental model is simpler than the implementation details:

1. Python reads your file.
2. Python checks that the syntax is valid.
3. Python runs the statements in order.

That mental model will stay useful throughout the course.

## The `print()` Function

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

## The `__main__` Guard

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

## Reading Input

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
# print(age + 1)  # TypeError: can't add str and int
print(int(age) + 1)
```

As a rule:

- `input()` gets text from the user.
- conversion functions like `int()` and `float()` turn that text into other types.
- `print()` shows results back to the user.
