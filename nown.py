#!/usr/bin/python3.5

import markovify
import os
import nltk
from nltk.corpus import gutenberg, webtext, nps_chat, brown, reuters, twitter_samples, movie_reviews, genesis

class WordChain(markovify.Text):
    def sentence_split(self, text):
        return text

    def word_split(self, sentence):
        return list(sentence)

    def word_join(self, sentence):
        return ''.join(sentence)

if not os.path.exists('model.json'):
    all_words = []
    for corpus in [gutenberg, webtext, nps_chat, brown, reuters, genesis, movie_reviews]:
        all_words.extend(corpus.words())

    flatten = lambda l: [item for sublist in l for item in sublist]
    # all_words.extend([word for word in flatten([tweet.split() for tweet in twitter_samples.strings()]) if not word.startswith('@')])

    print('Done adding words')

    model = WordChain(all_words, state_size=3)
    model_json = model.to_json()
    with open('model.json', 'w') as f:
        f.write(model_json)
else:
    with open('model.json', 'r') as f:
        model = WordChain.from_json(f.read())

print('Done making model')

total, count = 76, 0
while count < total:
    try:
        print(model.make_sentence(tries=100))
        count += 1
    except:
        pass



voices = (
    'Alice', 'Allison', 'Amelie', 'Angelica', 'Anna', 'Audrey', 'Aurelie',
    'Ava', 'Carlos', 'Chantal', 'Claire', 'Damayanti', 'Daniel', 'Diego',
    'Ellen', 'Federica', 'Fiona', 'Jorge', 'Juan', 'Karen', 'Kate', 'Lee',
    'Luca', 'Markus', 'Moira', 'Monica', 'Nicolas', 'Oliver', 'Paola',
    'Paulina', 'Petra', 'Samantha', 'Serena', 'Soledad', 'Susan', 'Tessa',
    'Thomas', 'Tom', 'Veena', 'Xander', 'Yannick',
)
