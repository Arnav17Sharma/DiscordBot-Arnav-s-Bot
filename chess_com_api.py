import requests
import time

def chess_info(username):
  data = {'status':404}
  profile = f"https://api.chess.com/pub/player/{username}"
  response = requests.get(profile).json()
  try:
    data['name'] = response['name']
  except:pass
  try:
    data['followers'] = response['followers']
    data['status'] = 200
  except:pass
  try:
    data['location'] = response['location']
  except:pass
  try:
    data['photo'] = response['avatar']
  except:pass
  try:
    data['url'] = response['url']
  except:pass
  try:
    data['last_online'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(response['last_online']))
  except:pass
  try:
    data['joined'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(response['joined']))
  except:pass
  try:
    data['username'] = response['username']
  except:pass

  stats = requests.get(profile+"/stats").json()
  try:
    data['rapid']=[[stats['chess_rapid']['last']['rating'], stats['chess_rapid']['best']['rating']], [stats['chess_rapid']['record']['win'], stats['chess_rapid']['record']['loss'], stats['chess_rapid']['record']['draw']]],
  except:pass
  try:
    data['bullet']=[[stats['chess_bullet']['last']['rating'], stats['chess_bullet']['best']['rating']], [stats['chess_bullet']['record']['win'], stats['chess_bullet']['record']['loss'], stats['chess_bullet']['record']['draw']]],
  except:pass
  try:
    data['blitz']=[[stats['chess_blitz']['last']['rating'], stats['chess_blitz']['best']['rating']], [stats['chess_blitz']['record']['win'], stats['chess_blitz']['record']['loss'], stats['chess_blitz']['record']['draw']]],
  except:pass
  try:
    data['fide']=stats['fide'],
  except:pass
  try:
    data['tactics']=[stats['tactics']['highest']['rating'], stats['tactics']['lowest']['rating']],
  except:pass
  try:
    data['rush']= [stats['puzzle_rush']['best']['score'], stats['puzzle_rush']['best']['total_attempts']]
  except:pass

  return data


def puzzle():
	from PIL import Image
	from random import randint
	import pandas as pd

	df = pd.read_csv('./puzzles.csv', nrows=randint(1, 999), dtype=str)

	j = df.to_string().split("\n")[-1]
	puzzle = j.split()

	moves = []
	for k in puzzle[8:]:
		if not k.isdigit():
			moves.append(k)
		else:
			moves.append(k)
			break
	im = Image.open('board.jpg')
	new_im = im.copy()
	FEN = puzzle[2]
	l = FEN.split("/")
	l[-1] = l[-1].split()[0]
	# print(l)
	for j in range(len(l)):
		a = -1 
		for i in l[j]:
			if i.isdigit():
				a+=int(i)
			else:
				a += 1
				if i.isupper():
					piece = Image.open(f'./pieces/WHITE/{i}.png')
				else:
					piece = Image.open(f'./pieces/BLACK/{i}.png')
				new_im.paste(piece, (20 + 66 * (a), 25 + 66 * (j)), piece)

	new_im.save('new_board0.jpg', quality=95)
	# print(puzzle)

	FEN = " ".join(puzzle[2:8])
	FEN1 = FEN
	def board(FEN, moves):
		import chess
		board = chess.Board(FEN)
		im = Image.open('board.jpg')
		for move in range(len(moves)):
			make_move = chess.Move.from_uci(moves[move])
			board.push(make_move)
			print(board)
			new_im = im.copy()
			FEN = board.fen()
			l = FEN.split("/")
			l[-1] = l[-1].split()[0]
			# print(l)
			for j in range(len(l)):
				a = -1 
				for i in l[j]:
					if i.isdigit():
						a+=int(i)
					else:
						a += 1
						if i.isupper():
							piece = Image.open(f'./pieces/WHITE/{i}.png')
						else:
							piece = Image.open(f'./pieces/BLACK/{i}.png')
						new_im.paste(piece, (20 + 66 * (a), 25 + 66 * (j)), piece)
			new_im.save(f'new_board{move+1}.jpg', quality=95)
	board(FEN, moves[:-1])

	l = []
	for i in range(len(moves[:-1])):
		img = Image.open(f'new_board{i+1}.jpg')
		l.append(img)

	# print(l)

	gif = Image.new("RGBA", im.size)
	gif.save(f'solution{puzzle[0]}.gif', save_all=True, append_images=l, optimize=True ,duration=1000, loop=0)

	return [FEN1,moves[-1], puzzle[-1], puzzle[4], moves[:-1], puzzle[0]]
