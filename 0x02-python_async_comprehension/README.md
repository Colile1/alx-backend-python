# 0x02. Python - Async Comprehension

This project explores advanced asynchronous programming in Python, focusing on async comprehensions and generators. The tasks demonstrate how to generate random numbers asynchronously, collect them using async comprehensions, and measure the performance of concurrent asynchronous operations.

## Table of Contents
- [General Requirements](#general-requirements)
- [Project Structure](#project-structure)
- [Tasks](#tasks)
  - [0. Async Generator](#0-async-generator)
  - [1. Async Comprehensions](#1-async-comprehensions)
  - [2. Run time for four parallel comprehensions](#2-run-time-for-four-parallel-comprehensions)
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
0x02-python_async_comprehension/
├── 0-async_generator.py        # Task 0: Async generator coroutine
├── 1-async_comprehension.py   # Task 1: Async comprehension coroutine
├── 2-measure_runtime.py       # Task 2: Measure runtime for parallel comprehensions
├── README.md
```

## Tasks

### 0. Async Generator
- **File:** `0-async_generator.py`
- **Function:** `async_generator() -> AsyncGenerator[float, None]`
- **Description:**
  - Asynchronous generator that yields a random float between 0 and 10, 10 times, waiting 1 second between each yield.

### 1. Async Comprehensions
- **File:** `1-async_comprehension.py`
- **Function:** `async_comprehension() -> List[float]`
- **Description:**
  - Collects 10 random numbers from `async_generator` using an async comprehension and returns them as a list.

### 2. Run time for four parallel comprehensions
- **File:** `2-measure_runtime.py`
- **Function:** `measure_runtime() -> float`
- **Description:**
  - Runs `async_comprehension` four times in parallel using `asyncio.gather` and measures the total runtime in seconds.

## Usage
1. Clone the repository and navigate to the project directory.
2. Run each script using Python 3.7+:
   ```bash
   python3 0x02-python_async_comprehension/0-async_generator.py
   ```
3. You can use the provided main files (e.g., `0-main.py`, `1-main.py`, etc.) to test each task.

## Style & Documentation
- All code is type-annotated and follows PEP8/pycodestyle.
- Each module and function includes a detailed docstring explaining its purpose and usage.

---

This project is part of the ALX Backend Python curriculum and demonstrates advanced asynchronous programming patterns in Python.
