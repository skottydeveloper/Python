# Reference used: https://stackoverflow.com/questions/4940032/how-to-search-for-a-string-in-text-files
# Author is "amccormack".
import sys

def contains(filename, test_word) -> bool:
    with open(filename, 'r') as f:
        fileScanner = f.readlines()

    for line in fileScanner:
        if test_word in line:
            return True
    return False

if __name__ == "__main__":
    if contains(sys.argv[1], sys.argv[2]):
        print("The file contains the word.")
    else:
        print("The file does not contain the word.")