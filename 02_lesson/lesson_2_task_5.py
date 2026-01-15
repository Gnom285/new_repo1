
def month_to_season(month):
    if month in (12, 1, 2):
        return "Зима"
    elif 3 <= month <= 5:
        return "Весна"
    elif 6 <= month <= 8:
        return "Лето"
    elif 9 <= month <= 11:
        return "Осень"
month = int(input("Введите номер месяца (1-12): "))
print(month_to_season(month))






