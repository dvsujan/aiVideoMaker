from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
import os

TEMP_VIDEO_PATH = './tempvids/'
prompt = "fun facts about cars";        
video = VideoFileClip(TEMP_VIDEO_PATH+f'{prompt}.mp4')
audio = AudioFileClip("./video_speech/final.mp3")

final = video.set_audio(audio)

final.write_videofile("./finalvids/fun facts about cars.mp4" , codec='libx264', audio_codec='aac' )