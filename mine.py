# реестр домашних животных
from view import create_animals,filter_animals,\
    get_commands, new_command
from menu import menu


def main():
    # pack_animals_list = []
    # home_animals_list = []
    # animal = create_animals("Borya", "1", "30-11-1998", ['sit', 'mew!'])
    # filter_animals(animal, pack_animals_list, home_animals_list)
    # # print(pack_animals_list[0].name)
    # print(new_command(animal, ['new_command']))
    menu()

if __name__ == '__main__':
    main()
