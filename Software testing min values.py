# find the minimum number of the input as a list without using sort or min
# all the other test cases like empty list
# Eamonn Pattersom
# 1/3/2024
#
###########
def find_minimum(values):
    # finds the minimum integer value in a list of nnumbers
    if not values:
        raise ValueError("List is empty. Cannot determine minimum of an empty list.")

    min_value = values[0]
    for value in values:
        if value < min_value:
            min_value = value
    return min_value


def inputs():
    # collects user inputs
    user_input = input("Enter a set of elements separated by space: ")
    elements = user_input.split()
    integers = []

    for element in elements:
        try:
            number = int(element)
            integers.append(number)
        except ValueError:
            print(f"Warning: '{element}' is not an integer and will be ignored")

    if not integers:
        print("no integers were given")
        return

    try:
        minimum = find_minimum(integers)
        print(f"The smallest of the entered elements is: {minimum}")
    except ValueError as e:
        print(e)


inputs()
