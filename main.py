import youtube_dl
import os
import random
import requests
import pytube
import bs4
import time
import discord
from discord.ext import commands, tasks
from data import horizontal, basic, get_gif, get_meme, watch_tmkoc
from utils import rip, meme1, meme2, jetha2, scared, tall, brain, meme3, triggered, change_my_mind, buttons, aadhar
from hear_me import yeah
from get_token import get_token
from alive import keep_alive
from chess_com_api import chess_info, puzzle
from wiki_info import wiki
from PIL import Image
from datetime import datetime
from coc_api_bot import get_clan, get_player
from DAC import match_result_generate, update_leaderboard, generate_leaderboard


# poetry.lock pyproject.toml requirements.txt

intents = discord.Intents.all()
# TOKEN = "NzU1NzU2NjkyMDM3NDM1NDcz.GROCWU.uAFIUvB_nzaD1tyybEuC27f0n2gHTwO-SUR9tc"

# """NzU1NzU2NjkyMDM3NDM1NDcz.X2H7RA.nGFhVn76SXYCJCCzkYcpZJIuFck"""
# 757215855476998165
# client = discord.Client()
bot = commands.Bot(command_prefix='=', intents=intents)
path = './'

PREFIX = "="

# import discord
# from discord.ext import commands, tasks
# bot = commands.Bot(command_prefix='$', intents=discord.Intents.all())
bot.remove_command('help')


def search_my_word(word):
	search_url = 'https://www.googleapis.com/youtube/v3/search'
	video_url = 'https://www.googleapis.com/youtube/v3/videos'
	video_list = []
	search_params = {
		'key': 'AIzaSyAN2VP46fGVQ3cj38aZKFkepOuneXMJvPE',
		'q': word,
		'part': 'snippet',
		'maxResults': 10,
		'type': 'video'
	}

	r = requests.get(search_url, params=search_params)

	videos = r.json()['items']
	video_ids = []
	for video in videos:
		video_ids.append(video['id']['videoId'])
	# print(video_ids)

	video_params = {
		'key': 'AIzaSyAN2VP46fGVQ3cj38aZKFkepOuneXMJvPE',
		'id': ','.join(video_ids),
		'part': 'snippet,contentDetails',
		'maxResults': 10
	}

	r = requests.get(video_url, params=video_params)

	# print()
	results = r.json()['items']
	# , f'title : {results[0]['snippet']['title']}'
	try:
		return f'https://www.youtube.com/watch?v={results[0]["id"]}'
	except:
		return 0
	# for result in results:
	#     video_data = {
	#         'id': result['id'],
	#         'url': f'https://www.youtube.com/watch?v={result["id"]}',
	#         'thumbnails': result['snippet']['thumbnails']['high']['url'],
	#         'duration': result['contentDetails']['duration'],
	#         'title': result['snippet']['title']
	#     }
	#     return(video_data)

	#     video_list.append(video_data)
	# print(video_list())


activity_l = ["SANCHIT'S GAUDNESS!!", "MUDIT'S BOTNESS!!", "MANAAAAAN's NUBNESS!!",
			  "TANISHQ's KING SACRIFICE!!", "SARTHAK's FIELDING!!", "AKSHAJ's SPAMMING SKILLS!!"]


# @client.event
# async def on_ready():
# 	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="=help or =helpdm"))
# 	print(f'{client.user.name} has connected to Discord!')

@tasks.loop(seconds=60)
async def check_nick():
	member_dict = {}
	dict_m = {}
	server = bot.get_guild(755661056969539654) #deadend
	channel = bot.get_channel(755661056969539658) #enderal
	# server = bot.get_guild(778598124976341033) #arnavserver
	# channel = bot.get_channel(778598124976341036) #general
	# server = bot.get_guild(998270947985469481) #MD
	# channel = bot.get_channel(998270948572680236) #miraceral
	with open('members.txt', 'r+') as file:
		lines = file.readlines()
		for line in lines:
			words = line[:-1].split(", ")
			dict_m[words[0]] = words[1:]
		file.seek(0)
		file.truncate()
		print(dict_m)
		for member in server.members:
			if str(member.id) in dict_m.keys():
				if member.nick not in dict_m[str(member.id)]:
					await channel.send(f"{member.mention} new nickname : {member.nick}")
					dict_m[str(member.id)].append(member.nick)
			else:
				dict_m[str(member.id)] = []
				if member.nick:
					dict_m[str(member.id)].append(member.nick)
		for i in dict_m.keys():
			if dict_m[i]:
				names = ", ".join(dict_m[i])
				file.write(i+", "+names+"\n")
		file.truncate()


@bot.event
async def on_ready():
	print(f'Logged in as {bot.user.name}')
	activity = discord.Game(name="Listening to =help or =helpdm", type=3)
	await bot.change_presence(status=discord.Status.idle, activity=activity)
	print('Recording...')
	# check_nick.start()
	# channel = bot.get_channel(755661056969539658) #enderal
	# await channel.send("Happy Independence Day @everyone :flag_in:")

# from discord import Spotify
# @bot.command()
# async def spotify(ctx, user: discord.Member=None):
# 	user = user or ctx.author
# 	for activity in user.activities:
# 		if isinstance(activity, Spotify):
# 			await ctx.send(f"{user} is listening to {activity.title} by {activity.artist}")

MAPS = ['sandstone', 'province', 'rust', 'sakura', 'zone 9']
# Team 100wpm,Godli Beta,Mishri Gamer
# Team Komdi Kings,Komedi King,Dr. Hathi
# Team LivCity,Taliben,MuZic
# Team Pawn Stars,Jetha Ji,Passion
TEAMS = {
	"Team 100wpm" : ["Godli Beta","Mishri Gamer"],
	"Team Komdi Kings" : ["Komedi King","Dr. Hathi"],
	"Team LivCity" : ["Taliben","MuZic"],
	"Team Pawn Stars" : ["Jetha Ji","Passion"]
}

def sort_order(sub):
	sub.sort(key = lambda x: x[1])
	return sub

@bot.event
async def on_message(message):
	if message.content.startswith('=match'):
		match_data = {}
		command, id = message.content.split(" ")
		channel = message.channel
		schedule = open('matches.txt')
		match = []
		players = {}
		match_data['id'] = id
	
		# finding relevant match
		for i in schedule.readlines():
			if int(i.strip().split(',')[0])==int(id):
				match =  i.strip().split(',')
				break
		teams = [match[1], match[2]]
		match_data['teams'] = teams
	
		# finding team members
		# team_members = open('team_members.txt')
		# for i in team_members.readlines():
		# 	t = i.strip().split(',')
		# 	if t[0] in teams:
		# 		players[t[1]] = players[t[2]] = [0,0,0,0]
		for i in teams:
			for player in TEAMS[i]:
				players[player] = [0,0,0,0]
		await channel.send('Enter map : ')

		def check(m):
			map = m.content.lower()
			print(map)
			match_data['map'] = map
			return m.content.lower() in MAPS and m.channel == channel
		msg = await bot.wait_for('message', check=check)
		await channel.send(f"Winner => 1 for {teams[0]} or 2 for {teams[1]}")
		
		def check2(m):
			winner = int(m.content)
			print(winner)
			match_data['winner']=teams[winner-1]
			return m.content in '12' and m.channel == channel
		msg = await bot.wait_for('message', check=check2)		
		
		await channel.send(f'{teams[0]} round wins: ')

		def check4(m):
			rounds_1 = int(m.content)
			print(rounds_1)
			match_data['score'] = []
			match_data['score'].append(rounds_1)
			return m.content.isdigit() and m.channel == channel
		msg = await bot.wait_for('message', check=check4)
		await channel.send(f'{teams[1]} round wins: ')

		def check5(m):
			rounds_2 = int(m.content)
			print(rounds_2)
			match_data['score'].append(rounds_2)
			return m.content.isdigit() and m.channel == channel
		msg = await bot.wait_for('message', check=check5)
		for player in players:
			await channel.send(f"Enter K,A,D,S of {player}")
			def check(m):
				data = [int(i) for i in m.content.split(',')]
				players[player] = data
				return len(data)==4
			msg = await bot.wait_for('message', check=check)
		match_data['player_data']=players

		data = []
		for player in match_data['player_data']:
			a = [player, match_data['player_data'][player][-1]]
			data.append(a)
		print(data)
		data1 = data[:2]
		data2 = data[2:]
		lst1 = sort_order(data1)
		lst2 = sort_order(data2)
		lst1_f = lst1[::-1]
		lst2_f = lst2[::-1]
		players_f = {}
		for p in lst1_f:
			player = p[0]
			players_f[player] = match_data['player_data'][player]
		for p in lst2_f:
			player = p[0]
			players_f[player] = match_data['player_data'][player]
		match_data['player_data'] = players_f
		await channel.send(f'``` {match_data} ```')
		match_result_generate(match_data)
		update_leaderboard(match_data)
		channel_results = bot.get_channel(901104101063024710)
		channel_leaderboard = bot.get_channel(900818237305020416)
		await channel_results.send(file=discord.File(f"./MATCH_RESULTS/{id}.png"))
		await channel_leaderboard.send(f"After Match {id}", file=discord.File("current_leaderboard.png"))
	await bot.process_commands(message)

