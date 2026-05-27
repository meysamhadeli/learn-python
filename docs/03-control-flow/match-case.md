# Match / Case (Python 3.10+)

## Overview

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

## Matching Sequences

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

## Matching Mappings (Dicts)

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

## Matching Class Instances

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

## OR Patterns and Guards

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

## Matching Command Sequences

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

## `as` Pattern

Bind a matched value to a name while still matching a pattern:

```python
match data:
    case [first, *rest] as full_list:
        print(f"First: {first}, Total: {len(full_list)}")
```
