expenses = []

while True:
    print("\nExpense Tracker")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Show total")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        amount = float(input("Enter amount:  "))
        category = input("Enter category: ")
        description= input("Enter description:  ")

        expense = {
            "amount": amount,
            "category": category,
            "description": description
        }
        expenses.append(expense)
        print("Expense added successfully!")
        
    elif choice == "2":
        
        if len(expenses)==0:
             print("No expense recorded")
        else:
            for ex in expenses:
                print(ex["amount"], ex["category"], ex["description"])

    elif choice == "3":
        total =0

        for ex in expenses:
            total += ex["amount"]

        print(total)



    elif choice == "4":
        print("Goodbye!")
        break
    else:
        
        print("Invalid choice")
