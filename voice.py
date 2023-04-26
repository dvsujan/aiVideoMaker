from gtts import gTTS
import pyttsx3
import os 

def save_audio_gtts(text,filename):
    language = 'en'
    output = gTTS(text=text, lang=language, slow=False)
    # text = text.replace(" ", "_");
    output.save(f"./speech/{filename}.mp3")
    # speed up the audio
    # path absolute folder
    path_to_this_folder = os.path.abspath(os.path.dirname(__file__))
    print(path_to_this_folder); 
    # text = text.replace(" ", "_"); 
    os.system(f"ffmpeg -i {path_to_this_folder}/speech/{filename}.mp3 -filter:a \"atempo=2\" -vn -y {path_to_this_folder}/video_speech/{filename}.mp3")

def save_autio_pytttsx3(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
    engine.save_to_file(text, f"./speech/{text}.mp3")
    engine.runAndWait()

if __name__ == "__main__":
    save_audio_gtts("Hello my name is sujan and i am a software engineer and i love to build stuff")
    # save_autio_pytttsx3("hello world")

