# -*- coding: utf-8 -*-

    
import pytube as Y
import os

def DownloadSong(link,folder='./'):
    yt=Y.YouTube(link)
    print(f"\nTittle: {yt.title}\n Author: {yt.author}")
    l=yt.length
    print(f"Length: {l//60}min {l%60}s")

    audio_str=yt.streams.get_audio_only()
    audio_str.download(folder,
                       filename=audio_str.default_filename)
 
        
    return

def Playlist(link):
    p=Y.Playlist(link)
    name=p.title
    try:
        os.mkdir(name)
    except:
        print("La carpeta ya está creada")   
    for song in p.video_urls:
        DownloadSong(song,f'./{name}/')
    


def main():
    try:
        os.mkdir('YT_Downloads')
    except:
        pass
    finally:
        os.chdir('YT_Downloads')
        
    choose=int(input('Type:\n1.Song\n2.Playlist\n:'))
    link=str(input('URL:'))
    if choose==1:
        DownloadSong(link)
    elif choose==2:
        Playlist(link)
    os.chdir('..')
    

    

if __name__=="__main__":
    main()