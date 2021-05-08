from PIL import Image, ImageDraw, ImageFont
import requests


def rip(url):
	im1 = Image.open('./assets/rip.jpg')
	response = requests.get(url)

	file = open("rip.jpg", "wb")
	file.write(response.content)
	file.close()
	im2 = Image.open("rip.jpg")
	im2 = im2.resize((400, 400))
	im1.paste(im2, (300, 850))
	im1.save('ripped.png', quality=95)

# rip("https://cdn.discordapp.com/attachments/780329622654156802/780493026124234803/board.png")


def meme1(jetha, daya, cylinder):
	im1 = Image.open('./assets/meme1.jpg')
	draw = ImageDraw.Draw(im1)
	font = ImageFont.truetype(r'./SpaceMono-Bold.ttf', 25)
	draw.text((100, 300), jetha, (0, 0, 0), font=font)
	draw.text((380, 20), daya, (0, 0, 0), font=font)
	draw.text((360, 140), cylinder, (0, 0, 0), font=font)
	im1.save("jetha1.jpg")


def meme2(sender, reciever, message):
	im1 = Image.open('./assets/cheating1.jpeg')
	draw = ImageDraw.Draw(im1)
	font = ImageFont.truetype(r'./SpaceMono-Bold.ttf', 25)
	draw.text((50, 5), sender, (0, 0, 0), font=font)
	draw.text((300, 20), reciever, (0, 0, 0), font=font)
	draw.text((300, 340), message, (0, 0, 0), font=font)
	im1.save("cheating1.jpg")


def scared(daya, jetha, about):
	im1 = Image.open('./assets/scared.jpg')
	draw = ImageDraw.Draw(im1)
	font = ImageFont.truetype(r'./SpaceMono-Bold.ttf', 30)
	draw.text((150, 600), jetha, (0, 0, 0), font=font)
	draw.text((80, 120), daya, (255, 255, 255), font=font)
	draw.text((320, 515), about, (255, 255, 255), font=font)
	im1.save("scared.jpg")


def tall(tapu, jetha, cond):
	im1 = Image.open('./assets/tall.jpeg')
	draw = ImageDraw.Draw(im1)
	font = ImageFont.truetype(r'./SpaceMono-Bold.ttf', 22)
	draw.text((250, 10), jetha, (255, 255, 255), font=font)
	draw.text((80, 120), tapu, (255, 255, 255), font=font)

	draw.text((80, 460), jetha, (0, 0, 0), font=font)
	draw.text((280, 450), tapu, (0, 0, 0), font=font)

	draw.text((5, 220), "Before "+cond, (0, 0, 0), font=font)
	draw.text((5, 260), "After "+cond, (0, 0, 0), font=font)
	im1.save("tall.jpg")


def jetha2(iyer, jetha, about):
	im1 = Image.open('./assets/jetha2.jpeg')
	draw = ImageDraw.Draw(im1)
	font = ImageFont.truetype(r'./SpaceMono-Bold.ttf', 30)
	draw.text((410, 100), jetha, (0, 0, 0), font=font)
	draw.text((80, 60), iyer, (255, 255, 255), font=font)
	draw.text((120, 415), about, (0, 0, 0), font=font)
	im1.save("jetha2.jpg")


def brain(f, s, t, h):
	im1 = Image.open('./assets/brain.jpeg')
	draw = ImageDraw.Draw(im1)
	font = ImageFont.truetype(r'./SpaceMono-Bold.ttf', 30)
	draw.text((20, 50), f, (0, 0, 0), font=font)
	draw.text((20, 200), s, (0, 0, 0), font=font)
	draw.text((20, 350), t, (0, 0, 0), font=font)
	draw.text((20, 500), h, (0, 0, 0), font=font)
	im1.save("brain.jpg")


def meme3(url1, url2):
	im1 = Image.open('./assets/meme2.jpeg')
	response1 = requests.get(url1)
	response2 = requests.get(url2)

	file = open("url1.jpeg", "wb")
	file.write(response1.content)
	file.close()

	file = open("url2.jpeg", "wb")
	file.write(response2.content)
	file.close()

	im2 = Image.open("url1.jpeg")
	im2 = im2.resize((125, 125))
	im1.paste(im2, (125, 0))

	im2 = Image.open("url2.jpeg")
	im2 = im2.resize((125, 125))
	im1.paste(im2, (125, 125))

	im1.save('meme3.jpeg', quality=95)


def triggered(url):
	width = 400
	color_2 = (0, 0, 0)
	trig = Image.open("triggered.png")
	trig = trig.resize((400, 100))

	im = Image.new('RGBA', (width, width))

	response = requests.get(url)
	file = open("user.jpg", "wb")
	file.write(response.content);file.close()
	imm = Image.open("user.jpg")
	imm = imm.convert('RGB')
	imm = imm.resize((400,400), Image.ANTIALIAS)
	print(imm.size)

	im1 = imm.copy()

	im2 = im1.crop((0,0,350,350))
	im2 = im2.resize((400,400))
	im2.paste(trig, (0,300))


	im3 = im1.crop((50,50,420,420))
	im3 = im3.resize((400,400))
	im3.paste(trig, (0,300))

	im4 = im1.crop((0,0,310,310))
	im4 = im4.resize((400,400))
	im4.paste(trig, (0,300))

	im5 = im1.crop((150,150,450,450))
	im5 = im5.resize((400,400))
	im5.paste(trig, (0,300))

	im6 = im1.crop((0,0,300,300))
	im6 = im6.resize((400,400))
	im6.paste(trig, (0,300))

	im7 = im1.crop((100,100,450,450))
	im7 = im7.resize((400,400))
	im7.paste(trig, (0,300))

	im.save('./triggered.gif', save_all=True, append_images=[im1,im2,im3, im4, im5, im6, im7], loop=0)
