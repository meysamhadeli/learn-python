
## Decorators

Decorators wrap functions to add behavior without changing the original function body.

### What is a Decorator?

A decorator is a function that takes a function and returns another function.

```python
@log_time
def process_data(data):
    return [x * 2 for x in data]
```

This is equivalent to:

```python
def process_data(data):
    return [x * 2 for x in data]
process_data = log_time(process_data)
```

### Basic Decorator

```python
import time

def log_time(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper

@log_time
def get_users():
    time.sleep(0.5)
    return ["Alice", "Bob"]

users = get_users()  # Output: get_users took 0.5012s
```

### Decorators with Parameters

When a decorator takes arguments like `@retry(times=3)`, it is a decorator factory:

```python
def retry(times=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == times:
                        raise
                    print(f"Attempt {attempt} failed: {e}. Retrying...")
        return wrapper
    return decorator

@retry(times=3)
def fetch_user_data(user_id):
    import random
    if random.random() < 0.7:
        raise ConnectionError("API timeout")
    return {"id": user_id, "name": f"User{user_id}"}
```

### Multiple Decorators

Decorators can be stacked — they apply from bottom to top:

```python
@log_time
@retry(times=2)
def fetch_data():
    # Runs: retry first, then log_time wraps the result
    pass

# Equivalent to:
# fetch_data = log_time(retry(times=2)(fetch_data))
```

### Common Use Cases

The most common production use cases are logging, auth, caching, retry logic, and framework hooks.

#### Logging

```python
import logging

def log_call(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Called {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_call
def process_order(order_id, customer_id):
    print(f"Processing order {order_id} for customer {customer_id}")
    return {"order_id": order_id, "status": "processed"}

result = process_order(123, 456)
```

#### Auth

```python
def require_role(required_role):
    def decorator(func):
        def wrapper(*args, **kwargs):
            current_user = get_current_user()  # hypothetical function
            if current_user.get("role") != required_role:
                raise PermissionError(f"Requires {required_role} role")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@require_role("admin")
def delete_user(user_id):
    print(f"Deleting user {user_id} from database")
    return {"status": "deleted", "user_id": user_id}
```

#### Caching

```python
from functools import cache

@cache
def expensive_calculation(n):
    print(f"Calculating for {n}...")
    result = sum(i * i for i in range(n))
    return result
```

#### Retry

```python
def retry_with_backoff(max_attempts=3, base_delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts:
                        raise
                    delay = base_delay * (2 ** (attempt - 1))  # Exponential backoff
                    print(f"Attempt {attempt} failed: {e}. Retrying in {delay}s...")
                    time.sleep(delay)
        return wrapper
    return decorator

@retry_with_backoff(max_attempts=3, base_delay=0.5)
def call_external_api(endpoint):
    import random
    if random.random() < 0.6:
        raise TimeoutError("External service timeout")
    return {"data": "successful response"}
```

Use `@functools.wraps` in production so wrapped functions keep their original name and metadata.