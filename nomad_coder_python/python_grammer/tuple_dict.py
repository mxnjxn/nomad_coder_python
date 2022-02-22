# tuple is immutable
# use parenthesis

days = ("Mon", "Tue", "Wed", "Thur", "Sat", "Sun")
print(type(days))
print("Mon" not in days)

# Dictionary
nico = {"name": "Nico", "age": 29, "Korean": True,
        "fav_food": ["kimchi", "Sashimi"]}
print(nico["name"])

print(nico)
nico["handsome"] = True  # adding new value in to dictionary
print(nico)
