from __future__ import unicode_literals
import sys
import argparse
import youtube_dl

def extractImages(url):
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        if url == None:
            url = input("ENTER YOUTUBE URL: ")
            link = url
        try:
            ydl.download(link)
        except:
            link = str(url)
            ydl.download([link])


if __name__=="__main__":
    print("OPEN README.MD FOR INSTRUCTIONS")
    a = argparse.ArgumentParser()
    a.add_argument("--pathIn", help="path to video")
    args = a.parse_args()
    if args != None:
        extractImages(args.pathIn)
    else:
        args.pathIn = None
        extractImages(args.pathIn)
