# Git-Practice — Testing instructions

This project contains `hello.py` and a small unittest file.

To run the tests (PowerShell / Windows):

python -m unittest tests.test_hello -v

Alternatively, to run all discovered tests (may require a package layout):

python -m unittest discover -v

Notes:
- The `hello.py` script now guards `main()` with `if __name__ == "__main__"` so importing the module won't run interactive prompts.
- Tests live in `tests/test_hello.py` and use Python's built-in `unittest`.
