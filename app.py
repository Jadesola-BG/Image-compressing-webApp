import os
from flask import Flask, render_template, request, redirect, url_for, flash, send_file
from werkzeug.utils import secure_filename
from compress import compress_image

OUTPUT_PATH = 'static/images/'

#initilizing flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hiii'
app.config['UPLOAD_FOLDER'] = OUTPUT_PATH
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.errorhandler(413)
def too_large(e):
    return "File is too large", 413

@app.route('/')
def home():
    return render_template('home.html')
    
def clean_uploadfolder():
    imagelist = [img for img in os.listdir(app.config['UPLOAD_FOLDER']) if not img.startswith("icon")]
    for images in imagelist:
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], images))
    

@app.route('/', methods=['POST'])
def image_upload():

    if "uploaded_image" not in request.files:
        flash("No file part")
        return redirect(request.url)

    image = request.files['uploaded_image']
    if image.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)

    if image and allowed_file(image.filename):
        clean_uploadfolder()
        image_name = secure_filename(image.filename)
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], image_name))
        flash('Image successfully uploaded & Compressing !!! ')
        #image compressing operation
        results = compress_image(image_name, app.config['UPLOAD_FOLDER'])
        return render_template('display.html', results = results)
        
    else:
        flash('Please ensure you uploaded only the allowed file types.')
        return redirect(request.url)


@app.route('/<filename>', methods=['GET','POST'])
def download_image(filename):
    path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    return send_file(path, as_attachment=True)
    

if __name__  == '__main__':
    app.run(debug=True)