# news-analyzer-aryamanbgupta
Secure File Uploader:  
    User Stories:  
        - I should login to a secure service to upload my content  
        - I should be able to upload documents  
        - I should be able to upload PDFs or images.  
        - I should be able to choose who access to my files.  
        - My documents should be secure and encrypted.  
    Entity Based API  
    Operations:  
        - Authorization and Authentication management for users so that only authorized users have access to files.  
        - Multiple file type uploads allowed.  
        - Encryption of files during the upload process and storage.  
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
        - Keywords within paragraphs should be searchable in government opendata, wikipedia and media organizations  
        - I should find definition of keywords using open services  
        - I want to discover content from the WEB to enhance story  
        - I should be able to get summaries of each document  
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


Database Design:

I plan to use a relational SQL database.
- The database will have different tables containing data about users, their documents, access management and key words
- One table will contain all the user information with column headers like unique user ID, username, encrypted password, number of documents etc.
- Each user will have a table that lists all the documents that they have access to with headers like document ID, key words from analysis, list of users who have access to it, owner ID, link to the document etc.
- A separate table will contain data about all the publicly shared documents for the News Feed with columns like Key word list, original source and link.
