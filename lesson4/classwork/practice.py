import random

# Problem 1
# Create a list of 4 car brands.
# Print the first and last.
# Then add another brand using append() and print the updated list.
cars = ["toyota", "bmw", "mercedes", "honda"]
print("first car", cars[0])
print("last car", cars[-1])
cars.append("mazda")
print(cars)


# Problem 2
# Create a list of 5 numbers.
# Print the number at index 2.
# Then insert a new number at index 2 and print the updated list.
numbers = [2,12,35,8,16]
print("number at index 2:", numbers[2])
numbers.insert(2,15)
print("numbers:", numbers)


# Problem 3
# Create a list of 3 cities.
# Print the length of the list.
# Then use a for loop to print each city.
cities = ["Seattle", "Paris", "London"]
print("Cities length:", len(cities))
for c in cities:
    print("City:", c)

# Problem 4
# Create a list of 6 file extensions.
# Print a random one.
# Then pop one at index 3 and print the updated list.
extensions = ["zip", "exe", "doc", "xls", "ppt", "src"]
print("Random extension:", random.choice(extensions))
extensions.pop(3)
print("Extensions:", extensions)


# Problem 5
# Create a list of 8 names.
# Print the one at the middle index using len().
# Then use a for loop to print all the names.
names = ["Eric", "Peter", "Jack", "John", "Adam", "Lucie", "Jessica", "Laura"]
mi = len(names)//2
print("Name at the middle index:", names[mi])
for n in names:
    print("Name:", n)