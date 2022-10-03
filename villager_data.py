"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """

    unique_species = set()
    data = open(filename)

    for line in data:
        species = line.rstrip().split('|')[1]
        unique_species.add(species)

    return unique_species


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    villagers = []
    data = open(filename)

    for line in data:
        name, species = line.rstrip().split('|')[:2]
        #print(name)

        if search_string == species:
            villagers.append(name)
        
    #print(villagers)
 
    return sorted(villagers)


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    data = open(filename)
    
    fitness = []
    nature = []
    education = []
    music = []
    fashion = []
    play = []


    for line in data:    
        name, hobby = line.rstrip().split('|')[:4:3]

        if hobby == "Fitness":
            fitness.append(name)
            print(fitness)
        elif hobby == "Nature":
            nature.append(name)
        elif hobby == "Education":
            education.append(name)
        elif hobby == "Music":
            music.append(name)
        elif hobby == "Fashion":
            fashion.append(name)
        elif hobby == "Play":
            play.append(name)


    return [
        sorted(fitness),
        sorted(nature),
        sorted(education),
        sorted(music),
        sorted(fashion),
        sorted(play)
    ]


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    data = open(filename)

    for line in data:
        all_data.append(tuple(line.rstrip().split("|")))   


    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """


    data = open(filename)

    motto = []

    for line in data:
        name, motto = line.rstrip().split('|')[:5:4]
        if villager_name == name:
            motto.append(motto)

    return motto



def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    data = open(filename)

    likeminded = set()
  

    for line in data:
        name, _, personality = line.rstrip().split("|")
        
        if villager_name == name:
            target_personality = personality
            break

    if target_personality:
        for villager_data in all_data(filename):
            name, _, personality = villager_data[: 3]
            if personality == target_personality:
               likeminded.add(name)


    return likeminded

