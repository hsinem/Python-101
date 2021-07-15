# Fibonacci Program
i = int(input("Step:"))
n1, n2 = 0, 1
counter = 0

if i > 0:
    while counter < i:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        counter += 1
        
elif i == 1:
   print(n1)

else:
   print("invalid input")
