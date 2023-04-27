n = int(input("Enter no. to print number pattern: "))
counter = 1
for i in range(n):
    for j in range(n):
        print(counter, end=" ")
        counter += 1
    print()
