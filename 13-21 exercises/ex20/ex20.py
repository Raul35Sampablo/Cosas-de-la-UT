from sys import argv        #Use the library sys and import argv for implement arguments
script, i_f = argv          #Save the name of the archive and the name when your type in the console


def p_all(f):     #We create a function to read the file
    print(f.read())   #and read

def r(f):        #In this we can reread the file
    f.seek(0,0)

def p_l(line_count, f):               #In this print a line of the archive
    print(line_count, f.readline())

c_f = open(i_f)

print("First let's print the whole file:\n")

p_all(c_f)                     #First print the .txt

print("Now let's rewind, kind of like a tape.")

r(c_f)                        #reread the .txt

print("Let's print three lines:")     #and finally print only 3 lines of the .txt

c_l = 1
p_l(c_l, c_f)

c_l = c_l + 1
p_l(c_l, c_f)

c_l = c_l + 1
p_l(c_l, c_f)
