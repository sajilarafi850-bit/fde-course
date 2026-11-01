
import json

EXPENSES_FILE = "week-01/expenses.json"
APPROVAL_LIMIT = 25000


# Function 1: Load expenses from JSON file
def load_expenses(path):
    try:
        with open(path, "r") as file:
            expenses = json.load(file)
        return expenses

    except FileNotFoundError:
        print(f"Could not read {path}: file not found")
        return None

    except json.JSONDecodeError:
        print(f"Could not read {path}: invalid JSON")
        return None


# Function 2: Calculate totals for each category
def category_totals(expenses):
    totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category not in totals:
            totals[category] = 0

        totals[category] += amount

    return totals


# Function 3: Format amounts with commas
def format_rupees(amount):
    return f"Rs {amount:,}"


# Load expenses
expenses = load_expenses(EXPENSES_FILE)


if expenses is not None:

    # Calculate total expenses
    total = 0

    for expense in expenses:
        total += expense["amount"]

    # Print report heading and count
    print("Cafe expense report")
    print(f"Expenses recorded: {len(expenses)}")
    print(f"Total spent: {format_rupees(total)}")

    # Calculate category totals
    totals = category_totals(expenses)

    print("\nBy category:")

    for category, amount in totals.items():
        print(f"  {category}: {format_rupees(amount)}")

    # Find the largest expense
    largest = expenses[0]

    for expense in expenses:
        if expense["amount"] > largest["amount"]:
            largest = expense

    print(
        f"\nLargest expense: {largest['item']} "
        f"({format_rupees(largest['amount'])})"
    )

    # Find expenses needing approval
    approval_expenses = []

    for expense in expenses:
        if expense["amount"] > APPROVAL_LIMIT:
            approval_expenses.append(expense)

    print(
        f"\nNeeds approval (over {format_rupees(APPROVAL_LIMIT)}): "
        f"{len(approval_expenses)}"
    )

    for expense in approval_expenses:
        print(
            f"  - {expense['item']}: "
            f"{format_rupees(expense['amount'])}"
        )

    # Save summary to JSON
    summary = {
        "expense_count": len(expenses),
        "total": total,
        "by_category": totals
    }

    with open("week-01/summary.json", "w") as file:
        json.dump(summary, file, indent=4)

    print("\nSummary saved to week-01/summary.json")
