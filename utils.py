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

def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 *
                                                     (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()


def getSpeechLengths(script):
    speechLengths = []
    for i in range(len(script)):
        speechLengths.append(get_audio_length(i))
    return speechLengths


def deleteallcontentfromfolder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))