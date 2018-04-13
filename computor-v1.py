import sys
import re

term_matcher = r"(\d*(?:\.\d+)?(?: ?\* ?[a-zA-Z]|[a-zA-Z])(?: ?\^ ?\d*)?|\d+(?:\.\d+)?)"

def main():
    tab = sys.argv[1:]
    operation = tab[len(tab) - 1]
    print(operation)
    terms = re.findall(term_matcher, operation)
    print(terms)


if __name__ == "__main__":
    main()

