num = int(input("Enter a number: "))
armstrong = 0

for number in str(num):
    armstrong += int(number) ** len(str(num))

if armstrong == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")