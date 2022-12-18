def horizontal():
	import random
	import colorsys
	from math import floor
	path = './'

	def hcfnaive(a,b): 
		if(b==0): 
			return a 
		else: 
			return hcfnaive(b,a%b) 

	def color_ran():
		h = random.randint(0, 360)
		s = random.randint(0, 100)#31
		v = random.randint(0, 100)
		print(f'h-{h},s-{s},v-{v}')
		print('\n')

		if v>30 and s<=35: 
			s = random.randint(36,100)
		if v<=30:
			v = random.randint(31,100)
			if s<=35: s = random.randint(36,100)


		print(f'h-{h},s-{s},v-{v}')
		rgb = colorsys.hsv_to_rgb(h/360,s/100,v/100)
		rgb = [floor(i*255) for i in rgb]
		print(rgb)

		return tuple(rgb)

	def coor_ran(hcf):
		x = random.randint(0, hcf)
		return x


	def inc(c):
		if c%200 != 0:
			c+=100
			return(c)
		return(c)


	screen_x = 2536
	screen_y = 1664
	hcf = random.choice([100,200])
	screen_x1 = screen_x - (screen_x%100)
	screen_y1 = screen_y - (screen_y%100)

	screen_x1 = inc(screen_x1)
	screen_y1 = inc(screen_y1)

	from PIL import Image, ImageDraw

	color = color_ran()

	im = Image.new('RGBA', (screen_x1,screen_y1), (0,0,0))
	draw = ImageDraw.Draw(im)

	# hcf = hcfnaive(screen_x, screen_y)
	# if hcf>=100:
	# 	hcf = 200
	print(hcf)

	# def screen(x, hcf):
	# 	if (x//hcf)%2 != 0:
	# 		return (x//hcf)+1
	# 	else:
	# 		return x//hcf

	d = 6 if hcf == 100 else 10

	print(screen_y1//hcf)
	print(screen_x1//hcf)
	y0 = coor_ran(hcf)
	for j in range(screen_y1//hcf):
		for i in range(screen_x1//hcf):
			y = coor_ran(hcf)
			draw.polygon(((i*hcf, j*hcf), (i*hcf,(j*hcf)+y0),((i+1)*hcf,(j*hcf)+y),((i+1)*hcf, j*hcf)), fill=(color[0]-d,color[1]-d,color[2]-d))
			draw.polygon((((i+1)*hcf, (j+1)*hcf), (i*hcf, (j+1)*hcf),(i*hcf,(j*hcf)+y0),((i+1)*hcf,(j*hcf)+y)), fill=(color[0]-(2*d),color[1]-(2*d),color[2]-(2*d)))
			y0 = y
		color = (color[0]-d,color[1]-d,color[2]-d)

		im.save(f'{path}sample3.png')

	# im.crop(((0,0),(0,screen_y),(screen_x,screen_y),(screen_x,0)))
	cropped = im.crop((0,0,screen_x,screen_y))
	cropped.save(f'{path}sample3.png')
	# cropped.show()



path = './'
 
#FOR BASIC IDEA
def basic():
	from PIL import Image, ImageDraw
	import random
 
 
	def coor_ran(j,i):
		x = random.randint((i-1)*(img_size//5)+10, i*(img_size//5))
		y = random.randint((j-1)*(img_size//5)+10, j*(img_size//5))
		print(x,y)
		return (x, y)
 
	def color_ran():
		r = random.randint(0, 255)
		g = random.randint(0, 255)
		b = random.randint(0, 255)
		return [r,g,b]
 

	def draw_fill(j, i, img_size, color):
		if j%2== 0:
			if i%2 != 0:
				draw.polygon((c,(i*(img_size//5),j*(img_size//5)),((i-1)*(img_size//5),j*(img_size//5))), fill=(color[0]+10, color[1]+10, color[2]+10))#1
				draw.polygon((c,(i*(img_size//5),j*(img_size//5)),(i*(img_size//5),(j-1)*img_size//5)), fill=(color[0]+20, color[1]+20, color[2]+20))#2
				draw.polygon((c,((i-1)*(img_size//5),(j-1)*(img_size//5)),(i*(img_size//5),((j-1)*(img_size//5)))), fill=(color[0]+30, color[1]+30, color[2]+30))#3
				draw.polygon((c,((i-1)*(img_size//5),j*(img_size//5)),((i-1)*(img_size//5),(j-1)*(img_size//5))), fill=(color[0]+40, color[1]+40, color[2]+40))#4
			else:
				draw.polygon((c,(i*(img_size//5),j*(img_size//5)),((i-1)*(img_size//5),j*(img_size//5))), fill=(color[0]+10, color[1]+10, color[2]+10))#1
				draw.polygon((c,(i*(img_size//5),j*(img_size//5)),(i*(img_size//5),(j-1)*img_size//5)), fill=(color[0]+40, color[1]+40, color[2]+40))#2
				draw.polygon((c,((i-1)*(img_size//5),(j-1)*(img_size//5)),(i*(img_size//5),((j-1)*(img_size//5)))), fill=(color[0]+30, color[1]+30, color[2]+30))#3
				draw.polygon((c,((i-1)*(img_size//5),j*(img_size//5)),((i-1)*(img_size//5),(j-1)*(img_size//5))), fill=(color[0]+20, color[1]+20, color[2]+20))#4
		else:
			if i % 2 != 0:
				draw.polygon((c,(i*(img_size//5),j*(img_size//5)),((i-1)*(img_size//5),j*(img_size//5))), fill=(color[0]+30, color[1]+30, color[2]+30))#1
				draw.polygon((c,(i*(img_size//5),j*(img_size//5)),(i*(img_size//5),(j-1)*img_size//5)), fill=(color[0]+20, color[1]+20, color[2]+20))#2
				draw.polygon((c,((i-1)*(img_size//5),(j-1)*(img_size//5)),(i*(img_size//5),((j-1)*(img_size//5)))), fill=(color[0]+10, color[1]+10, color[2]+10))#3
				draw.polygon((c,((i-1)*(img_size//5),j*(img_size//5)),((i-1)*(img_size//5),(j-1)*(img_size//5))), fill=(color[0]+40, color[1]+40, color[2]+40))#4
			else:
				draw.polygon((c,(i*(img_size//5),j*(img_size//5)),((i-1)*(img_size//5),j*(img_size//5))), fill=(color[0]+10, color[1]+10, color[2]+10))#1
				draw.polygon((c,(i*(img_size//5),j*(img_size//5)),(i*(img_size//5),(j-1)*img_size//5)), fill=(color[0]+40, color[1]+40, color[2]+40))#2
				draw.polygon((c,((i-1)*(img_size//5),(j-1)*(img_size//5)),(i*(img_size//5),((j-1)*(img_size//5)))), fill=(color[0]+30, color[1]+30, color[2]+30))#3
				draw.polygon((c,((i-1)*(img_size//5),j*(img_size//5)),((i-1)*(img_size//5),(j-1)*(img_size//5))), fill=(color[0]+20, color[1]+20, color[2]+20))#4
 
 
 
	color = color_ran()
 
 
 

	img_sizex = 400
	img_sizey = 240
	img_size = img_sizex if img_sizex>img_sizey else img_sizey
	img_size = 1536


	im = Image.new('RGB', (img_size, img_size), (0,0,0))
	draw = ImageDraw.Draw(im)
 
	for j in range(1, (img_size//(img_size//5))+1):
		for i in range(1, (img_size//(img_size//5))+1):
			c = coor_ran(j,i)
			draw_fill(j, i, img_size, color)
			im.save(f'{path}/basic/demo1.png', quality=95)
 
def get_gif(word, u=0):
    # set the apikey and limit
	import requests
	apikey = "UFNJ3FSAJWCK"  # test value
	lmt = 10
	import json
	# our test search
	search_term = word

	# get the top 8 GIFs for the search term
	r = requests.get(
		"https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, apikey, lmt))

	if r.status_code == 200:
		# load the GIFs using the urls for the smaller GIF sizes
		top_8gifs = json.loads(r.content)
		return top_8gifs['results'][u]['url']
	else:
		top_8gifs = None


import os

def get_meme():
	CLIENT = os.getenv("CLIENT")
	SECRET = os.getenv("SECRET")

	import requests

	auth = requests.auth.HTTPBasicAuth(CLIENT, SECRET)

	data = {
		'grant_type': 'password',
		'username' : "Arnav17Sharma",
		'password' : os.getenv("PASS")
	}

	headers = {'User-Agent' : 'MyAPI/0.0.1'}
	import random
	access_token = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers).json()['access_token']
	headers = {**headers, **{'Authorization': f'bearer {access_token}'}}
	sub = random.choice(["indiandankvideos"]) # JEEMemes
	response = requests.get(f'https://oauth.reddit.com/r/{sub}/random', headers=headers).json()

	# print(response)
	print(response[0]['data']['children'][0]['data']['is_video'])
	# lst = "/".join(lst.split("?")[:-1])+"/audio"
	print(response[0]['data']['children'][0])
	link = f"https://www.reddit.com"+response[0]['data']['children'][0]['data']['permalink']
	if not response[0]['data']['children'][0]['data']['is_video']:
		get_meme()
	id = response[0]['data']['children'][0]['data']['id']
	lst = response[0]['data']['children'][0]['data']['media']['reddit_video']['fallback_url']
	return ([response[0]['data']['children'][0]['data']['title'], link, lst, id])

def watch_tmkoc():
	import requests
	from random import choice

	words = ["Jethalal", "Daya TMKOC", "Tapu TMKOC", "Taarak Mehta ka Ooltah chashma", "TMKOC", "TMKOC OLD", "TMKOC LATEST","BABITA TMKOC","POPATLAL", "BHIDE"]

	word = choice(words)

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
		'maxResults': 40
	}

	r = requests.get(video_url, params=video_params)

	# print()
	results = r.json()['items']

	video = choice(results)

	print(video['snippet']['title'])
	print(video['id'])
	return [video['snippet']['title'], video['id']]