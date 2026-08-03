# converts the videos in mp3
import whisper
import os
import subprocess

files=os.listdir("videos")
for file in files:
    # print(file)
    file_name=file.split(".webm")[0]
    # Separate tutorial number
    tutorial_num=file_name.split("#")[1]
    # separate the file name
    title=file_name.split(" - ")[1]
    title=title.split(" ｜")[0]
    print(tutorial_num,title)
    subprocess.run(["ffmpeg","-i",f"videos/{file}",f"audio/{tutorial_num}_{title}.mp3"])


