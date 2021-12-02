print("Giraffe Academy")
print("Giraffe\nAcademy")
#to put a " mark in string we cant just do print(""") to do this we use backward slash
print("\"") #after backward slash evereything is rendered literally
phrase= "Giraffe Academy"
#index   0123456789...
print(phrase + " is fine") #concatnation i.e. appending string inside of another string
#we can also use some common functions to modify these strings
print(phrase.lower()) #will convert entire string into lower case
print(phrase.upper()) #will convert entire string into upper case
#to check whether a give nstrings is entirely  upper case or lower case we use following function:
print(phrase.isupper())
print(phrase.upper().isupper())
#to know the length of a string
print(len(phrase))
#to get individual characters of a string we do:
print(phrase[0])
print(phrase.index("iraffe"))
print(phrase.index("i"))
print(phrase.replace("Giraffe", "Elephant"))
