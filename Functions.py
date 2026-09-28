#  #Functions: block of codes which is executed when it is called
#  # def functionname(<parameters>):
#  #    code to be executed
#
#  ##indentation
#
# # def hello():
# #     print("Helloo Good Morningg")
# # hello()
#
# ## function can be assigned to a variable
# # a=hello
# # a()
#
# # mohan=print
# # mohan("Vyshnavi")
#
# ##ARGUMENTS: values to be passed to a functions
# # parameters values mapped in the fn.
#
# ##Parameters are of 2 types
# #1. Positional arguments
# #2.Ketword arguments
#
# # def add(a,b):
# #     print(a+b)
# # add(1,2)
#
# # def add(a=0,b=0):
# #     print(a+b)
# # add(7,8)
#
# def add(a,b):
#     return a+b
# print(add(3,5))
#
# ##PRINT A BASIC CALCULATOR
#
# # print("Hello Welcome to Basic calculator")
# # print("Choose the operation that you need")
# # print("Operators:")
# # print("1. Addition")
# # print("2. Subtraction")
# # print("3. Multiplication")
# # print("4. Division")
# # print("5. Exit")
# # operation=int(input("Enter the operation you want: "))
# #
# # if operation==1:
# #     def add(a=0,b=0):
# #         return a+b
# #     print(add(a,b))
# #
# # # def add(a,b)
# # #
# # # ##add
# # # def add(a,b):
# # #     return a+b
# # # print(add(int(input("enter no:")
#
#
def add(a,b):
    return (a+b)
def sub(a,b):
    return (a-b)
def mul(a,b):
    return (a*b)
def div(a,b):
    return (a/b)
#
def main():
    print("Welcome to Basic calculator")
    while True:
        x = int(input("Enter a number: "))
        y = int(input("Enter a number:"))
        ch = int(input("enter your choice\n1.add\n2.sub\n3.mul\n4.div\n5.exit\nChoose:"))
        if ch==1:
            print(f"the sum is {add(x,y)}")
        elif ch==2:
            print(f"difference is {sub(x,y)}")
        elif ch==3:
            print(f"product is {mul(x,y)}")
        elif ch==4:
            print(f"result is {div(x,y)}")
        elif ch==5:
            break
        else:
            print("invalid choice")
main()

# ##home work
# # Age calculator
# # BMI calculator
#
# # #FACTORIAL O
# def fact(a):

# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     return fact
# # n=int(input("enter the number"))
# # print(factorial(n))
# print(factorial(7))