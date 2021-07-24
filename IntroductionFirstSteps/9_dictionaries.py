# key value pairs
# no duplicate keys in dictionaries

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April"
}

print(monthConversions["Jan"])
print(monthConversions["Mar"])

# get(key to be searched, default value if not found)
print(monthConversions.get("Luv", "Not a Valid key"))
