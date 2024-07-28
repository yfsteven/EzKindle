# ezkindle.py
""" EzKindle is a program that makes it easy to upload books to Kindle"""
import re
import sys
from convert_jp import fetch_meaning
from smtp import send_mail
from clean import cleanse

SUPPORTED_FILE_EXTENSIONS = ['.doc', '.docx', '.html', '.htm', '.rtf', '.txt', '.jpeg', '.jpg', '.gif', '.png', '.bmp', '.pdf', '.epub']

def send_to_kindle(book: str):
    """ send_to_kindle accepts an attachment parameter of file you want to send to your kindle"""
    file_extension_pattern = re.compile( '$|'.join(SUPPORTED_FILE_EXTENSIONS) + '$' )

    if file_extension_pattern.search(str(book)) is None:
        print("File is not supported!")
        sys.exit()

    try:
        send_mail(book)
    except Exception as err:
        print(f"Unable to send email due to {err}")
        sys.exit()

def extract_clippings(clipping: str):
    """ extract_clippings takes your my clipping text file to help make Anki card"""
    try:
        word_list = cleanse(clipping)
        fetch_meaning(word_list)

    except FileNotFoundError:
        print("Clipping text file does not exist!")
        sys.exit()
