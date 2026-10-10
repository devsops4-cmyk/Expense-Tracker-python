import expense_functions


expenses =  expense_functions.load_expenses_json()

while True:
    expense_functions.display_menu()

    choice =expense_functions.get_menu_choice()
    if choice == "1":
        amount = expense_functions.get_valid_amount()
        
        category = expense_functions.get_valid_category()

      
        description = expense_functions.get_valid_description()
             

        expense = expense_functions.create_expense(amount, category, description)
        expenses.append(expense)
        expense_functions.save_expenses_json(expenses)
        print("Expense added successfully!")
        
    elif choice == "2":
        expense_functions.view_expenses(expenses)

    elif choice == "3":
        if len(expenses)==0:
             print("*****No expenses recorded*****")
        else:
        
            total = expense_functions.calculate_total(expenses)
            print("total expenses:", total)

    elif choice == "4":
         if len(expenses)==0:
                     print("*******No expense recorded*******")
         else:
                category = expense_functions.get_valid_category()
                total =expense_functions.calculate_category_total(expenses, category)

                if total >0: 
                     print("Total spent on category: ", total)
                else:
                    print("No expense found for category:", category)



    elif choice == "5":
        if len(expenses)==0:
             print("*******No expenses to delete*******")
        else:
            delete_number = expense_functions.get_valid_delete_number(expenses)
            expense_functions.delete_expenses(expenses, delete_number)
       
    elif choice== "6":
         print("======{Thank You For Using our Expense Tracker}=====")
         print("*******{Goodbye!}*******")
         break
    else:
        print("*****Invalid choice*****")

        print("======Would you like to continue?======")

    continue_choice =expense_functions. get_continue_choice()

    if continue_choice == "x":
        print("======{Thank You For Using our Expense Tracker}=====")
        print("*******{Goodbye!}*******")
        break