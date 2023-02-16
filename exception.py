def calculate(num1,num2,num3):
    sum=num1+num2+num3
    diff=num1-num2
    product=num1*num2
    quotient=0
    try:
        quotient=num1//num2
    except ZeroDivisionError:
        print("denominator is  0")
    finally:
        print("done")
    return sum, diff, product, quotient
num1= int(input("enter the number1: "))
num2 = int(input("enter the number2: "))
num3 = int(input("enter the number3: "))
sum,diff,product,quotient=calculate(num1,num2,num3)
print(sum,diff,product,quotient)