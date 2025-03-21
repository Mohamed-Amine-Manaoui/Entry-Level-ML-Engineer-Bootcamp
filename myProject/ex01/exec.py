import sys

def main ():
    if len(sys.argv) == 1:
          exit(0)
    av = sys.argv[1:][::-1]
    argr = [arg[::-1].upper() for arg in av]
    print(" ".join(argr))

if __name__ == "__main__":
        main ()