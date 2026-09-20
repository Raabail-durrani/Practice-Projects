expenses = []

def add_expense():
    description = input("what did you buy: \n")
    price = float(input("what was the price of the product : $ "  ))
    print("01. food")
    print("02. traveling")
    print("03. adventure")
    print("04. expenditures")
    print("05. entertainment")
    print("06. health")
    category = input("select from above: \n")


    expense = { "description": description , "price": price, "category": category,}

    expenses.append(expense)



def view_expense():
    if len(expenses) == 0:
        print("No expense recorded yet")

    else:
        for index,expense in enumerate(expenses, start=1):
            print(f"{index}.item : {expense['description']} | price  $ {expense['price']} | category  {expense['category']}")

def total_spending():
    if len(expenses) == 0:
        print("No expense recorded yet")

    else:
        total = 0.0
        for expense in expenses:
            total = total + expense["price"]
        print(f"Total spent: {total:.2f}")








while True:
    print("\n ----- EXPENSE TRACKER ----- \n")
    print(" 1. Add expense")
    print(" 2. view expense")
    print(" 3. view total spending")
    print(" 4. exit")


    choice = input("choose from menu 1-4 : ").strip()


    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expense()
    elif choice == "3":
        total_spending()
    elif choice == "4":
        print("Goodbye!!!")
        break
    else:
        print("Invalid option")


