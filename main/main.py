import pyperclip

meds = ["Діаформін","Карведілол","Магнікор", "Соритмік","Мемокс","Клівас","Сибутин","Епадол","Меркана"]

for index, name in enumerate(meds, start=1):
    print(f"{index}. {name}")

raw_index = input("\nВведіть номери через пробіл:\n").split()
list_of_need = []

for s in raw_index:
    try:
        index = int(s)

        if 1 <= index <= len(meds): 
            list_of_need.append(index - 1)
        else: print(f"Помилка: Номера {index} немає в списку.")

    except ValueError:
        print(f"Помилка: '{s}' не є числом!")

print("")

bufer = []
for i in list_of_need:
    print(meds[i])
    bufer.append(meds[i])

pyperclip.copy("\n".join(bufer))

