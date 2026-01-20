import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')

text = "Tokenization is an important NLP step"
print(word_tokenize(text))
  

 