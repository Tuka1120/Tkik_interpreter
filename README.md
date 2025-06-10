# Aingal Language

## 1. Project Overview

This project implements an interpreter for a custom English-like programming language.

The interpreter:

- Processes source code written in a natural language syntax  
- Executes programs with variables, control structures, functions, and I/O operations  
- Provides error diagnostics and type handling  
- Built using ANTLR4 for parsing and Python for execution  

### Key Features:

- Variables with explicit types: `int`, `string`, `bool`, `float`, `matrix`  
- Arithmetic and logical operations  
- Control flow: `If/Else`, `While`, `For` loops  
- Function declarations and recursive calls  
- Scope management for variables  
- Type promotion/conversion  
- Output display  

---

## 2. Installation & Setup

### Prerequisites:

- Python 3.7+  
- Java Runtime (for ANTLR)

### Installation:

Install the ANTLR runtime for Python:

```bash
pip install antlr4-python3-runtime
