# import re
#
# phone_regex = '^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$'
# phone_number = "(123) 456-7890"
# match = re.search(phone_regex, phone_number)
#
# print(match)


# Python program to check if
# given mobile number is valid
import re


def isValid(s):
    # 1) Begins with 0 or 91
    # 2) Then contains 6,7 or 8 or 9.
    # 3) Then contains 9 digits
    Pattern = re.compile("(0|91)?[6-9][0-9]{9}")
    return Pattern.match(s)


# Driver Code
s = "347873923408"
if (isValid(s)):
    print("Valid Number")
else:
    print("Invalid Number")

isValid(s)

