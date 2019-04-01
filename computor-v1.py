import math
import sys
import re

term_matcher = r"(\d*(?:\.\d+)?(?: ?\* ?[a-zA-Z]|[a-zA-Z])(?: ?\^ ?\d*)?|\d+(?:\.\d+)?)"

class Polynom:

    #
    # Builtins
    #

    def __init__(self, expression):
        """init

        Args:
            expression (string): expects a polynomial equation. The string will be parsed and the program will stop
            if any error occurs
        """
        self.input = expression
        print(self.input)

        self.reduced = self.parse_input(self.input)


    def __repr__(self):
        """Representation"""
        rep = "- Polynomial equation info -\n"
        rep += "input: " + self.input
        return rep

    #
    # Public
    #

    def parse_input(self, input):
        reduced = input
        return reduced


def display_usage():
    print("Usage:\n --> ./computor \"polynomial equation\"")

def display_error(message):
    print("Error: " + message, file=sys.stderr)


def main():

    if len(sys.argv) < 2:
        display_error("No argument provided")
        display_usage()
        exit(0)

    equation = Polynom(sys.argv[1])


if __name__ == "__main__":
    main()

