# python-backed Movie Analyzer Solution

## Overview

This code repository contains my solution for the movie analyzer take-home assessment, that is focused on refactoring implementing a look-up function and refactorization of an existing data structure.

## Setup and Run

1. **Clone the repository:**
   ```bash
   git clone [this-repo-url] [repo-directory-name]
   cd [repo-directory-name]
   ```
2. **Set up virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. **Dependency installation:**
   ```bash
   pip install -r requirements.txt
   ```

## Key Files & Directories

- `src` is the source code package, within it:
  - `models/movie_model.py` contains the Movie dataclass definition.
  - `movie_analyzer.py` contains the core business logic: The `get_top_movies` and `format_movie_list` functions.
- `tests` contains the unit testing package.
- `run.py` contains an examples calls for the business logic implemented.

## Solution Design Rationale

### 1. Data Structure Refactoring

- **Decision:** The raw `list[list]` structure was refactored into the `Movie` dataclass.
- **Justification:** Using this dataclass prevents relying on fragile index lookups and enables the easy addition of business logic to this entity over time. Using `frozen=True` prevents modifications done to these objects for downstream usage.

### 2. Look-up Function: Top N movies that are certified fresh

- **Decision:** The `get_top_movies` function leverages a Min-Heap, provided by Python's built-in `heapq` module.
- **Justification:**
  - Scale was assumed for this problem, with this in mind, a min-heap approach is well suited for top n problems where n is expected to be smaller than the large dataset.
  - For the specific problem, only `top_n` and `certified_fresh=True` are the required constraints. But the same function can be abstracted to support different **criteria** being passed and different **top N**, this is the reason behind the defaults of 10 for `top_n` and `condition_checker` looking for `certified_fresh=True` parameters.

## Testing

The `tests/` directory contains available unit tests for the core logic.

To run these tests:

```bash
pytest
```
