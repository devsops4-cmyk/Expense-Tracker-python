expenses = []

while True:
    print("\nExpense Tracker")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Show total")
    print("4. Show spending category: ")
    print("5. Delete expense: ")
    print("6. Exit")

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
            for index, ex in enumerate(expenses, start=1):
                print(index, ex["amount"], ex["category"], ex["description"])

    elif choice == "3":
        total =0

        for ex in expenses:
            total += ex["amount"]

        print(total)

    elif choice == "4":
        category =int(input("Enter category: "))
        total = 0
        for ex in expenses:
             if ex["category"]== category:
                total+=ex["amount"]

        print("Total spent on category: ", total)


# user user to enter value
    elif choice == "5":
        delete_number=int(input("Enter expense number to delete:  "))
        index = delete_number-1
        expenses.pop(index)
       
    elif choice== "6":
         print("Goodbye!")
         break
    else:
        
        print("Invalid choice")
