import constants
import copy

if __name__ == "__main__":
    pass

players_copy = copy.deepcopy(constants.PLAYERS)
teams_copy = copy.deepcopy(constants.TEAMS)
num_player_teams = int(len(players_copy) / len(teams_copy))
experience_player = []
not_experience_player = []


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
    
    for player in players_copy:
        if player['experience'] == True:
            experience_player.append(player)
        
        else:
            not_experience_player.append(player)


def balance_teams():
    counter = 0
    


    


clean_data()
