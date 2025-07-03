#import readline
import string
from math import log2
import hashlib

# need to start a seperate environment for the following: cryptography
# due to having a copy of this in the main system and uses it as part of the system


wall1="""
#################################
#       Password Entropy        #
#################################
"""

print(wall1)

#print(string.ascii_lowercase)
# adds 26
#print(string.ascii_uppercase)
# adds 26
#print(string.punctuation)
#adds 32
#print(string.digits)
#adds 10

print("Enter to start: ")
#the problem is to seperate -
#the input as none due to print
cap = input()
cap1 = type(cap)
cap2 = len(cap)
capint = int(cap2)

#print(cap)
#print(cap1)
print(cap2)

lettersU = 0
lettersL = 0
numbers = 0
symbols = 0
for chartype in cap:
    if chartype.isalpha() and chartype.isupper():
        lettersU += 1
    elif chartype.isalpha() and chartype.islower():
        lettersL += 1
    elif chartype.isnumeric():
        numbers += 1
    elif chartype.isalnum() != 1:
        symbols += 1
    else:
        print("error, does not work")

print("Upper Case:", lettersU)
print("Lower Case:", lettersL)
print("Numbers:", numbers)
print("Symbols:", symbols)

# https://medium.com/@jameskabbes/real-time-input-in-python-e6d6bfc38ddb


totCh = 0

if lettersU != 0:
    totCh += len(string.ascii_uppercase)
elif lettersL != 0:
    totCh += len(string.ascii_lowercase)
elif numbers != 0:
    totCh += len(string.digits)
elif symbols != 0:
    totCh += len(string.punctuation)

# E = L × log2(R)
# Entropy = Length x log2(all possible from pass)

Entropy = capint * log2(totCh)


if Entropy < 35:
    print("Password Entropy: {} - Very Weak".format(int(Entropy)))
elif Entropy >=36 and Entropy <59:
    print("Password Entropy: {} - Weak".format(int(Entropy)))
elif Entropy >=60 and Entropy <127:
    print("Password Entropy: {} - Acceptable".format(int(Entropy)))
elif Entropy >= 128 and Entropy <159:
    print("Password Entropy: {} - Strong".format(int(Entropy)))
elif Entropy >= 160:
    print("Password Entropy: {} - Very Strong".format(int(Entropy)))
else:
    print("ERROR in fake entropy")

wall2="""
#################################
#          Cryptic lair         #
#################################
"""

print(wall2)



md5 = hashlib.md5()
md5.update(cap.encode())

print(md5.hexdigest())

