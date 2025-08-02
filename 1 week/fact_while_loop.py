# Software Engineering
#defining the 
def factorilas():
    num = int(input("Please enter the postive number:"))

    # intializing for the postive and negative values
    if num < 0:
        print("Please enter a postive {num}:")
        return None

    elif num == 0 or num == 1:
        return 1

    else:
        result = 1
        i = 1
        while i <= num:
            result *= i
            i += 1
        return result

if __name__ == "__main__":
    print("factorilas are:", factorilas())
