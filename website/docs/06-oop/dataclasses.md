# Dataclasses

## What is a Dataclass?

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

## Default Values and `field()`

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

## `__post_init__`

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

## Ordering

Set `order=True` to generate `<`, `>`, `<=`, `>=` based on field order:

```python
@dataclass(order=True)
class Version:
    major: int
    minor: int
    patch: int

versions = [Version(1, 10, 0), Version(2, 0, 0), Version(1, 9, 5)]
print(sorted(versions))
# [Version(major=1, minor=9, patch=5), Version(major=1, minor=10, patch=0), Version(major=2, minor=0, patch=0)]
```

## Frozen Dataclasses

Set `frozen=True` to make instances immutable — enabling use as dict keys and set members:

```python
@dataclass(frozen=True)
class Config:
    host: str
    port: int

c = Config("localhost", 5432)
# c.port = 5433   # FrozenInstanceError
cache = {c: "connection"}  # works — frozen dataclasses are hashable
```

## Dataclass vs `namedtuple` vs Regular Class

| | `dataclass` | `namedtuple` | regular class |
|--|-------------|--------------|---------------|
| Mutable | ✅ (default) | ❌ | ✅ |
| `__repr__` auto | ✅ | ✅ | ❌ |
| Ordering | opt-in | ✅ | ❌ |
| Hashable | frozen only | ✅ | with `__hash__` |
| Inheritance | ✅ | limited | ✅ |
| Type hints | ✅ | ✅ | ✅ |

Use `@dataclass` for most new code. Use `namedtuple` for lightweight read-only records. Use a regular class when you need heavy customization.
