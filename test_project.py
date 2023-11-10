import pytest
from expense import Expense
from project import get_user_expense, save_expense_to_file

# Define a fixture that creates an Expense object with specific values
@pytest.fixture
def expense():
    return Expense("Test Expense", "Test Category", 100)

# Test function to simulate user input and check if the returned Expense object has the correct attributes
def test_get_user_expense(monkeypatch):
    inputs = ["Test Expense", "100", "1"]
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

    # Call the get_user_expense function, which interacts with the user through input()
    expense = get_user_expense()

    # Check if the returned Expense object has the expected attributes
    assert expense.name == "Test Expense"
    assert expense.amount == 100
    assert expense.category == "🍔 Food"

# Test function to save an Expense object to a file and verify the file content
def test_save_expense_to_file(tmp_path, expense):
    expense_file_path = tmp_path / "test_expenses.csv"

    # Call the save_expense_to_file function to save the expense to the specified file path
    save_expense_to_file(expense, expense_file_path)

    # Read the content of the saved file and check if it matches the expected content
    with open(expense_file_path, "r") as f:
        content = f.readlines()
        assert len(content) == 1
        expected_content = "Test Expense,100,Test Category\n"
        assert content[0] == expected_content
