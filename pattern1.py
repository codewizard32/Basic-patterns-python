''' For OUTPUT 

Enter number :3
1 2 3 
4 5 6 
7 8 9 '''

n = int(input("Enter number:\n"))
count = 1
i = 1
while i <= n:
    j = 1
    while j <= n:
        print(count, end=" ")
        count += 1
        j += 1
    print()
    i += 1
    
    
    