@bot.event
async def on_member_join(member):
	# await member.create_dm()
	# await member.dm_channel.send('https://tenor.com/bxzMk.gif')
	print("AAGYA")
	g = member.guild.text_channels
	for i in g:
		if i.name == "enderal":
			await i.send('https://tenor.com/bxzMk.gif')

# @client.event
# async def on_member_join(member):
# 	await member.create_dm()
# 	await member.dm_channel.send(
# 		f'Hi {member.name}, welcome to our Discord server!')


vc = False
players = {}

@bot.command(name="stars")
async def stars(ctx):
	lst = ctx.message.mentions
	# print(lst)
	channel = discord.utils.get(ctx.guild.channels, name="starboard")
	user = lst[0]
	u_id = user.id
	u_count, count = 0, 0
	print(channel, u_id)
	async for message in channel.history(limit=250):
		try:
			embeds = message.embeds
			embed = embeds[0]
			a = embed.to_dict()
			print(user, a['author']['name'])
			if str(user) == a['author']['name']:
				u_count += 1
			count += 1
		except:
			pass
	await ctx.send(f"Total stars for {user} : "+str(u_count))
	await ctx.send(f"Total stars : "+str(count))

@bot.command(pass_context=True, name="role")
# @commands.has_role("Arn4v") # This must be exactly the name of the appropriate role
async def addrole(ctx, *args):
	roles_num = len(list(ctx.guild.roles)) - 1
	print(roles_num)
	new_lines = []
	member = ctx.message.author
	content = args[0]
	print(args)
	if len(args)==4:
		r, g, b = args[1:]
		r, g, b = int(r), int(g), int(b) 
	else:
		r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
	print()
	a = 0
	with open("roles.txt", "r+") as role_file:
		lines = role_file.readlines()
		line_list = list(filter(lambda a: a != "\n", lines))
		for line in line_list:
			words = line.split(",")
			print(words)
			if words[0]==str(member.id) and words[1]==str(ctx.guild.id):
				a = 1
				words[2] = content
				words[4] = str(str(r)+" "+str(g)+" "+str(b))
				roleid = int(words[3])
				role = ctx.guild.get_role(roleid)
				print(words)
				await role.edit(name=content, reason=f"{member.name} changed their role!", color=discord.Colour.from_rgb(r, g, b), position=roles_num-1)
				await ctx.send("{} changed their role! {}".format(member.name, role.mention))
			new_words = ",".join(words)+"\n"
			new_lines.append(new_words)
		if a==0:
			role = await member.guild.create_role(name=content, color=discord.Colour.from_rgb(r, g, b))
			await role.edit(position=roles_num-1)
			add = ctx.guild.get_role(role.id)
			await member.add_roles(add)
			await ctx.send("{} created their role! {}".format(member.name, role.mention))
			new_member_words = [str(member.id), str(ctx.guild.id), content, str(role.id), str(str(r)+" "+str(g)+" "+str(b))]
			new_words = ",".join(new_member_words)
			new_lines.append(new_words)
			print(new_lines)
		role_file.seek(0)
		role_file.truncate()
		role_file.writelines(new_lines)


@bot.command(name="logo")
async def get_server_icon_url(ctx):
	icon_url = ctx.guild.icon_url
	await ctx.send(icon_url)


@bot.command(name="invite")
async def user_info(ctx):
	j = bot.user
	id = j.id
	name = j.name
	print(name)
	member = j
	print(member)
	d_img = member.default_avatar.url
	img = member.avatar.url
	f = ""
	embed = discord.Embed()
	embed.set_author(name=member, icon_url=d_img)
	embed.set_thumbnail(url=img)
	embed.set_footer(text="ID: "+str(id))
	embed.description = f"[Invite](https://discord.com/api/oauth2/authorize?client_id=755756692037435473&permissions=268435456&scope=bot)."
	await ctx.send(embed=embed)

@bot.event
async def on_message_delete(msg):
	chl = msg.channel
	attach = msg.attachments
	await chl.send("{} deleted a message from {} : **{}**".format(msg.author.mention, msg.channel.name, msg.content))
	for link in attach:
		await chl.send(link.url)


@bot.command(name="user")
async def user_info(ctx):
	lst = ctx.message.mentions
	if len(lst) == 0:
		id = ctx.author.id
		name = ctx.author.name
		print(name)
		member = ctx.author
		print(member)
		d_img = member.default_avatar.url
		img = member.avatar.url
		nick = member.nick
		created = member.created_at.strftime("%A, %B %d %Y @ %H:%M:%S %p")
		joined = member.joined_at.strftime("%A, %B %d %Y @ %H:%M:%S %p")
		roles = member.roles
		color = member.color
		status = member.desktop_status
		f = ""
		try:
			activity = member.activity.name
		except:
			activity = member.activity
		for i in roles:
			if i.name != "@everyone":
				f += i.mention+" "
		if not f:
			f = "None"
		embed = discord.Embed(title=f"Userinfo for {member.name}", color=color)
		embed.set_author(name=member, icon_url=d_img)
		embed.set_thumbnail(url=img)
		embed.add_field(name="Created at", value=created, inline=True)
		embed.add_field(name="Joined at", value=joined, inline=True)
		embed.add_field(name="Activty", value=activity, inline=True)
		embed.add_field(name="Nickname", value=nick, inline=True)
		embed.add_field(name="Roles - "+str(len(roles)-1), value=f)
		embed.set_footer(text="ID: "+str(id))
		await ctx.send(embed=embed)
	else:
		for j in lst:
			id = j.id
			name = j.name
			print(name)
			member = j
			print(member)
			d_img = member.default_avatar.url
			img = member.avatar.url
			nick = member.nick
			created = member.created_at.strftime("%A, %B %d %Y @ %H:%M:%S %p")
			joined = member.joined_at.strftime("%A, %B %d %Y @ %H:%M:%S %p")
			roles = member.roles
			color = member.colour
			status = member.desktop_status
			f = ""
			try:
				activity = member.activity.name
			except:
				activity = member.activity
			for i in roles:
				if i.name != "@everyone":
					f += i.mention+" "
			if not f:
				f = "None"
			embed = discord.Embed(
				title=f"Userinfo for {member.name}", color=color)
			embed.set_author(name=member, icon_url=d_img)
			embed.set_thumbnail(url=img)
			embed.add_field(name="Created at", value=created, inline=True)
			embed.add_field(name="Joined at", value=joined, inline=True)
			embed.add_field(name="Activty", value=activity, inline=True)
			embed.add_field(name="Nickname", value=nick, inline=True)
			embed.add_field(name="Roles - "+str(len(roles)-1), value=f)
			embed.set_footer(text="ID: "+str(id))
			await ctx.send(embed=embed)


# @bot.command(name="play")
# async def play(ctx):
# 	channel = ctx.author.voice.channel
# 	vc = await channel.connect()
# 	vc.play(discord.FFmpegPCMAudio(source="SHERLOCK___02_The_Game_is_On__Series_1_Soundtrack_.mp3"))

# @bot.command(name="leave")
# async def leave(ctx):
# 	await ctx.voice_client.disconnect()

@bot.command(name='stat')
async def stats(ctx):
	try:
		a = 0
		with open("mssg_stats.txt", "r+") as file:
			lines = file.readlines()
			user = ctx.message.author
			for line in lines:
				words = line.split(",")
				sender = words[0]
				print(sender+" " + str(user.id))
				if str(user.id) == sender:
					a = 1
					mssgs = len(words) - 1
					print(mssgs)
					await ctx.send("{} has {} messages.".format(user.mention, mssgs))
	except:
		os.system("kill 1")
		a = 0
		with open("mssg_stats.txt", "r+") as file:
			lines = file.readlines()
			user = ctx.message.author
			for line in lines:
				words = line.split(",")
				sender = words[0]
				print(sender+" " + str(user.id))
				if str(user.id) == sender:
					a = 1
					mssgs = len(words) - 1
					print(mssgs)
					await ctx.send("{} has {} messages.".format(user.mention, mssgs))
		

@bot.command(name='tip')
async def get_tip(ctx):
	tips = [['Nahane ja nahane ja!!!', "https://tenor.com/bjPqs.gif"],
			['Chup hoja saatvi fail!!!', "https://tenor.com/brP3j.gif"],
			["https://tenor.com/btb7I.gif", "https://tenor.com/btb7L.gif"],
			["https://tenor.com/bjOY0.gif", "https://tenor.com/buZbD.gif"]]
	lst = ctx.message.mentions
	await lst[0].create_dm()
	message = random.choice(tips)
	await lst[0].dm_channel.send(message[0])
	await lst[0].dm_channel.send(message[1])


