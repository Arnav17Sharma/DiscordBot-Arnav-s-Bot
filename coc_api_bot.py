import requests

headers = {
    'Accept': 'application/json',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjY3YWNhMGU2LTBjNTItNGNiZS04MTNhLWViNGQxOTYxMDVjZSIsImlhdCI6MTY0NjM5NTY5Mywic3ViIjoiZGV2ZWxvcGVyL2QzMWM0ZGZhLWIwNTMtOTU4Yy1mZWUzLWM4NjliYTc2ZTgzMyIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjM0LjgyLjE1Ny43NyJdLCJ0eXBlIjoiY2xpZW50In1dfQ.UCeGei3xPyDieNU4O9zxoWJwoGZNdtOOGYrD0nGwYxrDsigHtrKVhFjBK49XUL4YBD9aJ24ETWJBxUSJqiPELw'
}


def get_clan():
	response = requests.get(f'https://api.clashofclans.com/v1/clans/%232Q0PGLUPY', headers=headers)
	demo = response.json();print(demo)
	return demo

def get_player(player_tag):
	if player_tag[0] == "#":
		player_tag = player_tag[1:]
	response = requests.get(f'https://api.clashofclans.com/v1/players/%23{player_tag}', headers=headers)
	demo = response.json();print(demo)
	return demo