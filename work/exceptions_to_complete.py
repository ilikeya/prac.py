"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

finished = False
result = 0
while not finished:
    try:
        number = int(input("Enter the number: "))
        print(number)
        finished=True
    except ValueError:
        print("Please end a valid integer")
    print("Valid result is: ", result)
