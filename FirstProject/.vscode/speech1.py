# pip install pyttsx3 pypiwin32
import pyttsx3

# One time initialization
engine = pyttsx3.init()

voices = engine.getProperty('voices')
for voice in voices:
    print("Voice:")
    print(" - ID: %s" % voice.id)
    print(" - Name: %s" % voice.name)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)

# Set properties _before_ you add things to say
engine.setProperty('rate', 170)    # Speed percent (can go over 100)
engine.setProperty('volume', 0.9)  # Volume 0-1

# Voice IDs pulled from engine.getProperty('voices')
# These will be system specific // Kathy
en_voice_id = "com.apple.speech.synthesis.voice.karen"
# Use female English voice
engine.setProperty('voice', en_voice_id)

# Queue up things to say.
# There will be a short break between each one
# when spoken, like a pause between sentences.
engine.say("Hello Ronav!")
engine.say("How are you doing today? Have you finished your Kumon?")

# Flush the say() queue and play the audio
engine.runAndWait()

# Program will not continue execution until
# all speech is done talking