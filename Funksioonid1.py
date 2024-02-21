from MyModel import * #Summa as s

b=int(input("Sisesta arv2"))
summa_3=Summa(3,b,int(input("Kolmas arv: ")))
summa_31=Summa(100,100)

print(summa_3)
print(summa_3)

#1
def arithmetic(num1:int, num2:int, operation:str):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Деление на ноль невозможно"
    else:
        return "Неизвестная операция"
result = arithmetic(5, 3, '+')
print("Результат операции:", result)
result = arithmetic(10, 2, '/')
print("Результат операции:", result)
result = arithmetic(8, 4, '%')
print("Результат операции:", result)

#2
def is_year_leap(year):
    if year % 4 == 0:  # Год делится на 4
        if year % 100 == 0:  # Но не делится на 100
            if year % 400 == 0:  # Если делится на 400, то високосный
                return True
            else:
                return False
        else:
            return True
    else:
        return False
# Пример использования функции
year = 2024
if is_year_leap(year):
    print(year, "год является високосным.")
else:
    print(year, "год не является високосным.")


