# Inheritance

## Basic Inheritance

A subclass inherits all attributes and methods from its parent. Use `super()` to call the parent's implementation from within an override:

```python
class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        raise NotImplementedError(f"{type(self).__name__} must implement speak()")

    def __repr__(self) -> str:
        return f"{type(self).__name__}(name={self.name!r})"


class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name} says Woof!"


class Cat(Animal):
    def speak(self) -> str:
        return f"{self.name} says Meow!"


animals: list[Animal] = [Dog("Rex"), Cat("Whiskers"), Dog("Buddy")]
for animal in animals:
    print(animal.speak())   # polymorphism — each uses its own speak()
```

## `super()` and `__init__` Chaining

When a subclass defines `__init__`, it must explicitly call `super().__init__()` to initialize the parent's attributes:

```python
class Vehicle:
    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year

    def description(self) -> str:
        return f"{self.year} {self.make} {self.model}"


class ElectricVehicle(Vehicle):
    def __init__(self, make: str, model: str, year: int, range_km: int):
        super().__init__(make, model, year)   # initialize parent attributes
        self.range_km = range_km              # add new attribute

    def description(self) -> str:
        base = super().description()           # reuse parent method
        return f"{base} — EV ({self.range_km} km range)"


tesla = ElectricVehicle("Tesla", "Model 3", 2024, 570)
print(tesla.description())
# 2024 Tesla Model 3 — EV (570 km range)
```

## `isinstance()` and `issubclass()`

```python
print(isinstance(tesla, ElectricVehicle))   # True
print(isinstance(tesla, Vehicle))           # True — also an instance of the parent
print(isinstance(tesla, Animal))            # False

print(issubclass(ElectricVehicle, Vehicle)) # True
print(issubclass(Dog, Animal))              # True
```

## Multiple Inheritance and MRO

Python supports multiple inheritance. The **Method Resolution Order (MRO)** defines the order in which Python searches for a method. It uses the C3 linearization algorithm and is accessible via `ClassName.__mro__`:

```python
class Flyable:
    def move(self):
        return "Flying"

class Swimmable:
    def move(self):
        return "Swimming"

class Duck(Flyable, Swimmable):
    pass

d = Duck()
print(d.move())            # "Flying" — Flyable comes first in MRO
print(Duck.__mro__)        # (Duck, Flyable, Swimmable, object)
```

## Composition vs Inheritance

Inheritance models **is-a** relationships. Composition (holding a reference to another object) models **has-a** relationships, and is often more flexible:

```python
# Inheritance: Duck IS-A Bird
class Bird:
    def fly(self): ...

class Duck(Bird):
    pass

# Composition: Car HAS-A Engine
class Engine:
    def start(self): ...

class Car:
    def __init__(self):
        self.engine = Engine()   # has-a, not is-a

    def start(self):
        self.engine.start()
```

Prefer composition when the relationship is not a strict "is-a", or when you want to swap components at runtime.
