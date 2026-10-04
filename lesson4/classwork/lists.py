#list example: colors = ["red", "green", "blue", "yellow"]

#indexing always starts at 0

#print("Second color:", colors[1])
#print("Third color:", colors[2])
#print("Fourth color:", colors[3])

# Example of Error: index out of range
# print(colors[10])

#to replace in list: colors[0] = "maroon"

#to add to list: colors.append("orange")

#to insert in list: colors.insert(2, "purple")

#to remove in list: colors.remove("green")

#Example of Error: removing item not in list
# colors.remove("pink")

#to remove last in list and know what you removed: popped_color = colors.pop()

#to remove and know what you removed: popped_color_at_index = colors.pop(1)

#searches for a value in a list and tells you where it is: index_of_blue = colors.index("blue")

# Error: finding index of item not in list
# colors.index("pink")

#counts how many times a value appears in a list: blue_count = colors.count("blue")

#to sort: colors.sort()

#to reverse: colors.reverse()

colors = ["maroon", "green", "blue", "yellow"]

popped_color_at_index = colors.pop(1)
print("Popped color:", popped_color_at_index)
print("colors:", colors)

index_of_blue = colors.index("blue")
print("index of blue:", index_of_blue)

colors.append("blue")
blue_count = colors.count("blue")
print("Count of blue: ", blue_count)

colors.sort();
print("after sort: ", colors)

colors.reverse();
print("after reverse: ", colors)