from pytube import YouTube
import os
from pathlib import Path
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--path", type=str, default="/Input_Data/video2.mp4", help="path to save video")
args = vars(ap.parse_args()) 

link = input("Enter Link")
url = YouTube(link)
print("downloading....")
video = url.streams.get_highest_resolution()
video.download(args['path'])
print("Downloaded! :)")