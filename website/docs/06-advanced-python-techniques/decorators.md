
## Decorators

Decorators let you modify or enhance functions without changing their actual code. 

### What is a Decorator?

A decorator is a function that takes another function as input and returns a new function that wraps the original. The `@decorator` syntax is just syntactic sugar — this:

```python
@log_time
def process_data(data):
    return [x * 2 for x in data]
```

Is exactly the same as:

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
    # Simulate API call
    time.sleep(0.5)
    return ["Alice", "Bob"]

users = get_users()  # Output: get_users took 0.5012s
```

**What's happening:**
1. `log_time` receives `get_users` as an argument
2. `wrapper` is created with the timing logic
3. `wrapper` replaces the original `get_users`

### Decorators with Parameters

When you see decorators with `()` like `@retry(times=3)`, it's a decorator factory:

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

# Will retry up to 3 times if it fails
user = fetch_user_data(123)
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

The decorators you'll actually use in production:

#### 1. Logging/Tracing

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
# Logs: Called process_order with args=(123, 456), kwargs={}
# Logs: process_order returned {'order_id': 123, 'status': 'processed'}
```

#### 2. Authentication/Authorization

```python
def require_role(required_role):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Simulate getting current user from session/token
            current_user = get_current_user()  # hypothetical function
            if current_user.get("role") != required_role:
                raise PermissionError(f"Requires {required_role} role")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@require_role("admin")
def delete_user(user_id):
    print(f"Deleting user {user_id} from database")
    # Delete logic here
    return {"status": "deleted", "user_id": user_id}

# This would work for admin users
try:
    delete_user(42)
except PermissionError as e:
    print(f"Access denied: {e}")
```

#### 3. Caching Results

```python
from functools import cache

@cache
def expensive_calculation(n):
    print(f"Calculating for {n}...")
    result = sum(i * i for i in range(n))
    return result

# First call - calculates
result1 = expensive_calculation(1000)  # Prints: Calculating for 1000...
# Second call - uses cache
result2 = expensive_calculation(1000)  # No print, returns cached result
result3 = expensive_calculation(2000)  # Calculates new value
```

#### 4. Retry Logic with Backoff

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

#### 5. Input Validation

```python
def validate_types(types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Validate positional args
            for i, (arg, expected_type) in enumerate(zip(args, types)):
                if not isinstance(arg, expected_type):
                    raise TypeError(f"Argument {i} expected {expected_type.__name__}, got {type(arg).__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@validate_types([int, str, float])
def create_product(product_id, name, price):
    print(f"Creating product: {product_id} - {name} (${price})")
    return {"id": product_id, "name": name, "price": price}

# Works correctly
product = create_product(101, "Laptop", 999.99)

# Raises TypeError
try:
    product = create_product("101", "Laptop", 999.99)  # First arg should be int
except TypeError as e:
    print(f"Validation failed: {e}")
```

#### 6. Rate Limiting

```python
def rate_limit(calls_per_minute=10):
    def decorator(func):
        last_called = [0.0]  # Use list for mutable state
        interval = 60.0 / calls_per_minute
        def wrapper(*args, **kwargs):
            now = time.time()
            if now - last_called[0] < interval:
                wait = interval - (now - last_called[0])
                print(f"Rate limited, waiting {wait:.2f}s...")
                time.sleep(wait)
            last_called[0] = time.time()
            return func(*args, **kwargs)
        return wrapper
    return decorator

@rate_limit(calls_per_minute=2)
def make_api_request(endpoint):
    print(f"Making API request to {endpoint}")
    return {"status": "success"}

# Trying to call too quickly will be throttled
result1 = make_api_request("/users")
result2 = make_api_request("/orders")
result3 = make_api_request("/products")  # This one will be rate limited
```

`@functools.wraps` is good practice for production code but not required to understand the concept.