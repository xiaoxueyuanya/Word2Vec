from gensim.models import Word2Vec
from my_sentences import MySentences   
            
data_folder = 'G:/NLP/word2vec/yelp_dataset_review/'
save_folder = 'G:/NLP/word2vec/trained_model/'
sentences = MySentences(data_folder) # a memory-friendly iterator

max_sentence_len = 0
for sentence in sentences: 
    if len(sentence) > max_sentence_len:
        max_sentence_len = len(sentence)
        
print("Max sentence length: " + str(max_sentence_len))


# w2v = Word2Vec(sentences, vector_size=200, window=5, epochs=1, min_count=5, sg=1, negative=5)
# print("Train Word2Vec done!")

# w2v.save(save_folder + 'my_word2vec_model_00')
# print("Save the trained model at " + save_folder)