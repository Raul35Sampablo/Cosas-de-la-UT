def add(a1, b1):
    print(f"ADDING {a1} + {b1}")
    return a1 + b1  #In this function we make and addition


def subtract(a1, b1):
    print(f"SUBTRACTING {a1} - {b1}")
    return a1 - b1  #In this make a substraction


def multiply(a1, b1):
    print(f"MULTIPLYING {a1} * {b1}")
    return a1 * b1  #In this make a multiplication


def divide(a1, b1):
    print(f"DIVIDING {a1} / {b1}")
    return a1 / b1   #In this maake a divition



print("Let's do some math with just functions!")   #Make the operations

ag = add(10, 9)
hg = subtract(167, 2)
wg = multiply(25.5, 2)
iq = divide(100, 3)

print(f"Age: {ag}, Height: {hg}, Weight: {wg}, IQ: {iq}")   #And finally print
