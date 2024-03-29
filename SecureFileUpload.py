import sqlite3
import uuid
import re
import hashlib
import os
from NLPAnalysis import ExtractText, FindKeyWords, SentimentAnalysis

#sample global variables
SUPPORTED_FILE_TYPES = ['pdf', 'txt', 'docx']
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB in bytes

def SignUpUser(user_name,password):
    sanitized_user_name= SanitizeInput(user_name)
    sanitized_password= SanitizeInput(password)

    #Hash password befor storing it
    password_bytes = sanitized_password.encode('utf-8')
    hashed_password = hashlib.sha256(password_bytes).hexdigest()

    conn = sqlite3.connect('pdf_reader.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (sanitized_user_name, hashed_password))
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (sanitized_user_name, hashed_password))
    row = c.fetchone()
    conn.commit()
    conn.close()
    return row[0]

def DeleteUser(user_name, password):
    sanitized_user_name= SanitizeInput(user_name)
    sanitized_password= SanitizeInput(password)

    password_bytes = sanitized_password.encode('utf-8')
    hashed_password = hashlib.sha256(password_bytes).hexdigest()

    conn = sqlite3.connect('pdf_reader.db')
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE username = ? AND password = ?", (sanitized_user_name, hashed_password))
    if c.rowcount == 0:
        raise ValueError("User not found.")
    else:
        conn.commit()
        conn.close()
        return True
    
def AuthenticateUser(user_name,password):
    #Authenticate user using login credentials
    #Sanitize user input
    sanitized_user_name= SanitizeInput(user_name)
    sanitized_password= SanitizeInput(password)

    password_bytes = sanitized_password.encode('utf-8')
    hashed_password = hashlib.sha256(password_bytes).hexdigest()

    #Connect to database and check credentials
    conn = sqlite3.connect('pdf_reader.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (sanitized_user_name, hashed_password))
    row = c.fetchone()
    conn.close()
    if row is not None:
        return row[0]
    else:
        #If credentials are not found, raise an error
        raise ValueError("Invalid login credentials")

    return login_authentication


def FileUpload(file_path,users):
    #define File upload procedure for all valid file types
    #check if file type is supported
    '''
    if not IsFileTypeSupported(file_path):
        raise ValueError("Invalid File Type")
    #check file size
    if os.path.getsize(file_path)> MAX_FILE_SIZE:
        raise ValueError("File size too large")
    '''
    # Get key words from document
    text= ExtractText(file_path)
    key_words= FindKeyWords(text)
    sentiment = str(SentimentAnalysis(text))

    # Generate a unique document ID
    doc_id = str(uuid.uuid4())

    # Insert the document information into the database
    conn = sqlite3.connect('pdf_reader.db')
    c = conn.cursor()
    c.execute("INSERT INTO User_Documents (ID, KEYWORD1,KEYWORD2,KEYWORD3,KEYWORD4,KEYWORD5, UUSERID, SENTIMENT) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
              (doc_id, key_words[0], key_words[1], key_words[2], key_words[3], key_words[4], users, sentiment))
    conn.commit()
    conn.close()


    return doc_id


def EncryptFile():
    #define procedure to encrypt files for upload

    raise ValueError("Encryption Failed")
    return successful_encryption


def SanitizeInput(input_str):
    #only certain characters are allowed and the rest are filtered out
    allowed_chars = r'[a-zA-Z0-9!_@]'
    sanitized_str = re.sub(f'[^{allowed_chars}]', '', input_str)

    return sanitized_str


def IsFileTypeSupported(file_name):
    file_type = file_name.split('.')[-1].lower()
    if file_type in SUPPORTED_FILE_TYPES:
        return True
    else:
        return False