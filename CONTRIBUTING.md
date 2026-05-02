# Contributing to suleimanAlQusaimi Python Course

Thank you for your interest in contributing to this educational Python course!
This repository is designed specifically for **blind and visually impaired learners**,
and your contributions help make programming education more accessible.

---

## Table of Contents

- [Who Can Contribute](#who-can-contribute)
- [Ways to Contribute](#ways-to-contribute)
- [Getting Started](#getting-started)
- [File and Folder Naming Conventions](#file-and-folder-naming-conventions)
- [Code Style Guidelines](#code-style-guidelines)
- [Submitting Your Contribution](#submitting-your-contribution)
- [Accessibility Guidelines](#accessibility-guidelines)

---

## Who Can Contribute

Everyone is welcome, including:
- Students who completed the course and want to improve materials
- Educators with suggestions for better explanations
- Developers who want to add new exercises or fix bugs
- Accessibility advocates who can improve screen reader compatibility

---

## Ways to Contribute

1. **Fix typos or errors** in Python code files or guide documents
2. **Add new exercises** that reinforce concepts taught in each lecture
3. **Improve guide.md files** with clearer explanations or additional examples
4. **Translate materials** to support learners in other languages
5. **Report issues** by opening a GitHub Issue
6. **Suggest accessibility improvements** for blind and visually impaired users

---

## Getting Started

### 1. Fork the Repository

Click the **Fork** button on GitHub to create your own copy:
```
https://github.com/mahmoudshaabo1984/suleimanAlQusaimiPythonCourse
```

### 2. Clone Your Fork

```bash
git clone https://github.com/YOUR_USERNAME/suleimanAlQusaimiPythonCourse.git
cd suleimanAlQusaimiPythonCourse
```

### 3. Create a New Branch

Always work on a separate branch, never directly on `main`:
```bash
git checkout -b feature/your-improvement-name
```

### 4. Make Your Changes

Follow the naming conventions and code style guidelines below.

### 5. Test Your Changes

Make sure your Python files run without errors:
```bash
python your_file.py
```

Check for syntax issues:
```bash
python -m py_compile your_file.py
```

---

## File and Folder Naming Conventions

To ensure compatibility across all operating systems and command-line tools:

### Files

| Good (Recommended) | Bad (Avoid) |
|---|---|
| `password_generator.py` | `password generator.py` |
| `number_guessing_game.py` | `Number Guessing Game.py` |
| `link_manager_v1.py` | `linkManager_v1.py` |
| `guide.md` | `Guide.MD` |

### Rules:
- Use **lowercase letters** only
- Use **underscores `_`** instead of spaces
- Use **descriptive names** that explain the file's purpose
- Python files must end with `.py`

### Folders

| Good (Recommended) | Current (Being Updated) |
|---|---|
| `python_extra_files/` | `python extra files/` |
| `extra_codes_for_all_lectures/` | `extra codes for all lectures/` |
| `lecture_2/` | `lecture2/` (acceptable) |

---

## Code Style Guidelines

This course targets beginners, so keep the code **simple and readable**:

### Do:
- Write clear, descriptive variable names: `student_grade` not `sg`
- Add Arabic comments when the primary audience is Arabic speakers
- Keep functions short and focused on one task
- Include `print()` statements that explain what the program is doing
- Handle common errors with `try/except` for a better user experience

### Example — Good style:
```python
# Ask the student for their grade
student_grade = float(input("Enter your grade (0-100): "))

# Determine the letter grade
if student_grade >= 90:
    print("Excellent! Grade: A")
elif student_grade >= 75:
    print("Very Good! Grade: B")
else:
    print("Keep practicing! Grade: C")
```

### Avoid:
- Single-letter variable names (`x`, `y`, `z`) unless in math formulas
- Complex one-liners that are hard for beginners to read
- External library imports not already used in the course

---

## Submitting Your Contribution

### 1. Commit Your Changes

Write a clear commit message in English:
```bash
git add .
git commit -m "Add grade calculator exercise for lecture 4"
```

### 2. Push to Your Fork

```bash
git push origin feature/your-improvement-name
```

### 3. Open a Pull Request

1. Go to your fork on GitHub
2. Click **"Compare & pull request"**
3. Fill in the pull request template:
   - **What did you change?**
   - **Why is this improvement useful for learners?**
   - **Did you test the code?**

---

## Accessibility Guidelines

Since this course is designed for **blind and visually impaired learners**, all contributions must:

- Use **descriptive print messages** that work well with screen readers
- Avoid programs that depend purely on visual output (colors, graphics)
- Prefer **audio feedback** using `winsound` or `print` messages
- Write `guide.md` files using clear heading structure (H1, H2, H3)
- Use **ordered lists** for step-by-step instructions in documentation

---

## Questions?

If you have any questions about contributing, open an Issue on GitHub:
```
https://github.com/mahmoudshaabo1984/suleimanAlQusaimiPythonCourse/issues
```

Thank you for helping make programming education more accessible!
