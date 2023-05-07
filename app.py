from flask import Flask, render_template, request
from NLPAnalysis import ExtractText

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/upload')
def upload():
    #print("hello")
    return render_template('upload.html')

@app.route('/upload_file', methods=['POST'])
def upload_file():
    file = request.files['file']
    text = ExtractText(file)
    # Do something with the uploaded file
    return f"<p> {text} </p>"