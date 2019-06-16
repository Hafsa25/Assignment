import math
def area_of_circle():
    radius=int(input("Enter radius of a circle: "))
    area=math.pi*(radius**2)
    print("Area of the circle is : ",area)
def pos_neg():
    num=int(input("Enter a number : "))
    if num > 0:
        print(num,"is positive")
    elif num < 0:
        print(num, "is negative")
    else:
        print(num,"is zero")
def modulus():
    divisor=int(input("Enter the divisor: "))
    dividend=int(input("Enter the dividend: "))
    mod=dividend%divisor
    if mod==0:
      print(dividend,"is completely divisible by",divisor)
    else:
      print(dividend,"is not completely divisible by",divisor)
def expression(): 
     n=int(input("Enter an integer n:"))
     ans=n+n**2+n**3
     print("The value of (n+nn+nnn) is :",ans)
def volume():
    rad=int(input("Enter the radius of sphere : "))
    volume=(4/3)*math.pi*(rad**3)
    print("Volume of the sphere is : ",volume)
def diff():
    num=int(input("Enter a number : "))
    diff=num-17
    print("The difference between",num,"and 17 is :",abs(diff))
def str_copy():
    string=input("Enter a string : ")
    times=int(input("How many times you want to copy this string : "))
    string2=""
    string2=string*times
    print(string2)
def even_odd():
    num=int(input("Enter a number : "))
    if num%2==0:
        print(num,"is even")
    else:
        print(num,"is odd")
def vowel_or_consonant():
    vowels=('a','e','i','o','u')
    count=0
    alphabet=input("Enter a alphabet")
    for i in range(len(vowels)):
        if alphabet==vowels[i]:
           count=count+1
           break
    if count==1:
        print(alphabet, "is a vowel")
    else:
        print(alphabet, "is a consonant")
def area_of_triangle():
    base=int(input("Enter base of a triangle : "))
    height=int(input("Enter height of a triangle : "))
    area=(1/2)*base*height
    print("Area of the triangle is : ",area)
def equal_or_5():  
    return1= True
    return2=False 
    int1=int(input("Enter first integer : "))
    int2=int(input("Enter second integer : "))
    sum=int1+int2
    diff=abs(int1-int2)
    if int1==int2 or sum==5 or diff==5:
        print (return1)
    else: 
        print (return2)
def exp():
    x=int(input("Enter value of x: "))  
    y=int(input("Enter value of y: "))
    expression=(x+y)**2
    print("The result of (x+y)*(x+y) is : ",expression)
def future_value():
    amount=int(input("Enter the amount: "))
    int_rate=float(input("Enter the interest rate: "))
    yrs=int(input("Enter the compounding years : "))
    fut_value=amount*((1+int_rate))**yrs  
    print("Future value is : ",fut_value)
def distance():
    x1=int(input("Enter x1 : "))
    y1=int(input("Enter y1 : "))
    x2=int(input("Enter x2 : "))
    y2=int(input("Enter y2 : "))
    diff=math.sqrt(((x2-x1)**2)+((y2-y1)**2))
    print("The difference between (",x1,",",y1,") and (",x2,",",y2,") is: ",diff)
def feet_inches_to_cm():
    feet=int(input("Enter feet : "))  
    inches=int(input("Enter inches : "))
    cm=((feet*12)+inches)*2.54
    print(feet,"feet",inches,"inches = ",cm,"cm")
def hypotenuse():
    base=int(input("Enter the base of a right angled triangle: "))
    perp=int(input("Enter the perpendicular of a right angled triangle: "))
    hyp=math.sqrt((base**2)+(perp**2))
    print("Hypotenuse of the given right angled triangle is: ",hyp)
def feet_to_inches_yard_and_miles():    
    dist=int(input("Enter the distance in feet: "))
    inches=dist*12
    yards=dist*(1/3)
    miles=dist*(1/5280)
    print("Distance in inches is: ",inches)
    print("Distance in yards is: ",yards)
    print("Distance in miles is: ",miles)
def time_units():
    print("Enter your choice ?")
    print("1: Conversion from minutes to seconds") 
    print("2:Conversion from hours to seconds") 
    print("3: Conversion from days to seconds")
    print("4: Conversion from years to seconds")
    choice=int(input())
    time_sec=0
    if choice==1:
        min=float(input("Enter time in minutes : "))
        time_sec=min*60
        print(min,"minutes = ",time_sec,"seconds")
    if choice==2:
        hrs=float(input("Enter time in hours : "))
        time_sec=hrs*3600
        print(hrs,"hours = ",time_sec,"seconds")
    if choice==3:
        day=float(input("Enter time in day : "))
        time_sec=day*86400
        print(day,"day = ",time_sec,"seconds")
    if choice==4:
        yrs=float(input("Enter time in years : "))
        time_sec=hrs*31536000
        print(yrs,"years = ",time_sec,"seconds")
