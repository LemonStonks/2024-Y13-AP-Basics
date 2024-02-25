# Ask user for width and loop until they
# enter a number that is more than zero
def float_input(question):
    error = "Please enter a number that is more than zero\n"
    while True:

        try:
            # ask the user for a number
            response = float(input(question))

            # check that number is more than zero
            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main Route starts here...

keep_going = ""
while keep_going == "":
    # Get width, length, and cost
    width = float_input("Width: ")
    length = float_input("Length: ")
    cost = float_input("Cost per meter: ")

    # Calculate perimeter and price for the fence
    perimeter = 2 * (width + length)
    total_cost = perimeter * cost

    # Display Output
    print()
    print(f"Perimeter: {perimeter} meters")
    print(f"Total Cost: ${total_cost:.2f}")

    # Ask user if they want to keep going
    keep_going = input("Press enter to keep going or any key to quit.")
    print()

print("Thank you for using the area / perimeter calculator")
