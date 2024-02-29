from Python_program.animal import Animal


def create_animals(name: str, animal_class: str, birthday: str, commands: list):
    """Функция создания домашних животных"""
    animal = Animal(name, animal_class, birthday, commands)
    print(animal.signal())
    return animal


def filter_animals(animal, home_animals_list: list, pack_animals_list: list):
    """Функция определения животных в правильный класс"""
    if animal.animal_class == 'cat' or animal.animal_class == 'dog'\
            or animal.animal_class == 'hamster':
        home_animals_list.append(animal)
        print("Животное определено в класс 'Домашние животные'.")
    if animal.animal_class == 'donkey' or animal.animal_class == 'horse'\
            or animal.animal_class == 'camel':
        pack_animals_list.append(animal)
        print("Животное определено в класс 'Вьючные животные'.")


def get_commands(animal):
    return f"Список команд {animal.name} - {animal.commands}"


def new_command(animal, new_command: list):
    animal.commands = animal.commands + new_command
    return f"Список команд, включая новые: {animal.commands}"
