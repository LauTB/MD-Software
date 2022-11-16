import spacy
from itertools import chain
from googletrans import Translator
def get_an(sen):
    nlp = spacy.load("es_core_news_sm")
    an_set = set()
    doc = nlp(sen)
    for token in doc:
      if token.pos_ == 'NOUN':
          for related in chain(token.lefts, token.rights):
              if related.pos_ == 'ADJ':
                  pair = (str.lower(token.text), str.lower(related.text), token.i, related.i)
                  an_set.add(pair)
    return an_set

def translate(data):
    translator = Translator()
    return translator.translate(data).text

text = "La energía verde tiene potencial ilimitado."
print(get_an(text))
