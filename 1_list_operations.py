numbers = [10, 5, 8, 2, 15]

print("original list:", numbers)
print("first element:", numbers[0])
print("last element:", numbers[-1])

numbers.append(30)
numbers.insert(2,23)

print("updated list:", numbers)

numbers.pop(-2)
numbers.remove(23)

print("second updates list:", numbers)
