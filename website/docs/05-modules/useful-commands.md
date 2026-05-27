# Useful Commands

## pip — Package Installer

```bash
# Install a package
pip install requests

# Install a specific version
pip install "requests==2.31.0"

# Install minimum version
pip install "requests>=2.28"

# Install from a requirements file
pip install -r requirements.txt

# Upgrade a package
pip install --upgrade requests

# Upgrade pip itself
pip install --upgrade pip

# Uninstall a package
pip uninstall requests

# List installed packages
pip list

# Show details for a package (version, location, dependencies)
pip show requests

# Freeze current environment to a file (exact versions)
pip freeze > requirements.txt

# Search PyPI (deprecated in pip 21+; use https://pypi.org instead)
# pip search requests
```

## Python Interpreter Commands

```bash
# Start the interactive REPL
python3

# Run a script
python3 script.py

# Run a module as a script (e.g., the built-in http server)
python3 -m http.server 8000

# Execute a one-liner
python3 -c "print('Hello')"

# Check Python version
python3 --version

# Show where Python is installed
which python3     # macOS / Linux
where python3     # Windows
```

## Virtual Environment Commands

```bash
# Create a virtual environment
python3 -m venv venv

# Activate (macOS / Linux)
source venv/bin/activate

# Activate (Windows CMD)
venv\Scripts\activate.bat

# Activate (Windows PowerShell)
venv\Scripts\Activate.ps1

# Deactivate
deactivate

# Install all project dependencies
pip install -r requirements.txt
```

## Checking Installed Package Info

```bash
# Show package version and location
pip show numpy

# List outdated packages
pip list --outdated

# Verify installed packages against requirements
pip check
```
