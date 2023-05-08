import sqlite3


def FindRelatedDocuments(keywords):
    #find related documents from WEB using keywords
    conn=sqlite3.connect('pdf_reader.db')
    c=conn.cursor()

    related_documents = []
    
    c.execute("SELECT * FROM WEB_DOCUMENTS WHERE KEYWORDS LIKE ?", ('%' + keywords + '%',))
    results = c.fetchall()
    for row in results:
        related_documents += row[2]

    if related_documents is None:
            raise ValueError("Could not find related results")
    else:
        return related_documents

def SummariseResults():
    #use NLP model to get summaries of documents

    raise ValueError("Summaries failes")
    return summaries