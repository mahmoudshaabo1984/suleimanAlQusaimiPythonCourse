# Python Course for Blind Learners with Suleiman Al-Qusaimi — Level 1

A personal repository documenting the journey of learning the Python programming language. This course is designed specifically for blind and visually impaired learners. The original lessons are taught in Arabic on the Ali Al-Amri YouTube channel. This repository contains the source code, exercises, and final applications produced during the course.

## Accessibility Statement

This README is written and structured for screen reader users. It uses:

- A linear heading hierarchy with no skipped levels.
- Descriptive link text that makes sense out of context.
- Plain markdown tables with clear column headers.
- Code blocks with explicit language tags.
- No decorative ASCII art, icons, or emojis.

If you find any section that is difficult to navigate with a screen reader, please open an issue in this repository.

## Table of Contents

- [Course Links](#course-links)
- [Repository Structure](#repository-structure)
- [Detailed Lesson Content](#detailed-lesson-content)
- [Independent Applications](#independent-applications)
- [Extra Python Files](#extra-python-files)
- [Extra Codes for All Lectures](#extra-codes-for-all-lectures)
- [Tested Code Folder](#tested-code-folder)
- [How to Run the Programs](#how-to-run-the-programs)
- [Course Progression Table](#course-progression-table)
- [Target Audience](#target-audience)
- [Instructor](#instructor)
- [Repository Owner](#repository-owner)
- [How to Contribute and Accept Pull Requests](#how-to-contribute-and-accept-pull-requests)

## Course Links

| Description | Link |
| --- | --- |
| YouTube playlist for the course | [Python Course for Blind Learners — Level 1](https://www.youtube.com/playlist?list=PLNotpB8d1N19Xt7cCJi0R0mQZMKaZEOXL) |
| Instructor's website | [ali86.net/py2](https://www.ali86.net/py2) |
| Main repository on GitHub | [mahmoudshaabo1984/suleimanAlQusaimiPythonCourse](https://github.com/mahmoudshaabo1984/suleimanAlQusaimiPythonCourse) |

## Repository Structure

The repository is organised into five main top-level folders:

- `code/` — lesson source code, organised by lecture number from lecture 2 to lecture 10, plus a shared `sounds/` folder.
- `apps/` — independent standalone applications built during and after the course.
- `extra_codes_for_all_lectures/` — a flat collection of all lecture code files in one place for quick review.
- `python_extra_files/` — written summaries, references, and extra resources.
- `suleimanAlQusaimiPythonCourse tested/` — a separate folder containing tested and revised versions of the lecture code and the final applications.

A high level tree view of the repository is shown below.

```text
suleimanAlQusaimiPythonCourse/
├── code/
│   ├── lecture2/
│   ├── lecture3/
│   ├── lecture4/
│   ├── lecture5/
│   ├── lecture6/
│   ├── lecture7/
│   ├── lecture8/
│   ├── lecture9/
│   ├── lecture10/
│   └── sounds/
├── apps/
│   └── channel_name_gen/
├── extra_codes_for_all_lectures/
│   └── sounds/
├── python_extra_files/
├── suleimanAlQusaimiPythonCourse tested/
│   └── sounds/
└── README.md
```

## Detailed Lesson Content

The course covers nine lectures, numbered 2 through 10. Each lecture introduces a set of programming concepts and ends with a final application that combines the new ideas with everything learned so far.

### Lecture 2 — Printing Basics and Variables

Concepts covered:

- The `print()` function for displaying text and numbers.
- String concatenation using the `+` operator.
- Defining variables and storing values.
- The `input()` function for receiving user input.
- The `int()` type conversion from text to number.

Lesson files:

| File | Description |
| --- | --- |
| `code/lecture2/code.py` | Core lesson examples. |
| `code/lecture2/2.py` | Practice notes from the lesson. |
| `code/lecture2/welcome_add_amount.py` | Final application: asks for a name and an amount, then adds 5. |
| `code/lecture2/guide.md` | Lesson guide. |

### Lecture 3 — Variables and Type Conversion

Concepts covered:

- Data types: `str`, `int`, and `float`.
- Receiving user input with `input()`.
- Type conversion functions: `int()`, `float()`, `str()`.
- Performing arithmetic operations on user input.

Lesson files:

| File | Description |
| --- | --- |
| `code/lecture3/code.py` | Core lesson examples. |
| `code/lecture3/3.py` | Practice notes from the lesson. |
| `code/lecture3/mile_to_km_converter.py` | Final application: a miles to kilometres converter. |
| `code/lecture3/guide.md` | Lesson guide. |

### Lecture 4 — Conditional Statements

Concepts covered:

- The `if` conditional statement.
- The `elif` clause for multiple conditions.
- The `else` clause for the default case.
- Nested conditional statements.
- Logical operators: `and`, `or`, `not`.
- Comparison operators: `==`, `!=`, `>`, `<`, `>=`, `<=`.

Lesson files:

| File | Description |
| --- | --- |
| `code/lecture4/code.py` | Core lesson examples. |
| `code/lecture4/4.py` | Practice notes from the lesson. |
| `code/lecture4/grade_calculator.py` | Final application: calculates a student grade as A, B, C, or fail. |
| `code/lecture4/guide.md` | Lesson guide. |

### Lecture 5 — Strings and String Operations

Concepts covered:

- String methods: `.upper()`, `.lower()`, `.capitalize()`, `.title()`.
- Searching and replacing: `.find()`, `.replace()`.
- Indexing and slicing strings.
- The `.isdigit()` method for checking input type.
- Formatting strings with f-strings.
- The `len()` function for measuring string length.

Lesson files:

| File | Description |
| --- | --- |
| `code/lecture5/code.py` | Core lesson examples. |
| `code/lecture5/5.py` | Practice notes from the lesson. |
| `code/lecture5/5test.py` | Additional string exercises. |
| `code/lecture5/string_search.py` | Final application: an advanced text search program. |
| `code/lecture5/guide.md` | Lesson guide. |

### Lecture 6 — Lists

Concepts covered:

- Creating lists and accessing elements by index.
- List methods: `.append()`, `.insert()`, `.remove()`, `.pop()`, `.sort()`, `.copy()`.
- Built-in functions: `sum()`, `min()`, `max()`, `len()`.
- Iterating over lists with `for` loops.
- The difference between reference assignment and copying.

Lesson files:

| File | Description |
| --- | --- |
| `code/lecture6/code.py` | Core lesson examples. |
| `code/lecture6/6.py` | Practice notes from the lesson. |
| `code/lecture6/6test.py` | Exercises on sum, average, and copying. |
| `code/lecture6/average_calculator.py` | Final application: computes the arithmetic mean of five numbers. |
| `code/lecture6/guide.md` | Lesson guide. |

### Lecture 7 — Advanced Loops and Nested Lists

Concepts covered:

- Nested lists.
- The `break` statement to exit a loop.
- The `continue` statement to skip an iteration.
- Infinite loops with `while True`.
- The `for ... else` construct and the not-found case.
- Importing the `webbrowser` module.

Lesson files:

| File | Description |
| --- | --- |
| `code/lecture7/code.py` | Core lesson examples. |
| `code/lecture7/7.py` | Practice notes from the lesson. |
| `code/lecture7/7test.py` | Exercises on loops and search. |
| `code/lecture7/7test1.py` | Additional exercises. |
| `code/lecture7/student_grade_search.py` | Final application: a student grade search system. |
| `code/lecture7/guide.md` | Lesson guide. |

### Lecture 8 — Modules and Random Numbers

Concepts covered:

- The `random` module: `randint()` and `choice()`.
- The `winsound` module for playing sounds on Windows.
- The `while` loop with an attempt counter.
- The `while ... else` construct.
- Defining custom functions with `def`.

Lesson files:

| File | Description |
| --- | --- |
| `code/lecture8/code.py` | Core lesson examples. |
| `code/lecture8/8.py` | Practice notes from the lesson. |
| `code/lecture8/8test.py` | Exercises on the guessing game and the password generator. |
| `code/lecture8/Number Guessing Game.py` | Number guessing game with sound effects. |
| `code/lecture8/password generator.py` | Random password generator. |
| `code/lecture8/guess_game_and_password_generator.py` | Final application: the guessing game and the password generator combined. |
| `code/lecture8/guide.md` | Lesson guide. |

### Lecture 9 — Functions, Dictionaries, and Error Handling

Concepts covered:

- Defining functions with `def` and returning values with `return`.
- Error handling with `try` and `except`.
- Common exceptions: `ZeroDivisionError`, `ValueError`, `KeyError`.
- Dictionaries: creation, adding entries, removing entries with `.pop()`.
- Converting dictionary keys to a list with `list(urls.keys())`.
- The `webbrowser` module for opening URLs.

Lesson files:

| File | Description |
| --- | --- |
| `code/lecture9/code.py` | Core lesson examples. |
| `code/lecture9/9.py` | Practice notes from the lesson. |
| `code/lecture9/9test.py` | Additional exercises. |
| `code/lecture9/test.py` | Exercises on the average function. |
| `code/lecture9/9test from chat gpt.py` | Comparison version produced with ChatGPT. |
| `code/lecture9/9test from manus ai.py` | Comparison version produced with Manus AI. |
| `code/lecture9/9test from sky work ai.py` | Comparison version produced with SkyWork AI. |
| `code/lecture9/Calculate Average Using Function.py` | Computing the average using a function. |
| `code/lecture9/simple Calculator.py` | Simple calculator, version 1. |
| `code/lecture9/linkDictionary.py` | Basic links dictionary. |
| `code/lecture9/linksDictionary.py` | Alternative links dictionary implementation. |
| `code/lecture9/linkManager_v1.py` | Link manager, version 1. |
| `code/lecture9/smartLinkManagev2.py` | Smart link manager, version 2. |
| `code/lecture9/url_manager.py` | Final application: the interactive URL manager. |
| `code/lecture9/guide.md` | Lesson guide. |

### Lecture 10 — Working with Files

Concepts covered:

- Opening files with `open()`.
- File modes: write `"w"`, append `"a"`, and read `"r"`.
- Reading methods: `read()`, `readline()`, `readlines()`.
- Moving the file pointer with `seek()`.
- Closing files with `close()`.
- Arabic language support with `encoding="utf-8"`.
- Building real applications that read data from files.

Lesson files:

| File | Description |
| --- | --- |
| `code/lecture10/code.py` | Core lesson examples. |
| `code/lecture10/10.py` | Practice notes from the lesson. |
| `code/lecture10/multiplication_table.py` | Writes a multiplication table to a file. |
| `code/lecture10/student_grades.py` | Reads student grades from a file. |
| `code/lecture10/diary_system.py` | Final application: the daily diary system. |
| `code/lecture10/grades_data.txt` | Student data used by `student_grades.py`. |
| `code/lecture10/data.txt` | Sample data file for lesson exercises. |
| `code/lecture10/table.txt` | The generated multiplication table. |
| `code/lecture10/guide.md` | Lesson guide. |

## Independent Applications

The `apps/` folder contains standalone programs that were built during and after the course.

### Channel Name Generator

A multi-file project that generates creative YouTube channel names in Arabic and English.

```text
apps/channel_name_gen/
├── generator.py
├── cli.py
└── __init__.py
```

Usage example:

```bash
python apps/channel_name_gen/cli.py -n 5 -l ar -s kebab
```

Available command line options:

| Option | Description |
| --- | --- |
| `-n` | The number of names to generate. |
| `-l ar` or `-l en` | Output language: Arabic or English. |
| `-s kebab`, `-s snake`, `-s camel`, `-s plain` | Naming style for the generated name. |
| `--number` | Append a random number to the generated name. |

### Other Standalone Programs

| File | Description |
| --- | --- |
| `apps/file_operations.py` | File operations: write, append, and read with UTF-8 support. |
| `apps/multiplication_table.py` | Full multiplication table written to `table.txt`. |
| `apps/student_grades.py` | Reads student grades from a file and computes the average. |
| `apps/Number Guessing Game.py` | Number guessing game with sound effects. |
| `apps/password generator.py` | Random password generator. |
| `apps/Calculate Average Using Function.py` | Average computation using a function. |
| `apps/simple Calculator.py` | Simple calculator. |
| `apps/linkDictionary.py` | Links dictionary. |
| `apps/linkManager_v1.py` | Link manager, version 1. |
| `apps/smartLinkManagev2.py` | Smart link manager, version 2. |

The `apps/` folder also contains several Arabic-named utility programs covering an improved error-free calculator, a Gemini-based link manager, an arithmetic average program, a miles-to-kilometres distance converter, a tax calculation program, and a student grades program. These files keep their original Arabic names so that they match the course materials.

## Extra Python Files

The `python_extra_files/` folder contains written summaries, reference notes, and supporting resources.

| File | Description |
| --- | --- |
| `link store.txt` | Saved reference links. |
| `دوال القوائم.txt` | Written summary of list methods. |
| `ملخص الدرس 8[12274].txt` | Summary of lecture 8 — modules and random numbers. |
| `ملخص الدرس التاسع - الدوالي و القواميس .txt` | Summary of lecture 9 — functions and dictionaries. |
| `ملخص الدرس السابع - مواصلة لحلقة forو while و مقدمة عن المكتبات.txt` | Summary of lecture 7 — advanced loops and an introduction to modules. |
| `ملخص كتابي للدرس السادس - القوائم و الحلقات التكرارية.txt` | Summary of lecture 6 — lists and iteration. |
| `موجز لدرس النصوص (1).txt` | Summary of the strings lesson. |
| `sounds.rar` | Archive of the audio files used in the course. |

## Extra Codes for All Lectures

The `extra_codes_for_all_lectures/` folder contains a flat collection of all lecture code files in one place for quick review, along with test files and experiments.

| File | Lecture |
| --- | --- |
| `2.py` | Lecture 2. |
| `3.py` | Lecture 3. |
| `4.py` | Lecture 4. |
| `5.py` | Lecture 5. |
| `5test.py` | Lecture 5 exercises. |
| `6.py` | Lecture 6. |
| `6test.py` | Lecture 6 exercises. |
| `7.py` | Lecture 7. |
| `7test.py` | Lecture 7 exercises. |
| `7test1.py` | Additional lecture 7 exercises. |
| `8.py` | Lecture 8. |
| `8test.py` | Lecture 8 exercises. |
| `9.py` | Lecture 9. |
| `9test.py` | Lecture 9 exercises. |
| `9test from chat gpt.py` | Lecture 9 ChatGPT comparison. |
| `9test from manus ai.py` | Lecture 9 Manus AI comparison. |
| `9test from sky work ai.py` | Lecture 9 SkyWork AI comparison. |
| `10.py` | Lecture 10. |
| `test.py` | General test file. |
| `test1.py` | Additional test file. |
| `test2.py` | Additional test file. |
| `data.txt` | Sample data file. |
| `sounds/` | Audio files used by the lecture programs. |

## Tested Code Folder

The `suleimanAlQusaimiPythonCourse tested/` folder contains tested and revised versions of the lecture code together with the final applications produced from each lecture. It is intended as a clean, verified reference set.

| File | Description |
| --- | --- |
| `1.py` | Introductory test file. |
| `2.py` | Tested code for lecture 2. |
| `3.py` | Tested code for lecture 3. |
| `4.py` | Tested code for lecture 4. |
| `5.py` | Tested code for lecture 5. |
| `5test.py` | Lecture 5 exercises. |
| `6.py` | Tested code for lecture 6. |
| `7.py` | Tested code for lecture 7. |
| `8.py` | Tested code for lecture 8. |
| `9.py` | Tested code for lecture 9. |
| `final_appfor5.py` | Final application for lecture 5. |
| `final_app_for_6.py` | Final application for lecture 6. |
| `final_app_for_7.py` | Final application for lecture 7. |
| `final_app_number _guessing _game_for_8.py` | Number guessing game final application for lecture 8. |
| `final_app_password_generator_for_8.py` | Password generator final application for lecture 8. |
| `final_app_Custom Length Calculator_for8.py` | Custom length calculator final application for lecture 8. |
| `final_app_Calculate Average_Using _Function_for9.py` | Calculate average using function final application for lecture 9. |
| `final_app_Zero_Crash_Calculator_for9.py` | Zero crash calculator final application for lecture 9. |
| `final_app_links_Dictionary_for _9.py` | Links dictionary final application for lecture 9. |
| `final_app_smart_link_manager_v1_for_9.py` | Smart link manager version 1 final application for lecture 9. |
| `final_app_smart_link_manager_v2_for_9.py` | Smart link manager version 2 final application for lecture 9. |
| `sounds/` | Audio files used by the tested programs. |
| `.vscode/` | Visual Studio Code workspace settings. |

## How to Run the Programs

### Requirements

- Python 3.8 or later. Download from [python.org/downloads](https://www.python.org/downloads/).
- A screen reader. Recommended options:
  - NVDA on Windows. Download from [nvaccess.org](https://www.nvaccess.org/download/).
  - Orca on Linux.
- An accessible text editor. Visual Studio Code is recommended. Download from [code.visualstudio.com](https://code.visualstudio.com/).

### Running Lecture Programs

The following commands run the final application of selected lectures.

```bash
python code/lecture3/mile_to_km_converter.py
python code/lecture4/grade_calculator.py
python "code/lecture8/Number Guessing Game.py"
python code/lecture9/url_manager.py
python code/lecture10/diary_system.py
```

### Running the Independent Applications

```bash
python apps/file_operations.py
python apps/multiplication_table.py
python apps/student_grades.py
python "apps/Number Guessing Game.py"
```

### Important Note About Sound Files

The number guessing game uses audio files located in `code/sounds/`. Run the program from inside the `code/` folder so that the relative paths to the audio files resolve correctly:

```bash
cd code
python "lecture8/Number Guessing Game.py"
```

## Course Progression Table

| Lecture | Topic | New Concept | Final Application |
| --- | --- | --- | --- |
| 2 | Printing and variables | `print()`, `input()`, `int()` | Welcome and add an amount. |
| 3 | Data types | `float()`, arithmetic operations | Miles to kilometres converter. |
| 4 | Conditionals | `if` / `elif` / `else` | Grade calculator. |
| 5 | Strings | Slicing, `find()`, f-strings | Text search program. |
| 6 | Lists | `append()`, `sort()`, `sum()` | Average calculator. |
| 7 | Advanced loops | `break`, `continue`, `while True` | Student grade search. |
| 8 | Modules | `random`, `winsound` | Number guessing game and password generator. |
| 9 | Functions and dictionaries | `def`, `try` / `except`, `dict` | URL manager. |
| 10 | File handling | `open()`, `read()`, `write()` | Daily diary system. |

## Target Audience

This course is designed for:

- Blind and visually impaired learners who want to learn programming.
- Arabic speakers who are beginners in the Python ecosystem.
- Screen reader users on Windows with NVDA, or on Linux with Orca.

## Instructor

Suleiman Al-Qusaimi is the course instructor and a specialist in teaching programming to blind learners. The course is published on the Ali Al-Amri YouTube channel.

## Repository Owner

Mahmoud Shaabo, a web development trainee at CodeYourFuture, Sheffield.

## How to Contribute and Accept Pull Requests

### What is a Pull Request?

A pull request is a GitHub mechanism that allows any contributor to propose changes to the repository. The repository owner can review the proposed changes and either merge them into the main branch or close the pull request without merging.

### Steps to Review and Merge a Pull Request into the Main Branch

1. Open the repository page on GitHub at [mahmoudshaabo1984/suleimanAlQusaimiPythonCourse](https://github.com/mahmoudshaabo1984/suleimanAlQusaimiPythonCourse).
2. Select the Pull requests tab to see the list of open pull requests.
3. Open the pull request you want to review. Read the description of the proposed changes, then select the Files changed tab to review the modified code.
4. Optionally add a comment to discuss the proposed changes with the contributor.
5. If the changes are acceptable, select the Merge pull request button, then select Confirm merge to merge the changes into the `main` branch.
6. Optionally, delete the source branch after merging by selecting the Delete branch button.

If the Pull requests list is empty, there are no open pull requests at the moment. Make sure the contributor has actually submitted a pull request and that the correct repository URL is being used.

---

This repository documents a personal Python learning journey with accessibility for blind and visually impaired learners as a primary design goal.
