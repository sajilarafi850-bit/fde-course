
# FDE course work

My code for the Forward Deployed Engineer Training Program.

## Week 1

- `week-01/orders.py`: summarises a day's orders, with revenue and pending orders.


### Café Expense Report

The `expenses.py` script reads café expenses from a JSON file and generates a monthly expense report.

**Features:**
- Counts the total number of expenses.
- Calculates total spending.
- Calculates expenses by category automatically.
- Identifies the largest expense.
- Lists expenses above the approval limit.
- Saves a summary in `week-01/summary.json`.
- Handles missing or invalid JSON files.

**How to run:**

```bash
python week-01/expenses.py
```

**Files:**
- `week-01/expenses.json` — Input expense data.
- `week-01/expenses.py` — Python expense report script.
- `week-01/summary.json` — Generated expense summary.