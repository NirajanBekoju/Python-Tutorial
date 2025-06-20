# 10 Simple Python Projects for Beginners

## Project 1: Contact Book

Create a menu-driven program to manage a contact book that stores names and phone numbers in a dictionary. Implement functions to add a contact, remove a contact, display all contacts, and search for a contact by name. Include error handling for invalid phone numbers (e.g., non-digits) and save contacts to a file for persistence. Show the results in a Streamlit app where users can input a name and phone number, select actions (add, remove, search, display), and view the output.

**Python Code**:

```python
# contact_book.py
def add_contact(contacts, name, phone):
    try:
        if not phone.isdigit():
            raise ValueError("Phone number must be digits")
        contacts[name] = phone
        save_contacts(contacts)
        return f"Added {name}"
    except ValueError as e:
        return str(e)

def remove_contact(contacts, name):
    try:
        return contacts.pop(name, f"{name} not found")
    except KeyError:
        return f"{name} not found"

def display_contacts(contacts):
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()]) if contacts else "No contacts"

def search_contact(contacts, name):
    return contacts.get(name, f"{name} not found")

def save_contacts(contacts):
    with open("contacts.txt", "w") as f:
        for name, phone in contacts.items():
            f.write(f"{name},{phone}\n")

def load_contacts():
    contacts = {}
    try:
        with open("contacts.txt", "r") as f:
            for line in f:
                name, phone = line.strip().split(",")
                contacts[name] = phone
    except FileNotFoundError:
        pass
    return contacts

if __name__ == "__main__":
    contacts = load_contacts()
    print(add_contact(contacts, "Alice", "1234567890"))
    print(display_contacts(contacts))
```

**Streamlit Note**: Create a Streamlit app using `st.text_input` for name and phone, `st.selectbox` for actions (add, remove, search, display), and `st.write` to show results. Save contacts to a file for persistence.

---

## Project 2: To-Do List Manager

Create a program to manage a to-do list using a list of dictionaries, where each task has a description and a completion status. Implement functions to add a task, remove a task by index, mark a task as complete, and display all tasks. Save tasks to a file for persistence and handle errors for invalid indices. Show the results in a Streamlit app where users can input tasks, select tasks to mark complete or remove, and view the task list.  
**Python Code**:

```python
# todo_list.py
def add_task(tasks, task):
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    return f"Added {task}"

def remove_task(tasks, index):
    try:
        task = tasks.pop(index)
        save_tasks(tasks)
        return f"Removed {task['task']}"
    except IndexError:
        return "Invalid index"

def complete_task(tasks, index):
    try:
        tasks[index]["completed"] = True
        save_tasks(tasks)
        return f"Completed {tasks[index]['task']}"
    except IndexError:
        return "Invalid index"

def display_tasks(tasks):
    return "\n".join([f"{i}: {t['task']} {'(Done)' if t['completed'] else ''}" for i, t in enumerate(tasks)]) if tasks else "No tasks"

def save_tasks(tasks):
    with open("tasks.txt", "w") as f:
        for t in tasks:
            f.write(f"{t['task']},{t['completed']}\n")

def load_tasks():
    tasks = []
    try:
        with open("tasks.txt", "r") as f:
            for line in f:
                task, completed = line.strip().split(",")
                tasks.append({"task": task, "completed": completed == "True"})
    except FileNotFoundError:
        pass
    return tasks

if __name__ == "__main__":
    tasks = load_tasks()
    print(add_task(tasks, "Buy groceries"))
    print(display_tasks(tasks))
```

**Streamlit Note**: Create a Streamlit app using `st.text_input` for task input, `st.number_input` for task index, `st.button` for actions (add, remove, complete, display), and `st.write` to show the task list.

---

## Project 3: Simple Calculator

Create a calculator program that performs basic operations (add, subtract, multiply, divide) using separate functions. Include error handling for division by zero and invalid operations. Show the results in a Streamlit app where users can input two numbers, select an operation, and view the result.  
**Python Code**:

