# реестр домашних животных
from view import create_animals, filter_animals


def main():
    pack_animals_list = []
    home_animals_list = []
    animal = create_animals("Borya", "1", "30-11-1998", "sit!")
    filter_animals(animal, pack_animals_list, home_animals_list)
    print(pack_animals_list[0].name)
    # print(home_animals_list[0].name)

if __name__ == '__main__':
    main()
