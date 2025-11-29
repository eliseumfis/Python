# Create a variable num_list and set it equal to a list
num_list = [42, 46, 54, 65, 90]

# Set a variable called sliced to num_list[3]
sliced = num_list[3]

# Print both variables
print("num_list:", num_list)
print("sliced:", sliced)

# Define a variable called "total" and use dictionaries to set it equal to the sum of the first two elements in the list
total = {"sum": sum(num_list[:2])}

# Print the total
print("total:", total["sum"])
