# menu
dishes = [
    {"name": "Борщ", "price": 80, "desc": "Український суп"},
    {"name": "Піца", "price": 150, "desc": "Сирна піца"},
    {"name": "Суші", "price": 200, "desc": "Роли з лососем"},
    {"name": "Салат", "price": 70, "desc": "Овочевий салат"},
    {"name": "Картопля по-селянськи", "price": 50, "desc": "Картопля з печі"}
]


def show_dishes():
    print("\n" + "=" * 40)
    print("МЕНЮ РЕСТОРАНУ")
    print("=" * 40)

    if not dishes:
        print("Немає страв")
        return

    for i, d in enumerate(dishes):
        print(f"\n[{i}] {d['name']}")
        print(f"Ціна: {d['price']} грн")
        print(f"Опис: {d['desc']}")

    print("\n" + "=" * 40)


def add_dish():
    name = input("Назва: ")

    while True:
        try:
            price = float(input("Ціна: "))
            if price < 0:
                print("Ціна не може бути від'ємною!")
            else:
                break
        except ValueError:
            print("Введи число!")

    desc = input("Опис: ")

    dishes.append({
        "name": name,
        "price": price,
        "desc": desc
    })

    print("Страву додано!")


def edit_dish():
    index = int(input("Номер страви: "))

    if 0 <= index < len(dishes):
        name = input("Нова назва: ")

        while True:
            try:
                price = float(input("Нова ціна: "))
                if price < 0:
                    print("Ціна не може бути від'ємною!")
                else:
                    break
            except ValueError:
                print("Введи число!")

        desc = input("Новий опис: ")

        dishes[index] = {
            "name": name,
            "price": price,
            "desc": desc
        }

        print("Страву оновлено!")
    else:
        print("Немає такої страви")


def delete_dish():
    index = int(input("Номер страви: "))

    if 0 <= index < len(dishes):
        dishes.pop(index)
        print("Страву видалено!")
    else:
        print("Немає такої страви")


def total_price():
    total = sum(d["price"] for d in dishes)
    print(f"\n Загальна ціна всіх страв: {total} грн")


while True:
    show_dishes()

    print("\n1 Додати")
    print("2 Редагувати")
    print("3 Видалити")
    print("4 Загальна ціна")
    print("0 Вихід")

    choice = input("Вибір: ")

    if choice == "1":
        add_dish()
    elif choice == "2":
        edit_dish()
    elif choice == "3":
        delete_dish()
    elif choice == "4":
        total_price()
    elif choice == "0":
        break