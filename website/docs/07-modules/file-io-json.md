# File I/O & JSON

File I/O and JSON are core tools for scripts, APIs, configs, and AI workflows.

## Opening Files

Use `with open(...)` so the file always closes:

```python
with open("data.txt", "r") as f:
    content = f.read()
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

For text files, specify UTF-8:

```python
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
```

## Reading Files

```python
with open("data.txt", encoding="utf-8") as f:
    content = f.read()

with open("data.txt", encoding="utf-8") as f:
    lines = f.readlines()

with open("data.txt", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
```

## Writing Files

```python
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello, World!\n")

lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("output.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)

with open("log.txt", "a", encoding="utf-8") as f:
    f.write("New log entry\n")
```

## Working with Paths — `pathlib`

`pathlib.Path` is the modern way to handle paths:

```python
from pathlib import Path

p = Path("data") / "config.json"   # path joining with /
print(p.exists())
print(p.suffix)      # ".json"
print(p.stem)        # "config"
print(p.parent)      # Path("data")

text = p.read_text(encoding="utf-8")
p.write_text("new content", encoding="utf-8")
```

## JSON

Python's `json` module maps Python data to JSON and back:

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

`json.dumps()` writes to a string. `json.dump()` writes to a file.

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

This pattern matters a lot for config files, cached model outputs, prompts, and API payloads.
