# from flask import Flask, request, jsonify, render_template
# import cv2
# import numpy as np
# from werkzeug.utils import secure_filename
# import os

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = 'uploads/'

# if not os.path.exists('uploads'):
#     os.makedirs('uploads')

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/upload', methods=['POST'])
# def upload_image():
#     if 'image' not in request.files:
#         return jsonify({'error': 'No file part'})
#     file = request.files['image']
#     if file.filename == '':
#         return jsonify({'error': 'No selected file'})
#     if file:
#         filename = secure_filename(file.filename)
#         filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         file.save(filepath)
#         return jsonify({'filepath': filepath})

# @app.route('/histogram', methods=['POST'])
# def histogram():
#     filepath = request.json['filepath']
#     image = cv2.imread(filepath, 0)
#     equ = cv2.equalizeHist(image)
#     equ_filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'equalized_' + os.path.basename(filepath))
#     cv2.imwrite(equ_filepath, equ)
#     return jsonify({'filepath': equ_filepath})

# @app.route('/edge_detection', methods=['POST'])
# def edge_detection():
#     filepath = request.json['filepath']
#     image = cv2.imread(filepath, 0)
#     edges = cv2.Canny(image, 100, 200)
#     edges_filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'edges_' + os.path.basename(filepath))
#     cv2.imwrite(edges_filepath, edges)
#     return jsonify({'filepath': edges_filepath})

# @app.route('/convolution', methods=['POST'])
# def convolution():
#     filepath = request.json['filepath']
#     kernel = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])
#     image = cv2.imread(filepath, 0)
#     conv_image = cv2.filter2D(image, -1, kernel)
#     conv_filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'conv_' + os.path.basename(filepath))
#     cv2.imwrite(conv_filepath, conv_image)
#     return jsonify({'filepath': conv_filepath})

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, request, jsonify, render_template, send_from_directory
import cv2
import numpy as np
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['OUTPUT_FOLDER'] = 'static/output/'

if not os.path.exists('uploads'):
    os.makedirs('uploads')
if not os.path.exists('static/output'):
    os.makedirs('static/output')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'})
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        return jsonify({'filepath': filepath})

@app.route('/histogram', methods=['POST'])
def histogram():
    filepath = request.json['filepath']
    image = cv2.imread(filepath, 0)
    equ = cv2.equalizeHist(image)
    equ_filepath = os.path.join(app.config['OUTPUT_FOLDER'], 'equalized_' + os.path.basename(filepath))
    cv2.imwrite(equ_filepath, equ)
    return send_from_directory(app.config['OUTPUT_FOLDER'], os.path.basename(equ_filepath))

@app.route('/edge_detection', methods=['POST'])
def edge_detection():
    filepath = request.json['filepath']
    image = cv2.imread(filepath, 0)
    edges = cv2.Canny(image, 100, 200)
    edges_filepath = os.path.join(app.config['OUTPUT_FOLDER'], 'edges_' + os.path.basename(filepath))
    cv2.imwrite(edges_filepath, edges)
    return send_from_directory(app.config['OUTPUT_FOLDER'], os.path.basename(edges_filepath))

@app.route('/convolution', methods=['POST'])
def convolution():
    filepath = request.json['filepath']
    kernel = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])
    image = cv2.imread(filepath, 0)
    conv_image = cv2.filter2D(image, -1, kernel)
    conv_filepath = os.path.join(app.config['OUTPUT_FOLDER'], 'conv_' + os.path.basename(filepath))
    cv2.imwrite(conv_filepath, conv_image)
    return send_from_directory(app.config['OUTPUT_FOLDER'], os.path.basename(conv_filepath))

if __name__ == '__main__':
    app.run(debug=True)
