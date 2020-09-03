import constants
import copy
import random

if __name__ == "__main__":
    pass

players_copy = copy.deepcopy(constants.PLAYERS)
teams_copy = copy.deepcopy(constants.TEAMS)
experience_player = []
not_experience_player = []
experience_player_name = []
not_experience_player_name = []
team = ''
user_input = ''
user_team = ''
panthers = []
bandits = []
warriors = []


def clean_data():
    for player in players_copy:

        player['height'] = int(player['height'].split()[0])

        if player['experience'] == 'YES':
            player['experience'] = bool('TRUE')

        else:
            player['experience'] = bool('')


def experience_player_split():
    global experience_player
    global not_experience_player
    global not_experience_player_name
    global not_experience_player

    for player in players_copy:
        if player['experience'] is True:
            experience_player.append(player)

        else:
            not_experience_player.append(player)

    for experience in experience_player:
        experience_player_name.append(experience['name'])

    for not_experience in not_experience_player:
        not_experience_player_name.append(not_experience['name'])


def balance_teams():
    global player_select
    global not_experience_player
    global experience_player
    global num_player_teams
    counter = 0
    player_select = []
    num_player_teams = int(len(players_copy)) / int(len(teams_copy))

    while counter != num_player_teams:
        random_number = random.randint(0, len(experience_player_name) - 1)
        counter += 1
        player_pick = experience_player_name.pop(random_number)
        player_select.append(player_pick)
        counter += 1
        player_pick = not_experience_player_name.pop(random_number)
        player_select.append(player_pick)


def main_menu():
    global user_input
    print('Welcome to the BasketBall stat tool')
    while True:
        user_input = input('What would you like to do. 1 or 2 \n 1. Display teams \n 2. Quit \n')
        try:
            if user_input != '1' and user_input != '2':
                raise ValueError('That is not a valid option. Please pick 1 or 2 \n')

        except ValueError:
            print('That is not a valid option. Please pick 1 or 2 \n')

        else:
            break


main_menu()

if user_input == '1':

    clean_data()
    experience_player_split()
    balance_teams()
    panthers = player_select
    balance_teams()
    bandits = player_select
    balance_teams()
    warriors = player_select
    
    while True:
        user_team = input('Please select which team you want \n1. Panthers \n2. Bandits \n3. Warriors \n')

        try:
            if user_team != '1' and user_team != '2' and user_team != '3':
                raise ValueError('That is not a valid option. Please pick  a number between 1 and 3')

        except ValueError:
            print('That is not a valid option. Please pick a number between 1 and 3')

        if user_team == '1' or user_team == '2' or user_team == '3':
            print('Team: {}'.format(teams_copy[int(user_team) - 1]))
            print('Number of player: {}'.format(len(panthers)))
            print('Players on team:')
            print(*panthers, sep=', ')
            break
