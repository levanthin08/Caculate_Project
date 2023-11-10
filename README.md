
# Expense Tracker Application Project

## Description:
Expense Tracker is a Python program that helps you track and manage your expenses. It provides a user-friendly interface for recording your expenses, categorizing them, and analyzing your spending patterns. The program saves your expenses to a CSV file and generates useful summaries to help you stay on top of your budget.



## Table of Contents
- [Overview](#overview)
- [Key Features](#key-features)
- [Usage / Examples](#usage--examples)
- [Developer Instructions](#developer-instructions)
- [Contributor Expectations](#contributor-expectations)
- [Known Issues](#known-issues)
- [Installation and Usage](#installation-and-usage)
- [Dependencies](#dependencies)
- [License](#license)
- [Conclusion](#conclusion)

## Overview

The Expense Tracker is written in Python and consists of three main files: project.py, expense.py, and test_project.py.

The project.py file contains the main logic of the application. It prompts the user to enter their expense details, such as name, amount, and category. The user can choose from predefined expense categories, including food, home, work, fun, and miscellaneous. The entered expenses are then saved to a CSV file. The application also reads the expense file and provides a summary of expenses by category, total spent, remaining budget, and daily budget.

The expense.py file defines the Expense class, which represents an individual expense. It has attributes such as name, category, and amount. The class also provides a __repr__ method for a formatted representation of the expense.

The test_project.py file contains pytest unit tests for the get_user_expense and save_expense_to_file functions. It uses the pytest library to define test cases and fixtures.

## Features

- User-friendly interface for entering expense details.
- Categorization of expenses into predefined categories (food, home, work, fun, misc).
- Saving expenses to a file for future reference.
- Summarizing expenses by category and calculating total spent.
- Displaying the remaining budget and budget per day based on the current date.


## Installation

To install and use the Expense Tracker:

- Clone the project repository: git clone [repository URL].
- Navigate to the project directory: cd expense tracker.
- Make sure you have Python 3.x installed on your system.
- Install the required dependencies using pip: pip install -r requirements.txt.
## Usage/Examples

To use the Expense Tracker:

- Run the project.py file: python project.py.
Follow the prompts to enter the expense details, including name, amount, and category.
- The entered expenses will be saved to the expenses.csv file.
- The application will provide a summary of expenses by category, total spent, remaining budget, and daily budget.
Here's an example interaction with the Expense Tracker:
```🎯 Running Expense Tracker!
🎯 Getting User Expense
Enter expense name: Grocery
Enter expense amount: 50
Select a category:
  1. 🍔 Food
  2. 🏠 Home
  3. 💼 Work
  4. 🎉 Fun
  5. ✨ Misc
Enter a category number [1 - 5]: 1
🎯 Saving User Expense: <Expense: Grocery, 🍔 Food, $50.00> to expenses.csv
🎯 Summarizing User Expense
Expenses By Category 📈:
  🍔 Food: $50.00
💵 Total Spent: $50.00
✅ Budget Remaining: $1950.00
👉 Budget Per Day: $65.00

```


## Dependencies:

The Expense Tracker application has the following dependencies:

- Python 3.x
- pytest (for running unit tests)

## Developer Instructions

If you want to modify or enhance the Expense Tracker, follow these instructions:

- Clone the project repository: git clone [repository URL].
- Navigate to the project directory: cd expense-tracker.
- Make sure you have Python 3.x installed on your system.
- Install the required dependencies using pip: pip install -r - requirements.txt.
- Modify the project.py or expense.py files to add your desired changes.
- Run the project.py file to test your modifications: python project.py.
- Run the project.py file to test your modifications: python project.py.
## Contributor Expectations

If you wish to contribute to the Expense Tracker project, please adhere to the following guidelines:

- Fork the repository and create a new branch for your contribution.
- Make your changes and ensure that the project still runs without any errors.
- Write unit tests to cover your changes.
- Update the documentation if necessary.
- Submit a pull request clearly explaining the changes you have made and their purpose.
## Known Issues

Currently, there are no known issues with the Expense Tracker application. However, if you encounter any problems or have suggestions for improvements, please create an issue on the project's GitHub repository.
## License

[MIT](https://choosealicense.com/licenses/mit/)


## Conclusion

The Expense Tracker is a useful tool for individuals who want to keep track of their expenses and manage their budgets effectively. By providing a simple and intuitive interface, it allows users to easily input and categorize their expenses. The summary feature helps users understand their spending patterns and make informed financial decisions. With its open-source nature, the Expense Tracker welcomes contributions from developers to enhance its functionality and usability.