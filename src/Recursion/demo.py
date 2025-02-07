def display(num):#5 4 3 2 1 0
    if num == 0: #base condition
        return
    print(num, end=" ") #task
    display(num-1) #recursion call-iterating
    print(num, end=" ")  # task

if __name__ == "__main__":
    num = int(input())
    temp = num

    while True:
        print(temp, end=" ")#5 4 3 2 1
        temp -= 1
        if temp == 0:
            break
    print()

    display(num)#5

