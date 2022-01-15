def cube(num):
   print( num*num*num )
   print("this will not get printed out")

result =cube(4)
print(result)
print(cube(4))
#Return statement allows us to return value back to the caller.
#Without return statement it will not print any value.