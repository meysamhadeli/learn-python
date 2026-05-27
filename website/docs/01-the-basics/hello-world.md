# Hello World

## Your First Program

The traditional starting point for any language is printing "Hello, World!" to the screen. In Python this is a single line:

```python
print("Hello, World!")
```

Save this to `main.py` and run it:

```bash
python3 main.py
```

Output:
```
Hello, World!
```

## How Python Executes Code

When you run `python3 main.py`, the CPython interpreter reads your source file, compiles it to **bytecode** (a low-level, platform-independent instruction set), and executes that bytecode on the Python Virtual Machine (PVM). You never see the bytecode directly — it is cached in `__pycache__/` as `.pyc` files to speed up future runs.

Unlike compiled languages (C, Go, Rust), there is no separate compilation step you must run manually. The compile-and-run happens transparently each time you invoke the interpreter.

## The `print()` Function

`print()` is a built-in function that writes its arguments to **standard output** (`stdout`), followed by a newline by default. It accepts multiple arguments and several keyword parameters:

```python
print("Hello", "World")          # Hello World  (space-separated by default)
print("Hello", "World", sep="-") # Hello-World
print("Hello", end="")           # no newline at the end
print(42, 3.14, True, None)      # 42 3.14 True None
```

The `sep` parameter controls what goes between arguments (default: `" "`). The `end` parameter controls what is appended after the last argument (default: `"\n"`).

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

- `def main():` defines a function named `main`.
- `if __name__ == "__main__":` ensures this runs only when executed directly, not when imported.
