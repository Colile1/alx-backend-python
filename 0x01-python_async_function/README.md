# 0x01. Python - Async

This project covers the basics and practical use of asynchronous programming in Python using the `asyncio` library. The tasks demonstrate how to write, execute, and manage asynchronous coroutines, measure their performance, and work with asyncio tasks.

## Table of Contents
- [General Requirements](#general-requirements)
- [Project Structure](#project-structure)
- [Tasks](#tasks)
  - [0. The basics of async](#0-the-basics-of-async)
  - [1. Let's execute multiple coroutines at the same time with async](#1-lets-execute-multiple-coroutines-at-the-same-time-with-async)
  - [2. Measure the runtime](#2-measure-the-runtime)
  - [3. Tasks](#3-tasks)
  - [4. Tasks (advanced)](#4-tasks-advanced)
- [Usage](#usage)
- [Style & Documentation](#style--documentation)

## General Requirements
- All files are interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7
- All files end with a new line and are executable
- Code follows `pycodestyle` (version 2.5.x)
- All functions and coroutines are type-annotated
- All modules and functions have detailed documentation
- Only standard editors (vi, vim, emacs) are allowed

## Project Structure
```
0x01-python_async_function/
├── 0-basic_async_syntax.py         # Task 0: Basic async coroutine
├── 1-concurrent_coroutines.py      # Task 1: Concurrent coroutines
├── 2-measure_runtime.py            # Task 2: Measure runtime
├── 3-tasks.py                      # Task 3: Asyncio tasks
├── 4-tasks.py                      # Task 4: Advanced tasks
```

## Tasks

### 0. The basics of async
- **File:** `0-basic_async_syntax.py`
- **Function:** `wait_random(max_delay: int = 10) -> float`
- **Description:**
  - Asynchronous coroutine that waits for a random delay between 0 and `max_delay` seconds and returns the delay.
  - Uses the `random` module and `asyncio.sleep`.

### 1. Let's execute multiple coroutines at the same time with async
- **File:** `1-concurrent_coroutines.py`
- **Function:** `wait_n(n: int, max_delay: int) -> List[float]`
- **Description:**
  - Spawns `wait_random` n times with the specified `max_delay`.
  - Returns a list of all delays in ascending order (without using `sort()`).

### 2. Measure the runtime
- **File:** `2-measure_runtime.py`
- **Function:** `measure_time(n: int, max_delay: int) -> float`
- **Description:**
  - Measures the total execution time for `wait_n(n, max_delay)` and returns the average time per coroutine.
  - Uses the `time` module for measurement.

### 3. Tasks
- **File:** `3-tasks.py`
- **Function:** `task_wait_random(max_delay: int) -> asyncio.Task`
- **Description:**
  - Returns an `asyncio.Task` for `wait_random` with the given `max_delay`.
  - Not an async function; uses `asyncio.create_task`.

### 4. Tasks (advanced)
- **File:** `4-tasks.py`
- **Function:** `task_wait_n(n: int, max_delay: int) -> List[float]`
- **Description:**
  - Spawns `task_wait_random` n times and returns a list of delays in ascending order.
  - Similar to `wait_n` but uses tasks.

## Usage
1. Clone the repository and navigate to the project directory.
2. Run each script using Python 3.7+:
   ```bash
   python3 0x01-python_async_function/0-basic_async_syntax.py
   ```
3. You can use the provided main files (e.g., `0-main.py`, `1-main.py`, etc.) to test each task.

## Style & Documentation
- All code is type-annotated and follows PEP8/pycodestyle.
- Each module and function includes a detailed docstring explaining its purpose and usage.

---

This project is part of the ALX Backend Python curriculum and demonstrates practical asynchronous programming patterns in Python.
