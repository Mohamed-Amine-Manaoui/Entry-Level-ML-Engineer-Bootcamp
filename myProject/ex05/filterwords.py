import sys
import string

def main():
    if len(sys.argv) != 3:
        print("ERROR !!")
        return
    try :
        text = sys.argv[1]
        num = int(sys.argv[2])
    except ValueError:
        print("ERROR !!")
        return
    my_list = ''.join([item for item in text if item not in string.punctuation])
    my_list = my_list.split()
    my_list1 = [item for item in my_list if len(item) > num]
    print(my_list1)
       
if __name__ == "__main__" :
    main()
