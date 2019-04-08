import math

def ft_sqrt(nb):

    if nb <= 0:
        print("Dafuq?")
        exit(0)

    guess = nb / 2
    i = 0
    while i < 10:
        bigger = nb / guess if nb / guess >= guess else guess
        smaller = nb / guess if nb / guess < guess else guess
        satisfying_sqrt = 1 if bigger - smaller < 0.0000000001 else 0
        if satisfying_sqrt:
            return guess
        print("\nnb is: " + str(nb) + "\nguess is: " + str(guess))
        guess = (guess + (nb / guess)) / 2
        i += 1
    return guess


nb1 = 9
result1 = math.sqrt(nb1)
ft_result1 = ft_sqrt(nb1)
print("\nSquare root of " + str(nb1) + ": " + str(result1))
print("Square root of " + str(nb1) + ": " + str(ft_result1))

nb1 = 3
result1 = math.sqrt(nb1)
ft_result1 = ft_sqrt(nb1)
print("\nSquare root of " + str(nb1) + ": " + str(result1))
print("Square root of " + str(nb1) + ": " + str(ft_result1))

nb1 = 0.001
result1 = math.sqrt(nb1)
ft_result1 = ft_sqrt(nb1)
print("\nSquare root of " + str(nb1) + ": " + str(result1))
print("Square root of " + str(nb1) + ": " + str(ft_result1))

nb1 = 5
result1 = math.sqrt(nb1)
ft_result1 = ft_sqrt(nb1)
print("\nSquare root of " + str(nb1) + ": " + str(result1))
print("Square root of " + str(nb1) + ": " + str(ft_result1))

nb1 = 17.4
result1 = math.sqrt(nb1)
ft_result1 = ft_sqrt(nb1)
print("\nSquare root of " + str(nb1) + ": " + str(result1))
print("Square root of " + str(nb1) + ": " + str(ft_result1))