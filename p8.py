def removef(fruites, fruit):
    fruites.remove(fruit)


def max_num(numbers) :
    if not numbers :
        return None
    i = numbers[0]
    for j in numbers :
        if i < j:
            i =j
    return i

numbers = [10, 20, 30]
numbers.append(40)
print(numbers)

cities = ["tehran", "shiraz", "tabriz"]
cities.insert(1, "isfahan")
print(cities)

numbers1 = [9, 1, 7, 3, 5]
numbers1.sort(reverse=True)
print(numbers1)

fruites = ["apple", "banana", "orange", "banana"]
removef(fruites, "banana")
print(fruites)

numbers2 = [12, 8, 35, 4, 20]
print(max_num(numbers2))