```python
# calculator.py
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

def calculate(operation, a, b):
    operations = {"add": add, "subtract": subtract, "multiply": multiply, "divide": divide}
    return operations.get(operation, lambda x, y: "Invalid operation")(a, b)

if __name__ == "__main__":
    print(calculate("add", 5, 3))
    print(calculate("divide", 10, 0))
```

**Streamlit Note**: Create a Streamlit app using `st.number_input` for two numbers, `st.selectbox` for operation (add, subtract, multiply, divide), `st.button` to calculate, and `st.write` to display the result.

---

## Project 4: Number Guessing Game

Create a number guessing game where the program generates a random number between 1 and 100, and the user guesses it. Provide feedback (too high, too low, or correct) and track the number of attempts. Handle invalid inputs (e.g., non-numeric guesses). Show the results in a Streamlit app where users can input guesses and see feedback and attempt count.  
**Python Code**:

```python
# number_guessing.py
import random

def guess_game(guess, number, attempts):
    try:
        guess = int(guess)
        attempts += 1
        if guess < number:
            return "Too low", attempts
        elif guess > number:
            return "Too high", attempts
        else:
            return f"Correct! Took {attempts} attempts", attempts
    except ValueError:
        return "Enter a valid number", attempts

if __name__ == "__main__":
    number = random.randint(1, 100)
    attempts = 0
    guess = input("Guess a number (1-100): ")
    result, attempts = guess_game(guess, number, attempts)
    print(result)
```

**Streamlit Note**: Create a Streamlit app using `st.number_input` for guesses, `st.button` to submit guesses, and `st.write` to show feedback and attempt count. Store the random number and attempts in session state.

---

## Project 5: Student Grade Calculator

Create a program to calculate student grades based on numeric scores, assigning letter grades (A: 90–100, B: 80–89, C: 70–79, D: 60–69, F: <60). Store students and scores in a dictionary and use list comprehension to process grades. Show the results in a Streamlit app where users can input student names and scores, and view the grade list.
**Python Code**:

```python
# grade_calculator.py
def calculate_grade(score):
    if score >= 90: return "A"
    elif score >= 80: return "B"
    elif score >= 70: return "C"
    elif score >= 60: return "D"
    else: return "F"

def process_grades(students):
    return {name: calculate_grade(score) for name, score in students.items()}

if __name__ == "__main__":
    students = {"Alice": 85, "Bob": 92, "Charlie": 78}
    print(process_grades(students))
```

**Streamlit Note**: Create a Streamlit app using `st.text_input` for student names, `st.number_input` for scores, `st.button` to add students and display grades, and `st.write` to show the grade list.

---

## Project 6: Word Counter

Create a program to count the frequency of words in a text string, ignoring punctuation and case. Use string methods to clean the text and a dictionary to store word counts. Show the results in a Streamlit app where users can input text and view the word frequency dictionary.  
**Python Code**:

```python
# word_counter.py
import string

def count_words(text):
    text = text.translate(str.maketrans("", "", string.punctuation)).lower()
    words = text.split()
    return {word: words.count(word) for word in set(words)}

if __name__ == "__main__":
    print(count_words("Hello world! Hello Python."))
```

**Streamlit Note**: Create a Streamlit app using `st.text_area` for text input, `st.button` to count words, and `st.write` to display the word frequency dictionary.

---

## Project 7: Simple Bank Account

Create a bank account class with methods for deposit, withdrawal, and balance checking. Use OOP principles and include error handling for negative amounts and insufficient funds. Show the results in a Streamlit app where users can input amounts for deposit or withdrawal and view the balance.  
**Python Code**:

