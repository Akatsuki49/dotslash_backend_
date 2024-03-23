import re
import numpy as np
from pydub import AudioSegment
from flask import Flask, request, jsonify, send_file
import json

app = Flask(__name__)


@app.route('/image_endpoint', methods=['POST'])
def visualize_paragraph():
    paragraph_text = request.form['paragraph']
    title = request.form['title']
    image_context = generate_SummarizedPrompt_image(paragraph_text, title)
    print(image_context)

    image_data = imggen(image_context)

    return jsonify({'image': image_data})


# generate_SummarizedPrompt_image(
#     paragraph_text, title)
generate_SummarizedPrompt_audio(paragraph_text)

if __name__ == '__main__':
    app.run()
