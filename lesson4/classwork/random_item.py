import random

animals = ["cat", "dog", "rabbit", "hamster", "parrot", "triple t"]

length = len(animals)

random_index =  random.randint(0, length-1)

random_animal = animals[random_index]
print("Random animal:", random_animal)

shortcut_animal = random.choice(animals)
print("Shortcut animal: ", shortcut_animal)