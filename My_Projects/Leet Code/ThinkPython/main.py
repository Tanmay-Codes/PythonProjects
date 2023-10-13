print("Learning Basics of Python again")
a = (input('enter a string'))
print('''“A person who never made a
mistake never tried anything new.”''')
try:
    upper_case = a.upper()
    lower_case = a.lower()
    length = len(a)
    string_title = a.title()
    print(upper_case)
    print(lower_case)
    print(length)
    print(string_title)
    print(a.rstrip())
except ValueError:
    print("wrong input")
