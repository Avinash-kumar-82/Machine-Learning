num = int(input("Enter a number: "))

# convert int to string
if str(num) == str(num)[::-1]:
    print("Palindrome number")
else:
    print("Not a palindrome")