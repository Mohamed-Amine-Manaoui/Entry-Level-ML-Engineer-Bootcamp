import sys

def main ():
    if (len(sys.argv) != 2):
        print("AssertionError: more than one argument is provided") 
        return
    try:
        num = int(sys.argv[1])  # Convert input to integer
    except ValueError:
        print("AssertionError: argument is not an integer")
        return
    if num == 0:
        print("I'm Zero"), exit (0)
    quotient, remainder = divmod(num, 2)
    if remainder == 0:
        print("I'm Even")
    else:
        print("I'm Odd")
if __name__ == "__main__":
    main()