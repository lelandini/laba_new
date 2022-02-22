import random

number = int(input("Введите целое число: "))
beg = 1
end = 10
First_Number = number + random.randint(beg, end)
Second_Number = number - random.randint(beg, end)

print("First Number:", First_Number, "Second Number:", Second_Number)

arr = [random.randint(beg, end) for i in range(number)]
print("Массив:", arr)
