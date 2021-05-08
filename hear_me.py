def yeah(link):
    import pytube
    # SAVE_PATH = "/"
    # link="https://www.youtube.com/watch?v=xWOoBJUqlbI"
    # try:
    #     yt = YouTube(link) 
    # except: 
    #     print("Connection Error")
    # mp4files = yt.filter('mp4')
    # yt.set_filename('play_me') 
    # d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution) 
    # try: 
    #     d_video.download(SAVE_PATH) 
    # except: 
    #     print("Some Error!")
    # print('Task Completed!')
    # link = "https://www.youtube.com/watch?v=mpjREfvZiDs"
    yt = pytube.YouTube(link)
    stream = yt.streams.first()
    stream.download("/")
    print("Saved!")
    return yt.title
# name=yeah("https://www.youtube.com/watch?v=cDqChal4TTE&t=10s")
# print(name+".mp4")