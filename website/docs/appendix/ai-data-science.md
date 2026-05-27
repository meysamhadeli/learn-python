# AI & Data Science

## The Ecosystem

Python dominates AI, machine learning, and data science. The core libraries are:

| Library | Purpose |
|---------|---------|
| `numpy` | Fast multi-dimensional arrays and math |
| `pandas` | Tabular data manipulation (DataFrames) |
| `pytorch` | Deep learning (Meta) — research and production |
| `tensorflow` | Deep learning (Google) — production-focused |
| `langchain` | Build LLM workflows, retrieval pipelines, and agent-style applications |
| `pydantic-ai` | Build AI agents with typed inputs, outputs, and validation |

Install the essentials:

```bash
pip install numpy pandas langchain pydantic-ai
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

## LangChain — LLM Workflows

LangChain helps you connect prompts, models, tools, and retrieved documents into larger LLM-powered workflows. It is commonly used for chatbots, retrieval-augmented generation (RAG), and agent-style applications.

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a concise Python tutor."),
    ("human", "Explain {topic} in 3 short bullet points."),
])

model = ChatOpenAI(model="gpt-4o-mini")
chain = prompt | model

response = chain.invoke({"topic": "Python decorators"})
print(response.content)
```

The value of LangChain is composition: you can add memory, retrieval, tools, and output parsing without rewriting your whole application.

## PydanticAI — Typed AI Agents

PydanticAI focuses on building AI agents with strong typing and validation. That makes it a good fit when you want model output to match a Python schema instead of returning loose text.

```python
from dataclasses import dataclass

from pydantic_ai import Agent

@dataclass
class StudyPlan:
    topic: str
    difficulty: str
    next_step: str

agent = Agent(
    "openai:gpt-4o-mini",
    output_type=StudyPlan,
    system_prompt="You create short Python study plans.",
)

result = agent.run_sync("Create a beginner study plan for list comprehensions.")
print(result.output)
```

This style is useful when you want predictable, structured outputs that can be passed directly into Python code, APIs, or UIs.
