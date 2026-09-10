<div align="center">

# 🐍 Introduction to Python

**The starting point of the journey — what Python is, why it dominates modern software, and how to get set up.**

![Topic](https://img.shields.io/badge/Topic-Python%20Basics-3776AB?style=flat-square&logo=python&logoColor=white)
![Level](https://img.shields.io/badge/Level-Beginner-brightgreen?style=flat-square)

</div>

[⬅ Back to Python module](../README.md)

---

## 🤔 What is Python?

Python is a **high-level, general-purpose, object-oriented programming language** — designed to be readable, concise, and easy to pick up even for someone with zero programming background.

| | |
|---|---|
| **Created by** | Guido van Rossum |
| **First released** | 1991 |
| **Name origin** | Named after *Monty Python's Flying Circus*, the British comedy show — not the snake |
| **Paradigm** | Object-oriented, dynamically typed |
| **Execution** | Interpreted, via the **Python Virtual Machine (PVM)** |

> Python's philosophy favors **less code, more clarity** — a big reason it became the default language for beginners *and* professionals alike.

---

## 🚀 Why Python?

Python's popularity isn't accidental — it's a product of a few deliberate design choices:

- **Concise & readable** — close to plain English, minimal boilerplate compared to languages like Java or C++
- **Dynamically typed** — no need to declare variable types explicitly
- **Interpreted, not compiled** — code runs line-by-line, making debugging and experimentation fast
- **Massive ecosystem** — a library for almost everything (data, web, automation, AI)
- **Beginner-friendly, industry-proven** — same language for a first "Hello World" and for production ML systems at scale

### Where the demand is coming from

Python currently rides the wave of four major industry trends:

`Machine Learning` · `Artificial Intelligence` · `Data Science` · `IoT (Internet of Things)`

### Who's using it

Some of the biggest names in tech run critical systems on Python:

**Google** · **NASA** · **Uber** · **Netflix** · **Reddit** · **Meta (Facebook)** · **Spotify**

---

## 🧩 Real-World Applications

| Domain | What Python Is Used For | Common Libraries/Frameworks |
|---|---|---|
| 🌐 **Web Development** | Building full websites & web apps | Django, Flask |
| 🤖 **Machine Learning & AI** | Training models, building intelligent systems | TensorFlow, PyTorch, scikit-learn |
| 🖥️ **Desktop Applications** | GUI apps with buttons, menus, windows | PyQt, Tkinter |
| 🕸️ **Web Scraping** | Collecting and parsing data from websites | BeautifulSoup, Scrapy |
| 🔬 **Scientific Computing** | Complex math, scientific data analysis | NumPy, SciPy, pandas |
| 📝 **Text Processing / NLP** | Language understanding, sentiment analysis | NLTK, spaCy |
| 🎮 **Game Development** | Building games & simulations | Pygame, Pyglet |
| 📊 **Business Applications** | Reporting, dashboards, product analytics | pandas, matplotlib |

### Career paths this opens up

Python skills map to a wide range of roles: **Web Developer, Backend Developer, Data Scientist, Machine Learning Engineer, Research Engineer, Quality Assurance Engineer, Product Manager,** and **Technical Support Specialist** — among others. The common thread is that Python shows up at nearly every layer of the modern tech stack.

---

## 🕰️ Python Versions

Python has two major historical version lines. **Python 3.x is the current, actively developed standard** — Python 2.x reached end-of-life and is legacy only.

| Python 3.x | Release Date | | Python 2.x | Release Date |
|---|---|---|---|---|
| 3.0 | 2008-12-03 | | 2.0 | 2000-10-16 |
| 3.1 | 2009-06-26 | | 2.1 | 2001-04-15 |
| 3.2 | 2011-02-20 | | 2.2 | 2001-12-21 |
| 3.3 | 2012-09-29 | | 2.3 | 2003-07-29 |
| 3.4 | 2014-03-17 | | 2.4 | 2004-11-30 |
| 3.5 | 2015-09-13 | | 2.5 | 2006-09-19 |
| 3.6 | 2016-12-23 | | 2.6 | 2008-10-02 |
| 3.7 | 2018-06-27 | | 2.7 | 2010-07-03 |
| 3.8 | 2020-04-29 | | | |
| 3.9 | 2020-10-05 | | | |
| 3.10 | 2021-10-04 | | | |
| 3.13 | 2024-10-07 | | | |

---

## ⚙️ Interpreter vs. Compiler

Python is an **interpreted language** — understanding what that means (and how it differs from compiled languages) is core to understanding how Python actually runs your code.

| | Interpreter (Python) | Compiler |
|---|---|---|
| **How it runs code** | Translates and executes one statement at a time | Scans the entire program and translates it all at once into machine code |
| **On error** | Runs until it hits the broken line, then stops | Won't execute at all if any error exists anywhere |
| **Debugging** | Easy — step through line by line | Harder — no line-by-line execution |
| **Speed** | Generally slower (translation happens at runtime) | Generally faster (already translated ahead of time) |

**What is a Python interpreter, exactly?** It's the program (`python` / `python3`) installed on your machine that reads your `.py` file and converts each line into machine code the computer can execute — in real time, as your program runs.

---

## 🧰 Python IDEs

An **IDE (Integrated Development Environment)** bundles everything you need to write, run, and debug code into one tool — it handles interpreting your Python code, running scripts, and catching errors, so you're not juggling separate tools.

Popular choices for this course:

| IDE | Best For |
|---|---|
| **Jupyter Notebook** | Interactive, cell-by-cell data science work *(used throughout this repo)* |
| **VS Code** | General-purpose, lightweight, highly extensible |
| **PyCharm** | Full-featured, best suited for dedicated Python development |
| **Spyder** | Scientific computing, similar feel to MATLAB |

---

## 🛠️ Setting Up Python (Windows Environment Variables)

If running `python` from the command line doesn't work, it usually means Python isn't on your system's PATH yet. Quick fix:

1. Open Command Prompt and try `python` — if it fails, continue below
2. Locate where Python is installed, e.g.:
   `C:\Users\<YourUser>\AppData\Local\Programs\Python\Python311`
3. Open **System Properties → Environment Variables**
4. Under **System variables**, select `Path` → **Edit** → **New**
5. Paste the Python installation path (and its `Scripts` subfolder) into the list
6. Save, reopen Command Prompt, and try `python` again

---

## 📁 Contents

| File | Type | What's Inside |
|---|---|---|
| 📓 `Python_Introduction.ipynb` | Jupyter Notebook | The core lecture notes this README is based on — Python basics, history, interpreter vs. compiler, IDEs, and environment setup |
| 📄 `LEARN PYTHON FOR DATASCIENCE & AI.pdf` | Notes / PDF | Extended notes on Python's real-world applications and the career paths it opens up |
| 📄 `python_tutorial_to_strings_notes.pdf` | Notes / PDF | Reference notes carried into the next topic (Strings, Indexing & Slicing) |
# Introduction to Python

[⬅ Back to Python module](../README.md)

First steps into Python for data science and AI — environment setup, basic syntax, and why Python is the language of choice for this field.

## 📁 Contents

| File | Type |
|---|---|
| 📄 `LEARN PYTHON FOR DATASCIENCE & AI.pdf` | Notes / PDF |
| 📓 `Python_Introduction.ipynb` | Jupyter Notebook |
| 📄 `python_tutorial_to_strings_notes.pdf` | Notes / PDF |
