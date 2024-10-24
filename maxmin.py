def maxmin(array):
    min_counter = 10000
    max_counter = -10000
    for number in array:
        if number < min_counter:
            min_counter = number
        if number > max_counter:
            max_counter = number
    return [min_counter, max_counter]


def main():
    given_array = []
    while True:
        digit = input("Enter number for array or enter Q to quit: ")
        if digit == "Q":
            break
        else:
            try:
                number = int(digit)  # Convert input to integer
                given_array.append(number)  # Append the number to the list
            except ValueError:
                print("Please enter a valid number.")

    print("Min and Max:", maxmin(given_array))


# Test commit with new name
main()
