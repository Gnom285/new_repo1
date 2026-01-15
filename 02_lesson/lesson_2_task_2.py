

def is_year_leap(number):
    return number % 4 == 0

num = int(input("Введите число: "))
result = is_year_leap(num)
print(f"год {num}: {result}")



