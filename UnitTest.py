from SecureFileUpload import *
from NLPAnalysis import *
from NewsIngester import *
import pytest

def test_ExtractText():
    res = ExtractText("Trial.pdf")
    assert res == "Trial 1 2 \\n  "

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