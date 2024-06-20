from flask import Flask, request, send_file, render_template
from io import BytesIO
import random
import string
import threading
import time

app = Flask(__name__)
uploads = {}

# Tiempo en segundos para mantener el archivo en memoria antes de eliminarlo
EXPIRATION_TIME = 300  # 5 minutos

def remove_file_after_timeout(filename):
    time.sleep(EXPIRATION_TIME)
    if filename in uploads:
        del uploads[filename]

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return render_template('error.html', message='No file part'), 400
    file = request.files['file']
    if file.filename == '':
        return render_template('no_file_selected.html'), 400
    if file:
        filename = ''.join(random.choices(string.ascii_lowercase + string.digits, k=16))
        file_content = file.read()
        uploads[filename] = file_content
        # Elimino la imagen
        threading.Thread(target=remove_file_after_timeout, args=(filename,)).start()
        return f'https://cypherapi.vercel.app/uploads/{filename}', 200

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    file_content = uploads.get(filename)
    if file_content:
        return send_file(BytesIO(file_content), mimetype='image/png')
    else:
        return render_template('file_not_found.html'), 404

@app.route('/')
def index():
    return render_template('index.html'), 200

if __name__ == '__main__':
    app.run(debug=True)
