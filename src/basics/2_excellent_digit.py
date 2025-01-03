#Concatenating the n, k times and find the sum of the string
#find the excellent digit
#excellect digit is a sigle digit
#12 3
n = int(input("Enter n"))
k = int(input("Enter k"))

#121212
p = sum([int(i) for i in str(n)]) * k
while p>9:
    p = sum([int(i) for i in str(p)])
else:
    print(p)

