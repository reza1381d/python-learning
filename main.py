name = input("What is your name? ")
age = int(input("How old are you? "))
height = float(input("How tall are you? "))
is_programmer = input("Are you a programmer? ").lower() == "yes" or "Yes" or "y" or "Y"
country = input("Where are you from? ")

print("Hello", name)
print("You are", age, "years old")
if age>18 :
    print("you are an adult")
else :
    print("you are a minor")
print("You are", height, "tall")

if is_programmer:
    print("programmer")
else:
    print("not programmer")

print("from", country)