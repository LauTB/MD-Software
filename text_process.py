#import spacy
from itertools import chain
from googletrans import Translator
import pymagnitude as magnitude
from numpy import zeros
# def get_an(sen):
#     nlp = spacy.load("es_core_news_sm")
#     an_set = set()
#     doc = nlp(sen)
#     for token in doc:
#       if token.pos_ == 'NOUN':
#           for related in chain(token.lefts, token.rights):
#               if related.pos_ == 'ADJ':
#                   pair = (str.lower(token.text), str.lower(related.text), token.i, related.i)
#                   an_set.add(pair)
#     return an_set

def translate(data):
    translator = Translator()
    return translator.translate(data).text

def embeddings(tokens, filepath=r'files\wiki-news-300d-1M.magnitude'):
        """
        Transforms a list of tokens into a list of embeddings

        :param list tokens: List of tokens to transform into Embeddings
        :return: List of embeddings for given tokens
        """
        padding_marker = '*'
        dimensions = 300
        vectors = magnitude.Magnitude(filepath)
        return_list = []
        for token in tokens:
            if token == padding_marker:
                return_list.append(zeros(dimensions))
            elif token in vectors:
                vec = vectors.query(token)
                return_list.append(vec)
            else:
                # pymagnitude finds the most similar
                vec = vectors.query(token)
                return_list.append(vec)

        return return_list


