def Summa(arv1:int,arv2:int,arv3:int)->int:
    """ Funktsioon tagastab kolme arvu summa
        Summa(arv1+arv2+arv3) 
    
     param int arv1: Arv1 sisestab kasutaja
     param int arv2: Arv2 sisestab kasutaja
     param int arv3: Vaikimisi arv3 võrdub nulliga
     rtype: int

    """
    s=arv1+arv2+arv3
    return s

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