def BMI():
    mass=float(input("Enter your mass in kgs: "))
    height=float(input("Enter your height in meters: "))
    bmi=mass/(height**2)
    print("Your Body mass index is :",bmi)
def temp():
    print("Choose your conversion:")
    print("1: From celcius to farenheit: ")
    print("2: From farenheit to celcius: ")
    choice=int(input())
    if choice==1:
        celcius=float(input("Enter temperature in celcius: "))
        farenheit=(celcius*1.8)+1.8
        print(farenheit,"degree farenheit =",celcius,"degree celcius")
    if choice==2:
        farenheit=float(input("Enter temperature in farenheit: "))
        celcius=(farenheit-32)/1.8
        print(farenheit,"degree farenheit =",celcius,"degree celcius")
def summation():
    num=int(input("Enter a number to find the sum: "))
    summ=0
    for i in range(num+1):
        summ+=i
    print("The sum of first",num,"integers is : ",summ)
def sum_of_digits():
    digit=input("Enter a digit: ")
    summ=0
    for i in digit:
        summ+=int(i)
    print("The sum of digits in ",digit,"is : ",summ)
def bin_octal_hex():
    num=int(input("Enter an integer: "))
    print(num,"in binary is",bin(num))
    print(num,"in Octal is",oct(num))
    print(num,"in Hexadecimal is",hex(num))
def GCD():
    num1=int(input("Enter 1st number: "))
    num2=int(input("Enter 2nd number: "))
    temp1=num1
    temp2=num2
    while num1!=num2:
        if num1>num2:
            num1-=num2
        else:
            num2-=num1
    print("GCD of",temp1,"and",temp2,"is: ",num1)
def count_string():
    str1=input("Enter a string : ")
    char=input("Enter the character you want to count in the text : ")
    count=0
    for i in str1:
        if i==char:
            count=count+1
    print("The number of occurences of ",char,"are",count)
def LCM():
    num1=int(input("Enter 1st number: "))
    num2=int(input("Enter 2nd number: "))
    lcm=(num1*num2)/math.gcd(num1,num2)
    print("LCM of",num1,"and",num2,"is: ",lcm)
def reverse():
    name=input("Enter your first and last name with a space: ")
    print(name[::-1])
def count_vowel_consonant():
    text=input("Enter a text: ")
    count1=count2=0
    for i in text:
        if i in 'aeiou':
            count1+=1
        else:
            count2+=1
    print("Number of vowels are: ",count1,"while number of consonants are: ",count2)
def palindrome():
    num=input("Enter a number: ")
    if num==num[::-1]:
        print(num,"is palindrome")
    else:
        print(num,"is not palindrome")   
def no_of_notes():
    Notes = (500, 200, 100, 50, 20, 10)
    no_of_notes = 0
    Amount=int(input("Enter the amount: "))
    amt=Amount
    for i in range(len(Notes)):
        q = Notes[i]
        no_of_notes += int(Amount / q)
        Amount = int(Amount % q)
    if Amount > 0:
        no_of_notes = -1
    print("The no of notes in ",amt,"are: ",no_of_notes)
def fibonacci_series():
    first=0
    second=1
    print("Fibonacci series from 0 to 50 : ")
    while first <= 50:
            print(first,end=",")
            next=first+second
            first=second
            second=next
def tables(): 
    count=1
    num=int(input("Enter a number to print its table:"))
    while count<=10:
        print(num, "*",count,"=",num*count)
        count+=1
def digits_and_letters():
    digits=0
    letters=0
    string=input("Enter a string to count digits and letters: ")
    for i in string:
        if i.isdigit() and i!="\n":
            digits+=1
        elif i.isalpha() and i!="\n":
            letters+=1
    print("Digits = ",digits,"Letters = ",letters)
def star_pattern():
    for i in range(5):
        for j in range(i+1):
            print("*",end=" ")
        print("\n")
    for i in range(5,0,-1):
        for j in range(0,i-1):
            print("*",end=" ")
        print("\n")
def num_pattern():
    for i in range(1,6):
        for j in range(1,i+1):
            print(j,end=" ")
        print("\n")
    for i in range(6,1,-1):
        for j in range(1,i-1):
            print(j,end=" ")
        print("\n")
def same_num_pattern():
    for i in range(10):
        for j in range(i):
            print(i,end=" ")
        print("\n")
def bin_to_dec():
    dec=0
    num=input("Enter a binary number for conversion: ")
    num_len=len(num)
    for i in range(1,num_len+1):
        dec+=int(num[i-1])*(2**(num_len-i))
    print("Deciaml of ",num,"is: ",dec)
def octal_to_dec():
    dec=0
    octal=input("Enter an octal number: ")
    num_len=len(octal)
    for i in range(1,num_len+1):
        dec+=int(octal[i-1])*(8**(num_len-i))
    print("Decimal of",octal,"is: ",dec)
