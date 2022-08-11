'''
Jerard Carney (NCB) New Chat bot
4/26/2021
ai_app.py
'''

'''""""""""""""""""""""""""""""""
LIBRARIES
'''""""""""""""""""""""""""""""""
'''
LIB. IMPORTS
'''
import nltk as language_processor
import pickle as py_ickle
import numpy as python_numbers
import tensorflow
import random as rand
import json as json_file_type
'''
IMPORT PULLS
'''
from nltk.stem import WordNetLemmatizer as stemmer
from tensorflow.keras.models import Sequential as seq_model
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD
'''
IMPORT DOWNLOADS
'''
language_processor.download('punkt')
language_processor.download('wordnet')
'''
INITIALIZE IMPORTS/PULLS
'''
lemmatizer = stemmer()


'''""""""""""""""""""""""""""""""
DEFINED FUNCTIONS
'''""""""""""""""""""""""""""""""
# OPEN .json FILES
def open_json_files(json_file):
    # take .json given and open it
    # obj for .json file content
    data = json_file_type.loads(open(json_file).read())
    # ERROR HANDLE PRINT!!!
    # print(open_json_files('intent.json'))
    # return obj content from .json file
    return data


# SAVE TO .pkl FILE
def save_pkl_file(words, label):
    # save list of words to .pkl file
    # save list of labels to . pkl file of new words
    py_ickle.dump(words, open('words.pkl', 'wb'))
    py_ickle.dump(label, open('labels.pkl', 'wb'))


# DATA SHUFFLER
def shuffle_data(data):
    # randomly shuffle data from list
    # load shuffled data into a new array obj
    # return new array obj
    rand.shuffle(data)
    data = python_numbers.array(data, dtype=object)
    return data


'''""""""""""""""""""""""""""""""
WORD STEMMER AND FILE CREATIONS
'''""""""""""""""""""""""""""""""
'''
CONSTANTS
'''
# obj for intentions
# list for stemmed words
# list for labels of stemmed words via json dictionary
# list for load intentions via json dictionary
# list of undesired characters to be ignore when stemming
intent_data = open_json_files('intent.json')
words = []
labels = []
docs = []
ignore_char_list = ['?', '!', '.', ',']


'''
WORD STEMMING PROCESS
'''
# for each item in the dictionary intent:
for intent in intent_data['intent']:
    # for each "pattern" in each item of intent
    for pattern in intent['pattern']:
        # tokenize(spilt) the words that are in the item patterns
        # add the to the tokenized words to a word list
        # change a 2d list in a document list of word to tag in dictionary
        tokenized_words = language_processor.word_tokenize(pattern)
        words.extend(tokenized_words)
        docs.append((tokenized_words, intent['tag']))

        # if the tag of intent is not in the dictionary
        if intent['tag'] not in labels:
            # change the labels list to include new tag
            labels.append(intent['tag'])
# ERROR HANDLE PRINT!!!
# print(docs)


'''
CREATING WORD SORTED SETS LIST
'''
# go through items in list and get rid of unwanted chars.
# sort the words in the word list
# sort the words in the label list
words = [lemmatizer.lemmatize(word) for word in words if word not in ignore_char_list]
words = sorted(set(words))
labels = sorted(set(labels))
# ERROR HANDLE PRINT!!!
#print(words)


'''
SAVE WORDS TO .pkl FILE
'''
# Save sets to file
save_pkl_file(words, labels)


'''""""""""""""""""""""""""""""""
MACHINE LEARNING MECHANICS
'''""""""""""""""""""""""""""""""
'''
CONSTANTS
'''
# trainer list to be fed into Neuro net
# output template, this has spots (0)s equal to the number of labels
train = []
output_void = [0] * len(labels)

'''
TRAINER SETUP
'''
# each word in documents:
for document in docs:
    # make and object for it to hold group of words
    # start at index 0 to group words
    # stem all words into lower case
    word_bag = []
    word_patterns = document[0]
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]

    # for each item in the list words:
    for word in words:
        # if the word is a pattern word:
        word_bag.append(1) if word in word_patterns else word_bag.append(0)

    # copy output list
    # add output to the right label and index and set to 1
    # then append the training list with the newly organized output
    output_row = list(output_void)
    output_row[labels.index(document[1])] = 1
    train.append([word_bag, output_row])

'''
SHUFFLE DATA FOR RESPONSES
'''
# training list get shuffle and put into an array
# x value is set with list values
# y value is set with list values
'''
# OPTIONAL FOR FUNCTION
# train = shuffle_data(train)
# rand.shuffle(train)
# train = python_numbers.array(train, dtype=object)
'''
train = shuffle_data(train)
training_alpha = list(train[:, 0])
training_beta = list(train[:, 1])


'''""""""""""""""""""""""""""""""
NEURO NETWORK
'''""""""""""""""""""""""""""""""
'''
NETWORK MODEL
'''
# make sequential model
network_model = seq_model()
# layer 1
network_model.add(Dense(128, input_shape=(len(training_alpha[0]),), activation='relu'))
network_model.add(Dropout(0.5))
# layer 2
network_model.add(Dense(64, activation='relu'))
network_model.add(Dropout(0.5))
# add to trainer
network_model.add(Dense(len(training_beta[0]), activation='softmax'))
'''
NESTEROV/SGD EXPLAINED - I choose eto use nestrov because if the small incrementation. ot in this
case de incrementation. THis is a great determiner for the large chucks of data being fed into
the network. I wouldn't use this without the (SGD) Stochastic Gradiant Decent. The SGD with analyze
each data bpoint after at a certain interval and allow a more accurate determination of what the 
data goal is. ALSO SEE - Mini Batch Gradiant Decent, which is what we are mimicking here. This 
momentum will push the likelyhood of the data passed an anomaly and the nesterov will simulate batches.
To prevent the momentum from being to grat in the random batches the network sees, we will decay the 
momentum over time. Basically if all is well gain momentum, if something strange happens slow down.
'''
stochastic_gradiant_decent = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
network_model.compile(loss='categorical_crossentropy', optimizer=stochastic_gradiant_decent,
                      metrics=['accuracy'])

# cycle training data 200 time into the network at a batch size of 5. Thiw will give us a good amount of data to use.
network_model_object = network_model.fit(python_numbers.array(training_alpha), python_numbers.array(training_beta), epochs=200,
                  batch_size=5, verbose=1)

# save the network model as an .h5
network_model.save('ai_model.h5', network_model_object)

# let user know process is done
print('DONE')