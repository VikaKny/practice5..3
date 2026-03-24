dishes = [
    {"name": "Борщ", "price": 80, "desc": "Український суп"},
    {"name": "Піца", "price": 150, "desc": "Сирна піца"},
    {"name": "Суші", "price": 200, "desc": "Роли з лососем"},
    {"name": "Салат", "price": 70, "desc": "Овочевий салат"},
    {"name": "Картопля по-селянськи", "price": 50, "desc": "Картопля з печі"}

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

def count_dishes():
    print(f"\n[INFO] У меню залишилось страв: {len(dishes)}")

def delete_by_name():
    name = input("Введіть назву для видалення: ").lower()
    global dishes
    dishes = [d for d in dishes if d['name'].lower() != name]
    count_dishes()

def delete_by_category():
    cat = input("Яку категорію видалити?: ").lower()
    global dishes
    dishes = [d for d in dishes if d.get('category', '').lower() != cat]
    count_dishes()

while True:

    show_dishes()   # ← СПОЧАТКУ список

    print("\n1 Додати")
    print("2 Редагувати")
    print("3 Видалити")
    print("4 Загальна ціна")
    print("5 Видалити за назвою")
    print("6 Видалити за категорією")
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
    elif choice == "5":
        delete_by_name()
    elif choice == "6":
        delete_by_category()
    elif choice == "0":
        break