from flask import Flask, render_template, request, send_file
import os
from subprocess import run

app = Flask(__name__)

# Folder to store uploaded files
UPLOAD_FOLDER = 'static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    
    file = request.files['file']
    
    global file_path

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)

    global file_name

    file_name=file.filename

    if file_name == '':
        return 'No selected file'
    
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
    return render_template('upscale.html',name=file_name)

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    return send_file(os.path.join(app.config['UPLOAD_FOLDER'], filename), as_attachment=True)

@app.route('/upscale', methods=['POST'])
def upscale():
    run(['python', 'esrgan.py', file_path])
    return render_template('upscale.html',name=file_name)

if __name__ == '__main__':
    app.run(debug=True)