import json

def calculate_total(expenses):
        total =0

        for ex in expenses:
            total += ex["amount"]
        
        return total



def save_expense(amount, category, description):
     with open("expenses.txt", "a") as file:
         file.write(f"{amount}, {category}, {description}\n")

def calculate_category_total(expenses, category):
        total = 0

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

def load_expenses():
     expenses = []
     try:
          
        with open("expenses.txt", "r") as file:
          for line in file:
               parts = line.strip().split(",")

               amount =float(parts[0])
               category = parts[1].strip()
               description = parts[2].strip()

               expense = create_expense(amount, category, description)
               expenses.append(expense)
     except FileNotFoundError:
          print("*****No expenses saved found*****")
     return expenses

def update_expenses_file(expenses):
     with open("expenses.txt", "w") as file:
          for ex in expenses:
               amount=ex["amount"]
               category=ex["category"]
               description=ex["description"]
               file.write(f"{amount}, {category}, {description}\n")


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

            save_expenses_json(expenses)

            print("*******Expense deleted successfully!******")
        else:
            print("Enter valid number to delete")

def save_expenses_json(expenses):
        with open("expenses.json", "w") as file:
          json.dump(expenses, file)

def load_expenses_json():
        try: 
            with open("expenses.json", "r") as file:
                expenses = json.load(file)

        except FileNotFoundError:
             print("No JsonFile to read")
             expenses = []

        except json.JSONDecodeError:
             print("Json file is empty or invalid")
             expenses = []
        return expenses

          

        
    

expenses =  load_expenses_json()

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
        save_expenses_json(expenses)
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


    while True:
        print("Would you like to continue?")
        continue_choice = input("A = Menu, X = Exit: ").strip().lower()

        if continue_choice == "a":
             break
        elif continue_choice == "x":
            break
        else:
            print("Invalid choice! Enter A or X.")

    if continue_choice == "x":
        print("Goodbye!")
        break