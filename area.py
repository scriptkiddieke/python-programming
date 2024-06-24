# Prompt the user to enter the radius
radius = int(input("Enter the radius: "))

# Calculate the area of the circle
area = (22 * radius * radius) / 7

# Display the area
print(f"The area of a circle with radius {radius} is: {area}")

myMixedDataTypes = [10, 20.3, 12.34j, "John Doe", True]

for item in myMixedDataTypes:
    print("{} is a datatype of {}".format(item,type(item)))
