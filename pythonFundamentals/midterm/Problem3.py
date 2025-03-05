str = input("Enter a string: ")
prefix = input("Enter a prefix to check: ")

if str.startswith(prefix):
    print("The string starts with: ", prefix)
else:
    print("The string doesn't start with: ", prefix)