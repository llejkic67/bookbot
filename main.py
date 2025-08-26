from stats import print_report
import sys

path_to_book = ""

def main():
    print("Usage: python3 main.py <path_to_book>")
    if len(sys.argv) != 2:
        sys.exit(1)
    path_to_book = sys.argv[1]
    print_report(path_to_book)


main()