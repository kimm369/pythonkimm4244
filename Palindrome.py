def is_palindrome(s):
    return s == s[::-1]

s = "Mamam"
ans = is_palindrome(s)

if ans:
    print("Yes, the string is palindrome")
else:
    print("No, the string is not palindrome")

