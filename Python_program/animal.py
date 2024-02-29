"""Класс создания животных"""


class Animal:
    def __init__(self, name, animal_class, birthday, commands):
        self.name = name
        self.animal_class = animal_class
        self.birthday = birthday
        self.commands = commands

    def signal(self):
        return f"Animal this name - {self.name} is add."
