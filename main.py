import os, random, requests, pytube, bs4, time
import discord
from discord.ext import commands, tasks
from data import horizontal, basic, get_gif, get_meme, watch_tmkoc
from utils import rip, meme1, meme2, jetha2, scared, tall, brain, meme3, triggered
from hear_me import yeah
from get_token import get_token
from alive import keep_alive
from chess_com_api import chess_info, puzzle
from wiki_info import wiki
from PIL import Image


TOKEN = # No token ¯\_(ツ)_/¯
# 757215855476998165
# client = discord.Client()
bot = commands.Bot(command_prefix='=')
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
	except:return 0
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


activity_l = ["SANCHIT'S GAUDNESS!!", "MUDIT'S BOTNESS!!", "MANAAAAAN's NUBNESS!!", "TANISHQ's KING SACRIFICE!!", "SARTHAK's FIELDING!!","AKSHAJ's SPAMMING SKILLS!!"]


# @client.event
# async def on_ready():
# 	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="=help or =helpdm"))
# 	print(f'{client.user.name} has connected to Discord!')

@bot.event
async def on_ready():
	print(f'Logged in as {bot.user.name}')
	activity = discord.Game(name="Listening to =help or =helpdm", type=3)
	await bot.change_presence(status=discord.Status.idle, activity=activity)

# @client.event
# async def on_member_join(member):
# 	await member.create_dm()
# 	await member.dm_channel.send(
# 		f'Hi {member.name}, welcome to our Discord server!')


vc = False
players = {}


# @bot.command(name='epic', help='I AM A GOD')
# async def epic(ctx):
# 	await ctx.send('THIS IS EPICNESS!')


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
	if data:await ctx.send(data)
	else:await ctx.send(f"NOTHING FOUND")


@bot.command(name='ss')
async def get_ss(ctx, arg):
	q = arg
	if q.startswith('https://'):
		url=f'https://shot.screenshotapi.net/screenshot?&url={q}&full_page=true&output=image&file_type=png&block_ads=true&no_cookie_banners=true&retina=true&block_tracking=true'
	else:
		url=f'https://shot.screenshotapi.net/screenshot?&url=https://{q}&full_page=true&output=image&file_type=png&block_ads=true&no_cookie_banners=true&retina=true&block_tracking=true'
	im = Image.open(requests.get(url, stream=True).raw)
	im.save("ss.png")
	print(url)
	await ctx.send(file=discord.File('ss.png'))

@bot.command(name='puzzle')
async def get_puzzle(ctx):
	data = puzzle()
	print(data)
	play = data[0].split()[-5]
	if play.lower() == "w":play="Black to play!"
	else:play="White to play!"
	e = discord.Embed(title = f"Puzzle for {ctx.author.name}", description=play)
	file = discord.File("new_board1.jpg", filename="new_board1.jpg")
	e.set_image(url="attachment://new_board1.jpg")
	e.set_footer(text="Puzzle link : "+data[2]+f"\nPuzzle Rating : {data[1]}\tPuzzle ID : {data[-1]}")
	await ctx.send(file=file, embed=e)
	import time
	now = time.time()
	while int(time.time()-now) <= 20:
		pass# print(int(time.time()-now))pass
	else:await ctx.send("Solution for the puzzle", file=discord.File(f'solution{data[-1]}.gif'))
	os.remove(f'solution{data[-1]}.gif')
	os.remove('new_board0.jpg')
	for i in range(len(data[-2])):
		os.remove(f'new_board{i+1}.jpg')

@bot.command(name='chess')
async def get_chess(ctx, *args):
	username = "".join(args)
	data = chess_info(username)
	if data['status'] != 200:
		await ctx.send(f"No player with username as {username} available.")
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
		await ctx.send("", embed=e)
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
		await ctx.send("", embed=e)
	
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
		await ctx.send("", embed=e)

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
	title,id = watch_tmkoc()
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=title+" Write =help or =helpdm", url=f'http://www.youtube.com/watch?v={id}'))
	await ctx.send(f"Watching **{title}** at http://www.youtube.com/watch?v={id}")

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
			triggered(i.avatar_url)
			await ctx.send(file=discord.File("triggered.gif"))
			# await ctx.send(file=discord.File("user.jpg"))
	else:
		triggered(ctx.author.avatar_url)
		await ctx.send(file=discord.File("triggered.gif"))
		# await ctx.send(file=discord.File("user.jpg"))



@bot.command(name='avatar')
async def get_avatar(ctx, *args):
	lst = ctx.message.mentions
	print(lst)
	if len(lst) != 0:
		for i in lst:
			await ctx.send("{}".format(i.avatar_url))
	else:
		await ctx.send("{}".format(ctx.author.avatar_url))

@bot.command(name='rip')
async def get_rip(ctx):
	lst = ctx.message.mentions
	if len(lst) != 0:
		for i in lst:
			rip(i.avatar_url)
			await ctx.send(file=discord.File("ripped.png"))
	else:
		rip(ctx.author.avatar_url)
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

@bot.command(name='meme')
async def get_meme2(ctx):
	desc,link = get_meme()
	while link[-4:] not in ['.png', '.jpg']:
		print("Failed!")
		desc,link = get_meme()
	e=discord.Embed(title=desc)
	e.set_image(url=link)
	await ctx.send(embed=e)

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
	lst = [];d = ""
	j = 1
	q = args[0]
	options = lst[1:]
	embed=discord.Embed(title=args[0], description=f"Poll by {ctx.author.mention}", color=0x00e1ff)
	embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
	for j in range(len(args[1:])):
		embed.add_field(name="{:^10}".format("------"), value=f"{args[1:][j]} - {op[j]}", inline=False)
	embed.set_footer(text="React below to vote!")
	mess = await ctx.send(embed=embed)
	a = 0
	react_me = []
	for i in range(len(args[1:])):
		await mess.add_reaction(reactions[op[i]])

@bot.command(name='help')
async def get_helpme(ctx):
	embed=discord.Embed(title="Arnav's Bot Help", description="This is a list of all the commands available in me!", color=0x00d9ff)
	embed.add_field(name="=yt {search_word(s)}", value="Returns the first result for searched word(s). Example : `=yt discord bot`", inline=True)
	embed.add_field(name="=ss {website_url}", value="Returns a screenshot of the website url. Example : `=ss google.com`", inline=True)
	embed.add_field(name="=puzzle", value="Returns lichess chess puzzle. Example : `=puzzle`", inline=True)
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
	await ctx.send(embed=embed)

@bot.command(name='helpdm')
async def get_helpdm(ctx):
	await ctx.author.create_dm()
	embed=discord.Embed(title="Arnav's Bot Help", description="This is a list of all the commands available in me!", color=0x00d9ff)
	embed.add_field(name="=yt {search_word(s)}", value="Returns the first result for searched word(s). Example : `=yt discord bot`", inline=True)
	embed.add_field(name="=ss {website_url}", value="Returns a screenshot of the website url. Example : `=ss google.com`", inline=True)
	embed.add_field(name="=chess {username}", value="Returns chess.com profile info for the username. Example : `=chess viditchess`", inline=True)
	embed.add_field(name="=puzzle", value="Returns lichess chess puzzle. Example : `=puzzle`", inline=True)
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
keep_alive()
# client.run(TOKEN)
bot.run(TOKEN)
# [<Member id=755756692037435473 name="Arnav's Bot" discriminator='6172' bot=True nick=None guild=<Guild id=778598124976341033
# name='ARNAV17SHARMA' shard_id=None chunked=False member_count=3>>]