from mutagen.mp3 import MP3
from pydub import AudioSegment

def get_audio_length(audio_index):
    audio = MP3(f"./video_speech/{audio_index}.mp3")
    return audio.info.length + 1

def combine_audio(audios):
    combined = AudioSegment.empty()
    # audios are are file paths to audio files 
    for audio in audios:
        # add one second of silence to the beginning of each audio file
        combined += AudioSegment.from_mp3(audio)
        combined += AudioSegment.silent(duration=1000)
    combined.export("./video_speech/final.mp3", format="mp3")



if __name__ == '__main__': 
    # get_audio_length()
    combine_audio(["./video_speech/0.mp3", "./video_speech/1.mp3"])