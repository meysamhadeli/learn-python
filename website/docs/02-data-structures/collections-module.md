# Collections Module

The `collections` module exists because Python's basic containers are powerful, but some recurring problems deserve more specialized tools. This page introduces those tools so you can choose clearer abstractions instead of forcing every problem into a plain list or dictionary.

Read these types as practical upgrades for common situations, not as features you must memorize all at once.

`collections` provides specialized container types that solve common patterns more cleanly than plain dicts and lists.

## defaultdict

A dict that auto-initializes missing keys — eliminates the need for manual key checks.

```python
from collections import defaultdict

word_count = defaultdict(int)
words = ["apple", "banana", "apple", "cherry"]
for word in words:
    word_count[word] += 1

print(dict(word_count))  # {'apple': 2, 'banana': 1, 'cherry': 1}

# Grouping by first letter
groups = defaultdict(list)
for word in words:
    groups[word[0]].append(word)
```

## Counter

Counts hashable objects and supports arithmetic between counters.

```python
from collections import Counter

text = "hello world"
char_count = Counter(text)
print(char_count.most_common(3))  # [('l', 3), ('o', 2), ('h', 1)]

votes = Counter(["Python", "Python", "Rust", "Go", "Python"])
print(votes["Python"])  # 3

a = Counter("aab")
b = Counter("abb")
print(a + b)  # Counter({'a': 3, 'b': 3})
print(a - b)  # Counter({'a': 1})
```

## deque

A double-ended queue — O(1) appends/pops from both ends (lists are O(n) at the front).

```python
from collections import deque

queue = deque([1, 2, 3])
queue.append(4)      # [1, 2, 3, 4]
queue.appendleft(0)  # [0, 1, 2, 3, 4]
queue.pop()          # returns 4, queue: [0, 1, 2, 3]
queue.popleft()      # returns 0, queue: [1, 2, 3]

history = deque(maxlen=3)
for i in range(5):
    history.append(i)
print(history)  # deque([2, 3, 4], maxlen=3) — auto-evicts oldest
```
