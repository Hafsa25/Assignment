"""
************************** CLASS ACTIVITY************************************
**************************FUNCTIONS******************************************
**************************MADE BY HAFSA BHATTI*******************************
"""
def add(num1,num2):# FUNCTION TO ADD TWO NUMBERS
    my_sum=num1+num2
    print(my_sum)
def sub(num1,num2):#FUNCTION TO SUBTRACT TWO NUMBERS
    my_diff=num1-num2
    print(my_diff)
def mul(num1,num2):#FUNCTION TO MULTIPLY TWO NUMBERS
    my_mul=num1*num2
    print(my_mul)
def div(num1,num2):#FUNCTION TO DIVIDE TWO NUMBERS
    my_div=num1/num2
    print(my_div)
def calculator():#FUNCTION FOR CALCULATOR
    print("1: Press 1 to add")
    print("2: Press 2 to subtract")
    print("3: Press 3 to multiply")
    print("4: Press 4 to divide")
    choice=int(input())
    num1=int(input("Enter number 1: "))
    num2=int(input("Enter number 2: "))
    if choice==1:
        add(num1,num2)
    elif choice==2:
        sub(num1,num2)
    elif choice==3:
        mul(num1,num2)
    elif choice==4:
        div(num1,num2)
    else:
        print("Invlid Choice")    
def even(num):#FUNCTION TO CHECK IF A NUMBER IS EVEN 
    if num%2==0:
        ev="Number is even"
    else:
        ev="Number is not even"
    return ev    
def odd(num):#FUNCTION TO CHECK IF A NUMBER IS ODD
    if num%2!=0:
        od="Number is odd"
    else:
        od="Number is not odd"
    return od 
print("Press 1 to check even")
print("Press 2 to check odd")
choice=int(input())
num=int(input("Enter the number you want to check"))
if choice==1:
    print(even(num))#EVEN FUNCTION CALLING
elif choice==2:
    print(odd(num))#ODD FUNCTION CALLING
else:
    print("Invalid choice")
    
calculator()#CALCULATOR FUNCTION CALLING


