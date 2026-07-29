#!/usr/bin/env python3

import os
import string
import random
import sys
import platform



# Specific for Linux users: use the correct clipboard
# depending on what runtime thing they're using
if platform.system() == "Linux":
    if os.getenv("XDG_SESSION_TYPE") == "wayland":
        pyperclip.set_clipboard('wl-clipboard')
    elif os.getenv("XDG_SESSION_TYPE") == "x11":
        pyperclip.set_clipboard('xclip')
    else:
        pass
    



# If the user uses an argument when running the program,
# check that it's a) an integer and b) more than 0 chars
try:
    temp = int(sys.argv[1])
    if temp <= 0:
        print("It needs to be longer than 0 characters, genius")
        sys.exit()
    else: 
        length = temp
# This occurs if the user doesn't provide any arguments,
# in which the program resumes with prompting the length
# from the user.
except IndexError:
    length = None

except ValueError:
    print("Argument needs to be a number")
    sys.exit()

    


# Set the password variable for later use
# and create the list of potential password characters
password = []

findingarg = True
chars = ""


# Arguments for the characters that the user wants

for arg in sys.argv:
    if "+" in arg:
        if "l" in arg:
            chars += string.ascii_letters
        if "d" in arg:
            chars += string.digits
        if "p" in arg:
            chars += string.punctuation
        break

if chars == "":
    chars = string.ascii_letters + string.digits + string.punctuation

# Decide the length of the password
if length == None:
    while True:
        try:
            while True:
                length = int(input("How long do you want your password to be? "))
                if length <= 0:
                    print("It needs to be longer than 0 characters, genius")
                    continue
                else:
                    break
        except ValueError:
            print("You need to enter a number!")
            continue
        else:
            break

# Make the random password
for x in range(0, length):
    char = random.choice(chars)
    password.append(char)

# LOL done
password = (f"{''.join(password)}")
print(password)
