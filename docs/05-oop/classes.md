# Classes

Classes are Python's main tool for bundling related data and behavior into a single abstraction. They are useful when values need associated operations or when many objects share the same structure.

The key beginner shift is to see a class as a definition and an instance as a concrete object created from that definition.

## Defining a Class

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

## `self` — The Instance Reference

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

## Class vs Instance Attributes

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

## Class Methods and Static Methods

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

## Properties

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
# c.radius = -1     # ValueError
```
