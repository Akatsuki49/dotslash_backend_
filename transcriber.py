
import os
from dotenv import load_dotenv

from deepgram import (
    DeepgramClient,
    PrerecordedOptions,
    FileSource,
)

load_dotenv()

AUDIO_FILE = "test.mp3"

API_KEY = "135b47d20ff4581e9581149b1ad38eb65e12ddd7"

deepgram = DeepgramClient(API_KEY)

with open(AUDIO_FILE, "rb") as file:
    buffer_data = file.read()

payload: FileSource = {
    "buffer": buffer_data,
}

options = PrerecordedOptions(
    model="nova-2",
    smart_format=True,
)

response = deepgram.listen.prerecorded.v("1").transcribe_file(payload, options)


transcribed = response["results"]["channels"][0]["alternatives"][0]["transcript"]
# print(transcribed)
