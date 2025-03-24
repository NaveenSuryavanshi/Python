# print("name is")
# name = "tony stark"
# print(name)
# print("age is")
# age = 50
# print(age)

# name = input("what is your name?")
# print("hello", name)
# print("what is your superhero name?")
# superhero_name = input()
# print(superhero_name)

# # add two numbers
# num1 = input("enter first number: ")
# num2 = input("enter second number: ")
# sum = int(num1) + int(num2)
# print("sum is", sum)

# sub two numbers
# num1 = input("enter first number: ")
# num2 = input("enter second number: ")
# sub = int(num1) - int(num2)
# print("sub is", sub)
 
 
# facts about strings
# print(name.upper())
# print(name.lower())
# print(name.find("any wprd or letter")) # it will give the index of the word or letter
# print(name.replace("tony", "robert")) # it will replace the word
# print(name.title()) # it will make the first letter capital

# facts about arathematic operators
# + is used for addition
# - is used for subtraction 
# * is used for multiplication
# / is used for division
# % is used for modulus or remainder
# // is used for floor division or value after decimal point is removed
# ** is used for exponentiation or power

# # facts about comparison operators
# Order	    Rule Component      	            Operators
# 1st	    Parentheses	                            ()
# 2nd	     Exponents	                            **
# 3rd	    Multiplication and Division	            *, /
# 4th   	Addition and Subtraction	            +, -
# 5th	    Comparison	                            ==, !=, <, <=, >, >=

# logical operators
# 1 or operator - if any one of the condition is true then it will return true
# 2 and operator - if all the conditions are true then it will return true
# 3 not operator - it will return the opposite of the condition or we can say it will return the opposite of the result



# # project making a calculator

# num1 = input("enter first number: ")
# operator = input("enter operator (+,-,/,%): ")
# num2 = input("enter second number: ")

# if operator == "+":
#     sum = int(num1) + int(num2)
#     print("sum is", sum)
# elif operator == "-":
#     sub = int(num1) - int(num2)
#     print("sub is", sub)
# elif operator == "*":
#     mul = int(num1) * int(num2)
#     print("mul is", mul)
# elif operator == "/":
#     div = int(num1) / int(num2)
#     print("div is", div)
# elif operator == "%":
#     mod = int(num1) % int(num2)
#     print("mod is", mod)
# else:
#     print("invalid operator")
    
    
    
    # loops
    
    # 1. while loop
    
# printing numbers from 1 to 100

# i = 1
# while i <= 100:
#     print(i)
#     i = i + 1

# 2. for loop

# for i in range(0 , 20):
#     print(i)


#only even numbers and if we want odd numbers then we can write range(1, 20, 2) or if we want the numbers in the multiples of 3 then we can write range(0, 20, 3)
# for i in range(1 , 20, 2):
#     print(i)


# i + 1 will start the numbers from 1 to 20
# for i in range(0 , 20,):
#     print(i + 1)

# marks = [10, 20, 30, 40, 50]
# for mark in marks:
#     if mark == 30:
#         break
#     print(mark)


# marks = [10, 20, 30, 40, 50]
# for mark in marks:
#     if mark == 30:
#         continue
#     print(mark)

# [] is used for list
# () is used for tuple
# {} is used for sets and dictionary 

# def print_sum(num1, num2):
#     sum = num1 + num2
#     return sum

# print(print_sum(10, 20))


# num1 = input("enter first number: ")
# num2 = input("enter second number: ")
# def sum(num1, num2):
#     sum = int(num1) + int(num2)
#     print("sum is")
#     return sum
# print(sum(num1, num2))
