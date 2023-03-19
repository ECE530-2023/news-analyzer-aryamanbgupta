import sqlite3

from matplotlib import use


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


def FileUpload():
    #define File upload procedure for all valid file types

    raise ValueError("Invalid File Type")
    raise ValueError("File size too large")
    return upload_status


def EncryptFile():
    #define procedure to encrypt files for upload

    raise ValueError("Encryption Failed")
    return successful_encryption


def SanitizeInput(input_str):
    sanitized_str = input_str.strip()  # Remove leading and trailing whitespaces
    sanitized_str = sanitized_str.replace("'", "''")  # Escape single quotes with double quotes
    return sanitized_str