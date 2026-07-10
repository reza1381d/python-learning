counter = 0

def increase() :
    global counter
    counter +=1

def calculate_tax(price) :
    tax = 0.09
    return price + price * tax

increase()
print (counter)
print(calculate_tax(80))