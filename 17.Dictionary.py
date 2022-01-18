#jan -> January keys should always be unique
monthConverter= {
    #keys   values
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",

}
print(monthConverter["Jan"])
print(monthConverter.get("Mar"))
print(monthConverter.get("Luv","not a valid value"))
#get gives default value
