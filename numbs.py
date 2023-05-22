#Your list with the numbers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]

#Finds the mean/average of your list.
total = 0
for num in numbers:
    total += num
mean = total / len(numbers)
print("The mean is: ")
print(mean)

#Finds the median of the numbers :).
numbers.sort()
if len(numbers) % 2 == 0:
    median = (numbers[len(numbers) // 2] + numbers[len(numbers) // 2 - 1]) / 2
else:
    median = numbers[len(numbers) // 2]
print("The median is: ")
print(median)

#Finds the mode of your list.
mode_count = 0
for num in numbers:
    if numbers.count(num) > mode_count:
        mode_count = numbers.count(num)
mode = []
for num in numbers:
    if numbers.count(num) == mode_count and num not in mode:
        mode.append(num)
print("The mode is: ")
print(mode)
