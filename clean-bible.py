import os
import sys
import nltk
import re
from nltk.corpus import stopwords

STOP_WORDS = stopwords.words('english')
REG = re.compile(r"([A-Za-z]+)")

def clean_bible(file='bible.txt'):
    using_word2vec =  len(sys.argv) > 1
    cleaned_bible_txt = ""
    lines_processed = 0
    lines = open(file).readlines()
    for line in lines[0:]:
        cleaned_line = " ".join([w.strip().lower() for w in REG.findall(line) \
            if (w.strip() not in STOP_WORDS) and
            (len(w) > 3) ])
        if using_word2vec:
            cleaned_bible_txt += " {}\n".format(cleaned_line)
        else:
            cleaned_bible_txt += " {}".format(cleaned_line)
        lines_processed += 1

        if lines_processed % 1000 == 0:
            print "{lines_processed} lines processed".format(lines_processed=lines_processed)
    
    if using_word2vec:
        output_file = "bible-clean-word2vec.txt"
    else:
         output_file = "bible-clean.txt"
    
    f  = open(output_file,'w')
    f.write(cleaned_bible_txt)
    f.close()
    
    #print cleaned_bible_txt
    
if __name__ == "__main__":
    clean_bible()