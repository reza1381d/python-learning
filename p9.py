name = input("Enter a name:")
print(name.upper())

text = "   Python Programming   "
text = text.strip()
print(text.lower())

text2 = "apple,banana,orange"
list1 = text2.split(",")
print(list1)

words = ["I", "love", "Python"]
sentence = " ".join(words)
print(sentence)


def is_email(email) :
    return email.lower().endswith(["@gmail.com", "@yahoo.com"])

while True :
    email = input("Enter your Email")
    if is_email(email) :
        break
    else :
        print("Invalid email")