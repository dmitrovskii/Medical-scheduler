import pyperclip

meds = ["Діаформін","Карведілол","Магнікор", "Соритмік","Мемокс","Клівас","Сибутин","Епадол","Меркана"]

# Вивід з нумерацією списку ліків
for index, name in enumerate(meds, start=1):
    print(f"{index}. {name}")

# Отримання індексів ліків для подальшого копіювання
raw_index = input("\nВведіть номери через пробіл:\n").split()
list_of_need = []

# Перевірка та додавання індексів в list_of_need
for s in raw_index:
    try:
        index = int(s)

        if 1 <= index <= len(meds): 
            list_of_need.append(index - 1)
        else: print(f"Помилка: Номера {index} немає в списку.")

    except ValueError:
        print(f"Помилка: '{s}' не є числом!")

print("")

# Буфер для копіювання та виводу вибраних ліків
bufer = []
for i in list_of_need:
    print(meds[i])
    bufer.append(meds[i])

# Копіювання ліків в буфер ОС
pyperclip.copy("\n".join(bufer))

