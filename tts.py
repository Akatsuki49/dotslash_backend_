import os
from dotenv import load_dotenv

from deepgram import (
    DeepgramClient,
    SpeakOptions,
)

def tts1(resp):
    load_dotenv()
    SPEAK_OPTIONS = {"text": resp}
    filename = "output.wav"
    deepgram = DeepgramClient(api_key='135b47d20ff4581e9581149b1ad38eb65e12ddd7')
    options = SpeakOptions(
        model="aura-orpheus-en",
        encoding="linear16",
        container="wav"
    )
    speech = deepgram.speak.v("1").save(filename, SPEAK_OPTIONS, options)
    

