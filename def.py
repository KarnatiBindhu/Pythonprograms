def msg(a,b):
    print("sum=",a+b)
msg(10,20)
msg(20,30)
msg(40,50)
    
def msg():
    print("Hello python")
msg()
#calculate area of a rectangle
def Rarea(l,b):
    area=l*b
    return area
    #print("Area=",area)
length=300
breadth=200
A=Rarea(length,breadth)
print("area=",A)
print("area1=",Rarea(50,20))

#calculaate sum of 2 numbers
def add(a,b):
    return a+b
print("Results=",add(20,80))

#write a program for calculator functions read 2 values from console then perform all opertion

def add(a,b):
    return a+b;
def subtract(a,b):
    return a-b;
def multiplication(a,b):
    return a,b;
def division(a/b):
    return a/b;
num1=int(input("Enter a number"))
num2=int(input("Enter a number"))
Print("Sum=",add(num1,num2))
Print("Difference=",Subtract(num1,num2))
Print("Multiplication=",mul(num1,num2))
Print("Division=",div(num1,num2))
