'''
Jerard Carney (NCB) New Chat bot
4/26/2021
bot_app.py
'''
'''""""""""""""""""""""""""""""""
LIBRARIES
'''""""""""""""""""""""""""""""""
'''
LIB. IMPORTS
'''
import random as rand
import json as json_file_type
import pickle as py_ickle
import numpy as python_numbers
import nltk as language_processor
import speech_recognition as recognizer
import pyttsx3 as speak
'''
IMPORT PULLS
'''
from nltk.stem import WordNetLemmatizer as stemmer
from tensorflow.keras.models import load_model as tensorflow_load_model
language_processor.download()
'''
INITIALIZE IMPORTS/PULLS
'''
lemmatizer = stemmer


'''""""""""""""""""""""""""""""""
DEFINED FUNCTIONS
'''""""""""""""""""""""""""""""""
# OPEN .json FILES
def open_json_files(json_file):
    # take .json given and open it
    # obj for .json file content
    data = json_file_type.loads(open(json_file, 'r').read())
    # ERROR HANDLE PRINT!!!
    # print(data)
    # return obj content from .json file
    return data


# OPEN .pkl FILES
def open_pkl_file(pkl_file):
    # take .pkl given and open it
    # obj for .pkl file content
    data = py_ickle.load(open(pkl_file, 'rb'))
    # ERROR HANDLE PPRINT!!!
    # print(data)
    # return obj content from .pkl file
    return data


# CLEAN-UP SENTENCE
def clean_up_sentence(sentence):
    # tokenize (Split apart words) the sentence content
    # stem each word in each sentence passed in
    # return the cleaned sentence
    # ERROR HANDLE PPRINT!!!
    # print(sentence)
    sentence_content = language_processor.word_tokenize(sentence)
    # ERROR HANDLE PPRINT!!!
    # print(sentence_content)
    sentence_content = [lemmatizer.lemmatize('r', word)for word in sentence_content]
    # ERROR HANDLE PPRINT!!!
    # print(sentence_content)
    return sentence_content


# MAKE OBJECT CONTAINER FOR WORDS FROM SENTENCE
def word_container_object_creation(sentence):
    # clean up sentence with function
    # make an object with place equal to the length of the list words.
    sentence_content = clean_up_sentence(sentence)
    # ERROR HANDLE PPRINT!!!
    # print(sentence_content)
    container_object = [0] * len(words)

    # for each word in sentence content:
    for x in sentence_content:
        # ERROR HANDLE PPRINT!!!
        # print(x, sentence_content)
        # for each in list of words from .pkl
        for y, word in enumerate(words):
            # ERROR HANDLE PPRINT!!!
            # print(y, x, word, words)
            # if the word is in the correct index
            if word == x:
                # ERROR HANDLE PPRINT!!!
                # print('Word = X: True')
                # container list at index to true = (1)
                # otherwise this it is 0
                container_object[y] = 1
    # return the container of words as array
    return python_numbers.array(container_object)


# CALCULATE POSSIBILITY OF INTENT
def understand_label(sentence):
    # obj for list of wards from container creation
    # obj for the model to predict the words in the word container 0= matching format in the list
    # ERROR LIMIT, if the predict is less the 25 percent correct(SURE) Ties into use of softmax function
    # ID if the result is less then 25% correct
    # used lambda cause of single use of anonymous function, sort list in reverse
    # make empty list to load and return
    word_container = word_container_object_creation(sentence)
    # ERROR HANDLE PPRINT!!!
    # print(word_container)
    res = ai_model.predict(python_numbers.array([word_container]))[0]
    # ERROR HANDLE PPRINT!!!
    # print(res)
    ERROR_LIMIT = 0.50
    result = [[x, y] for x, y in enumerate(res) if y > ERROR_LIMIT]
    result.sort(key=lambda x: x[1], reverse=True)
    return_result_list = []

    # for each item in the sorted result list which is 2D
    for item in result:
        # add to the new return list in sorted order (INDEX WISE) as intent to possibility string.
        return_result_list.append({'intent': labels[item[0]], 'probability': str(item[1])})
        
    # return this new results list of intent and possibility
    return return_result_list

# CREATE SPEECH RECOGNIZER
def create_recognizer():
    # set recognizer to object
    # return recognizer
    r = recognizer.Recognizer()
    return r


# USE MIC SOURCE
def use_mic_as_source(text_recognizer):

    # with the mic as audio source
    with recognizer.Microphone() as source:
        # assign audio from mic to object
        audio = text_recognizer.listen(source)

        # ERROR HANDLE
        # try block
        try:
            # assign recognized audio to object
            # print what is heard
            voice_data = text_recognizer.recognize_google(audio)
            print(f'Me: {voice_data}')
        # if this fails
        except:
            # print you can't be heard
            print('sorry i could not her you')
            # while not hearing you voice
            while voice_data != text_recognizer.recognize_google(audio):
                # run function again to hear voice
                use_mic_as_source()
    # return voice data for input
    return voice_data


# READ ALLOUD TO USER
def read_to_user(text_to_read):
    # create read object
    converter = speak.init()
    # set read rate to 151
    converter.setProperty('rate', 151)
    # set read volume
    converter.setProperty('volume', 0.7)
    # assign FEMALE voice location to object
    voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
    # set read voice to female
    converter.setProperty('voice', voice_id)
    # tell to passed read value
    converter.say(text_to_read)
    # pause program while reading
    converter.runAndWait()


# GET USER INPUT
def get_responce(intent_list, intent_json):
    # obj for list of user intents
    # obj for actual json intents
    tag = intent_list[0]['intent']
    list_of_intent = intent_json['intent']

    # for each item in json intents
    for x in list_of_intent:
        # if tag in diction is equal to the input tag
        if x['tag'] == tag:
            # pick a random result to answer back.
            # break
            result = rand.choice(x['response'])
            break
    # return the answer
    return result


'''""""""""""""""""""""""""""""""
WORD STEMMER AND FILE CREATIONS
'''""""""""""""""""""""""""""""""
'''
CONSTANTS
'''
# obj to hold json files intent dictionary
# obj to hold pkl file words 'rb' = read binary mode
# obj to hold pkl file labels 'rb' = read binary mode
# obj to load ai network model
intent = open_json_files('intent.json')
words = open_pkl_file('words.pkl')
labels = open_pkl_file('labels.pkl')
ai_model = tensorflow_load_model('ai_model.h5')
text_recognition = create_recognizer()
# ERROR HANDLE PPRINT
# print(intent)
# print(words)
# print(labels)
# print(ai_model)


'''""""""""""""""""""""""""""""""
BOT APP LOOP 
'''""""""""""""""""""""""""""""""

while True:
    # message = input("Me: ")
    message = use_mic_as_source(text_recognition)
    intents = understand_label(message)
    result = get_responce(intents, intent)
    read_to_user(result)
    # print(result)
    print(f'Sierra:  {result}')
