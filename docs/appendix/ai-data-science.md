# AI & Data Science

## The Ecosystem

Python dominates AI, machine learning, and data science. The core libraries are:

| Library | Purpose |
|---------|---------|
| `numpy` | Fast multi-dimensional arrays and math |
| `pandas` | Tabular data manipulation (DataFrames) |
| `matplotlib` | 2D plotting |
| `scikit-learn` | Classical machine learning |
| `pytorch` | Deep learning (Meta) — research and production |
| `tensorflow` | Deep learning (Google) — production-focused |
| `xgboost` | Gradient boosting for structured data |

Install the essentials:

```bash
pip install numpy pandas matplotlib scikit-learn
```

## NumPy — Fast Arrays

NumPy's `ndarray` is the foundation of scientific Python. Operations run in C, making them orders of magnitude faster than Python loops:

```python
import numpy as np

# Create arrays
arr = np.array([1, 2, 3, 4, 5])
matrix = np.zeros((3, 4))          # 3x4 matrix of zeros
identity = np.eye(3)               # 3x3 identity matrix
rand = np.random.rand(100, 100)    # random floats

# Vectorized operations — no loop needed
print(arr * 2)          # array([2, 4, 6, 8, 10])
print(arr ** 2)         # array([ 1,  4,  9, 16, 25])
print(arr[arr > 2])     # array([3, 4, 5])  — boolean indexing

# Statistics
print(arr.mean())       # 3.0
print(arr.std())        # 1.4142...
print(arr.sum())        # 15

# Matrix operations
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(a @ b)            # matrix multiply: [[19, 22], [43, 50]]
print(a.T)              # transpose

# Reshape
flat = np.arange(12)
grid = flat.reshape(3, 4)   # shape (3, 4) — same data, different view
```

## Pandas — DataFrames

Pandas provides the `DataFrame` — a table with labeled rows and columns:

```python
import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    "name":   ["Alice", "Bob", "Carol", "Dave"],
    "dept":   ["Eng",   "HR",  "Eng",   "HR"],
    "salary": [90_000,  60_000, 95_000, 65_000],
    "years":  [3, 7, 5, 2],
})

# Inspect
print(df.head())            # first 5 rows
print(df.dtypes)            # column types
print(df.describe())        # summary statistics

# Selecting
print(df["name"])           # column → Series
print(df[["name", "salary"]])  # multiple columns → DataFrame
print(df[df["salary"] > 70_000])  # filter rows

# Transforming
df["bonus"] = df["salary"] * 0.1     # new column
df["salary_k"] = df["salary"] / 1000

# Grouping
dept_stats = df.groupby("dept")["salary"].agg(["mean", "max", "count"])
print(dept_stats)

# Sorting
print(df.sort_values("salary", ascending=False))

# Reading / writing data
df.to_csv("employees.csv", index=False)
df2 = pd.read_csv("employees.csv")

df.to_json("employees.json", orient="records")
df3 = pd.read_json("employees.json")
```

## Matplotlib — Plotting

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 100)

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

axes[0].plot(x, np.sin(x), label="sin(x)")
axes[0].plot(x, np.cos(x), label="cos(x)")
axes[0].set_title("Trigonometric Functions")
axes[0].legend()
axes[0].grid(True)

data = np.random.randn(1000)
axes[1].hist(data, bins=30, color="steelblue", edgecolor="white")
axes[1].set_title("Normal Distribution")

plt.tight_layout()
plt.savefig("plot.png", dpi=150)
plt.show()
```

## scikit-learn — Machine Learning

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load a dataset
X, y = load_iris(return_X_y=True)

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
predictions = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, predictions):.2%}")
print(classification_report(y_test, predictions))
```

All scikit-learn estimators follow the same API: `fit()`, `predict()`, `score()` — making it easy to swap algorithms.
