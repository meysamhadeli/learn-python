# AI & Data Science

## The Ecosystem

Python dominates AI and data tooling. A few libraries matter most early:

| Library | Purpose |
|---------|---------|
| `numpy` | Fast multi-dimensional arrays and math |
| `pandas` | Tabular data manipulation (DataFrames) |
| `pytorch` | Deep learning (Meta) — research and production |
| `tensorflow` | Deep learning (Google) — production-focused |
| `langchain` | Build LLM workflows, retrieval pipelines, and agent-style applications |
| `pydantic-ai` | Build AI agents with typed inputs, outputs, and validation |

Install only what you need:

```bash
pip install numpy pandas langchain pydantic-ai
```

## NumPy — Fast Arrays

NumPy arrays are the foundation of scientific Python and vectorized math.

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
matrix = np.zeros((3, 4))          # 3x4 matrix of zeros

print(arr * 2)          # array([2, 4, 6, 8, 10])
print(arr ** 2)         # array([ 1,  4,  9, 16, 25])
print(arr[arr > 2])     # array([3, 4, 5])  — boolean indexing

print(arr.mean())       # 3.0
print(arr.sum())        # 15

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(a @ b)            # matrix multiply: [[19, 22], [43, 50]]
```

## Pandas — DataFrames

Pandas is the default tool for tabular data:

```python
import pandas as pd

df = pd.DataFrame({
    "name":   ["Alice", "Bob", "Carol", "Dave"],
    "dept":   ["Eng",   "HR",  "Eng",   "HR"],
    "salary": [90_000,  60_000, 95_000, 65_000],
    "years":  [3, 7, 5, 2],
})

print(df.head())            # first 5 rows
print(df["name"])           # column → Series
print(df[["name", "salary"]])  # multiple columns → DataFrame
print(df[df["salary"] > 70_000])  # filter rows

df["bonus"] = df["salary"] * 0.1     # new column
dept_stats = df.groupby("dept")["salary"].agg(["mean", "max", "count"])
print(dept_stats)
```

## LangChain — LLM Workflows

LangChain helps connect prompts, models, tools, and retrieval into larger LLM workflows.

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

## PydanticAI — Typed AI Agents

PydanticAI is useful when you want model output to match a Python schema.

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

For AI work, the practical Python stack is usually: JSON, HTTP clients, type hints, async basics, and one or two AI libraries rather than every data-science tool at once.
