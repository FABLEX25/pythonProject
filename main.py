#Калькулятор
znak = input("Выберите знак (+, -, /, *) ")
first = int(input("Введите число "))
second = int(input("Введите второе число "))
if znak == "+":
    result = first + second
elif znak == "-":
    result = first - second
elif znak == "/":
    if second == 0:
        print("На ноль делить нельзя ")
    result = first / second
elif znak == "*":
    result = first * second
print (result)
