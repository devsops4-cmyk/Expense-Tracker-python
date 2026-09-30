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

        expense = create_expense(amount, category, description)
        expenses.append(expense)
        print("Expense added successfully!")
        
    elif choice == "2":
        view_expenses(expenses)

    elif choice == "3":
        total = calculate_total(expenses)
        print(total)

    elif choice == "4":
        category =(input("Enter category: "))
        total =calculate_category_total(expenses, category)
        print("Total spent on category: ", total)



    elif choice == "5":
        delete_number=int(input("Enter expense number to delete:  "))

        if 1 <= delete_number <=len(expenses):
            index = delete_number-1
            expenses.pop(index)
            print("Expense deleted successfullly!")
        else:
            print("Enter valid number to delete")
       
    elif choice== "6":
         print("Goodbye!")
         break
    else:
        
        print("Invalid choice")


    def calculate_total(expenses):
        for ex in expenses:
            total += ex["amount"]
        
        return total

    def calculate_category_total(expenses, category):
        total =0

        for ex in expenses:
            if ex["category"]== category:
                total +=ex["amount"]
        return total

    def create_expense(amount, category, description):
        expense = {
            "amount": amount,
            "category": category,
            "description": description
        }

        return expense

    def view_expenses(expenses):
        if len(expenses)==0:
            print("No expense recorded")
        else:
            for index, ex in enumerate(expenses, start=1):
                print(index, ex["amount"], ex["category"], ex["description"])

    