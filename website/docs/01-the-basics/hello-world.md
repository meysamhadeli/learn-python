# Hello World

## Your First Program

The first useful Python program is a single line:

```python
print("Hello, World!")
```

Save this to `main.py` and run it:

```bash
python main.py
# or on Windows
py main.py
```

Output: `Hello, World!`

## Script Mode vs Interactive Mode

You will use Python in two common ways:

- **Script mode**: you run a file like `main.py`.
- **Interactive mode**: you start Python first, then type commands one at a time.

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

Use the REPL for quick checks. Use files for scripts and real projects.

## How Python Executes Code

The practical mental model is:

1. Python reads your file.
2. Python checks that the syntax is valid.
3. Python runs the statements in order.

## The `print()` Function

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

## The `__main__` Guard

Use `if __name__ == "__main__":` when a file should act as both an importable module and a runnable script:

```python
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("World"))
```

You do not need it in every tiny example, but you will see it often in real projects.

## Reading Input

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
