# ✅ Convert miles to kilometers
# ✅ Calculate simple interest
# ✅ Find the largest number in a list
# ✅ Check a number is a prime number or not
# ✅ Sum of all digits in a number
# ✅ Reverse a string (Check palindrome)
# ✅ Calculate age
# ✅ Build a simple calculator


# Covert Mile to Kilometer
# one_miles = 1.60934 # kilometers
# userMileInput = int(input("Enter your Mile :"))
# print("Your {} miles is {} kilometers".format(userMileInput, userMileInput*one_miles))


# // Calculate simple interest
# def simpleInterest() :
#     principal = float(input("Enter your principal : "))
#     times = float(input("Enter your times : "))
#     interestRate = float(input("Enter your interest Rate : "))
#     interest = (principal * times * interestRate)/100
#     print("Your interest is {}".format(interest))

# simpleInterest()


# // Find the largest number in a list
# def findLargetestNumber(*args):
#     numbersList = []
#     for x in args:
#         numbersList.append(x)

#     largetNumberFromList = max(numbersList)

#     print(numbersList, "Where most laret number is {}".format(largetNumberFromList))

# findLargetestNumber(2,4,6)


# // Check a number is a prime number or not
# def primeNumberCheck():
#     number = int(input("Please enter a number to check if it's a prime number: "))
#     if number <= 2:
#         print("Please input a number above 2")
#     else:
#         is_prime = True  # Assume the number is prime initially
#         for x in range(2, int(number**0.5) + 1):
#             if number % x == 0:
#                 is_prime = False
#                 break

#         if is_prime:
#             print("Yes, it's a Prime Number")
#         else:
#             print("No, it's not a Prime Number")

# primeNumberCheck()


# // Sum of all digits in a number
# def sumAllDigitsNumber(number):
#     string = [*str(number)]
#     total = 0
#     for i in range(0, len(string)):
#         total += int(string[i])
#     print(total)

# sumAllDigitsNumber(233) # 2 + 3 + 3 = 8




# // Reverse a string (Check palindrome)
# def revString():
#     string = input("Enter a string : ")
#     reverse = string[::-1]
#     print("You string is {} and your reverse string is {}".format(string, reverse))
#     if reverse.lower() == string.lower() :
#         print("String is palindrome")
#     else:
#         print("String is not palindrome")

# revString()




# // Calculate age
    # import datetime

    # def calculateAge() : 
    #     current_year = datetime.datetime.now().year
    #     bornYear = int(input("Enter your born year : "))
    #     yourAge = current_year - bornYear
    #     print("Your age is {}".format(yourAge))

    # calculateAge() 





# # // Build a simple calculator
# import re

# def calculate(expression):
#     try:
#         # Remove spaces from the expression
#         expression = expression.replace(" ", "")
        
#         # Use regular expressions to find and evaluate expressions within parentheses
#         while '(' in expression:
#             # Find the innermost parentheses expression
#             inner_expr = re.search(r'\(([^()]+)\)', expression).group(1)
            
#             # Calculate the value of the inner expression
#             inner_result = eval(inner_expr)
            
#             # Replace the inner expression with its result
#             expression = expression.replace(f'({inner_expr})', str(inner_result))
        
#         # Evaluate the remaining expression
#         result = eval(expression)
#         return result
#     except Exception as e:
#         return f"Error: {e}"

# # Get user input
# user_input = input("Enter an expression: ")

# # Calculate and display the result
# result = calculate(user_input)
# print("Result:", result)