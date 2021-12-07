lucky_numbers = [4, 8, 16, 24, 36]
friends = [ "Swaraj", "Shreeyanshi", "Tanya", "Shubham", "Shreya", "Suryansh", "Siddhi"]
friends.extend(lucky_numbers)
print(friends) ###it is now changed
friends.append("Shradda Verma") #this will add the element at the end of list by default
print(friends)
#to add at articular location
friends.insert(7, "Swati")
print(friends)
friends.remove(4)
print(friends)
friends.pop() #it will popout the last element
print(friends)
#friends.clear() will clear friends list
print(friends.index("Shreeyanshi"))
######print(friends.index("shreeyanshi")) #will give error
friends = [ "Swaraj", "Shreeyanshi", "Tanya", "Tanya", "Shubham", "Shreya", "Suryansh", "Siddhi"]
print(friends)
print(friends.count("Tanya"))
friends.sort()

print(friends)
####print(sort(friends)) is wrong 
#friends.sort(friends)

lucky_numbers.reverse()
print(lucky_numbers)
friends2 = friends.copy()
print(friends2)
#print(sum())
