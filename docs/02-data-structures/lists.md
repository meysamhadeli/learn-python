# Lists

Lists are ordered, mutable collections and the default sequence type in Python.

## What is a List?

A list can hold mixed types and can grow or shrink at runtime.

```python
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, None]
nested = [[1, 2], [3, 4], [5, 6]]
empty = []
```

## Indexing and Slicing

Lists are zero-indexed. Negative indexes count from the end. Slicing returns a new list.

```python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

print(fruits[0])     # "apple"
print(fruits[-1])    # "elderberry"
print(fruits[1:3])   # ["banana", "cherry"]  — stop index is exclusive
print(fruits[:2])    # ["apple", "banana"]
print(fruits[2:])    # ["cherry", "date", "elderberry"]
print(fruits[::2])   # ["apple", "cherry", "elderberry"]  — every 2nd
print(fruits[::-1])  # reverse
```

## Modifying Lists

Lists can be changed in place:

```python
fruits = ["apple", "banana", "cherry"]

fruits.append("date")            # add to end: O(1) amortized
fruits.insert(1, "blueberry")    # insert at index: O(n)
fruits.extend(["elderberry", "fig"])  # add multiple: O(k)

fruits.remove("banana")          # remove first occurrence by value: O(n)
popped = fruits.pop()            # remove and return last: O(1)
popped2 = fruits.pop(0)         # remove and return at index: O(n)
del fruits[1]                    # remove at index without returning

fruits[0] = "avocado"            # replace by index
fruits[1:3] = ["kiwi", "mango"] # replace a slice
```

## Sorting

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

numbers.sort()                    # in-place, ascending
numbers.sort(reverse=True)        # in-place, descending

sorted_copy = sorted(numbers)     # returns NEW list, original unchanged

words = ["banana", "apple", "cherry", "date"]
words.sort(key=len)               # sort by string length
words.sort(key=str.lower)         # case-insensitive sort
```

## Useful List Methods

```python
items = [3, 1, 4, 1, 5, 1]

print(len(items))          # 6
print(items.count(1))      # 3  — how many times 1 appears
print(items.index(4))      # 2  — index of first occurrence
items.reverse()            # in-place reverse
items.clear()              # remove all elements
```

## Performance Notes

Indexing and appending are fast. Inserting or removing near the front is slow. For queue-like behavior, use `collections.deque`.

## List Copying

Assignment shares the same list object:

```python
a = [1, 2, 3]
b = a             # b is the SAME list
b.append(4)
print(a)          # [1, 2, 3, 4]

# Shallow copy — new list, but nested objects still shared
c = a.copy()      # or: a[:]  or: list(a)
c.append(99)
print(a)          # [1, 2, 3, 4] — unaffected
```
