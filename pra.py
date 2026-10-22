def calculate_total(expenses):
    total = 0

    for ex in expenses:
        total+=ex["amount"]

    return total    