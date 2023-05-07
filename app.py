from flask import Flask, render_template, request
import sqlite3
from NLPAnalysis import ExtractText
from SecureFileUpload import AuthenticateUser, FileUpload, SignUpUser

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/upload')
def upload():
    #print("hello")
    user_id = request.args.get('user_id')
    print("upload: " + user_id)
    return render_template('upload.html', user_id = user_id)

@app.route('/upload_file', methods=['POST'])
def upload_file():
    file = request.files['file']
    user_id = request.form['user_id']
    print ("fileUpload: " + user_id)
    doc_id = FileUpload(file, user_id)
    # Do something with the uploaded file
    conn = sqlite3.connect('pdf_reader.db')
    c = conn.cursor()
    c.execute(f'SELECT * FROM User_Documents WHERE UUSERID == {user_id}')
    data = c.fetchall()
    conn.close()
    return render_template('successful_upload.html', user_id = user_id, data = data, doc_id = doc_id) 


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        try:
            user_id = AuthenticateUser(username, password)
            conn = sqlite3.connect('pdf_reader.db')
            c = conn.cursor()
            c.execute(f'SELECT * FROM User_Documents WHERE UUSERID == {user_id}')
            data = c.fetchall()
            conn.close()
            return render_template('successful_login.html', user_id = user_id, username = username, data = data)
        except ValueError:
            return render_template('failed_login.html')

    else:
        return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        SignUpUser(username, password)
        
        return render_template('successful_signup.html')
    else:
        return render_template('signup.html')
    
@app.route('/sentiment')
def sentiment():
    #print("hello")
    user_id = request.args.get('user_id')
    print("upload: " + user_id)
    return render_template('upload.html', user_id = user_id)
    
@app.route('/similar')
def similar():
    return render_template('feed.html')