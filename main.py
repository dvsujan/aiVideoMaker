from getimage import getGoogleImage
from conv import generate_script, parse_script
from voice import save_audio_gtts
from Audio import get_audio_length, combine_audio
import cv2
import os
import shutil
import textwrap
from PIL import ImageFont, ImageDraw, Image
import PIL
import time
import numpy as np
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
import os
from utils import printProgressBar, getSpeechLengths, deleteallcontentfromfolder
import argparse
import imutils


parse = argparse.ArgumentParser()
parse.add_argument("-p", "--prompt", required=True,
                   help="prompt for the video")
parse.add_argument("-o", "--output_name", help="output path for the video")
parse.add_argument("-op", "--output_path", help="output path for the video")
args = vars(parse.parse_args())
prompt = args["prompt"]


# UNCOMMENT
deleteallcontentfromfolder('./images')
deleteallcontentfromfolder('./speech')
deleteallcontentfromfolder('./video_speech')
deleteallcontentfromfolder('./tempvids')

OUT_NAME = ''
if args["output_name"] is not None:
    OUT_NAME = args["output_name"]
else:
    OUT_NAME = prompt


VIDEO_PATH = './videos/videoforaimine.mp4'
OUTPUT_VIDEO_PATH = ''
TEMP_VIDEO_PATH = './tempvids/'
VIDEO_OUT = cv2.VideoWriter(
    TEMP_VIDEO_PATH+f'{OUT_NAME}.mp4', -1, 30, (1080, 1920))
# font_path ='./fonts/Roboto/Roboto-Regular.ttf';
font_path = './fonts/Lato/Lato-Bold.ttf'

if args["output_path"] is not None:
    OUTPUT_VIDEO_PATH = args["output_path"]
else:
    OUTPUT_VIDEO_PATH = './finalvids/'


# logo = '''


#  _____  .___  ____   ____.__    .___               ________                                   __
#   /  _  \ |   | \   \ /   /|__| __| _/____  ____    /  _____/  ____   ____   ________________ _/  |_  ___________
#  /  /_\  \|   |  \   Y   / |  |/ __ |/ __ \/  _ \  /   \  ____/ __ \ /    \_/ __ \_  __ \__  \\   __\/  _ \_  __ \
# /    |    \   |   \     /  |  / /_/ \  ___(  <_> ) \    \_\  \  ___/|   |  \  ___/|  | \// __ \|  | (  <_> )  | \/
# \____|__  /___|    \___/   |__\____ |\___  >____/   \______  /\___  >___|  /\___  >__|  (____  /__|  \____/|__|
#         \/                         \/    \/                \/     \/     \/     \/           \/


# '''

logo = '''
            _____  __      ___     _               _____                           _             
     /\   |_   _| \ \    / (_)   | |             / ____|                         | |            
    /  \    | |    \ \  / / _  __| | ___  ___   | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
   / /\ \   | |     \ \/ / | |/ _` |/ _ \/ _ \  | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
  / ____ \ _| |_     \  /  | | (_| |  __/ (_) | | |__| |  __/ | | |  __/ | | (_| | || (_) | |   
 /_/    \_\_____|     \/   |_|\__,_|\___|\___/   \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
                                                                                                
                                                                                                
'''


def main():
    # UNCOMMENT
    script = generate_script(prompt)
    script = script.split('\n')[1:]
    script = "\n".join(script)
    # print(script)
    script = parse_script(script)

    script.insert(0, prompt)

    script.append("Don't Forget To Subscribe")

    # UNCOMMENT
    xx = 0
    for i in script:
        getGoogleImage(i, xx)
        save_audio_gtts(i, xx)
        xx += 1

    audios = []
    for i in range(len(script)):
        audios.append(f"./video_speech/{i}.mp3")

    combine_audio(audios)

    # get the length of each audio file
    speechLengths = getSpeechLengths(script)

    cap = cv2.VideoCapture(VIDEO_PATH)

    printProgressBar(0, len(script), prefix='GeneratingVideo:',
                     suffix='Complete', length=30)
    print(logo)
    while cap.isOpened():
        ret, frame = cap.read()

        # get time in sec
        time = cap.get(cv2.CAP_PROP_POS_MSEC)/1000

        # progress bar based on time and sum of speech lengths

        if time > sum(speechLengths):
            break
        printProgressBar(time, sum(speechLengths),
                         prefix='GeneratingVideo:', suffix='Complete', length=50)
        for i in range(len(speechLengths)):
            if time >= sum(speechLengths[:i]) and time <= sum(speechLengths[:i+1]):
                # add text to frame
                # font = ImageFont.truetype(font_path, 32)
                # font = cv2.FONT_HERSHEY_COMPLEX
                shape = frame.shape

                # palce text in the middle of the frame with custom font using pillow and ans wrap the text

                img_pil = PIL.Image.fromarray(frame)
                draw = ImageDraw.Draw(img_pil)
                font = ImageFont.truetype(font_path, 85)
                margin = 50
                offset = 900

                # palce text in the middle of the frame with custom font using pillow and ans wrap the text
                
                for line in textwrap.wrap(script[i], width=25):
                    draw.text((margin, offset), line, font=font,
                              fill=(255, 255, 255), align="center")
                    # offset += font.getsize(line)[1]
                    # use getbox
                    offset += font.getbbox(line)[3]
                
                frame = np.array(img_pil)
                # add 512x512 image to frame
                img = cv2.imread(f'./images/{i}.jpg')
                # img = cv2.resize(img, (512, 5))
                # resize the image but keep the aspect ratio
                img = imutils.resize(img, width=512, height=min(
                    512, img.shape[0]
                ), inter=cv2.INTER_AREA)

                # place image in middle of frame
                # middle

                x_offset = int(shape[1]/2)-256
                y_offset = int(shape[0]/2)-800
                frame[y_offset:y_offset+img.shape[0],
                      x_offset:x_offset+img.shape[1]] = img

                VIDEO_OUT.write(frame)
                break

        # print(time);

    print("\n\nVideo Generation Done")
    cap.release()
    VIDEO_OUT.release()
    cv2.destroyAllWindows()

    # video_clip = VideoFileClip(TEMP_VIDEO_PATH+f'{prompt}.mp4')
    # audio_clip = AudioFileClip('./video_speech/final.mp3')
    # final_clip = video_clip.set_audio(audio_clip)
    # final_clip.write_videofile(OUTPUT_VIDEO_PATH+f'{prompt}.mp4',)
    print("-------------------path---------------------")
    print(TEMP_VIDEO_PATH+f'{prompt}.mp4')
    print("-------------------path---------------------")

    video = VideoFileClip(TEMP_VIDEO_PATH+f'{prompt}.mp4')

    audio = AudioFileClip('./video_speech/final.mp3')

    final = video.set_audio(audio)

    final.write_videofile(
        OUTPUT_VIDEO_PATH+f'{prompt}.mp4', codec='libx264', audio_codec='aac')


if __name__ == "__main__":
    main()
