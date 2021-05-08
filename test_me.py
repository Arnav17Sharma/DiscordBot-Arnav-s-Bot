# set the apikey and limit
import requests
# apikey = "UFNJ3FSAJWCK"  # test value
# lmt = 8
# import json
# # our test search
# search_term = "jethalal"

# # get the top 8 GIFs for the search term
# r = requests.get(
#     "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, apikey, lmt))

# if r.status_code == 200:
#     # load the GIFs using the urls for the smaller GIF sizes
#     top_8gifs = json.loads(r.content)
#     print(top_8gifs['results'][0]['url'])
# else:
#     top_8gifs = None


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
    return f'https://www.youtube.com/watch?v={results[0]["id"]}'
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


mess = "kuch bhi"
mess = mess.split(" ")
print(search_my_word(''.join(mess)))
