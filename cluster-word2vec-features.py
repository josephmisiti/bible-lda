
#
# cluster word2vec features
#

from gensim.models import Word2Vec
from sklearn.cluster import KMeans
import time

start = time.time()
model = Word2Vec.load("bible_word2vec.model")

word_vectors = model.syn0
num_clusters = word_vectors.shape[0] / 5

# Initalize a k-means object and use it to extract centroids
kmeans_clustering = KMeans( n_clusters = num_clusters )
idx = kmeans_clustering.fit_predict( word_vectors )

# Get the end time and print how long the process took
end = time.time()
elapsed = end - start
print "Time taken for K Means clustering: ", elapsed, "seconds."