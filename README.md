# Personal Expense Tracker 💰

A simple command-line expense management application built with Python. It allows users to record expenses, view expense records, calculate total spending, and filter expenses by category.

## Features

- **Add Expense:** Record an expense with a name, category, and amount.
- **View All Expenses:** Display all recorded expenses.
- **Calculate Total:** Calculate the total amount spent.
- **View by Category:** Display expenses belonging to a specific category and calculate their total.
- **Input Validation:** Handle invalid amounts, negative values, and empty name or category fields.
- **JSON Data Storage:** Save expenses in a JSON file so they remain available after restarting the program.
- **Error Handling:** Handle invalid numeric input and missing JSON files.

## Technologies Used

- Python
- JSON
- Git and GitHub

## How to Run

1. Install Python on your computer.
2. Clone this repository or download the project files.
3. Open a terminal in the project folder.
4. Run the application:

   ```bash
   python expanse_tracker.py
   ```

   Replace `expanse_tracker.py` with your actual Python filename if it differs.

## Data Storage

The application stores expense records in `expanse_data.json`. The file is created when the first expense is saved if it does not already exist.

**Note:** Keep the JSON file in the project directory so the application can find it.

## What I Learned

- Working with Python dictionaries and lists.
- Writing reusable functions.
- Handling exceptions with `try` and `except`.
- Validating user input.
- Reading and writing JSON files.
- Using Git and GitHub to track project changes.

## Future Improvements

- Edit and delete existing expenses.
- Add monthly expense summaries.
- Improve the application interface.
- Add automated tests.

## Author

Created as part of my Python learning journey — Month 1 Final Project.
