from SecureFileUpload import *
from NLPAnalysis import *
from NewsIngester import *
import pytest

def FileUploadTest():
    with pytest.raises(ValueError):
        FileUpload()

def EncryptFileTest():
    with pytest.raises(ValueError):
        EncryptFile()

def ExtractTextTest():
    with pytest.raises(ValueError):
        ExtractText()

def FindRelatedDocumentsTest():
    with pytest.raises(ValueError):
        FindRelatedDocuments()