def no_of_days():
    from datetime import date
    year1=int(input("Enter first year: "))
    month1=int(input("Enter first month: "))
    date1=int(input("Enter first date: "))
    year2=int(input("Enter second year: "))
    month2=int(input("Enter second month: "))
    date2=int(input("Enter second date: "))
    first=date(year1,month1,date1)
    second=date(year2,month2,date2)
    day=second-first
    print("Number of days between",first,"and",second,"are",day.days)
def Is_string():
    string=input("Enter a string: ")
    if string[0:2]=="Is" or string[0:2]=="is":
        print(string)
    else:
        print("is"+string)
def secinto_day_hrs_min():
    sec=float(input("Enter time is seconds: "))
    minute=sec/60
    hour=sec/3600
    day=sec/86400
    print(sec,"in minutes is: ",minute)
    print(sec,"in hours is: ",hour)
    print(sec,"in days is: ",day)
def half_diamond_stars():
    for i in range(5):
        for j in range(i+1):
            print("*",end=" ")
        print("\n")
def half_diamond_num():
      for i in range(1,6):
        for j in range(1,i+1):
            print(j,end=" ")
        print("\n")
def diamond_stars():
    num = 9
    for i in range(1, num+1):
        i = i - (num//2 +1)
        if i < 0:
            i = -i
        print(" " * i + "*" * (num - i*2) + " "*i)
print("Enter your choice: ")
print("1: Area of circle ")
print("2: Positive or negative ")
print("3: Divisible or not? ")
print("4: (n+nn+nnn) ")
print("5: Volume of Sphere ")
print("6: Difference between number and 17 ")
print("7: Copies of a string ")
print("8: Even or odd ")
print("9: Vowel or consonant ")
print("10: Area of Triangle ")
print("11: Equal or 5")
print("12: (x+y)*(x+y) ")
print("13: Future value")
print("14: Distance between two points")
print("15: Feet inches to cm ")
print("16: Hypotnuese of a Right angled triangle ")
print("17: Feet to inches yards and miles ")
print("18: Every time unit in seconds ")
print("19: Body mass index ")
print("20: Conversion of temperature ")
print("21: Sum of first n natural numbers ")
print("22: Sum of digits in an integer ")
print("23: Greatest Common Divisor ")
print("24: Count a given char in a string ")
print("25: Least Common Multiple ")
print("26: String Reverse ")
print("27: Count vowel and consonant ")
print("28: Palindrome or not ")
print("29: No of notes in a given amount ")
print("30: Fibonacci Series ")
print("31: Table of a number ")
print("32: Count digits and letters")
print("33: Star Pattern")
print("34: Number Pattern in increasing order")
print("35: Similar Number Pattern ")
print("36: Binary to decimal conversion ")
print("37: Octal to decimal conversion ")
print("38: Number of days between two dates")
print("39: String starting with is ")
print("40: Second in minutes,hours and days")
print("41: Half diamond of stars ")
print("42: Half diamond of numbers ")
print("43: Diamond stars")

choice=int(input())
if choice==1:
    area_of_circle()
elif choice==2:
    pos_neg()
elif choice==3:
    modulus()
elif choice==4:
    expression()
elif choice==5:
    volume()
elif choice==6:
    diff()
elif choice==7:
    str_copy()
elif choice==8:
    even_odd()
elif choice==9:
    vowel_or_consonant()
elif choice==10:
    area_of_triangle()
elif choice==11:
    equal_or_5()
elif choice==12:
    exp()
elif choice==13:
    future_value()
elif choice==14:
    distance()
elif choice==15:
    feet_inches_to_cm()
elif choice==16:
    hypotenuse()
elif choice==17:
    feet_to_inches_yard_and_miles()
elif choice==18:
    time_units()
elif choice==19:
    BMI()
elif choice==20:
    temp()
elif choice==21:
    summation()
elif choice==22:
    sum_of_digits()
elif choice==23:
    GCD()
elif choice==24:
    count_string()
elif choice==25:
    LCM()
elif choice==26:
    reverse()
elif choice==27:
    count_vowel_consonant()
elif choice==28:
    palindrome()
elif choice==29:
    no_of_notes()
elif choice==30:
   fibonacci_series()
elif choice==31:
   tables()
elif choice==32:
    digits_and_letters()
elif choice==33:
    star_pattern()
elif choice==34:
    num_pattern()
elif choice==35:
    same_num_pattern()
elif choice==36:
    bin_to_dec()
elif choice==37:
    octal_to_dec()
elif choice==38:
    no_of_days()
elif choice==39:
    Is_string()
elif choice==40:
    secinto_day_hrs_min()
elif choice==41:
    half_diamond_stars()
elif choice==42:
    half_diamond_num()
elif choice==43:
    diamond_stars()




        

