n = int(input("Enter no. to print number pattern: "))
counter = 1
for i in range(n):
    for j in range(n):
        print(counter, end=" ")
        counter += 1
    print()

'''
OUTPUT

input:n=4
1 2 3 4 
5 6 7 8 
9 10 11 12 
13 14 15 16 
'''
