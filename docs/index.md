# Getting Started

## What is Python?

Python is a high-level, general-purpose programming language created by Guido van Rossum and first released in 1991. It is designed around readability — Python code often reads almost like plain English, which makes it an excellent first language and a productive language for experienced developers alike.

Python is an **interpreted** language, meaning code is executed line by line at runtime rather than compiled ahead of time to machine code. CPython, the reference implementation, compiles your source to bytecode and runs it on the Python Virtual Machine. This makes Python highly portable — the same code runs on Linux, macOS, and Windows without changes.

Python is **dynamically typed**: you do not declare variable types. The interpreter determines types at runtime. This speeds up development but puts more responsibility on the programmer (and tools like `mypy`) to catch type errors.

```python
x = 10        # x is an int
x = "hello"   # now x is a str — perfectly valid in Python
```

## Why Learn Python?

Python has become the dominant language in several fields:

- **AI & Machine Learning** — PyTorch, TensorFlow, Hugging Face, LangChain, PydanticAI, and the OpenAI SDK are all Python-first. If you want to work in AI, Python is non-negotiable.
- **Data Science** — NumPy, pandas, and matplotlib form the foundation of data analysis workflows worldwide.
- **Web Development** — FastAPI, Django, and Flask power production backends at companies like Instagram, Spotify, and Dropbox.
- **Automation & Scripting** — Python is the go-to for DevOps scripts, CLI tools, and task automation.
- **Ecosystem** — PyPI hosts over 500,000 packages covering everything from HTTP clients to computer vision.

## Installation

### macOS / Linux

Python 3 is usually pre-installed. Verify with:

```bash
python3 --version
```

If missing, install from [python.org/downloads](https://www.python.org/downloads/) or via your package manager:

```bash
# Ubuntu / Debian
sudo apt update && sudo apt install python3 python3-pip python3-venv

# macOS with Homebrew
brew install python
```

### Windows

1. Download the installer from [python.org/downloads](https://www.python.org/downloads/).
2. **Tick "Add Python to PATH"** before clicking Install Now.
3. Verify in a new terminal:

```bash
python --version
```

## Running Python

There are three ways to run Python code:

**Interactive REPL** — great for quick experiments:
```bash
python3
>>> 1 + 1
2
>>> exit()
```

**Run a script directly:**
```bash
python3 hello.py
```

**Jupyter Notebook** — interactive cells in VS Code or browser. Open `learn-python.ipynb` in this repo to follow along interactively.

## Setting Up VS Code

1. Download from [code.visualstudio.com](https://code.visualstudio.com/).
2. Install the **Python** extension by Microsoft — provides IntelliSense, linting, and the debugger.
3. Select your Python interpreter: `Ctrl+Shift+P` → *Python: Select Interpreter*.

> 💡 Use the integrated terminal (`Ctrl+\``) and the **Jupyter** extension to run notebook cells directly inside VS Code.
