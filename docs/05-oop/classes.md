# Classes

Classes bundle related data and behavior.

## Defining a Class

The class defines the structure. The instance is a concrete object.

```python
class Dog:
    species = "Canis familiaris"

    def __init__(self, name: str, age: int):
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

## `self` — The Instance Reference

`self` refers to the current instance.

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

## Class vs Instance Attributes

Class attributes are shared. Instance attributes belong to one object.

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

## Class Methods and Static Methods

```python
class Temperature:
    def __init__(self, celsius: float):
        self.celsius = celsius

    def to_fahrenheit(self) -> float:
        return self.celsius * 9 / 5 + 32

    @classmethod
    def from_fahrenheit(cls, fahrenheit: float) -> "Temperature":
        return cls((fahrenheit - 32) * 5 / 9)

    @staticmethod
    def is_freezing(celsius: float) -> bool:
        return celsius <= 0

t = Temperature(100)
print(t.to_fahrenheit())                    # 212.0
t2 = Temperature.from_fahrenheit(32)        # factory
print(t2.celsius)                           # 0.0
print(Temperature.is_freezing(-5))          # True
```

## Properties

Use `@property` for computed values or validation:

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
```

For many real projects, classes plus dataclasses are enough. You do not need deep inheritance to write good Python.