```python
# bank_account.py
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Amount must be positive")
            self.balance += amount
            return f"Deposited {amount}, new balance: {self.balance}"
        except ValueError as e:
            return str(e)

    def withdraw(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Amount must be positive")
            if amount > self.balance:
                raise ValueError("Insufficient funds")
            self.balance -= amount
            return f"Withdrew {amount}, new balance: {self.balance}"
        except ValueError as e:
            return str(e)

    def get_balance(self):
        return f"Balance for {self.owner}: {self.balance}"

if __name__ == "__main__":
    account = BankAccount("Alice", 100)
    print(account.deposit(50))
    print(account.withdraw(30))
    print(account.get_balance())
```

**Streamlit Note**: Create a Streamlit app using `st.number_input` for amount, `st.button` for deposit, withdraw, and check balance actions, and `st.write` to display the results.

---

## Project 8: Palindrome Checker

Create a function to check if a string is a palindrome, ignoring case and punctuation. Use string methods and a lambda function for text cleaning. Show the results in a Streamlit app where users can input a string and see if it’s a palindrome.  
**Python Code**:

```python
# palindrome.py
def is_palindrome(s):
    clean = lambda x: "".join(c.lower() for c in x if c.isalnum())
    s = clean(s)
    return s == s[::-1]

if __name__ == "__main__":
    print(is_palindrome("A man, a plan, a canal: Panama"))
```

**Streamlit Note**: Create a Streamlit app using `st.text_input` for the string, `st.button` to check, and `st.write` to display whether the input is a palindrome.

---

## Project 9: Expense Tracker

Create a program to track expenses by category, storing amounts in a dictionary. Implement functions to add expenses and display all expenses, with file I/O for persistence and error handling for negative amounts. Show the results in a Streamlit app where users can input a category and amount, and view the expense summary.
**Python Code**:

```python
# expense_tracker.py
def add_expense(expenses, category, amount):
    try:
        if amount <= 0:
            raise ValueError("Amount must be positive")
        expenses[category] = expenses.get(category, 0) + amount
        save_expenses(expenses)
        return f"Added {amount} to {category}"
    except ValueError as e:
        return str(e)

def display_expenses(expenses):
    return "\n".join([f"{cat}: {amt}" for cat, amt in expenses.items()]) if expenses else "No expenses"

def save_expenses(expenses):
    with open("expenses.txt", "w") as f:
        for cat, amt in expenses.items():
            f.write(f"{cat},{amt}\n")

def load_expenses():
    expenses = {}
    try:
        with open("expenses.txt", "r") as f:
            for line in f:
                cat, amt = line.strip().split(",")
                expenses[cat] = float(amt)
    except FileNotFoundError:
        pass
    return expenses

if __name__ == "__main__":
    expenses = load_expenses()
    print(add_expense(expenses, "Food", 50))
    print(display_expenses(expenses))
```

**Streamlit Note**: Create a Streamlit app using `st.text_input` for category, `st.number_input` for amount, `st.button` for add and display actions, and `st.write` to show the expense summary.

---

## Project 10: Simple Data Visualizer

Create a program to visualize a small dataset of student scores using Matplotlib or Seaborn. Use Pandas to store the data as a DataFrame and NumPy for any calculations. Generate a bar plot and save it as an image. Show the results in a Streamlit app where users can input student names and scores, and view the data and plot.
**Python Code**:

```python
# data_visualizer.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_data(data):
    df = pd.DataFrame(data)
    plt.figure(figsize=(8, 6))
    sns.barplot(x="Score", y="Student"; data=df)
    plt.savefig("plot.png")
    plt.close()
    return "Plot saved as plot.png"

if __name__ == "__main__":
    data = {"Student": ["Alice", "Bob", "Charlie"], "Score": [85, 92, 78]}
    print(visualize_data(data))
```

**Streamlit Note**: Create a Streamlit app using `st.text_input` for student names, `st.number_input` for scores, `st.button` to add data and generate the plot, `st.write` to show the data, and `st.image` to display the saved plot.

---
