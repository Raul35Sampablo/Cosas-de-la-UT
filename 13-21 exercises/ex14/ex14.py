from sys import argv                    #Use the library sys and import argv for implement arguments

name_archive, username = argv          #Save the name of the archive and the name when your type in the console
x = '> '

print(f"Hi {username}, I'm the {name_archive} script." )   #Make questions
print(f"I need to make some questions {username}.")
print(f"How many dogs did you have?")
dogs = input(x)                                            #Save the answer

print(f"Where do you live {username}?")
live = input(x)

print(f"What is your favorite food {username}?")
food = input(x)

print(f"You are {username}, and you have had {dogs} dogs,")       #Finally we print all the answers in a sentence or expression
print(f"you live in {live}, and your favorite food is {food}.")
