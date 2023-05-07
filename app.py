from flask import Flask, render_template, request
from NLPAnalysis import ExtractText
from SecureFileUpload import AuthenticateUser

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        try:
            user_id = AuthenticateUser(username, password)
            return render_template('successful_login.html', user_id = user_id, username = username)
        except ValueError:
            return render_template('failed_login.html')

    else:
        return render_template('login.html')
