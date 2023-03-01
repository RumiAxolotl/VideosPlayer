from moviepy.editor import *
import sys
import os




if len(sys.argv) < 2:
    print("Please provide a video file")
    exit()

#Get the file name
video_file_name = sys.argv[1]

#Check if file exists
if not os.path.isfile(video_file_name):
    print(f"Can't find {video_file_name}.")
    exit()

# Create a VideoFileClip object for the video file
video = VideoFileClip(video_file_name)
# Create an AudioFileClip object for the audio file
audio = AudioFileClip(video_file_name)
# Set the audio for the video clip
video = video.set_audio(audio)

# Play the video with sound
video.preview()