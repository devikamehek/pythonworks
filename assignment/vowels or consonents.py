"""method 1"""

n=input("enter the alphabet: ")
if(n=='A' or n=='E' or n=='I' or n=='O' or n=='U' or n=='a' or n=='e' or n=='i' or n=='o' or n=='u'):
    print(f'{n} is a Vowel')
else:
    print(f'{n} is a Consonent')


"""method 2"""
print("method 2")
vowels=['a','e','i','o','u','A','E','I','O','U']
n=input("enter the alphabet")
if n in vowels:
    print(f'{n}is a vowel')
else:
    print(f'{n} is a consonant')
