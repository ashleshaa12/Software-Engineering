def Sum_odd_and_print_Evens():
    num = int(input("Please enter the postive num: "))

    if num < 0:
        print("Please enter the postive number")
        return None
    
    odd_sum = 0
    print_evens = []
    even_sum = 0
    total_sum = 0
    i = 1

    while i <= num:
        total_sum += i
        if i % 2 == 1:
            odd_sum += i
        else:
            print_evens.append(i)
            even_sum += i
        i += 1

    print("Even numbers between 1 and {num} are:", print_evens)
    print("sum of odd numbers:", odd_sum)
    print("sum of even numbers:", even_sum)
    print("sum of th total numbrs between 1 and given number is:", total_sum)

if __name__ == "__main__":
    Sum_odd_and_print_Evens()
        