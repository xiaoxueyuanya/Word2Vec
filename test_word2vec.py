from gensim.models import Word2Vec

data_folder = 'G:/NLP/word2vec/trained_model/'

test_words = ["cat", "car", "food", "computer", "travel", "academic", "picture", "camera"]

model = Word2Vec.load(data_folder + 'my_word2vec_model_00')
# model = Word2Vec.load(data_folder + 'my_word2vec_model_02')
# model = Word2Vec.load(data_folder + 'my_word2vec_model_03')
# model = Word2Vec.load(data_folder + 'my_word2vec_model_04')
# model = Word2Vec.load(data_folder + 'my_word2vec_model_05')
# model = Word2Vec.load(data_folder + 'my_word2vec_model_06')
# model = Word2Vec.load(data_folder + 'my_word2vec_model_07')

print("The trained Word2Vec models are loaded!")
print("Model information:")
print("\tvector_size  window  min_count  sg  "
      "negative  epochs  corpus_count  "
      "corpus_total_words  com_table.size  compute_loss")
print("\t %6d %8d %9d %6d"
      "%7d %8d %13d"
      "%18d %16d %13d" 
      %(model.vector_size, model.window, model.min_count, model.sg,
        model.negative, model.epochs, model.corpus_count,
        model.corpus_total_words, model.cum_table.size, model.compute_loss))

for word in test_words:
    print("Test'" + word + "':")
    # print("  " + word + "= [", end=" ")
    # for val in model.wv.get_vector(word):
    #     print(str(val), end=" ")
    # print("]")
    print("   similar words:", end=" ")
    similar_words = model.wv.most_similar(word) 
    for simword in similar_words:
        print("%15s" % str(simword[0]), end=" ")
    print("")
    print("   similarity:   ", end=" ")
    for simword in similar_words:
        print("%.13f" % (simword[1]), end=" ")
    print("")
        
