from view import create_animals, filter_animals, get_commands, new_command
import time

desc = "Меню:\n" \
       "1. Завести новое животное.\n" \
       "2. Определить животное в правильный класс.\n" \
       "3. Получить список команд, которое выполняет животное.\n" \
       "4. Добавить новые команды.\n"\
       "5. Завершение работы.\n"

animal_classes = ['cat', 'dog', 'hamster', 'camel', 'horse', 'donkey']


def menu(count: int):
    item: int = 0
    animals = {}
    pack_animals_list = []
    home_animals_list = []
    while item != 5:
        print(desc)
        try:
            item = int(input("Введите пункт меню: "))
        except ValueError:
            print(f"{40* '_'}\nОШИБКА!\nВведите целочисленное значение!\n{40* '_'}")
        if item == 1:
            name = input("Завести новое животное.\nВведите имя животного: ")
            animal_class = input(f"Введите класс животного({','.join(animal_classes)}): ")
            if animal_class not in animal_classes:
                print("Класс животного введен неверно, ваш компьютер будет уничтожен через")
                for i in range(5, 0, -1):
                    time.sleep(1)
                    print(i)
                break
            birthday = input("Введите дату рождения животного в формате 'DD-MM-YY': ")
            commands = input("Введите через запятую команды, которым животное обучено: ")
            animal = create_animals(name, animal_class, birthday, commands.split())
            animals[count] = animal
            count += 1
        if item == 2:
            try:
                filter_animals(animals[count - 1], home_animals_list, pack_animals_list)
            except Exception:
                print(f"{40 * '_'}\nОШИБКА!\nСписок животных пуст!\n{40 * '_'}")
        if item == 3:
            try:
                print(f"Список всех животных: \n")
                for k, v in animals.items():
                    print(f"{k} - {v.name}")
                number = int(input(f"\nВведите номер животного, чьи команды хотите увидеть: \n"))
                print(get_commands(animals[number]))
            except Exception:
                print(f"{40 * '_'}\nОШИБКА!\nСписок животных пуст!\n{40 * '_'}")
        if item == 4:
            try:
                print(f"Список всех животных: \n")
                for k, v in animals.items():
                    print(f"{k} - {v.name}")
                number = int(input(f"\nВведите номер животного, чьи команды хотите изменить: \n"))
                new_com = input("Введите через запятую команды, которым хотите обучить животное: ").split(',')
                print(new_command(animals[number], new_com))
            except Exception:
                print(f"{40 * '_'}\nОШИБКА!\nСписок животных пуст!\n{40 * '_'}")
        if item == 5:
            print("Работа завершена.")