@bot.command(name='yt')
async def get_yt(ctx, *args):
	data = search_my_word("".join(args))
	if data:
		await ctx.send(data)
	else:
		await ctx.send(f"NOTHING FOUND")


@bot.command(name='ss')
async def get_ss(ctx, arg):
	q = arg
	if q.startswith('https://'):
		url = f'https://api.apiflash.com/v1/urltoimage?access_key=e6879469431948479d038a9f93c87d05&url={q}&no_ads=true&wait_until=page_loaded'
	else:
		url = f'https://api.apiflash.com/v1/urltoimage?access_key=e6879469431948479d038a9f93c87d05&url=https://{q}&no_ads=true&wait_until=page_loaded'
	im = Image.open(requests.get(url, stream=True).raw)
	im.save("ss.png")
	print(url)
	await ctx.send(file=discord.File('ss.png'))


@bot.command(name='puzzle')
async def get_puzzle(ctx, *args):
	if len(args)!=0:rating = int(args[0])
	else:rating = 6969
	data = puzzle(ctx.author.id, rating)
	print(data)
	play = data[0].split()[-5]
	if play.lower() == "w":
		play = "Black to play!"
	else:
		play = "White to play!"
	e = discord.Embed(title=f"Puzzle for {ctx.author.name}", description=play)
	file = discord.File("new_board1.jpg", filename="new_board1.jpg")
	e.set_image(url="attachment://new_board1.jpg")
	e.set_footer(text="Puzzle link : " +
				 data[2]+f"\nPuzzle Rating : {data[1]}\tPuzzle ID : {data[-1]}")
	await ctx.send(file=file, embed=e)
	import time
	now = time.time()
	# while int(time.time()-now) <= 20:
	# 	pass# print(int(time.time()-now))pass
	# else:await ctx.send("Solution for the puzzle", file=discord.File(f'solution{data[-1]}.gif'))
	# os.remove(f'solution{data[-1]}.gif')
	os.remove('new_board0.jpg')
	for i in range(len(data[-2])):
		os.remove(f'new_board{i+1}.jpg')


@bot.command(name='sol')
async def get_sol(ctx):
	try:
		await ctx.send("Solution for the puzzle", file=discord.File(f'solution{ctx.author.id}.gif'))
		os.remove(f'solution{ctx.author.id}.gif')
	except:
		await ctx.send(f"No solutions found for {ctx.author.name}")

@bot.command(name='announce')
async def announce(ctx):
	if ctx.message.author.id == 920234799283720202:
		embed1 = discord.Embed(title="Fixtures-I for DEADEND ALLIES CUP 2.0", description="", color=0xffa80b)
		embed1.set_image(url="https://i.postimg.cc/V6kb4mvw/schedule-1.png")
		embed2 = discord.Embed(title="Fixtures-II for DEADEND ALLIES CUP 2.0", description="", color=0xffa80b)
		embed2.set_image(url="https://i.postimg.cc/G2vhkfJR/schedule-2.png")
		print("HALO CHIKS")
		await ctx.send("@everyone")
		await ctx.send(embed=embed1)
		await ctx.send(embed=embed2)
# 	embed = discord.Embed(title="DEADEND ALLIES CUP 2.0", description="Make your Allies team ASAP for the biggest standoff2 event in the server!!! \nTeams get to play 1 map against each team and then we head to the DOUBLE ELIMINATION!!! \nLET'S GO!!\n\n\nRULES - \n1. There will be 4 teams competing with each other in the DAC2.0 \n2. All the teams will be playing 1 match with each Team in the Round Robin( Round Robin means normal allies with points table like  DAC season 1) \n3. Breeze will be banned for all the Teams as it is a new map and most of us are not used to the map. \n4. You will get to to select the map before every match.\n5. After the Round Robin all the teams will head to the next stage of  DAC 2.0 that is  \"DOUBLE ELIMINATION ROUND\" .\n6. The seedings of double elimination will be taken from the results of Round Robin . The first two teams will be seeded into slot 1 and slot 2 and the 3rd and 4th team will be seeded into 3rd and 4th slot, through which they will make a run to the top to earn the server title @DAC WINNERS \n7. Players are requested to cooperate.\n\nThank you!!! **ALL THE BEST TO ALL THE TEAMS!!!**", color=0xffa80b)
# 	embed.set_thumbnail(url="https://i.postimg.cc/s2P6B5wF/logo-1.jpg")
# 	embed.set_image(url="https://i.postimg.cc/4xLFvMyb/horizontal.png")
# 	await ctx.send("@everyone", embed=embed)

@bot.command(name='chess')
async def get_chess(ctx, *args):
	username = "".join(args)
	data = chess_info(username)
	if data['status'] != 200:
		await ctx.send(f"No player with username as {username} available.")
	else:
		e = discord.Embed()
		e.set_author(
			name=username, icon_url="https://images.chesscomfiles.com/uploads/v1/images_users/tiny_mce/SamCopeland/phpmeXx6V.png")
		try:
			e.set_thumbnail(url=data['photo'])
		except:
			pass
		try:
			e.add_field(name="Name", value=data['name'], inline=True)
		except:
			pass
		try:
			e.add_field(name="Last online",
						value=data['last_online'], inline=False)
		except:
			pass
		try:
			e.add_field(name="Followers", value=data['followers'], inline=True)
		except:
			pass
		try:
			e.add_field(name="Location", value=data['location'], inline=True)
		except:
			pass
		try:
			e.add_field(name="Joined", value=data['joined'], inline=True)
		except:
			pass
		await ctx.send("", embed=e)
		e = discord.Embed()
		e.set_author(
			name="Bullet", icon_url="https://images.chesscomfiles.com/uploads/v1/images_users/tiny_mce/SamCopeland/phpmeXx6V.png")
		try:
			e.set_thumbnail(
				url="https://images.chesscomfiles.com/uploads/v1/chess_term/6d38c776-5832-11ea-b094-69ad1750e029.e5c4f168.5000x5000o.d49d1f49bc53.png")
		except:
			pass
		try:
			e.add_field(name="Current",
						value=data['bullet'][0][0][0], inline=True)
		except:
			pass
		try:
			e.add_field(
				name="Best", value=data['bullet'][0][0][1], inline=False)
		except:
			pass
		try:
			e.add_field(
				name="Wins", value=data['bullet'][0][1][0], inline=True)
		except:
			pass
		try:
			e.add_field(
				name="Loss", value=data['bullet'][0][1][1], inline=True)
		except:
			pass
		try:
			e.add_field(
				name="Draws", value=data['bullet'][0][1][2], inline=True)
		except:
			pass
		await ctx.send("", embed=e)

		e = discord.Embed()
		e.set_author(
			name="Blitz", icon_url="https://images.chesscomfiles.com/uploads/v1/images_users/tiny_mce/SamCopeland/phpmeXx6V.png")
		try:
			e.set_thumbnail(
				url="https://images.chesscomfiles.com/uploads/v1/chess_term/80febd7c-bcb1-11ea-8ef7-07dbcd6ea7c7.090c6f94.630x354o.46122acf9ffe@2x.png")
		except:
			pass
		try:
			e.add_field(name="Current",
						value=data['blitz'][0][0][0], inline=True)
		except:
			pass
		try:
			e.add_field(
				name="Best", value=data['blitz'][0][0][1], inline=False)
		except:
			pass

		try:
			e.add_field(name="Wins", value=data['blitz'][0][1][0], inline=True)
		except:
			pass
		try:
			e.add_field(name="Loss", value=data['blitz'][0][1][1], inline=True)
		except:
			pass
		try:
			e.add_field(
				name="Draws", value=data['blitz'][0][1][2], inline=True)
		except:
			pass
		await ctx.send("", embed=e)

		e = discord.Embed()
		e.set_author(
			name="Rapid", icon_url="https://images.chesscomfiles.com/uploads/v1/images_users/tiny_mce/SamCopeland/phpmeXx6V.png")
		try:
			e.set_thumbnail(
				url="https://arnav17sharma.github.io/assets/share-live.a3b92931.png")
		except:
			pass
		try:
			e.add_field(name="Current",
						value=data['rapid'][0][0][0], inline=True)
		except:
			pass
		try:
			e.add_field(
				name="Best", value=data['rapid'][0][0][1], inline=False)
		except:
			pass

		try:
			e.add_field(name="Wins", value=data['rapid'][0][1][0], inline=True)
		except:
			pass
		try:
			e.add_field(name="Loss", value=data['rapid'][0][1][1], inline=True)
		except:
			pass
		try:
			e.add_field(
				name="Draws", value=data['rapid'][0][1][2], inline=True)
		except:
			pass
		await ctx.send("", embed=e)


@bot.command(name='wallh')
async def get_wallh(ctx):
	horizontal()
	await ctx.send(file=discord.File(f'{path}/sample3.png'))


