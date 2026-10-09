import random

# Problem 1
# Create a list of 3 operating systems.
# Print the last one using len().
# Then reverse the list and print it.
osList = ["Windows", "Mac", "Linux"]
l = (len (osList)) 
print(osList[l - 1])
osList.reverse()
print("after reverse:", osList)
# Problem 2
# Create a list of 4 school subjects.
# Print the second subject.
# Then sort them alphabetically and print the result.
schoolSubj = ["English Language Arts", "Mathematics", "World History", "Science"]
l = (len (schoolSubj))
print(schoolSubj[1])
schoolSubj.sort()
print("After sort:", schoolSubj)

# Problem 3 
# Create a list of 5 error codes.
# Print how many there are.
# Then use a for loop to print each error code.
eCodes = ["404","403","308","507","106"]
print(len(eCodes))
for e in eCodes:
    print("Error codes:", e)


# Problem 4 
# Create a list of 2 programming languages.
# Print a random one.
# Then append another language and print the list.
pLanguages = ["Python","C++"]
random_pLanguage = random.choice(pLanguages)
print("Random programming language:", random_pLanguage)
pLanguages.append("java")
print(pLanguages)


# Problem 5
# Create a list of 6 passwords.
# Print the one in the middle using len().
# Then remove the first password in the list and print it.
passW = ["459060","123456","000000","0122345","333333","111111"]
print(len(passW))
l = (len(passW))
print(passW[l//2])

passW.pop(0)
print("Pass list:", passW)