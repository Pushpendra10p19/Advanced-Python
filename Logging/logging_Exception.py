import logging

logging.basicConfig(level=logging.INFO)

try:
    age = int(input("Enter your age: "))
    print(f"Your age is {age}")
except ValueError:
    logging.exception("Invalid input! Please enter a number.")

# Explaination :
# this is user input code where user enter is age like 20:
# then Output wll show like "Your age is 20"