@bot.command(name='wallb')
async def get_wallb(ctx):
	basic()
	await ctx.send(file=discord.File(f'{path}basic/demo1.png'))


@bot.command(name='watch')
async def get_watch(ctx):
	title, id = watch_tmkoc()
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=title+" Write =help or =helpdm", url=f'http://www.youtube.com/watch?v={id}'))
	await ctx.send(f"Watching **{title}** at http://www.youtube.com/watch?v={id}")


@bot.command(name='buttons')
async def button(ctx, *args):
	txt1, txt2 = args
	buttons(txt1, txt2)
	await ctx.send(file=discord.File(f'{path}/changed_buttons.jpg'))


@bot.command(name='meme1')
async def meme1(ctx, *args):
	lst = ctx.message.mentions
	print(lst)
	meme3(lst[0].avatar.url, lst[1].avatar.url)
	await ctx.send(file=discord.File(f'{path}/meme3.jpeg'))


@bot.command(name='jetha1')
async def get_jetha1(ctx, *args):
	j, d, c = args
	meme1(j, d, c)
	await ctx.send(file=discord.File(f'{path}/jetha1.jpg'))


@bot.command(name='note')
async def get_note(ctx, *args):
	j, d, c = args
	meme2(j, d, c)
	await ctx.send(file=discord.File(f'{path}/cheating1.jpg'))


@bot.command(name='befter')
async def get_befter(ctx, *args):
	j, d, c = args
	tall(j, d, c)
	await ctx.send(file=discord.File(f'{path}/tall.jpg'))


@bot.command(name='changemymind')
async def get_changemymind(ctx, args, size=50, width=20):
	txt, size, width = args, size, width
	change_my_mind(txt, size, width)
	await ctx.send(file=discord.File(f'{path}/changed.png'))


@bot.command(name='scared')
async def get_scared(ctx, *args):
	j, d, c = args
	scared(j, d, c)
	await ctx.send(file=discord.File(f'{path}/scared.jpg'))


@bot.command(name='jetha2')
async def get_jetha2(ctx, *args):
	j, d, c = args
	jetha2(j, d, c)
	await ctx.send(file=discord.File(f'{path}/jetha2.jpg'))


@bot.command(name='brain')
async def get_brain(ctx, *args):
	a, j, d, c = args
	brain(a, j, d, c)
	await ctx.send(file=discord.File(f'{path}/brain.jpg'))


@bot.command(name='trigger')
async def get_trigger(ctx, *args):
	lst = ctx.message.mentions
	print(lst)
	if len(lst) != 0:
		for i in lst:
			triggered(i.avatar.url)
			await ctx.send(file=discord.File("triggered.gif"))
			# await ctx.send(file=discord.File("user.jpg"))
	else:
		triggered(ctx.author.avatar.url)
		await ctx.send(file=discord.File("triggered.gif"))
		# await ctx.send(file=discord.File("user.jpg"))


@bot.command(name='avatar')
async def get_avatar(ctx, *args):
	lst = ctx.message.mentions
	print(lst)
	if len(lst) != 0:
		for i in lst:
			await ctx.send("{}".format(i.avatar.url))
	else:
		await ctx.send("{}".format(ctx.author.avatar.url))


@bot.command(name='rip')
async def get_rip(ctx):
	lst = ctx.message.mentions
	if len(lst) != 0:
		for i in lst:
			rip(i.avatar.url)
			await ctx.send(file=discord.File("ripped.png"))
	else:
		rip(ctx.author.avatar.url)
		await ctx.send(file=discord.File("ripped.png"))


@bot.command(name='gif')
async def get_gif2(ctx, *args):
	try:
		if args[-1].isdigit():
			print(args[:-1])
			url = get_gif("".join(args[:-1]), int(args[-1])-1)
		else:
			print(args)
			url = get_gif("".join(args).lower())
		print(url)
		if url != None:
			sent = await ctx.send("{}".format(url))
			await sent.add_reaction("\U0001F916")
			await sent.add_reaction("\U0001f44d")
			print("REACTED!!")
		else:
			await ctx.send("**NOT FOUND**")
	except:
		await ctx.send("**NOT FOUND**")


@bot.command(name='aadhar')
async def aadhar_get(ctx, *args):
	lst = ctx.message.mentions
	b = args[-1]
	if len(lst) != 0:
		for i in lst:
			img = i.avatar.url
			nick = i.nick
			if nick == None:
				nick = i.name
			bio = b
			id = str(i)[-5:]
			aadhar(img, nick, "Male", bio, id)
			await ctx.send(file=discord.File("aadhar-changed.png"))
	else:
		img = ctx.author.avatar.url
		nick = ctx.author.nick
		if nick == None:
			nick = ctx.author.name
		bio = b
		id = str(ctx.author)[-5:]
		aadhar(img, nick, "Male", bio, id)
		await ctx.send(file=discord.File("aadhar-changed.png"))


@bot.command(name='meme')
async def get_meme2(ctx):
	desc, link, lst, id = get_meme()
	await ctx.send(lst)
	await ctx.send(link)
	await ctx.send("https://www.redditmedia.com/mediaembed/"+id)

	# else:
	# 	e.set_image(url=lst[0]['data']['children'][0]['data']['url'])
	# try:
# 	except:
# 		await ctx.send(f'''
# ```
# {lst[0]['data']['children'][0]}
# ```''')

@bot.command(name='poll')
async def get_poll(ctx, *args):
	print(args)
	reactions = {
		' :red_square: ': "\U0001F7E5",
		' :orange_square: ': "\U0001F7E7",
		' :yellow_square: ': "\U0001F7E8",
		' :green_square: ': "\U0001F7E9"
	}
	op = [
		' :red_square: ',
		' :orange_square: ',
		' :yellow_square: ',
		' :green_square: '
	]
	lst = []
	d = ""
	j = 1
	q = args[0]
	options = lst[1:]
	embed = discord.Embed(
		title=args[0], description=f"Poll by {ctx.author.mention}", color=0x00e1ff)
	embed.set_author(name=f"{ctx.author.name}",
					 icon_url=f"{ctx.author.avatar.url}")
	for j in range(len(args[1:])):
		embed.add_field(name="{:^10}".format("------"),
						value=f"{args[1:][j]} - {op[j]}", inline=False)
	embed.set_footer(text="React below to vote!")
	mess = await ctx.send(embed=embed)
	a = 0
	react_me = []
	for i in range(len(args[1:])):
		await mess.add_reaction(reactions[op[i]])


@bot.command(name='clan')
async def show_clan(ctx):
	clan_json = get_clan()
	embed = discord.Embed(title=f"{clan_json['name']}\#{clan_json['tag'][:-1]}",
						  description=clan_json['description'], color=0xff8800)
	embed.set_thumbnail(url=clan_json['badgeUrls']['small'])
	embed.add_field(name="Clan Points", value=str(
		clan_json['clanPoints']), inline=True)
	embed.add_field(name="Clan Versus Points", value=str(
		clan_json['clanVersusPoints']), inline=True)
	embed.add_field(name="Required Trophies", value=str(
		clan_json['requiredTrophies']), inline=True)
	embed.add_field(name="Type", value=clan_json['type'], inline=True)
	embed.add_field(
		name="Members", value=f"{str(clan_json['members'])}/50", inline=True)
	await ctx.send(embed=embed)
	t = 0
	embed1 = discord.Embed(title=f"Member List", color=0xff8800)
	embed1.set_thumbnail(url=clan_json['badgeUrls']['small'])
	for member in clan_json['memberList']:
		embed1.add_field(
			name=f"{str(member['clanRank'])}. {member['name']}{member['tag']} ({str(member['trophies'])} :trophy:) - {member['role'].title()}", value=":heavy_minus_sign:"*5, inline=False)
		t += 1
		if t == 10:
			t = 0
			await ctx.send(embed=embed1)
			embed1 = discord.Embed(title=f"Member List", color=0xff8800)
			embed1.set_thumbnail(url=clan_json['badgeUrls']['small'])
		else:
			pass
	await ctx.send(embed=embed1)


