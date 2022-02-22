def age_check(age):
    print(f"you are {age}")
    if age < 18:
        print("you can't drink")
    elif age == 18 or age == 19:
        print("you are new to this")
    elif age > 20 and age < 25:
        print("you are kind of young")
    else:
        print("enjoy you drink")


age_check(18)
