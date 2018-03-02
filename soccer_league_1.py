import csv 
def read_file(file):
# Reading the soccer league CSV file. 
	data = [] 
	with open(file, 'r') as csv_file :
		csv_reader = csv.DictReader(csv_file)
		for line in csv_reader:
			data.append(line)
	return data 	

	

def sort_players(players):
# Sorted ex_players and un_players evenly to a list of three lists of dicts
	
	teams = [[], [], []]
	un_player_team_index = 0
	ex_player_team_index = 0
	for player in players:
		if player['Soccer Experience'] == 'YES':
			teams[ex_player_team_index].append(player)
			
			if ex_player_team_index == 2:
				ex_player_team_index = 0
			else:
				ex_player_team_index +=1	

		else:
			teams[un_player_team_index].append(player)
			
			if un_player_team_index == 2:
				un_player_team_index = 0
			else:
				un_player_team_index +=1

	return teams

# Writing into the 'sorted_players' file.
# Created three teams in a list 
def assing_team(sorted_players):
	file = open('sorted_players.txt', 'w')
	team_index = 0
	team_names = ['Shark', 'Dragon', 'Raptors']
	for team in sorted_players:
		file.write(team_names[team_index] + '\r') 
		team_index += 1

		for player in team:
			player_infos = ''
			for player_info in player.values():
				player_infos += player_info + ' '
			file.write(player_infos + '\r')
		file.write('\r')

	file.close() 




def main():
	players =  read_file('soccer_players.csv')
	sorted_players = sort_players(players)
	assing_team(sorted_players)
	

main()
