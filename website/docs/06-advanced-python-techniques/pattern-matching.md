# Pattern Matching (Python 3.10+)

This page focuses on pattern matching as a Pythonic technique rather than just as syntax. The value of `match` is not only branching on values, but also expressing shape, structure, and extraction in one place.

It overlaps with Chapter III's `match` introduction, but the emphasis here is on writing patterns idiomatically once the basic syntax already makes sense.

`match`/`case` goes beyond `switch` — it can destructure objects, sequences, and mappings.

```python
# Match on class instances
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

# Match on sequences
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
