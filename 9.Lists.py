friends = [ "Swaraj", "Shreeyanshi", "Tanya", "Shubham", "Shreya", "Suryansh", "Siddhi"]
list = [1, "two", False]
#index  0    1     2  
#      -3   -2     -1 
print(friends)
print(friends[0])
#We can also acces elements based on the indexes at the back of list.
print(friends[-3])
#To access portions of list
print(friends[0:]) ########Important###### 
print(friends[1:]) #It will grab element at posn1 and all the elements after that.
print(friends[1:4]) #Grab all the elements including first and all  after till 4h and excluding 4th
friends[0]="Ankur"
print(friends)
print(list[-0])