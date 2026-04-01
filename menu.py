dishes = [
    {"name": "Борщ", "price": 80, "desc": "Український суп"},
    {"name": "Піца", "price": 150, "desc": "Сирна піца"},
    {"name": "Суші", "price": 200, "desc": "Роли з лососем"},
    {"name": "Салат", "price": 70, "desc": "Овочевий салат"}
]


def show_dishes():
    print("\nСписок страв:")
    for i, d in enumerate(dishes):
        print(f"{i}. {d['name']} - {d['price']} грн - {d['desc']}")


def add_dish():
    name = input("Назва: ")
    price = float(input("Ціна: "))
    desc = input("Опис: ")

    dishes.append({
        "name": name,
        "price": price,
        "desc": desc
    })


def edit_dish():
    index = int(input("Номер страви: "))

    if 0 <= index < len(dishes):
        name = input("Нова назва: ")
        price = float(input("Нова ціна: "))
        desc = input("Новий опис: ")

        dishes[index] = {
            "name": name,
            "price": price,
            "desc": desc
        }
    else:
        print("Немає такої страви")


def delete_dish():
    index = int(input("Номер страви: "))

    if 0 <= index < len(dishes):
        dishes.pop(index)
    else:
        print("Немає такої страви")


def total_price():
    total = 0
    for d in dishes:
        total += d["price"]

    print("Загальна ціна:", total)


while True:

    show_dishes()   # ← СПОЧАТКУ список

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

def get_total_stats(menu_list):
    total_sum = sum(item['ціна'] for item in menu_list)
    count = len(menu_list)
    print(f"\nЗагальна ціна всіх страв: {total_sum} грн")
    print(f"Кількість страв у меню: {count}")
