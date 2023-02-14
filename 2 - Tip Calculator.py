print('Welcome to the tip calculator.')

while True:
    try:
        bill = float(input("What is the total bill?\n"))
        people = int(input("How many people to split the bill?\n"))
        if people <= 0:
            print("Number of people must be greater than zero. Please try again.")
            continue
        perc = float(input("What percentage tip would you like to give?\n"))
        tip = round((bill * (1 + (perc / 100))) / people, 2)
        print("Each person should pay: ${:.2f}".format(tip))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

print('Thank you for using the tip calculator. Goodbye!')
