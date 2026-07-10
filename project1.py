secret = 62
count = 0
while True :
    count +=1
    number = int(input(f"guess a number (attempt {count}): "))
    if number == secret :
        print(f"Congratulations!\nyou guessed it in {count} attempts")
        break
    elif number > secret :
        print("Too high! ")
    else :
        print("Too low! ")
        