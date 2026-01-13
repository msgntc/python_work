income = input("Enter your income: ")
if not income.isdigit():
    print("dont use letters/symbols")
else:
    income = int(income)
    tax = income * 0.12
    print(tax)