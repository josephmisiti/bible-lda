OldTestament.zip:
	curl -o OldTestament.zip 'http://ruwach.googlepages.com/OldTestament.zip'
	
NewTestament.zip:
	curl -o NewTestament.zip 'http://ruwach.googlepages.com/NewTestament.zip'

bible.txt:
	curl -o bible.txt 'http://www.ccel.org/ccel/bible/kjv.txt'

build: bible.txt
	cat bible.txt | head -n 10	
	rm *.zip
	
nlp: 
	#python clean-bible.py
	python lda.py -f bible-clean.txt -k 10 --alpha=0.5 --beta=0.5 -i 5