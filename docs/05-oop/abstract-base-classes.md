# Abstract Base Classes

Abstract base classes are about defining contracts. They let you say "any concrete subclass must provide this behavior" before you care about the exact implementation details.

That makes them useful when multiple classes should behave consistently, especially in larger designs or library code.

## What is an ABC?

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


# Shape()   # TypeError: Can't instantiate abstract class Shape
# Missing: area, perimeter
```

## Implementing Concrete Subclasses

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
# Circle: area=78.54, perimeter=31.42
# Rectangle: area=24.00, perimeter=20.00
```

## Abstract Properties

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

## ABCs from `collections.abc`

The standard library defines ABCs for Python's built-in protocols in `collections.abc`. These are useful both for implementing and for type-checking:

```python
from collections.abc import Mapping, Sequence, Iterable, Callable

def process(data: Iterable[int]) -> int:
    return sum(data)

process([1, 2, 3])          # ✅ list is Iterable
process((1, 2, 3))          # ✅ tuple is Iterable
process(range(10))          # ✅ range is Iterable

# isinstance checks with ABCs
print(isinstance([], Sequence))   # True — list implements Sequence
print(isinstance({}, Mapping))    # True — dict implements Mapping
print(isinstance("hi", Sequence)) # True — str implements Sequence
```

## `register()` — Virtual Subclasses

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
