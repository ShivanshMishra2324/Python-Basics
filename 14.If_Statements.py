#we can use boolean value like is_tall = True or not(is_tall)
a = input("Enter an integer: ")
if((int(a)%2)== 0 and (int(a)%4)== 0):
    print("no. is even and divisible by 4")
elif((int(a)%2)== 0 or (int(a)%3)== 0):
    print("it is divisble first two prime numbers ")
else:
    print("first two conditions were not met ")