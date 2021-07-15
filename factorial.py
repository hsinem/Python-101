# Factorial Program

n = int(input("Number: "))

factorial = 1

if n < 0:
   print("Invalid input")

elif n == 0:
   print("The factorial: 1")

else:
   for i in range(1,n + 1):
       factorial = factorial*i
   print("The factorial :",factorial)
