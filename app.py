from text_utils import greet, fullname

message = greet("Baby")
print(message)

nextfun = fullname("Aswathi","P A")
print(nextfun)

try:
    number = int(input("Enter a number"))
    print(number)
except ValueError :
    print("enter valid number")    