import spacy
from itertools import chain
nlp = spacy.load("es_core_news_sm")
def get_an(sen):
    an_set = set()
    doc = nlp(sen)
    for token in doc:
      if token.pos_ == 'NOUN':
          for related in chain(token.lefts, token.rights):
              if related.pos_ == 'ADJ':
                  pair = (str.lower(token.text), str.lower(related.text), token.i, related.i)
                  an_set.add(pair)
    return an_set

text = "La energía verde se usa mucho con feos cascos"
print(get_an(text))
