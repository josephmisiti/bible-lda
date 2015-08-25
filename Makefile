bible.txt:
	curl -o bible.txt 'http://www.ccel.org/ccel/bible/kjv.txt'

clean-text: bible.txt
	python clean-bible.py	

clean-text-word2vec: bible.txt
	python clean-bible.py word2vec	

train-word2vec:
	python build-word2vec-model.py

nlp: 
	python lda.py -f bible-clean.txt -k 25 --alpha=0.5 --beta=0.5 -i 50