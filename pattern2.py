'''FOR OUTPUT 

enter no.of rows : 
5
*
**
***
****
*****
'''

n = int(input("enter no.of rows : \n"))
i = 1
while i <= n:
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    print()
    i += 1
