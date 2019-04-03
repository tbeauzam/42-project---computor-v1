import sys
import re

###
# OBJECT
###

class Polynom:

    #
    # Constants
    #

    zero_expr = re.compile(r"^(?:([-+]?\d+(?:\.\d+)?)|([-+]?\d*(?:\.\d+)?) ?\*? ?(?:x\^0|1))$")
    one_expr = re.compile(r"^([-+]?\d*(?:\.\d+)?) ?\*? ?(?:x\^1|x)$")
    two_expr = re.compile(r"^([-+]?\d*(?:\.\d+)?) ?\*? ?x\^2$")
    any_other_expr = re.compile(r"^([-+]?\d*(?:\.\d+)?) ?\*? ?x\^(\d+)$")

    valid_charset = "0123456789.*-+=x^"

    #
    # Builtins
    #

    def __init__(self, expression):
        self.to_parse = expression
        self.reduced = self.parse_input(self.to_parse)


    def __repr__(self):
        rep = "- Polynomial equation info -\n"
        rep += "input: " + self.to_parse
        return rep

    #
    # Public
    #

    def parse_input(self, to_parse):

        print("Received input:")
        print(to_parse)

        to_parse = to_parse.lower()
        print("\nTo lower case:")
        print(to_parse)

        to_parse = re.sub(r"\s", "", to_parse)
        print("\nRemoved spaces:")
        print(to_parse)

        if to_parse.count("=") != 1 or not self.check_characters(to_parse):
            display_error("the provided input is not a polynomial equation, or contains unexpected characters")
            display_usage()
            exit(0) 

        while re.search(r"(--|\+\+|-\+|\+-)", to_parse):
            to_parse = re.sub(r"(\+\+|--)", "+", to_parse)
            to_parse = re.sub(r"(\+-|-\+)", "-", to_parse)
        print("\nChecked signs:")
        print(to_parse)

        to_parse = re.sub(r"([+-])", r" \1", to_parse)
        to_parse = re.sub(r"\s{2,}", " ", to_parse)
        to_parse = re.sub(r"^ -", "-", to_parse)
        to_parse = re.sub(r"= -", "=-", to_parse)
        print("\nRemade spacing:")
        print(to_parse)

        lhs = to_parse.split("=")[0]
        rhs = to_parse.split("=")[1]
        print("\nLeft part: " + lhs)
        print("Right part: " + rhs)

        lhs = lhs.split(" ")
        rhs = rhs.split(" ")
        i = 0
        for member in lhs:
            if member[0] not in "-+":
                lhs[i] = "+" + member
            i += 1

        for member in rhs:
            if member[0] == "-":
                member = "+" + member[1:]
            elif member[0] == "+":
                member = "-" + member[1:]
            else:
                member = "-" + member
            lhs.append(member)
        print("\nTransfer right terms to the left:")
        print(lhs)

        reduced = self.parse_terms(lhs)
        return reduced


    def parse_terms(self, terms):
        reduced_degrees = dict()
        i = 0
        for term in terms:
            result = re.search(self.zero_expr, term)
            if result:
                tmp = float(result.group(1)) if result.group(1) else float(result.group(2))
                if 0 in reduced_degrees:
                    reduced_degrees += tmp
                else:
                    reduced_degrees = tmp
                print("Found:")
                print(tmp)
            
            print("Current value of reduced_degrees:")
            print(reduced_degrees)



    def check_characters(self, to_parse):
        for c in to_parse:
            if c not in self.valid_charset:
                return False
        return True



###
# OTHER FUNCTIONS
###

def display_usage():
    message = "\nUsage:\n --> python3 computor-v1.py \"polynomial equation\""
    message += "\n\nExmaple of polynomial equation : 1 * X^0 + 2 * X^1 = - 1 * X^0 + 4 * X^1"
    message += "\n\nNotes:\n"
    message += "- polynomial degree of reduced form must be 0, 1 or 2\n"
    message += "- no negative or non-integer exponents allowed (valid range: 0 to 99)\n"
    message += "- valid charset: |" + Polynom.valid_charset +"|\n- x can be written x or X, but every occurence will be lower-cased\n"
    print(message)

def display_error(message):
    print("\nError: " + message, file=sys.stderr)


###
# MAIN
###

def main():

    if len(sys.argv) < 2:
        display_error("No argument provided")
        display_usage()
        exit(0)

    equation = Polynom(sys.argv[1])

# Execute main if this script is directly executed
if __name__ == "__main__":
    main()

