from PIL import Image, ImageDraw, ImageFont
def match_result_generate(data):
	#MAPS = ['Sandstone', 'Province', 'Rust', 'Sakura', 'Zone 9']
	COLORS = {
	'province': (255, 111, 7),
	'sandstone': (255, 168, 11),
	'rust': (255, 168, 11),
	'sakura': (250, 92, 205),
	'zone 9': (255, 26, 11)
	}
	player_list = list(data['player_data'].keys())
	
	team_name_font = ImageFont.truetype('Poppins-Black.ttf', 200)
	player_name_font = ImageFont.truetype('Poppins-Black.ttf', 125)
	player_data_font = ImageFont.truetype('Poppins-Black.ttf', 100)
	
	img = Image.open(f"./MAPS/{data['map']}.png")
	I1 = ImageDraw.Draw(img)

	# Team 1
	c=[(289,218),(289,1758)]
	for j,i in enumerate(c):
		I1.text(i, f"{data['teams'][j]}-{data['score'][j]}", font=team_name_font, fill=COLORS[data['map']])

	c=[(636,837),(638,1100),(636,2397),(638,2660)]
	for j,i in enumerate(c):
		I1.text(i, f"{player_list[j]}", font=player_name_font, fill=COLORS[data['map']])
	c=[[(1583+335,840),(2252+335,840),(2921+335,840),(3590+335,840),],
	   [(1583+335,1090),(2252+335,1090),(2921+335,1090),(3590+335,1090),],
	   [(1583+335,2380),(2252+335,2380),(2921+335,2380),(3590+335,2380),],
	   [(1583+335,2630),(2252+335,2630),(2921+335,2630),(3590+335,2630),]]
	for j,i in enumerate(c):
		for y,x in enumerate(i):
			I1.text(x, f"{data['player_data'][player_list[j]][y]}", font=player_data_font, fill=COLORS[data['map']])
	 
	# Save the edited image
	img.save(f"./MATCH_RESULTS/{str(data['id'])}.png")

def sort_order(sub):
	sub.sort(key = lambda x: x[1])
	return sub

def update_leaderboard(data):
	#data = {'map': 'Province', 'teams': ['A','B'], 'score': [8, 4], 'winner': 'A', 'player_data': {'A': [3,4,5,6], 'B': [3,4,5,6], 'G': [3,4,5,6], 'H': [3,4,5,6]}}
	
	# Team Leaderboard

	# Fetching team data
	file = open('teams.txt','r+')
	content = file.readlines()
	team_dict = {}
	for i in content:
		l = i.strip().split(',')
		team_dict[l[0]]=[int(x) for x in l[1:]]

	# Updating team dictionary	
	for i,team in enumerate(data['teams']):
		
		# Determining scores and round difference
		
		l = [1,0,2] if data['winner'] == team else [0,1,0]
		rd = data['score'][0] - data['score'][1]
		if i == 1: 
			rd *= -1
		l.append(rd)	
		
		final = list(map(sum, zip(team_dict[team], l)))
		print(final)
		team_dict[team] = final
	temp = []
	for team in team_dict:
		a = [team, team_dict[team][3]]
		temp.append(a)
	lst_f = sort_order(temp)
	lst_f1 = lst_f[::-1]
	team_dict_f = {}
	for i in lst_f1:
		team = i[0]
		team_dict_f[team] = team_dict[team]
		
	temp = []
	for team in team_dict:
		a = [team, team_dict[team][2]]
		temp.append(a)
	lst_f = sort_order(temp)
	lst_f1 = lst_f[::-1]
	team_dict_f = {}
	for i in lst_f1:
		team = i[0]
		team_dict_f[team] = team_dict[team]
	
	# Writing updated data onto file	
	file.seek(0)
	for i in team_dict_f:
		file.write(f"{','.join([i]+[str(x) for x in team_dict[i]])}\n")
	file.close()
	
	# Player Leaderboard	

	# Fetching player data
	file = open('players.txt','r+')
	content = file.readlines()
	player_dict = {}
	for i in content:
		l = i.strip().split(',')
		player_dict[l[0]]=[int(x) for x in l[1:]]

	# Updating player dictionary	

	for player in data['player_data']:
		final = list(map(sum, zip(player_dict[player], data['player_data'][player])))
		player_dict[player] = final
	print(player_dict)	
	
	# Writing updated data onto file	
	file.seek(0)
	for i in player_dict:
		file.write(f"{','.join([i]+[str(x) for x in player_dict[i]])}\n")
	file.close()

	generate_leaderboard()


def generate_leaderboard():
	img = Image.open("./MAPS/leaderboard.png")
	I1 = ImageDraw.Draw(img)
	font = ImageFont.truetype('Poppins-Black.ttf', 150)
	j=750
	
	file = open('teams.txt','r')
	content = file.readlines()
	l=[]
	for i in content:
		l.append(i.strip().split(','))
	for i in l:
		c=[(235,j),(1840,j),(2460,j),(3170,j),(3970,j)]
		for y,x in enumerate(c):
			I1.text(x, i[y], font=font, fill=(255,255,255))
		j+=370
	img.save("current_leaderboard.png")