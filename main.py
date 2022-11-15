tickets = int(input("Введите необходимое количество билетов:" ))
person = 1
cash = 0

while person <= tickets:
    age_for_ticket = int(input(f"Укажите возраст для кого вы хотите приобрести № {person}:"))
    if age_for_ticket < 18:
        print("Билет бесплатный")
    elif 18 <= age_for_ticket < 25:
        cash += 990
        print("Стоимость билета: 990 рублей")
    else:
        cash += 1390
        print("Стоимость билета: 1390 руб.")
    person += 1
if tickets > 3:
    sale = cash - (cash * 0.1)
    print(f"Сумма к оплате со скидкой 10% составила {sale} руб.")
else:
    print(f"Сумма к оплате {cash} руб.")


