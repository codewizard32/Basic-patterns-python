'''FOR OUTPUT 

Enter number of rows:
4
   A
  BCD
 EFGHI
JKLMNO
'''


n = int(input())
# 'n' must be odd
for i in range(n):
    for j in range(n):
        # left diagonal, right diagonal, top horizontal, bottom horizontal, left vertical, right vertical
        if i == j or i + j == n - 1 or i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
