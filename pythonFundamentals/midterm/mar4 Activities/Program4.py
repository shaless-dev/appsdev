num = int(input("Enter the number of terms: "))
num1, num2 = 0, 1

print("Fibonacci series: ")
for _ in range(num):
    print(num1, end=" ")
    num1, num2 = num2, num1 + num2