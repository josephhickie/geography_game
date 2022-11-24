import pprint
import numpy as np

from tools import distance_between_two_cities



file = '/Users/joseph/PycharmProjects/geography_game/data/concap.csv'



from tools import get_two_random_cities


city1, city2 = get_two_random_cities(file)


def game():

    print('Welcome to THE ULTIMATE GEOGRAPHY GAME\n')

    difficulties = {1: 5000, 2: 3000, 3: 1000, 4: 500, 5: 100}

    print('please choose your difficulty level: ')

    print("{:<8} {:<15}".format('Level','Distance (km)'))
    for difficulty, distance_km in difficulties.items():

        print("{:<8} {:<15}".format(difficulty, distance_km))

    level = int(input())

    while level not in difficulties.keys():
        print(f'difficulty level can be any number between 1 and 5')
        level = int(input())

    distance_delta = difficulties.get(level)
    continue_game = True

    while continue_game:

        city1, city2 = get_two_random_cities()

        distance = distance_between_two_cities(city1, city2)

        print(f'what is the distance between {city1["CapitalName"]} and {city2["CapitalName"]}?')
        print(f'you can be accurate to {distance_delta} km..')


        guess = float(input())
        counts = 1

        while np.abs((distance - guess)) > distance_delta:
            print('incorrect...')
            guess =  (input())
            counts += 1

            if counts > 5:

                string = 'higher' if guess < distance else 'lower'

                print(f'you should be guessing a bit {string}...')


        print(f'CONGRATULATIONS! IT {"ONLY" if counts <= 3 else ""} TOOK YOU {counts} {"guess" if counts == 1 else "guesses"} to guess the distance betweeen {city1["CapitalName"]} and {city2["CapitalName"]}')

        print(f'In fact, the distance is {distance:.2f} km. That is about as far as {distance * 1000 * 10:.0f} cheeseburgers')

        x = input('Do you want to continue? (return to continue)')

        if x != '':
            continue_game = False
