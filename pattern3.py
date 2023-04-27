n = int(input("Enter number of rows: \n"))
i = 1
ch = 'A'
while i <= n:
    space = n - i
    while space:
        print(" ", end="")
        space = space - 1
    j = 1
    while j <= i:
        print(ch, end="")
        ch = chr(ord(ch) + 1)
        j = j + 1
    print()
    i = i + 1
    
