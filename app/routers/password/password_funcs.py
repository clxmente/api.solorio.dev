import random
import string

from app.routers.exceptions import ExcludedAllSets
from typing import Optional

def gen_password(length: int, exclude: Optional[str] = None) -> str:
    specialChar = "!@#$%^&*()-_"
    bool_special = False
    bool_lower = False
    bool_upper = False
    bool_digits = False

    charsets = [
        string.ascii_lowercase, 
        string.ascii_uppercase, 
        string.digits, 
        specialChar
    ]
    # exclude certain character sets if user wants
    if (exclude):
        if ("special" in exclude):
            charsets.remove(specialChar)
            bool_special = True
        if ("digits" in exclude): 
            charsets.remove(string.digits)
            bool_digits = True
        if ("upper" in exclude): 
            charsets.remove(string.ascii_uppercase)
            bool_upper = True
        if ("lower" in exclude): 
            charsets.remove(string.ascii_lowercase)
            bool_lower = True

        # if all charasets excluded raise error
        if (len(charsets) == 0): raise ExcludedAllSets

    password = []
    for i in range(0, length):
        currsection = random.choice(charsets)
        if (currsection == string.ascii_lowercase): bool_lower=True
        elif (currsection == string.ascii_uppercase): bool_upper=True
        elif (currsection == string.digits): bool_digits=True
        elif (currsection == specialChar): bool_special=True

        currchar = random.choice(currsection)
        password.append(currchar)

    if (bool_lower and bool_upper and bool_digits and bool_special):
        # only return the output when all requirements are met
        output = "".join(password)
        return output
    else: return gen_password(length) # try again if all requirements not met
