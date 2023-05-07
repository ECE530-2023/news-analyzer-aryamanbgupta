# news-analyzer-aryamanbgupta

# PDF Text Analysis and Search Tool

This is a web application that allows users to create accounts, log in, upload PDF documents, extract text from the uploaded documents, analyze the text to find key words and conduct sentiment analysis on it. The application also includes a search function that helps users find similar documents from the web based on the analysis results.

## Features

- User registration and login system
- PDF document upload and extraction of text
- Text analysis to find key words
- Sentiment analysis of the text
- Search function to find similar documents from the web

## Technologies Used

- Python
- Flask web framework
- PyPDF library for extracting text from PDF documents
- Natural Language Toolkit (NLTK) for text analysis and sentiment analysis

## Installation

1. Clone the repository:

   ```
   git clone git@github.com:ECE530-2023/news-analyzer-aryamanbgupta.git
   ```

2. Start a virtual environment

   ```
   python3 -m venv .venv
   . .venv/bin/activate
   ```

3. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Run the application:

   ```
   python -m flask run
   ```

5. Open the application in your web browser at http://localhost:5000

## Usage

1. Register and log in to the application.

2. Upload a PDF document.

3. Wait for the text to be extracted and analyzed.

4. View the key words and sentiment analysis results.

5. Use the search function to find similar documents from the web.

## Credits

This project was created by Aryaman Bhavya Gupta for EC530 Spring 2023

## User Stories/Motivation and APIs
Secure File Uploader:  
    User Stories:  
        - I should login to a secure service to upload my content  
        - I should be able to upload documents  
        - I should be able to upload PDFs.  

    Entity Based API  
    Operations:  
        - Authorization and Authentication management for users so that only authorized users have access to files.  
        - Multiple file type uploads allowed.  
        - Post the encrypted files into the database.  
    Data:  
        - Uploaded files of various different types.  
        - Authorization and Authentication credentials.  
        - Encryption keys.  
    Status:  
        - Authentication success or failure  
        - File Type not supported error  
        - File size too large error  
        - Encryption success/failure  
        - Stored successfully / Database error  

Text NLP Analysis:  
    User Stories:  
        - The application should translate my documents to text  
        - I want the service to tag all my documents and paragraphs within every document with the keywords and know the topics     each document cover  
        - I should be able to access different paragraphs of different documents based on keywords  
        - I should be able to to find all positive, neutral and negative paragraphs and sentences  
    Procedure Based API  
    Operations:  
        - Read all text from PDF and other document types  
        - Use NLP models to find keywords from the text  
        - Search through multiple documents using keywords  
        - Predict sentiments of paragraph with NLP models  
    Data:  
        - User uploaded files  
        - text generated from the files  
    Status:  
        - Text extraction successful/failure  
        - Keyword/ Topic Analysis sucess/failure  
        - Sentiment Analysis sucess/failure  
        - decryption/authorization failure  

News Feed Ingester:  
    User Stories:  
        - Keywords within paragraphs should be searchable from the internet  
        - I should find definition of keywords using open services  
        - I want to discover content from the WEB to enhance story  
    Entity Based API  
    Operations:  
        - Search and find relevant documents, research papers, webpages to keywords  
        - Call the NLP API to get summaries of documents  
    Data:  
        - Documents, files collected from the web  
        - Keywords to search for  
    Status:  
        - Web Search Status  
        - Document Analysis Status  
        - Keywords found/ not found  


## Database Design:

I used a relational SQL database.
- The database has different tables containing data about users, their documents, access management and key words
- One table contains all the user information with column headers like unique user ID, username, encrypted password, number of documents etc.
- Each user will have a table that lists all the documents that they have access to with headers like document ID, key words from analysis, list of users who have access to it, owner ID, link to the document etc.
- A separate table will contain data about all the publicly shared documents for the News Feed with columns like Key word list, original source and link.

