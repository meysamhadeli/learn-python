# Virtual Environments

## Why Virtual Environments?

Without a virtual environment, every package you install with `pip` goes into the global Python installation. This causes problems:
- **Version conflicts** — project A needs `requests==2.28`, project B needs `requests==2.31`
- **Pollution** — unrelated packages from one project clutter another
- **Reproducibility** — "it works on my machine" problems when deploying

A **virtual environment** is an isolated directory containing its own Python interpreter copy, its own `pip`, and its own site-packages. Each project gets its own environment.

## Creating and Activating

```bash
# Create a virtual environment in a folder called 'venv'
python3 -m venv venv

# Activate (macOS / Linux)
source venv/bin/activate

# Activate (Windows CMD)
venv\Scripts\activate.bat

# Activate (Windows PowerShell)
venv\Scripts\Activate.ps1

# Deactivate — return to global Python
deactivate
```

When a virtual environment is active, your shell prompt shows its name: `(venv) $`. All `python` and `pip` commands now use the isolated environment.

## Managing Dependencies

```bash
# Install packages into the active venv
pip install requests fastapi

# Install a specific version
pip install "django==5.0"

# Install from a requirements file
pip install -r requirements.txt

# Freeze current environment to a file
pip freeze > requirements.txt

# Show installed packages
pip list
pip show requests
```

## `requirements.txt`

A `requirements.txt` pins exact versions for reproducible installs:

```
requests==2.31.0
fastapi==0.110.0
pydantic==2.6.0
uvicorn==0.27.0
```

Generate it with `pip freeze > requirements.txt` and commit it to source control. Teammates and CI systems can reproduce the exact environment with `pip install -r requirements.txt`.

## `.gitignore`

Always add the `venv/` directory to `.gitignore` — it should not be committed:

```
venv/
__pycache__/
*.pyc
.env
```

## Modern Alternatives

| Tool | Description |
|------|-------------|
| `uv` | Very fast Rust-based pip + venv replacement |
| `poetry` | Dependency management + packaging in one |
| `pipenv` | Combines pip + virtualenv with a `Pipfile` |
| `conda` | Manages Python versions + packages (popular in data science) |
