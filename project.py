expenses = []


def calculate_total(expenses):
        total =0

        for ex in expenses:
            total += ex["amount"]
        
        return total

def save_expense(amount, category, description):
     with open("expenses.txt", "a") as file:
         file.write(f"{amount}, {category}, {description}\n")

def calculate_category_total(expenses, category):
        total =0

        for ex in expenses:
            if ex["category"].lower()== category.lower():
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
            print("*****No expense recorded*****")
        else:
            for index, ex in enumerate(expenses, start=1):
                print(index, ex["amount"], ex["category"], ex["description"])

def delete_expenses(expenses, delete_number):
        if 1 <= delete_number <=len(expenses):
            index = delete_number-1
            expenses.pop(index)
            print("*******Expense deleted successfully!******")
        else:
            print("Enter valid number to delete")
        
    




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
        while True:
            try:
                amount = float(input("Enter amount: "))

                if 0 < amount:
                  break
                else:
                  print("Amount must be greater than 0")
            except ValueError:
            
                print("**********Enter a valid number**********")
        
        while True:
             category = input("Enter category: ").strip()

             if category !="":
                  break
             else:
                  print("******Category cannot be empty*****")

      
        while True:
             description= input("Enter description:  ").strip()
             if description !="":
                  break
             else:
                  print("Description cannot be empty")
             

        expense = create_expense(amount, category, description)
        expenses.append(expense)
        save_expense(amount, category, description)
        print("Expense added successfully!")
        
    elif choice == "2":
        view_expenses(expenses)

    elif choice == "3":
        if len(expenses)==0:
             print("*****No expenses recorded*****")
        else:
        
            total = calculate_total(expenses)
            print("total expenses:", total)

    elif choice == "4":
         if len(expenses)==0:
                     print("*******No expense recorded*******")
         else:
            while True:
             
                category =(input("Enter category: ")).strip()
                if category !="":
                 break
                else:
                 print("category cannot be empty")
            total =calculate_category_total(expenses, category)
            if total >0: 
                print("Total spent on category: ", total)
            else:
                 print("No expense found for category:", category)



    elif choice == "5":
        if len(expenses)==0:
             print("*******No expenses to delete*******")
        else:
        
            while True:
             try:
                  delete_number=int(input("Enter expense number to delete:  "))
                  if 1 <= delete_number <= len(expenses):
                       break
                  else:
                       print("=======Enter a valid expense number=======")

             except ValueError:
                    print("*****Enter a valid number to delete*****")
                  
            delete_expenses(expenses, delete_number)
       
    elif choice== "6":
         print("Goodbye!")
         break
    else:
        
        print("*****Invalid choice*****")

   

   
