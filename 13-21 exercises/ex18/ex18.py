def p_two(*args):                    #define a function
    a_1, a_2 = args                     #and two arguments
    print(f"arg1: {a_1}, arg2: {a_2}")  #and print then


def pta(a_1, a_2):                      #we take this two arguments in a new fuction
    print(f"arg1: {a_1}, arg2: {a_2}")  #and print then"

# this just takes one argument
def p_one(a_1):                         #In this, we only take the first
    print(f"arg1: {a_1}")

# this one takes no arguments
def p_n():
    print("I don't have anything.")


p_two("Hamburguer","Pizza")       #In this, we declarate the arguments between ()
pta("Hamburguer","Pizza")
p_one("1st")
p_n()
