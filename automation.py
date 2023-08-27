# ✅ Convert miles to kilometers
# ✅ Calculate simple interest
# ✅ Find the largest number in a list
# // Check a number is a prime number or not
# // Sum of all digits in a number
# // Reverse a string (Check palindrome)
# // Calculate age
# // Build a simple calculator



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
def primeNumberCheck():
    number = int(input("Please enter a number to check if it's a prime number: "))
    if number <= 2: 
        print("Please input a number above 2")
    else: 
        is_prime = True  # Assume the number is prime initially
        for x in range(2, int(number**0.5) + 1):
            if number % x == 0:
                is_prime = False
                break
        
        if is_prime:
            print("Yes, it's a Prime Number")
        else:
            print("No, it's not a Prime Number")

primeNumberCheck()