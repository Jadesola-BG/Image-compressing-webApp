from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
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

@app.before_request
def before_request_func():
    print("COMPRESSING IMAGE !!!")

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
        image_name = secure_filename(image.filename)
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], image_name))
        flash('Image successfully uploaded !!! ')
        #image compression operation
        #rendering html file that will show original and compressed images
        return render_template('')

    else:
        flash('Please ensure you uploaded only the allowed file types.')
        return redirect(request.url)
        #return "Invalid image", 400
    return render_template("home.html")




if __name__  == '__main__':
    app.run(debug=True)