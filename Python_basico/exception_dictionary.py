read_book = {
    'Sapiens': 'Yuval Noah Harari',
    'Getting Things Done': 'David Allen',
    'The Power of Now': 'Eckhart Tolle',
    'El otoño del patriarca': 'Gabriel Garcia Marquez',
    'Computer Sciende Distilled': 'Wladston Ferreira Filho',
}

def get_author(dictionary, key_input):
    """
    Looks up dictionary to find matches

    Inputs:
    dictionary
    Key = key_input
    Output:
    dictionary.value
    """
    try:
        return (print(f'The author of {key_input} is {dictionary[key_input]}'), True)
    except KeyError as e:
        return (print(f'{key_input} is not in our DB.'), False)

def add_title(dictionary):
    add_key = input('Add a title ---> ')
    add_author = input('Add an author for the title ---> ')
    dictionary.update({add_key:add_author})
    list_keys = list(dictionary.keys())
    print(f'The titles are... \n\n {list_keys}')



def main():
    message = """Welcome.
    This simple software is meant to find a title's author.
    -------------------------------------------------------
    These are the options:
        1. Type 'a' for adding a title.
        2. Type 's' for searching an author.
    -------------------------------------------------------
    """
    print(message)
    main_input = input('Type an option ')
    if main_input == 'a':
        add_title(read_book)
    elif main_input == 's':
        key_input = input('Type a title ---> ')
        get_author(read_book, key_input)
    else:
        print('Your entered option is not correct. Aborting...')


if __name__ == '__main__':
    main()
