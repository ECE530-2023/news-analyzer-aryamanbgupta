from pypdf import PdfReader
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import string
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('punkt')
nltk.download('vader_lexicon')
nltk.download('stopwords')

def ExtractText(file_path):
    #extract text from the uploaded document
    reader = PdfReader(file_path)
    extracted_text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        extracted_text += page_text
    #raise ValueError("Text Extraction Failed")
    return extracted_text

def FindKeyWords(total_text):
    #find key words from the text
    #removing punctuation
    total_text = total_text.translate(str.maketrans('', '', string.punctuation + "'" + '"'))

    # Tokenize the text into individual words
    words = word_tokenize(total_text)

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.lower() not in stop_words]

    # Lemmatize the words
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]

    # Calculate the frequency distribution of the words
    freq_dist = nltk.FreqDist(lemmatized_words)

    # Extract the most common keywords
    top_keywords = [word for word, count in freq_dist.most_common(5)]

    #raise ValueError("Key Words not Found")
    return top_keywords

def SentimentAnalysis(text):
    #Sentiment analysis on given text
    analyzer = SentimentIntensityAnalyzer()

    # use the polarity_scores() method to analyze the sentiment of the text
    sentiment_analysis_results = analyzer.polarity_scores(text)

    #raise ValueError("Sentiment Analysis Failed")
    return sentiment_analysis_results