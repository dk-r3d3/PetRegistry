from animal import Animal


def create_animals(name: str, animal_class: str, birthday: str, commands: str):
    """Функция создания домашних животных"""
    animal = Animal(name, animal_class, birthday, commands)
    print(animal.signal())
    return animal


def filter_animals(animal, home_animals_list: list, pack_animals_list: list):
    """Функция определения животных в правильный класс"""
    if animal.animal_class == '1':
        home_animals_list.append(animal)
    elif animal.animal_class == '2':
        pack_animals_list.append(animal)


def get_commands():
    pass
