num1 = int(input("Enter the lower bound: "))
num2 = int(input("Enter the upper bound: "))

for n in range(num1, num2 + 1):
    if n > 1:
        prime = True
        for i in range(2, int(n ** 0.5) + 1):
             if n % i == 0:
                 prime = False
                 break
        if prime:
            print(n,end=", ")