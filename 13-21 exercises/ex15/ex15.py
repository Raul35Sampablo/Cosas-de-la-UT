from sys import argv                    #Use the library sys and import argv for implement arguments

name_archive, username = argv          #Save the name of the archive and the name when your type in the console

text = open('ex15.txt')               #Open the archive

print(f"Your text is {text}")         #Print the name
print(text.read())                    #And finally print the text

x = "> "

print(f"Type the name of the text again:")     #And print the text again
a = input("> ")

t_a =  open(a)

print(t_a.read())
