import this
"""2-4. Name Cases: Use a variable to represent a persons name, and then print
that person's name in lowercase, uppercase, and title case."""

name = "daWid mkay"
print (name.lower())
print (name.upper())
print (name.title())

"""2-5. Famous Quote: Find a quote from a famous person you admire. Print the
quote and the name of its author. Your output should look something like the
following, including the quotation marks:
Albert Einstein once said, “A person who never made a
mistake never tried anything new.”"""

quote = "“if you want to live a happy life, tie it to a goal, not to people or things.”"
name = "albert einstein"
print (f"{name.title()} once said, {quote.replace("if", "If")}")

"""2-7. Stripping Names: Use a variable to represent a persons name, and include
some whitespace characters at the beginning and end of the name. Make sure
you use each character combination, "\t" and "\n", at least once.
Print the name once, so the whitespace around the name is displayed.
Then print the name using each of the three stripping functions, lstrip(),
rstrip(), and strip()."""

persons_name = "\n     \tdawid\n   "
print (persons_name)
print (persons_name.lstrip())
print (persons_name.rstrip())
print (persons_name.strip())
x, y, z = 0, 0, 0
print (x, y, z)
print (x)
print (y)
print (z)

CONSTANT = "THIS IS CONSTANT CUZ IT USES CAPITAL LETTERS"


def nextGreatestLetter(self, letters, target):
        if min(letters) > target:
            return min(letters)
        else:
            return letters[1]
        
"""3-1. Names: Store the names of a few of your friends in a list called names. Print
each persons name by accessing each element in the list, one at a time."""

names = ["Farid", "Alex", "Yuri", "Rhaa"]
print(names)
x = 0
print (names[0])
print (names[1])
print (names[2])
print (names[3])