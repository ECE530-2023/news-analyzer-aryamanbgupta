import sqlite3
import os
import uuid
from NLPAnalysis import ExtractText, FindKeyWords


#sample global variables
SUPPORTED_FILE_TYPES = ['pdf', 'txt', 'docx']
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB in bytes


def AuthenticateUser(user_name,password):
    #Authenticate user using login credentials
    #Sanitize user input
    sanitized_user_name= SanitizeInput(user_name)
    sanitized_password= SanitizeInput(password)

    #Connect to database and check credentials
    conn = sqlite3.connect('pdf_reader.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (sanitized_user_name, sanitized_password))
    row = c.fetchone()
    conn.close()
    if row is not None:
        return True
    else:
        #If credentials are not found, raise an error
        raise ValueError("Invalid login credentials")
    return login_authentication


def FileUpload(file_path,users):
    #define File upload procedure for all valid file types
    #check if file type is supported
    if not IsFileTypeSupported(file_path):
        raise ValueError("Invalid File Type")
    #check file size
    if file_size > MAX_FILE_SIZE:
        raise ValueError("File size too large")
    
    # Get key words from document
    text= ExtractText(file_path)
    key_words= FindKeyWords(text)

    # Generate a unique document ID
    doc_id = str(uuid.uuid4())

    # Insert the document information into the database
    conn = sqlite3.connect('pdf_reader.db')
    c = conn.cursor()
    c.execute("INSERT INTO USER_DOCUMENTS (ID, KEYWORDS, LINK, USERS) VALUES (?, ?, ?, ?)",
              (doc_id, key_words, file_path, users))
    conn.commit()
    conn.close()


    return doc_id


def EncryptFile():
    #define procedure to encrypt files for upload

    raise ValueError("Encryption Failed")
    return successful_encryption


def SanitizeInput(input_str):
    sanitized_str = input_str.strip()  # Remove leading and trailing whitespaces
    sanitized_str = sanitized_str.replace("'", "''")  # Escape single quotes with double quotes
    return sanitized_str


def IsFileTypeSupported(file_name):
    file_type = file_name.split('.')[-1].lower()
    if file_type in SUPPORTED_FILE_TYPES:
        return True
    else:
        return False