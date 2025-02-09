def display(num):#5 4 3 2 1 0
    if num == 0: #base condition
        return
    print(num, end=" ") #task
    display(num-1) #recursion call-iterating
    print(num, end=" ")  # task

def add(num):#5
    if num==0:
        return 0 #initial value

    return num+add(num-1) #operation executed while coming back

def fact(num):
    if num==0 or num==1:
        return 1
    return num * fact(num-1)

if __name__ == "__main__":
    num = int(input())
    temp = num

    while True:
        print(temp, end=" ")#5 4 3 2 1
        temp -= 1
        if temp == 0:
            break
    print()

    temp = num
    sum = 0
    while True:
        sum = sum + temp#5 9 12 14 15
        temp = temp-1#4 3 2 1 0
        if temp==0:
            break
    print("while loop:", sum)
    display(num)#5
    print(add(num, 0))

