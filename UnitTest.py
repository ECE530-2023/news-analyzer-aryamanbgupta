from SecureFileUpload import *
from NLPAnalysis import *
from NewsIngester import *
import pytest



def test_ExtractText():
    res = ExtractText("Trial.pdf")
    assert res == "Trial 1 2 \\n  "

def test_FindKeyWords():
    text = "This is an example text to see if the program can find Key Words. The top 5 key words should be identified by the program in this example"
    res = FindKeyWords(text)
    assert res == ['example', 'program', 'text', 'see', 'find']

def test_SentimentAnalysis():
    text = "This is an example text to see if the program can find Key Words. The top 5 key words should be identified by the program in this example"
    res = SentimentAnalysis(text)
    assert res['compound'] == 0.2023

def test_AuthenticateUser():
    username = "check"
    password = "hash"
    assert AuthenticateUser(username,password) == 5

def test_SignUpUser():
    username = "test"
    password = "easy"
    assert type(SignUpUser(username,password)) == int

def test_DeleteUser():
    username = "test"
    password = "easy"
    assert DeleteUser(username,password) == True

def test_FileUpload():
    file = "example_text.pdf"
    user = 1
    assert type(FileUpload(file,user)) == str
'''

def FileUploadTest():
    with pytest.raises(ValueError):
        FileUpload()

def EncryptFileTest():
    with pytest.raises(ValueError):
        EncryptFile()


def FindRelatedDocumentsTest():
    with pytest.raises(ValueError):
        FindRelatedDocuments()

'''