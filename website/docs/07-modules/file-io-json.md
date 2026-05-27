# File I/O & JSON

File handling is where Python programs start interacting with the outside world. That also means mistakes matter more here: wrong paths, wrong modes, wrong encodings, and missing files are all common real-world issues.

This page is easiest to read if you keep two concerns separate: how to read and write files safely, and how JSON turns Python data into a portable text format.

## Opening Files

Use the built-in `open()` function to open a file. The `with` statement is the correct way to do so — it guarantees the file is closed when the block exits, even if an exception is raised:

```python
with open("data.txt", "r") as f:
    content = f.read()
# File is automatically closed here
```

Common mode strings:

| Mode | Meaning |
|------|---------|
| `"r"` | Read text (default) |
| `"w"` | Write text — **truncates** the file if it exists |
| `"a"` | Append text |
| `"x"` | Exclusive creation — fails if file exists |
| `"rb"` | Read binary |
| `"wb"` | Write binary |

Always specify `encoding="utf-8"` explicitly on text files to avoid platform-dependent behavior:

```python
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
```

## Reading Files

```python
# Read entire file as a single string
with open("data.txt", encoding="utf-8") as f:
    content = f.read()

# Read all lines into a list (includes newline characters)
with open("data.txt", encoding="utf-8") as f:
    lines = f.readlines()

# Iterate line by line — best for large files (no memory spike)
with open("data.txt", encoding="utf-8") as f:
    for line in f:
        print(line.strip())   # strip() removes the trailing newline

# Read a fixed number of characters
with open("data.txt", encoding="utf-8") as f:
    chunk = f.read(1024)
```

## Writing Files

```python
# Write a single string ("w" truncates if file exists)
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello, World!\n")

# Write multiple lines
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("output.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)

# Append without overwriting
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("New log entry\n")
```

## Working with Paths — `pathlib`

The modern way to handle file paths is `pathlib.Path` — it is cross-platform and object-oriented:

```python
from pathlib import Path

p = Path("data") / "config.json"   # path joining with /
print(p.exists())
print(p.suffix)      # ".json"
print(p.stem)        # "config"
print(p.parent)      # Path("data")

# Read and write directly
text = p.read_text(encoding="utf-8")
p.write_text("new content", encoding="utf-8")

# Iterate over directory contents
for file in Path(".").glob("*.py"):
    print(file)
```

## JSON

Python's `json` module serializes Python objects to JSON strings and back. The mapping is:

| Python | JSON |
|--------|------|
| `dict` | object `{}` |
| `list`, `tuple` | array `[]` |
| `str` | string |
| `int`, `float` | number |
| `True`/`False` | `true`/`false` |
| `None` | `null` |

```python
import json

data = {
    "name": "Alice",
    "age": 30,
    "scores": [95, 87, 92],
    "active": True,
    "address": None,
}

# Serialize to JSON string
json_str = json.dumps(data)                # compact
json_pretty = json.dumps(data, indent=2)   # readable

# Deserialize from JSON string
parsed = json.loads(json_str)
print(parsed["name"])   # "Alice"

# Write to file
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

# Read from file
with open("data.json", encoding="utf-8") as f:
    loaded = json.load(f)
```

**`json.dumps()`** = "dump to string", **`json.dump()`** = "dump to file". Same distinction for `json.loads()` / `json.load()`.

## Handling Missing Files Gracefully

```python
from pathlib import Path
import json

config_file = Path("config.json")

try:
    data = json.loads(config_file.read_text(encoding="utf-8"))
except FileNotFoundError:
    data = {}   # use defaults
except json.JSONDecodeError as e:
    print(f"Invalid JSON in config: {e}")
    data = {}
```