@bot.command(name='coc')
async def show_coc(ctx, *args):
	player_tag = args[0]
	print(player_tag)
	player_info = get_player(player_tag)
	th = player_info['townHallLevel']
	if th >= 12:
		description = f"Town Hall Level - {str(player_info['townHallLevel'])} (Town Hall Weapon Level - {str(player_info['townHallWeaponLevel'])})"
		th_image_name = f"Town_Hall{str(player_info['townHallLevel'])}_{str(player_info['townHallWeaponLevel'])}"
	else:
		description = f"Town Hall Level - {str(player_info['townHallLevel'])}"
		th_image_name = f"Town_Hall{str(player_info['townHallLevel'])}"

	file = discord.File(f'THS/{th_image_name}.png',
						filename=f'{th_image_name}.png')
	embed = discord.Embed(
		title=player_info['league']['name'], description=description, color=0x00b3ff)
	embed.set_author(name=f"{player_info['name']} {str(player_info['tag'])}",
					 icon_url=player_info['league']['iconUrls']['small'])
	embed.set_thumbnail(url=f"attachment://{th_image_name}.png")
	embed.add_field(
		name="Clan", value=f"{player_info['clan']['name']}{player_info['clan']['tag']}", inline=True)
	embed.add_field(name="Exp Level", value=str(
		player_info['expLevel']), inline=True)
	embed.add_field(name="Builder Hall Level", value=str(
		player_info['builderHallLevel']), inline=False)
	embed.add_field(name="Versus Trophies", value=str(
		player_info['versusTrophies']), inline=True)
	embed.add_field(name="Achievements", value=str(
		len(player_info['achievements'])), inline=True)
	embed.add_field(name="Troops Unlocked", value=str(
		len(player_info['troops'])), inline=True)
	embed.add_field(name="Spells Unlocked", value=str(
		len(player_info['spells'])), inline=True)
	embed.add_field(name="Heroes Unlocked", value=str(
		len(player_info['heroes'])), inline=True)
	for hero in player_info['heroes']:
		embed.add_field(name=hero['name'], value=str(
			hero['level']), inline=True)
	embed.set_footer(text="Arnav's Bot#6172")
	await ctx.send(file=file, embed=embed)


# MUSIC COMMANDS


def get_file_by_url(video_url):
	video_info = youtube_dl.YoutubeDL().extract_info(url=video_url, download=False)
	filename = "VC.mp3"
	options = {
		'format': 'worstaudio/worst',
		'keepvideo': False,
		'outtmpl': filename,
	}
	with youtube_dl.YoutubeDL(options) as ydl:
		ydl.download([video_info['webpage_url']])
		print("Download complete... {}".format(filename))
	return video_info['title']


@bot.command(name='join')
async def join_CHANNEL(ctx):
	if not ctx.message.author.voice:
		await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
		return
	else:
		channel = ctx.message.author.voice.channel
	await channel.connect()


@bot.command(name='play')
async def play(ctx, url):
	try:
		os.remove('VC.mp3')
	except:
		pass
	if url.startswith('https://'):
		url = url
	else:
		try:
			url = search_my_word("".join(url))
		except:
			await ctx.send("NOT FOUND")
			return
	server = ctx.message.guild
	voice_channel = server.voice_client
	await ctx.send("Waiting...")
	try:
		get_file_by_url(url)
	except:
		await ctx.send("Cannot be downloaded!")
	voice_channel.play(discord.FFmpegPCMAudio(source="VC.mp3"))
	await ctx.send('**Now playing:** Kuch toh baja raha')


@bot.command(name='pause')
async def pause(ctx):
	voice_client = ctx.message.guild.voice_client
	if voice_client.is_playing():
		await voice_client.pause()
	else:
		await ctx.send("Kuch nahi baja raha hu be..Bajj mat tu...")


@bot.command(name='resume')
async def resume(ctx):
	voice_client = ctx.message.guild.voice_client
	if voice_client.is_paused():
		await voice_client.resume()
	else:
		await ctx.send("Waidi hai tu...")


@bot.command(name='leave')
async def leave_CHANNEL(ctx):
	voice_client = ctx.message.guild.voice_client
	if voice_client.is_connected():
		await voice_client.disconnect()
	else:
		await ctx.send("The bot is not connected to a voice channel.")


# MUSIC COMMANDS

@bot.command(name='check_nick')
async def c_nick(ctx):
	print('Recording nicknames...')
	check_nick.start()


@bot.command(name='nicknames')
async def nick(ctx):
	lst = ctx.message.mentions
	for member in lst:
		with open('members.txt', 'r') as file:
			lines = file.readlines()
			for line in lines:
				words = line.split(", ")
				id = words[0]
				if str(member.id) == id:
					nicknames = words[1]
					for name in words[2:]:
						if name in nicknames:
							nicknames += ", "+name
					await ctx.send(f"{member.mention}'s nicknames : {nicknames}")
	if len(lst) == 0:
		member = ctx.author
		with open('members.txt', 'r') as file:
			lines = file.readlines()
			for line in lines:
				words = line.split(", ")
				id = words[0]
				if str(member.id) == id:
					nicknames = ", ".join(words[1:])
					await ctx.send(f"{member.mention}'s nicknames : {nicknames}")


@bot.command(name='help')
async def get_helpme(ctx):
	embed = discord.Embed(title="Arnav's Bot Help",
						  description="This is a list of all the commands available in me!", color=0x00d9ff)
	embed.add_field(name="=role {role_name} {r} {g} {b}",
					value='Creates or modifies a role for a user(rgb values are optional). Example : `=role "DeadendMember69" "69" "69" "69"`', inline=True)
	embed.add_field(name="=yt {search_word(s)}",
					value="Returns the first result for searched word(s). Example : `=yt discord bot`", inline=True)
	embed.add_field(
		name="=ss {website_url}", value="Returns a screenshot of the website url. Example : `=ss google.com`", inline=True)
	embed.add_field(
		name="=puzzle", value="Returns lichess chess puzzle. Example : `=puzzle`", inline=True)
	embed.add_field(
		name="=chess {username}", value="Returns chess.com profile info for the username. Example : `=chess viditchess`", inline=True)
	embed.add_field(
		name="=wallh", value="Returns a randomly generated Horizontal wallpaper for you!", inline=True)
	embed.add_field(
		name="=wallb", value="Returns a randomly generated Basic wallpaper for you!", inline=True)
	embed.add_field(
		name="=watch", value="Make my watch a TMKOC Video!", inline=True)
	embed.add_field(name="=new_act",
					value="Changes my activity randomly!", inline=True)
	embed.add_field(name="=avatar user_mention",
					value="Sends the avatar image for any user. Example : `=avatar @ME`", inline=True)
	embed.add_field(name="=rip user_mention",
					value="RIP for the user mentioned. Check it out! `=rip @ME`", inline=True)
	embed.add_field(name="=gif {search_word(s)} {number}",
					value="Sends a gif from tenor for the word . The number is optional and should be used to see the next result for the search word in tenor (till 10). Example : `=gif jethalal` `=gif jethalal 2`", inline=True)
	embed.add_field(
		name="=meme", value="Sends a meme from reddit.", inline=True)
	embed.add_field(name="=poll \"Question\" \"Option1\" \"Option2\" \"Option3\" \"Option4\"",
					value="Creates a poll for a Question . Atleat 2 options required and max options can be 4. Example : `=poll \"Who will IPL 2021?\" \"CSK\" \"MI\" \"RCB\" \"DC\"`", inline=True)
	embed.add_field(name="=tip user_mention",
					value="Dms a tip to the user!", inline=True)
	embed.add_field(name="=jetha1 a b c",
					value="Check it out and type anything in place of a b c!. Example : `=jetha1 a b c`", inline=True)
	embed.add_field(name="=jetha2 a b c",
					value="Check it out and put thing in place of a b c! . Example : `=jetha a b c`", inline=True)
	embed.add_field(name="=befter a b c",
					value="Check it out and put thing in place of a b c! . Example : `=befter a b c`", inline=True)
	embed.add_field(name="=scared a b c",
					value="Check it out and put thing in place of a b c! . Example : `=scared a b c`", inline=True)
	embed.add_field(name="=note a b c",
					value="Check it out and put thing in place of a b c! . Example : `=note a b c`", inline=True)
	embed.add_field(name="=brain a b c d",
					value="Check it out and put thing in place of a b c d! . Example : `=brain a b c d`", inline=True)
	embed.add_field(name="=meme1 user1_mention user2_mention",
					value="Check it out and put thing in place of a, b! . Example : `=meme1 @a @d`", inline=True)
	embed.add_field(name="=trigger user_mention",
					value="Sends a gif for the triggered user avatar!. Example : `=trigger @user`", inline=True)
	embed.add_field(name="=user (optional)user_mention",
					value="Sends a description of the user. Example : `=user` OR `=user @user1 @user2`", inline=True)
	embed.add_field(name="=changemymind {text} {font_size} {max_length}",
					value="font_size and max_length are optional. Example : `=changemymind \"KATEGA SABKA(Bade sayane kehke gye haina...\")`", inline=True)
	embed.add_field(name="=buttons {text1} {text2}",
					value="two button meme template. Example : `=buttons \"Deepak Vs Guptill\" \"Anderson Vs Kohli\"`", inline=True)
	await ctx.send(embed=embed)


