import sys
import string

def text_analyzer(text) :
    count_upper = sum(1 for char in text if char.isupper())
    count_lower = sum(1 for char in text if char.islower())
    count_space = sum(1 for char in text if char.isspace())
    count_punct = sum(1 for char in text if char in string.punctuation)
    print("- ", count_upper, " upper letter(s)")
    print("- ", count_lower, " lower letter(s)")
    print("- ", count_space, " space letter(s)")
    print("- ", count_punct, " puctuation letter(s)")

def main ():
    text = sys.argv[1]
    if text.isdigit():
        print("AssertionError: argument is not a string !!")
        return
    text_analyzer(text)
    

if __name__ == "__main__":
    main()