from flask import Flask, request, send_file
from io import BytesIO
import os

app = Flask(__name__)

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file uploaded!', 400
    file = request.files['file']
    return send_file(BytesIO(file.read()), download_name=file.filename)

if __name__ == '__main__':
    app.run(debug=True)

