"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter sales: $"))
while sales >= 0:
    if 0 <= sales < 1000:
        bonus = sales * float(0.1)
        print(f"With ${sales}, bonus: ${bonus} your bonus is 10%")
    elif sales > 1000:
        bonus = sales * float(0.15)
        print(f"With ${sales}, bonus: ${bonus} your bonus is 15% ")
    else:
        print("invalid sales number")
    sales = float(input("Enter sales: $"))
print("fin")