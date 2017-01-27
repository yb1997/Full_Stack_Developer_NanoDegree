#check_profanity.py

import urllib

def read_file():
    quotes = open("C:\Users\KARAN PC\Desktop\movie_quotes.txt");  #pah of the file
    contents_of_file = quotes.read();
    print(contents_of_file)
    check_prof(contents_of_file)

def check_prof(check_text):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + check_text) #opens the url in background
    output = connection.read()
    print(" ")
    if "true" in output:
        print("Profanity Alert!!")
    elif "false" in output:
        print("This document has no curse words!")
       
    connection.close()

read_file()
