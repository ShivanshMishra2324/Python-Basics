num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = num1 + num2
print(result) # will give errorwhen we get input from user using input by default we gwet it in string format

#We have to convert those stings into numbers.
#It can be done in two ways the first is:
#result = int(num1) + int(num2)
#print(result)
#The above won't work with float data types so...
result = float(num1) + float(num2)
print(result)

