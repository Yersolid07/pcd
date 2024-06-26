
# from flask import Flask, request, jsonify, render_template, send_from_directory
# import cv2
# import numpy as np
# from werkzeug.utils import secure_filename
# import os

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = 'uploads/'
# app.config['OUTPUT_FOLDER'] = 'static/output/'

# os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
# os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/upload', methods=['POST'])
# def upload_image():
#     if 'image' not in request.files:
#         return jsonify({'error': 'No file part'}), 400
#     file = request.files['image']
#     if file.filename == '':
#         return jsonify({'error': 'No selected file'}), 400
#     if file:
#         filename = secure_filename(file.filename)
#         filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         file.save(filepath)
#         print(f"File saved to {filepath}")  # Debugging statement
#         return jsonify({'filepath': filepath}), 200

# @app.route('/histogram', methods=['POST'])
# def histogram():
#     filepath = request.json.get('filepath')
#     print(f"Histogram request for {filepath}")  # Debugging statement
#     if not filepath or not os.path.exists(filepath):
#         print(f"File not found: {filepath}")  # Debugging statement
#         return jsonify({'error': 'File not found'}), 404

#     image = cv2.imread(filepath, 0)
#     if image is None:
#         print(f"Error reading image file: {filepath}")  # Debugging statement
#         return jsonify({'error': 'Error reading image file'}), 500

#     equ = cv2.equalizeHist(image)
#     equ_filepath = os.path.join(app.config['OUTPUT_FOLDER'], 'equalized_' + os.path.basename(filepath))
#     cv2.imwrite(equ_filepath, equ)
#     print(f"Equalized image saved to {equ_filepath}")  # Debugging statement
#     return send_from_directory(app.config['OUTPUT_FOLDER'], os.path.basename(equ_filepath))

# @app.route('/edge_detection', methods=['POST'])
# def edge_detection():
#     filepath = request.json.get('filepath')
#     print(f"Edge detection request for {filepath}")  # Debugging statement
#     if not filepath or not os.path.exists(filepath):
#         print(f"File not found: {filepath}")  # Debugging statement
#         return jsonify({'error': 'File not found'}), 404

#     image = cv2.imread(filepath, 0)
#     if image is None:
#         print(f"Error reading image file: {filepath}")  # Debugging statement
#         return jsonify({'error': 'Error reading image file'}), 500

#     edges = cv2.Canny(image, 100, 200)
#     edges_filepath = os.path.join(app.config['OUTPUT_FOLDER'], 'edges_' + os.path.basename(filepath))
#     cv2.imwrite(edges_filepath, edges)
#     print(f"Edges image saved to {edges_filepath}")  # Debugging statement
#     return send_from_directory(app.config['OUTPUT_FOLDER'], os.path.basename(edges_filepath))

# @app.route('/convolution', methods=['POST'])
# def convolution():
#     filepath = request.json.get('filepath')
#     print(f"Convolution request for {filepath}")  # Debugging statement
#     if not filepath or not os.path.exists(filepath):
#         print(f"File not found: {filepath}")  # Debugging statement
#         return jsonify({'error': 'File not found'}), 404

#     image = cv2.imread(filepath, 0)
#     if image is None:
#         print(f"Error reading image file: {filepath}")  # Debugging statement
#         return jsonify({'error': 'Error reading image file'}), 500

#     kernel = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])
#     conv_image = cv2.filter2D(image, -1, kernel)
#     conv_filepath = os.path.join(app.config['OUTPUT_FOLDER'], 'conv_' + os.path.basename(filepath))
#     cv2.imwrite(conv_filepath, conv_image)
#     print(f"Convolution image saved to {conv_filepath}")  # Debugging statement
#     return send_from_directory(app.config['OUTPUT_FOLDER'], os.path.basename(conv_filepath))

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
        return jsonify({'filepath': filepath})  # Return relative path

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

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
