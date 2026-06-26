# Magic Methods

Magic methods let custom classes work with Python syntax such as `print()`, `len()`, operators, iteration, and context managers.

## What Are Magic Methods?

Magic methods, or dunder methods, are special methods that Python calls automatically.

## String Representation

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Point({self.x!r}, {self.y!r})"

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

p = Point(3, 4)
print(repr(p))   # Point(3, 4)
print(str(p))    # (3, 4)
print(p)         # (3, 4)  — print() calls __str__
```

## Arithmetic Operators

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
        return self.__mul__(scalar)

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

## Comparison Operators

```python
from functools import total_ordering

@total_ordering
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
print(t2 >= t1)   # True
```

## Container Protocol

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

## `__call__` — Making Instances Callable

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

## `__enter__` and `__exit__` — Context Manager Protocol

These power the `with` statement.

```python
class Timer:
    def __enter__(self):
        import time
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.elapsed = time.time() - self.start
        return False

with Timer() as t:
    sum(range(1_000_000))
print(f"Elapsed: {t.elapsed:.4f}s")
```

You do not need to memorize every magic method. Focus on the common ones: `__init__`, `__repr__`, `__str__`, comparison methods, iterator methods, and context-manager methods.
