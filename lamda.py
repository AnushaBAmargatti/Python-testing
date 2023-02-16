'''x=lambda x:x+3
print(x(10))
sum=lambda num1,num2:num1+num2
print(sum(10,23))'''
def anu():
    return lambda name1,name2:name1.concat(name2)
name=anu()
print(name(5,6))