"""
У будинку кілька під’їздів. У кожному під’їзді однакова кількість
квартир. Квартири нумеруються підряд, починаючи з одиниці.
Чи може в деякому під’їзді перша квартира мати номер x, а
остання - номер y? Вводяться два натуральних числа x і y (x ≤ y),
що не перевищують 10000. Виведіть слово Yes, якщо таке можливо,
і No у протилежному випадку.

Автор: КАСЬЯН М.А.
"""
a = int(input())
b = int(input())
if a == 1:
    print("YES")
elif b % (b - a + 1) == 0:
    print("YES")
else:
    print("NO")