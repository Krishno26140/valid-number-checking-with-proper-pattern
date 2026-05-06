# Number Validator Using Regular Expressions



## Overview

This project is a Python-based number validation system that uses Regular Expressions (`re` module) to verify whether a number follows a strict predefined format.

The program only accepts numbers in the following format:

```text
98-1234-5678
```

Any incorrect input is rejected, and the user is asked to enter the number again until a valid format is provided.

---

## Features

* Validates numbers using Regular Expressions
* Ensures the number starts with `98`
* Enforces exact formatting using hyphens (`-`)
* Requires exactly 4 digits after each hyphen
* Re-prompts user until valid input is entered
* Clean and modular function-based structure

---

## Technologies Used

* Python 3
* `re` module (Regular Expressions)

---

## Regex Pattern Used

```python
r"(98)-\d{4}-\d{4}"
```

---

## Pattern Explanation

| Pattern | Meaning                            |
| ------- | ---------------------------------- |
| `(98)`  | Groups and matches the number `98` |
| `-`     | Matches the hyphen character       |
| `\d{4}` | Matches exactly 4 digits           |
| `-`     | Matches another hyphen             |
| `\d{4}` | Matches exactly 4 digits again     |

---

## Example Inputs

### Valid Input

```text
98-1234-5678
```

### Invalid Inputs

```text
97-1234-5678
98-12345-5678
98-1234-567
9812345678
98_1234_5678
```

---

## Project Structure

```text
number-validator/
│
├── number_validator.py
└── README.md
```

---

## How to Run

### 1. Clone the Repository


git clone https://github.com/your-username/number-validator.git


### 2. Open the Project Directory


cd number-validator


### 3. Run the Program


python number_validator.py




## Program Workflow

1. User enters a number
2. Program checks the format using regex
3. If valid:

   * Displays `Valid Number`
4. If invalid:

   * Displays error message
   * Requests input again



## Learning Objectives

This project demonstrates:

* Regular Expressions in Python
* Input validation
* Function-based programming
* Loops and conditional statements
* Clean code structuring



## Future Improvements

* Support multiple prefixes
* Add country code validation
* Convert into GUI application
* Create web-based version using HTML/CSS/JavaScript
* Store validated numbers in a database



## Author

Subhradeep Sardar
BCA Student


