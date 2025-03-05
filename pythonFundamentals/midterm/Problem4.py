str = input("Enter a string: ")
suffix = input("Enter a suffix to check: ")

if str.endswith(suffix):
    print("The string ends with: ", suffix)
else:
    print("The string doesn't end with: ", suffix)