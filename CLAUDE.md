# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

RULES:

1. Be as simple as possible. ALWAYS think ultra hard about the simplest possible changes to code with the least amount of extra characters.

## Project Overview

BookBot is a text analysis tool designed to analyze books. Currently implements word counting functionality for text files. This is a Boot.dev learning project.

## Architecture

**Current structure has a circular import issue:**
- `main.py` imports `get_num_words` from `stats.py`
- `stats.py` imports `get_book_text` from `main.py`

**Key functions:**
- `main.py:get_book_text(book_filepath)` - Reads a book file and returns its contents
- `stats.py:get_num_words()` - Counts words in the Frankenstein book (hardcoded path)

## Development Commands

```bash
# Run the program
python main.py

# No test, lint, or build commands currently configured
```

## Critical Issues to Address

1. **Circular Import**: The circular dependency between main.py and stats.py needs to be resolved
2. **Hardcoded Path**: `stats.py` has hardcoded path to `books/frankenstein.txt`
3. **No CLI Interface**: Program runs immediately without accepting arguments

## Project Structure

```
bookbot/
├── main.py          # Entry point with file reading utility
├── stats.py         # Text analysis functions
├── books/           # Book files (gitignored)
│   └── frankenstein.txt
└── README.md        # Minimal project description
```

## Notes for Development

- This is an early-stage Boot.dev project
- No external dependencies (uses only Python standard library)
- Potential for expansion: character counting, word frequency analysis, multiple book support
- Consider refactoring to eliminate circular imports before adding new features