        `sales = float(input("Enter sales : $"))
        while sales >= 0:
            if sales < 1000:
                bonus = sales * 0.01
            else:
                bonus = sales * 0.15
            print("bonus is {} ".format(bonus))
            sales = float(input("Enter sales:$"))`