import json
def calculate_total(expenses):
        total =0

        for ex in expenses:
            total += ex["amount"]
        
        return total


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

def get_valid_amount():
     while True:
          try:
              amount = float(input("Enter amount:  "))
              if amount >0:
                   return amount
              else:
                   print("Amount must be greater than 0")
          except ValueError:
                print("**********Enter a valid number**********")

def get_valid_category():
     while True:
               category = input("Enter category:  ").strip()
               if category != "":
                    return category
               else:
                    print("Category cannot be empty")

def get_valid_description():
     while True:
          description = input("Enter Description:  ").strip()
          if description !="":
               return description
          else:
               print("Description cannot be empty")

def get_valid_delete_number(expenses):
     while True:
          try:
              delete_number = int(input("Enter expense number to delete: "))

              if 1 <= delete_number <=len(expenses):
                    return delete_number
              else:
                   print("Enter a valid expense number")

          except ValueError:
               print("Enter a valid number")

def display_menu():
    print("\nExpense Tracker")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Show total")
    print("4. Show spending category: ")
    print("5. Delete expense: ")
    print("6. Exit")

def get_menu_choice():
     while True:
          
        choice = input("Choose an Option: ").strip()

        if choice in ["1", "2", "3", "4", "5", "6"]:
            return choice
        else:
             print("Invalid choice! please try again. ")

def  get_continue_choice():
     while True:
          choice = input("A = Menu,  X = Exit: ").strip().lower()
          if choice in ["a", "x"]:
            return choice
          else:
               print("Invalid choice! Enter A or X.")
          
               
