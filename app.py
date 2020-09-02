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
        if player['experience'] == True:
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
        player_pick= not_experience_player_name.pop(random_number)
        player_select.append(player_pick)
    
    
    
        

    
        
        
       
        

    

    


    


clean_data()
experience_player_split()
balance_teams()



