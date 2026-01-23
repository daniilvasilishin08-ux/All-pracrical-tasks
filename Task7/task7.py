print("АНКЕТА КОРИСТУВАЧА")

name = input("Введіть ваше ім'я: ")
surname = input("Введіть ваше прізвище: ")
age = input("Скільки вам років: ")
city = input("З якого ви міста: ")
hobby = input("Ваше улюблене захоплення: ")

print("\n" + "="*30)
print("      ВАШІ ДАНІ")
print("="*30)

print(f"Прізвище та ім'я: {surname} {name}")
print(f"Вік: {age}")
print(f"Місце проживання: {city}")
print(f"Хобі: {hobby}")

print("="*30)
print("Анкету завершено успішно!")