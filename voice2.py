import pyttsx3

text = '''
1. Cats are carnivorous and need to eat animal-based foods.
2. Cats have sharp teeth which help them chew meat easily.
3. Cats like warmth so their body temperature is around 40 °C (104 °F).
4. They have 32 muscles in a single whisker.
5. A cat’s hearing range covers up to 8 octaves higher than a human’s hearing.
'''

# import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
engine.save_to_file(text, 'output.mp3')
engine.runAndWait()