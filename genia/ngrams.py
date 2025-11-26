import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
# Baixar os recursos necessários
nltk.download('punkt')
nltk.download('punkt_tab')   # Necessário em versões novas do NLTK

'''
sentence = 'Estou aprendendo IA'
tokens = word_tokenize(sentence)
trigrams = list(ngrams(tokens, 2))

print(trigrams) '''

texto_simples = 'eu estou aprendendo NLP (Natural Language Processing)'
tokens = word_tokenize(texto_simples)

unigrams = list(ngrams(tokens, 1))
print('Unigrams: \n', unigrams)

bigrams = list(ngrams(tokens, 2))
print('Bigrams: \n', bigrams)

trigrams = list(ngrams(tokens, 3))
print('Trigrams: \n', trigrams)




