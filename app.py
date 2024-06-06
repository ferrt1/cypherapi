from flask import Flask, request, send_file
from io import BytesIO
import os
import random
import string

app = Flask(__name__)
uploads = {}

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    if file:
        filename = ''.join(random.choices(string.ascii_lowercase + string.digits, k=16))
        file_content = file.read()
        uploads[filename] = file_content
        return f'https://constantly-able-crawdad.ngrok-free.app/uploads/{filename}', 200

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    file_content = uploads.get(filename)
    if file_content:
        return send_file(BytesIO(file_content), mimetype='image/png')
    else:
        return 'File not found', 404

if __name__ == '__main__':
    app.run(debug=True)
