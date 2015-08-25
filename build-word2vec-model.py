#
# training word2vec model
#

import logging
from gensim.models import word2vec

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

num_features = 5000    # Word vector dimensionality                      
min_word_count = 10   # Minimum word count                        
num_workers = 4       # Number of threads to run in parallel
context = 10          # Context window size                                                                                    
downsampling = 1e-3   # Downsample setting for frequent words

bible = open("bible-clean-word2vec.txt").read().split("\n");bible = [b.split() for b in bible if len(b) > 2]

model = word2vec.Word2Vec(bible, workers=num_workers, \
                        size=num_features, min_count = min_word_count, \
                        window = context, sample = downsampling)
model.init_sims(replace=True)
model.save("bible_word2vec.model")