@bot.command(name='helpdm')
async def get_helpdm(ctx):
	await ctx.author.create_dm()
	embed = discord.Embed(title="Arnav's Bot Help",
						  description="This is a list of all the commands available in me!", color=0x00d9ff)
	embed.add_field(name="=role {role_name} {r} {g} {b}",
					value='Creates or modifies a role for a user(rgb values are optional). Example : `=role "DeadendMember69" "69" "69" "69"`', inline=True)
	embed.add_field(name="=yt {search_word(s)}",
					value="Returns the first result for searched word(s). Example : `=yt discord bot`", inline=True)
	embed.add_field(
		name="=ss {website_url}", value="Returns a screenshot of the website url. Example : `=ss google.com`", inline=True)
	embed.add_field(
		name="=chess {username}", value="Returns chess.com profile info for the username. Example : `=chess viditchess`", inline=True)
	embed.add_field(
		name="=puzzle", value="Returns lichess chess puzzle. Example : `=puzzle`", inline=True)
	embed.add_field(
		name="=wallh", value="Returns a randomly generated Horizontal wallpaper for you!", inline=True)
	embed.add_field(
		name="=wallb", value="Returns a randomly generated Basic wallpaper for you!", inline=True)
	embed.add_field(
		name="=watch", value="Make my watch a TMKOC Video!", inline=True)
	embed.add_field(name="=new_act",
					value="Changes my activity randomly!", inline=True)
	embed.add_field(name="=avatar user_mention",
					value="Sends the avatar image for any user. Example : `=avatar @ME`", inline=True)
	embed.add_field(name="=rip user_mention",
					value="RIP for the user mentioned. Check it out! `=rip @ME`", inline=True)
	embed.add_field(name="=gif {search_word(s)} {number}",
					value="Sends a gif from tenor for the word . The number is optional and should be used to see the next result for the search word in tenor (till 10). Example : `=gif jethalal` `=gif jethalal 2`", inline=True)
	embed.add_field(
		name="=meme", value="Sends a meme from reddit.", inline=True)
	embed.add_field(name="=poll \"Question\" \"Option1\" \"Option2\" \"Option3\" \"Option4\"",
					value="Creates a poll for a Question . Atleat 2 options required and max options can be 4. Example : `=poll \"Who will IPL 2021?\" \"CSK\" \"MI\" \"RCB\" \"DC\"`", inline=True)
	embed.add_field(name="=tip user_mention",
					value="Dms a tip to the user!", inline=True)
	embed.add_field(name="=jetha1 a , b, c ,d",
					value="Check it out and type anything in place of a, b, c, d! . Example : `=jetha1 a , b, c ,d`", inline=True)
	embed.add_field(name="=jetha2 a, b, c",
					value="Check it out and put thing in place of a, b, c! . Example : `=jetha a , b, c`", inline=True)
	embed.add_field(name="=befter a, b, c",
					value="Check it out and put thing in place of a, b, c! . Example : `=befter a , b, c`", inline=True)
	embed.add_field(name="=scared a, b, c",
					value="Check it out and put thing in place of a, b, c! . Example : `=scared a , b, c`", inline=True)
	embed.add_field(name="=note a, b, c",
					value="Check it out and put thing in place of a, b, c! . Example : `=note a , b, c`", inline=True)
	embed.add_field(name="=brain a, b, c, d",
					value="Check it out and put thing in place of a, b, c, d! . Example : `=brain a , b, c , d`", inline=True)
	embed.add_field(name="=meme1 user1_mention user2_mention",
					value="Check it out and put thing in place of a, b! . Example : `=meme1 @a @d`", inline=True)
	embed.add_field(name="=trigger user_mention",
					value="Sends a gif for the triggered user avatar!. Example : `=trigger @user`", inline=True)
	embed.add_field(name="=changemymind {text} {font_size} {max_length}",
					value="font_size and max_length are optional. Example : `=changemymind \"KATEGA SABKA(Bade sayane kehke gye haina...\")`", inline=True)
	embed.add_field(name="=buttons {text1} {text2}",
					value="two button meme template. Example : `=buttons \"Deepak Vs Guptill\" \"Anderson Vs Kohli\"`", inline=True)
	await ctx.author.dm_channel.send(embed=embed)
	await ctx.send(f"{ctx.author.mention} check your dms")


