def arithematic_operation(meal_cost, meal_tip, meal_tax):
    # meal = 100
    # tip = 15
    # tax = 8

    meal_cost = float(input('Enter float value: '))
    meal_tip = int(input('Enter an integer value: '))
    meal_tax = int(input('Enter an integer value: ')) 

    tip = meal_cost/100 * meal_tip
    tax = meal_tax/100 * meal_tip
    print(tax)
    print(tax)
    total_cost = meal_cost + tip + tax 
    print(total_cost)


arithematic_operation(100, 15, 8)
