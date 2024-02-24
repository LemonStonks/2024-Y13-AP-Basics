# Ask user for width and loop until they
# enter a number that is more than zero
def num_check(question):
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


# Main Route Goes Here
for item in range(0, 2):
    width = num_check("Width: ")
    print(width)

for item in range(0, 3):
    height = num_check("Height: ")
    print(height)