import queue
import concurrent.futures
from SecureFileUpload import FileUpload


PDFQueue = queue.Queue()


def PdfReaderQueueAdd(file_path):
    PDFQueue.put(file_path)   


with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    while True:
        job = pool.submit(PDFQueue.get())
        job.add_done_callback(lambda future: FileUpload(future.result()))
        pool.submit(PdfReaderQueueAdd, PDFQueue.qsize())