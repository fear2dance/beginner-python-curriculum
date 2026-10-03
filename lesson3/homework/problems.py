# Problem 1
# Ask user for two test scores.
# If BOTH scores are at least 50, print "You passed both!"
# Otherwise, print "You failed at least one."
score = int(input( "What is your score on your test?"))
score2 = int(input( "What is your score on your second test?"))
if (score >= 50 and score2 >= 50):
    print("You passed both!")     
else:
    print("You failed at least one")
                  


# Problem 2
# Ask user if they brought lunch and water (yes/no).
# If they brought lunch OR water, print "You're somewhat ready."
# If they brought both, print "You're fully ready!"
# If they brought neither, print "You're not ready."
lunch = str(input(" Did you bring your lunch? (yes/no)"))
water = str(input( "Did you bring your water? (yes/no)" ))
if (lunch == "yes"  and water == "yes"): 
   print(" You're fully ready")
elif (lunch == "no" and water =="no"):
   print(" You're not ready ")
else:
    print( " You're somewhat ready ")



# Problem 3
# Ask user to enter a number.
# If the number is NOT between 1 and 10 (inclusive), print "Out of range."
# Otherwise, print "In range."
number = int(input( "Please enter a number"))
if (number >= 1 and number <= 10 ):
    print("In range.")
else:
    print("Out of range.")



# Problem 4
# Ask the user for a test score (0-100).
# Print the grade based on score:
#   90 and above: "A"
#   80 to 89: "B"
#   70 to 79: "C"
#   60 to 69: "D"
#   below 60: "F"
score = int(input("What is your test score?"))
if (score >= 90):
    print("A")
elif (score >= 80 and score <= 89):
    print("B")
elif (score >= 70 and score <= 79):
    print("C")
else:
    print("F")



# Problem 5
# Ask the user for two numbers.
# If one is divisible by 5 AND the other is NOT divisible by 2, print "Interesting pair!"
# Otherwise, print "Plain pair."
number = int(input("Please enter a number:"))
number2 = int(input(" Please enter your second number:"))
if (number % 5 ==0 and number2 % 2 != 0):
    print("Interesting pair!")
else:
    print("Plain pair")