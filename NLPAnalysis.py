from pypdf import PdfReader

def ExtractText(file_path):
    #extract text from the uploaded document
    reader = PdfReader(file_path)
    extracted_text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        extracted_text += page_text
    #raise ValueError("Text Extraction Failed")
    return extracted_text

def FindKeyWords():
    #find key words from the text
    #call NLP model
    key_words=[]
    #raise ValueError("Key Words not Found")
    return key_words

def SentimentAnalysis():
    #Sentiment analysis on given text

    raise ValueError("Sentiment Analysis Failed")
    return sentiment_analysis_results