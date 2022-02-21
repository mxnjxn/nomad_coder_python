# python have something called a "sequenced type"(something like a list)

# Strings, list, range, tuples, *byte sequence & byte array.
# computer counts from zero
days = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat"]
print(days)
days.append("Sunny")  # list is mutable(changable)
print(days)
days.reverse()
print(days)
days.reverse("sunny")  # list.reverse() takes no arguments

print(type(days))
print("Mon" in days)
print(days[3])
print(len(days))
