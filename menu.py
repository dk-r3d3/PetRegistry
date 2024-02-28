from view import create_animals, filter_animals

desc = "Меню:\n" \
       "1. Завести новое животное.\n" \
       "2. Определить животное в правильный класс.\n" \
       "3. Получить список команд, которое выполняет животное.\n" \
       "4. Добавить новые команды.\n"

animal_classes = ['cat', 'dog', 'hamster', 'camel', 'horse', 'donkey']


def menu():
    print(desc)
    item = input("Введите пункт меню: ")
    animals = []
    pack_animals_list = []
    home_animals_list = []
    while item != 'end':
        item = input("Введите пункт меню: ")
        if item == "1":
            print("Завести новое животное.")
            # name = input("Введите имя жвиотного: ")
            name = 'Borya'
            # animal_class = input(f"Введите класс животного({','.join(animal_classes)}): ")
            animal_class = "horse"
            birthday = input("Введите дату рождения животного в формате 'DD-MM-YY': ")
            birthday = '30-11-1998'
            # commands = input("Введите через запятую команды, которым животное обучено: ")
            commands = "sit, mew!"
            animal = create_animals(name, animal_class, birthday, commands.split())
            animals.append(animal)
        if item == "2":
            if len(animals) == 0:
                print("Список животных пуст.")
            else:
                filter_animals(animals[-1], home_animals_list, pack_animals_list)
