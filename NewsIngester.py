import sqlite3


def FindRelatedDocuments(keywords):
    #find related documents from WEB using keywords
    conn=sqlite3.connect('pdf_reader.db')
    c=conn.cursor()

    related_docs = set()
    for keyword in keywords:
        c.execute("SELECT DOCUMENT_ID FROM WEB_DOCUMENTS WHERE KEYWORDS LIKE ?", ('%' + keyword + '%',))
        results = c.fetchall()
        for row in results:
            related_docs.add(row[0])

    if related_docs is None:
            raise ValueError("Could not find related results")
    else:
        return related_docs

def SummariseResults():
    #use NLP model to get summaries of documents

    raise ValueError("Summaries failes")
    return summaries