'''
@client.event
async def on_message(message):
	# if message.author.id==user_token:
	# 	channel = client.get_channel(832934072229298226)
	# 	await channel.send(message.content)


	if PREFIX + "yt" in message.content.split(" ")[0]:
		data = search_my_word("".join(message.content.split(" ")[1:]))
		if data:await message.channel.send(data)
		else:await message.channel.send(f"NOTHING FOUND")

	if PREFIX + "ss" in message.content.split(" ")[0]:
		q = message.content.split(" ")[1].strip()
		if q[:4]=="www.":
			url=f'https://shot.screenshotapi.net/screenshot?&url=https://{q}&full_page=true&output=image&file_type=png&block_ads=true&no_cookie_banners=true&retina=true&block_tracking=true'
		elif q.startswith('https://'):
			url=f'https://shot.screenshotapi.net/screenshot?&url={q}&full_page=true&output=image&file_type=png&block_ads=true&no_cookie_banners=true&retina=true&block_tracking=true'
		else:
			url=f'https://shot.screenshotapi.net/screenshot?&url=https://{q}&full_page=true&output=image&file_type=png&block_ads=true&no_cookie_banners=true&retina=true&block_tracking=true'
		im = Image.open(requests.get(url, stream=True).raw)
		im.save("ss.png")
		print(url)
		await message.channel.send(file=discord.File('ss.png'))
	
	# not adding now
	if PREFIX + "wiki" in message.content.lower():
		query = " ".join(message.content.split(" ")[1:]).title();print(query)
		try:
			data = wiki(query);print(data);a=0
			e = discord.Embed()
			e.set_author(name=query,icon_url="https://upload.wikimedia.org/wikipedia/en/thumb/8/80/Wikipedia-logo-v2.svg/1200px-Wikipedia-logo-v2.svg.png")
			try:e.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/en/thumb/8/80/Wikipedia-logo-v2.svg/1200px-Wikipedia-logo-v2.svg.png')
			except:pass
			for i in data:
				e.add_field(name=i, value=data[i], inline=True);a+=1
				if a==len(data):await message.channel.send("", embed=e)
		except:await message.channel.send(f"No results found for `{query}` in wikipedia :( \n Or try searching with some modifications...")

	if PREFIX + "chess" in message.content.lower():
		username = message.content.split(" ")[1]
		data = chess_info(username)
		if data['status'] != 200:
			await message.channel.send(f"No player with username as {username} available.")
		else:
			e = discord.Embed()
			e.set_author(name=username,icon_url="https://images.chesscomfiles.com/uploads/v1/images_users/tiny_mce/SamCopeland/phpmeXx6V.png")
			try:e.set_thumbnail(url=data['photo'])
			except:pass
			try:e.add_field(name="Name", value=data['name'], inline=True)
			except:pass
			try:e.add_field(name="Last online",value=data['last_online'],inline=False)
			except:pass
			try:e.add_field(name="Followers", value=data['followers'], inline=True)
			except:pass
			try:e.add_field(name="Location", value=data['location'],inline=True)
			except:pass
			try:e.add_field(name="Joined", value=data['joined'], inline=True)
			except:pass
			await message.channel.send("", embed=e)
			e = discord.Embed()
			e.set_author(name="Bullet",icon_url="https://images.chesscomfiles.com/uploads/v1/images_users/tiny_mce/SamCopeland/phpmeXx6V.png")
			try:e.set_thumbnail(url="https://images.chesscomfiles.com/uploads/v1/chess_term/6d38c776-5832-11ea-b094-69ad1750e029.e5c4f168.5000x5000o.d49d1f49bc53.png")
			except:pass
			try:e.add_field(name="Current", value=data['bullet'][0][0][0], inline=True)
			except:pass
			try:e.add_field(name="Best",value=data['bullet'][0][0][1],inline=False)
			except:pass
			try:e.add_field(name="Wins", value=data['bullet'][0][1][0], inline=True)
			except:pass
			try:e.add_field(name="Loss", value=data['bullet'][0][1][1], inline=True)
			except:pass
			try:e.add_field(name="Draws", value=data['bullet'][0][1][2], inline=True)
			except:pass
			await message.channel.send("", embed=e)
		
			e = discord.Embed()
			e.set_author(name="Blitz",icon_url="https://images.chesscomfiles.com/uploads/v1/images_users/tiny_mce/SamCopeland/phpmeXx6V.png")
			try:e.set_thumbnail(url="https://images.chesscomfiles.com/uploads/v1/chess_term/80febd7c-bcb1-11ea-8ef7-07dbcd6ea7c7.090c6f94.630x354o.46122acf9ffe@2x.png")
			except:pass
			try:e.add_field(name="Current", value=data['blitz'][0][0][0], inline=True)
			except:pass
			try:e.add_field(name="Best",value=data['blitz'][0][0][1],inline=False)
			except:pass
	
			try:e.add_field(name="Wins", value=data['blitz'][0][1][0], inline=True)
			except:pass
			try:e.add_field(name="Loss", value=data['blitz'][0][1][1], inline=True)
			except:pass
			try:e.add_field(name="Draws", value=data['blitz'][0][1][2], inline=True)
			except:pass
			await message.channel.send("", embed=e)

			e = discord.Embed()
			e.set_author(name="Rapid",icon_url="https://images.chesscomfiles.com/uploads/v1/images_users/tiny_mce/SamCopeland/phpmeXx6V.png")
			try:e.set_thumbnail(url="https://arnav17sharma.github.io/assets/share-live.a3b92931.png")
			except:pass
			try:e.add_field(name="Current", value=data['rapid'][0][0][0], inline=True)
			except:pass
			try:e.add_field(name="Best",value=data['rapid'][0][0][1],inline=False)
			except:pass
	
			try:e.add_field(name="Wins", value=data['rapid'][0][1][0], inline=True)
			except:pass
			try:e.add_field(name="Loss", value=data['rapid'][0][1][1], inline=True)
			except:pass
			try:e.add_field(name="Draws", value=data['rapid'][0][1][2], inline=True)
			except:pass
			await message.channel.send("", embed=e)

	brooklyn_99_quotes = ['SANCHIT BOT', 'MUDIT BOT', "No one", "You"]
	# Serious Tips needed!!!
	tips = [['Nahane ja nahane ja!!!', "https://tenor.com/bjPqs.gif"],
			['Chup hoja saatvi fail!!!', "https://tenor.com/brP3j.gif"],
			["https://tenor.com/btb7I.gif", "https://tenor.com/btb7L.gif"],
			["https://tenor.com/bjOY0.gif", "https://tenor.com/buZbD.gif"]]
	if PREFIX + "tip" in message.content.lower():
		lst = message.mentions
		await lst[0].create_dm()
		message = random.choice(tips)
		await lst[0].dm_channel.send(message[0])
		await lst[0].dm_channel.send(message[1])

	if message.content.lower() == PREFIX + 'who_bot':
		response = random.choice(brooklyn_99_quotes)
		if response == "You":
			response = '{0.author.mention} BOT'.format(message)
		await message.channel.send(response)

	if message.content.lower() in ['yo', 'hey', 'hi', 'hello', 'bye',"bye", "nikal", "bhag"]:
		msg = message.content.capitalize() + ' {0.author.mention}'.format(
			message)
		await message.channel.send(msg)

	if message.content.lower() == PREFIX + "wallh":
		horizontal()
		await message.channel.send(
			file=discord.File(f'{path}horizontal/sample3.png'))

	if message.content.lower() == PREFIX + "wallb":
		basic()
		await message.channel.send(file=discord.File(f'{path}basic/demo1.png'))
	
	if message.content.lower() == PREFIX + "watch":
		title,id = watch_tmkoc()
		await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=title+" Write =help or =helpdm", url=f'http://www.youtube.com/watch?v={id}'))
		await message.channel.send(f"Watching **{title}** at http://www.youtube.com/watch?v={id}")

	if message.content.lower() == PREFIX + "new_act":
		# await message.channel.send("DISABLED HAI **GAVAR**")
		new = random.choice(activity_l)
		await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=new))
		msg = "Playing " + new + " !! Write =help or =helpdm"
		await message.channel.send(msg)

	if PREFIX + "jetha1" in message.content.lower():
		j, d, c = message.content[7:].split(",")
		meme1(j, d, c)
		await message.channel.send(file=discord.File(f'{path}/jetha1.jpg'))

	if PREFIX + "note" in message.content.lower():
		j, d, c = message.content[5:].split(",")
		meme2(j, d, c)
		await message.channel.send(file=discord.File(f'{path}/cheating1.jpg'))

	if PREFIX + "befter" in message.content.lower():
		j, d, c = message.content[7:].split(",")
		tall(j, d, c)
		await message.channel.send(file=discord.File(f'{path}/tall.jpg'))

	if PREFIX + "scared" in message.content.lower():
		j, d, c = message.content[7:].split(",")
		scared(j, d, c)
		await message.channel.send(file=discord.File(f'{path}/scared.jpg'))

	if PREFIX + "jetha2" in message.content.lower():
		j, d, c = message.content[7:].split(",")
		jetha2(j, d, c)
		await message.channel.send(file=discord.File(f'{path}/jetha2.jpg'))

	if PREFIX + "brain" in message.content.lower():
		a, j, d, c = message.content[6:].split(",")
		brain(a, j, d, c)
		await message.channel.send(file=discord.File(f'{path}/brain.jpg'))

	# not included
	if PREFIX + "meme1" in message.content.lower():
		lst = message.mentions
		meme3(lst[0].avatar_url, lst[1].avatar_url)
		await message.channel.send(file=discord.File(f'{path}/meme3.jpeg'))


	if PREFIX + "trigger" in message.content.lower():
		lst = message.mentions
		print(lst)
		if len(lst) != 0:
			for i in lst:
				triggered(i.avatar_url)
				await message.channel.send(file=discord.File("triggered.gif"))
				# await message.channel.send(file=discord.File("user.jpg"))

		else:
			triggered(message.author.avatar_url)
			await message.channel.send(file=discord.File("triggered.gif"))
			# await message.channel.send(file=discord.File("user.jpg"))

	if PREFIX + "avatar" in message.content.lower():
		lst = message.mentions
		print(lst)
		if len(lst) != 0:
			for i in lst:
				await message.channel.send("{}".format(i.avatar_url))
		else:
			await message.channel.send("{}".format(message.author.avatar_url))

	if PREFIX + "rip" in message.content.lower():
		lst = message.mentions
		if len(lst) != 0:
			for i in lst:
				rip(i.avatar_url)
				await message.channel.send(file=discord.File("ripped.png"))
		else:
			rip(message.author.avatar_url)
			await message.channel.send(file=discord.File("ripped.png"))

	if message.content.split(" ")[0].lower() == PREFIX + "gif":
		try:
			if message.content.split(" ")[-1].isdigit():
				print(message.content.split(" ")[1:-1])
				url = get_gif("".join(message.content.split(" ")[1:-1]), int(message.content.split(" ")[-1])-1)
			else:
				print(message.content.split(" ")[1:])
				url = get_gif("".join(message.content.split(" ")[1:]).lower())
			if url != None:
				sent = await message.channel.send("{}".format(url))
				await sent.add_reaction("\U0001F916")
				await sent.add_reaction("\U0001f44d")
				print("REACTED!!")
			else:
				await message.channel.send("**NOT FOUND**")
		except:
			await message.channel.send("**NOT FOUND**")

	if message.content.split(" ")[0].lower() == PREFIX + "meme":
		desc,link = get_meme()
		while link[-4:] not in ['.png', '.jpg']:
			print("Failed!")
			desc,link = get_meme()
		e=discord.Embed(title=desc)
		e.set_image(url=link)
		await message.channel.send(embed=e)

	if message.content.lower().split(" ")[0] == PREFIX + "poll":
		reactions = {
			' :red_square: ': "\U0001F7E5",
			' :orange_square: ': "\U0001F7E7",
			' :yellow_square: ': "\U0001F7E8",
			' :green_square: ': "\U0001F7E9"
		}
		op = [
			' :red_square: ',
			' :orange_square: ',
			' :yellow_square: ',
			' :green_square: '
		]
		lst = [];d = ""
		j = 1
		for i in message.content:
			if ord(i)==34:
				j+=1
			if j%2:
				lst.append(d)
				d = ""
			else:
				d+=i
		l = []
		for i in lst:
			if i:l.append(i.strip("\""))
		lst = []
		lst = l[:]
		if 5 >= len(lst) >= 3:
			q = lst[0]
			options = lst[1:]
			embed=discord.Embed(title=lst[0], description=f"Poll by {message.author.mention}", color=0x00e1ff)
			embed.set_author(name=f"{message.author.name}", icon_url=f"{message.author.avatar_url}")
			for j in range(len(lst[1:])):
				embed.add_field(name="{:^10}".format("------"), value=f"{lst[1:][j]} - {op[j]}", inline=False)
			embed.set_footer(text="React below to vote!")
			mess = await message.channel.send(embed=embed)
			a = 0
			react_me = []
			for i in range(len(lst[1:])):
				a += 1
				react_me.append(reactions[op[i]])
				if a == len(options):
					for i in react_me:
						await mess.add_reaction(i)
					break
		else:
			await message.channel.send('**Please check command (Min 2 options Max 4 options)**')

	if message.content.lower().split(" ")[0] == PREFIX + "help":
		embed=discord.Embed(title="Arnav's Bot Help", description="This is a list of all the commands available in me!", color=0x00d9ff)
		embed.add_field(name="=yt {search_word(s)}", value="Returns the first result for searched word(s). Example : `=yt discord bot`", inline=True)
		embed.add_field(name="=ss {website_url}", value="Returns a screenshot of the website url. Example : `=ss google.com`", inline=True)
		embed.add_field(name="=chess {username}", value="Returns chess.com profile info for the username. Example : `=chess viditchess`", inline=True)
		embed.add_field(name="=wallh", value="Returns a randomly generated Horizontal wallpaper for you!", inline=True)
		embed.add_field(name="=wallb", value="Returns a randomly generated Basic wallpaper for you!", inline=True)
		embed.add_field(name="=watch", value="Make my watch a TMKOC Video!", inline=True)
		embed.add_field(name="=new_act", value="Changes my activity randomly!", inline=True)
		embed.add_field(name="=avatar user_mention", value="Sends the avatar image for any user. Example : `=avatar @ME`", inline=True)
		embed.add_field(name="=rip user_mention", value="RIP for the user mentioned. Check it out! `=rip @ME`", inline=True)
		embed.add_field(name="=gif {search_word(s)} {number}", value="Sends a gif from tenor for the word . The number is optional and should be used to see the next result for the search word in tenor (till 10). Example : `=gif jethalal` `=gif jethalal 2`", inline=True)
		embed.add_field(name="=meme", value="Sends a meme from reddit.", inline=True)
		embed.add_field(name="=poll \"Question\" \"Option1\" \"Option2\" \"Option3\" \"Option4\"", value="Creates a poll for a Question . Atleat 2 options required and max options can be 4. Example : `=poll \"Who will IPL 2021?\" \"CSK\" \"MI\" \"RCB\" \"DC\"`", inline=True)
		embed.add_field(name="=tip user_mention", value="Dms a tip to the user!", inline=True)
		embed.add_field(name="=jetha1 a , b, c ,d", value="Check it out and type anything in place of a, b, c, d! . Example : `=jetha1 a , b, c ,d`", inline=True)
		embed.add_field(name="=jetha2 a, b, c", value="Check it out and put thing in place of a, b, c! . Example : `=jetha a , b, c`", inline=True)
		embed.add_field(name="=befter a, b, c", value="Check it out and put thing in place of a, b, c! . Example : `=befter a , b, c`", inline=True)
		embed.add_field(name="=scared a, b, c", value="Check it out and put thing in place of a, b, c! . Example : `=scared a , b, c`", inline=True)
		embed.add_field(name="=note a, b, c", value="Check it out and put thing in place of a, b, c! . Example : `=note a , b, c`", inline=True)
		embed.add_field(name="=brain a, b, c, d", value="Check it out and put thing in place of a, b, c, d! . Example : `=brain a , b, c , d`", inline=True)
		embed.add_field(name="=meme1 user1_mention user2_mention", value="Check it out and put thing in place of a, b! . Example : `=meme1 @a @d`", inline=True)
		embed.add_field(name="=trigger user_mention", value="Sends a gif for the triggered user avatar!. Example : `=trigger @user`", inline=True)
		await message.channel.send(embed=embed)

	if message.content.lower().split(" ")[0] == PREFIX + "helpdm":
		await message.author.create_dm()
		embed=discord.Embed(title="Arnav's Bot Help", description="This is a list of all the commands available in me!", color=0x00d9ff)
		embed.add_field(name="=yt {search_word(s)}", value="Returns the first result for searched word(s). Example : `=yt discord bot`", inline=True)
		embed.add_field(name="=ss {website_url}", value="Returns a screenshot of the website url. Example : `=ss google.com`", inline=True)
		embed.add_field(name="=chess {username}", value="Returns chess.com profile info for the username. Example : `=chess viditchess`", inline=True)
		embed.add_field(name="=wallh", value="Returns a randomly generated Horizontal wallpaper for you!", inline=True)
		embed.add_field(name="=wallb", value="Returns a randomly generated Basic wallpaper for you!", inline=True)
		embed.add_field(name="=watch", value="Make my watch a TMKOC Video!", inline=True)
		embed.add_field(name="=new_act", value="Changes my activity randomly!", inline=True)
		embed.add_field(name="=avatar user_mention", value="Sends the avatar image for any user. Example : `=avatar @ME`", inline=True)
		embed.add_field(name="=rip user_mention", value="RIP for the user mentioned. Check it out! `=rip @ME`", inline=True)
		embed.add_field(name="=gif {search_word(s)} {number}", value="Sends a gif from tenor for the word . The number is optional and should be used to see the next result for the search word in tenor (till 10). Example : `=gif jethalal` `=gif jethalal 2`", inline=True)
		embed.add_field(name="=meme", value="Sends a meme from reddit.", inline=True)
		embed.add_field(name="=poll \"Question\" \"Option1\" \"Option2\" \"Option3\" \"Option4\"", value="Creates a poll for a Question . Atleat 2 options required and max options can be 4. Example : `=poll \"Who will IPL 2021?\" \"CSK\" \"MI\" \"RCB\" \"DC\"`", inline=True)
		embed.add_field(name="=tip user_mention", value="Dms a tip to the user!", inline=True)
		embed.add_field(name="=jetha1 a , b, c ,d", value="Check it out and type anything in place of a, b, c, d! . Example : `=jetha1 a , b, c ,d`", inline=True)
		embed.add_field(name="=jetha2 a, b, c", value="Check it out and put thing in place of a, b, c! . Example : `=jetha a , b, c`", inline=True)
		embed.add_field(name="=befter a, b, c", value="Check it out and put thing in place of a, b, c! . Example : `=befter a , b, c`", inline=True)
		embed.add_field(name="=scared a, b, c", value="Check it out and put thing in place of a, b, c! . Example : `=scared a , b, c`", inline=True)
		embed.add_field(name="=note a, b, c", value="Check it out and put thing in place of a, b, c! . Example : `=note a , b, c`", inline=True)
		embed.add_field(name="=brain a, b, c, d", value="Check it out and put thing in place of a, b, c, d! . Example : `=brain a , b, c , d`", inline=True)
		embed.add_field(name="=meme1 user1_mention user2_mention", value="Check it out and put thing in place of a, b! . Example : `=meme1 @a @d`", inline=True)
		embed.add_field(name="=trigger user_mention", value="Sends a gif for the triggered user avatar!. Example : `=trigger @user`", inline=True)
		await message.author.dm_channel.send(embed=embed)
		await message.channel.send(f"{message.author.mention} check your dms")

'''

