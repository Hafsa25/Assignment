"""
************************** CLASS ACTIVITY************************************
**************************FUNCTIONS******************************************
**************************MADE BY HAFSA BHATTI*******************************
"""
def pizza(crust,*toppings):#MULTIPLE ARGUMENTS AS A TUPLE
    print("You have ordered pizza with",crust,"crust and the following things")
    for each in toppings:
        print(each)
pizza("thick","Extra Cheese","Extra Chicken","Extra Sauce")
"""
* : Tuple
**: Dictionary
"""
def pizza1(crust,**toppings):#MULTIPLE ARGUMENTS AS A DICTIONARY
    print("You have ordered pizza with",crust,"crust and the following things")
    for key,value in toppings.items():
        print(key,":",value)
pizza1("thick",topping1="Extra Cheese",topping2="Extra Chicken",topping3="Extra Sauce")