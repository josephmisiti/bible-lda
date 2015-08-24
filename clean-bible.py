import os
import nltk
import re
from nltk.corpus import stopwords

STOP_WORDS = stopwords.words('english')

def clean_bible(file='bible.txt'):
    cleaned_bible_txt = ""
    lines_processed = 0
    lines = open(file).readlines()
    for line in lines[0:]:
        cleaned_line = " ".join([w.strip().lower() for w in line.split() if w.strip() not in STOP_WORDS])
        cleaned_bible_txt += " {}".format(cleaned_line)
        lines_processed += 1
        
        if lines_processed % 1000 == 0:
            print "{lines_processed} lines processed".format(lines_processed=lines_processed)
    
    f  = open("bible-clean.txt",'w')
    f.write(cleaned_bible_txt)
    f.close()
    
    #print cleaned_bible_txt
    
if __name__ == "__main__":
    clean_bible()