# @bot.command(name='stat')
# async def stats(ctx):
# 	with open("mssg_stats.txt", "r") as file:
# 		lines = file.readlines()
# 		user = ctx.message.author
# 		for line in lines:
# 			words = line.split(",")
# 			sender = words[0]
# 			print(sender+" " + str(user.id))
# 			if str(user.id) == sender:
# 				mssgs = len(words) - 1
# 				print(mssgs)
# 				await ctx.send("{} has {} messages.".format(user.mention, mssgs))
	
					
		
# 	fakes = ["ARNAB", "ORNAV", "ORNAB", "ARNOV", "ARNOB", "ORNOB", "ORNOV", "Ornev"]
# 	cwords = ["BSDK", "BOT AADMI", "BISI", "CHUMTIYE"]
# 	cword = random.choice(cwords)
# 	for fake in fakes:
# 		if fake.lower() in msg.content.lower() and str(msg.author)[-5:]!="#9054":
# 			await msg.channel.send(f"**ARNAV** HOTA HAI {cword}")
# keep_alive()"

# client.run(TOKEN)
try:
	keep_alive()
	bot.run(os.environ['TOKEN1'])
	# bot.run(TOKEN)
except:
	os.system("kill 1")
	keep_alive()
	bot.run(os.environ['TOKEN1'])
	# bot.run(TOKEN)
# [<Member id=755756692037435473 name="Arnav's Bot" discriminator='6172' bot=True nick=None guild=<Guild id=778598124976341033
# name='ARNAV17SHARMA' shard_id=None chunked=False member_count=3>>]


# req
# aiohttp==3.6.2
# async-timeout==3.0.1
# attrs==20.2.0
# chardet==3.0.4
# discord==1.0.1
# discord.py==1.4.1
# idna==2.10
# multidict==4.7.6
# python-dotenv==0.14.0
# typing-extensions==3.7.4.3
# yarl==1.5.1
# Pillow==7.1.2
# requests==2.23.0
# PyNaCl==1.3.0
# youtube-dl==2020.12.9
# pytube==10.0.0

# toml
# [tool.poetry]
# name = "discordbot"
# version = "0.1.0"
# description = ""
# authors = ["Your Name <you@example.com>"]

# [tool.poetry.dependencies]
# python = "^3.8"
# discord = "^1.0.1"
# pytube = "^10.5.1"
# flask = "^1.1.2"
# telegram = "^0.0.1"
# bs4 = "^0.0.1"
# lxml = "^4.6.2"
# pycairo = "^1.20.0"
# pandas = "^1.2.4"
# python-chess = "^1.999"
# PyNaCl = "^1.5.0"
# pytube3 = "^9.6.4"
# youtube_dl = "^2021.12.17"

# [tool.poetry.dev-dependencies]

# [build-system]
# requires = ["poetry>=0.12"]
# build-backend = "poetry.masonry.api"
