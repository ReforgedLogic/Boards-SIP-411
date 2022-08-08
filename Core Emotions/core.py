# Jerard Carney
# 12/18/21
# App 5 (FINAL PROJECT - Emotion)


#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
# Libraries/Modules
#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
# imported numpy numbers
# sklearn classifier tree
# pandas for .csv files
import numpy as numpy
from sklearn import tree
import pandas as pandas


#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
# UX and Input Functions
#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
# welcome and explanation UX
def welcome_mat():
    print('<><><><><><><><><><><><-><><><><><><><><><><><>\n')
    print('<><><><><><><><><>  Welcome  <><><><><><><><><>\n')
    print('<><><><><><><><>< to Emotions ><><><><><><><><>\n')
    print('<><><><><><><><><><><><-><><><><><><><><><><><>\n\n')
    print('This simulation uses Machine learning to predict\n',
    'a proper emotional responce to a stimuli, input that\n',
    'you "the user" give it or from experience you yourself\n',
    'feel at this moment. whether you emulate your emotion\n',
    'or attempt a new one the result will shock you.\n\n',
    'How does this work?\n',
    'I researched basic emotions that tie with biologic, hormonal,\n',
    'arousal types, and stimuli pathways to create an emotional\n',
    'network. In term of the ML the takes data and predicts\n',
    'sub-emotions form hormones, compares them with\n', 
    'core emotional states, currrent states, stimuli inputs/paths\n',
    'to form a current emotion. To sum this up the ML is using\n',
    'prediction to compare againts other data and prdiction to\n',
    'find a happy medium/accurate emotional state.\n\n')
    print("The best thing to do is to pretent you are\n",
    "acting out and event(opeing a present, a kiss,\n",
    'drinking coffee, etc).\n',
    "Just follow the prompts below and enjoy!!\n\n")

# UX directions for BIO input
    # input for pupil
    # input for breathing
    # input for heart rate
    # input for blood sugar
    # input for mouth shape
    # return all values (they load into array)
def get_bio_input():
    print("<-><-><-><-><-><-><-><----------------------------\n")
    print("The following is asked as if being assested\n",
    "by another person looking at you or\n",
    "as you, realising your own current biological\n",
    "state of being.\n\n")
    print("<-><-><-><-><-><-><-><----------------------------\n")
    print("Choose a number of the following options",
    "to describe your Pupils: \n",
    "0 - Narrowed\n",
    "1 - Normal\n",
    "2 - Large\n",
    "3 - Dialated\n\n")
    pupil = input()
    print("<-><-><-><-><-><-><-><----------------------------\n")
    print("Choose a number of the following options",
    "to describe your Breathing: \n",
    "0 - Slowed\n",
    "1 - Normal\n",
    "2 - Quick\n",
    "3 - Heavy\n\n")
    breaths = input()
    print("<-><-><-><-><-><-><-><----------------------------\n")
    print("Choose a number of the following options",
    "to describe your Heart Rate: \n",
    "0 - Slowed\n",
    "1 - Normal\n",
    "2 - Quick\n",
    "3 - Very Fast\n\n")
    rate = input()
    print("<-><-><-><-><-><-><-><----------------------------\n")
    print("Choose a number of the following options",
    "to describe your Blood Sugar: \n",
    "0 - Low\n",
    "1 - Normal\n",
    "2 - High\n\n")
    sugar = input()
    print("<-><-><-><-><-><-><-><----------------------------\n")
    print("Choose a number of the following options",
    "to describe your Mouth: \n",
    "0 - Frowning\n",
    "1 - Smiling\n",
    "2 - Open Mouth\n\n")
    mouth = input()
    print("<-><-><-><-><-><-><-><----------------------------\n")
    return pupil, breaths, rate, sugar, mouth


# UX directions for AROUSAL type input
    # input for sight
    # input for hearing
    # input for smell
    # input for touch
    # input for taste
    # return all values (they load into array)
def get_arousal_input():
    print("<-><-><-><-><-><-><-><----------------------------\n")
    print("The following is asked as if being assested\n",
    "as if you have expeinced the arousal. This word arousal \n",
    "means activated, as your current input state.\n\n")
    print("<-><-><-><-><-><-><-><----------------------------\n")
    print("Was arousal from Sight? \n",
    "1 - Yes\n",
    "2 - No\n\n")
    sight = input()
    print("<-><-><-><-><-><-><-><----------------------------\n")
    print("Was arousal from Hearing? \n",
    "1 - Yes\n",
    "2 - No\n\n")
    hear = input()
    print("<-><-><-><-><-><-><-><----------------------------\n")
    print("Was arousal from Smell? \n",
    "1 - Yes\n",
    "2 - No\n\n")
    smell = input()
    print("<-><-><-><-><-><-><-><----------------------------\n")
    print("Was arousal from Touch? \n",
    "1 - Yes\n",
    "2 - No\n\n")
    touch = input()
    print("<-><-><-><-><-><-><-><----------------------------\n")
    print("Was arousal from Taste? \n",
    "1 - Yes\n",
    "2 - No\n\n")
    taste = input()
    print("<-><-><-><-><-><-><-><----------------------------\n")
    return sight, hear, smell, touch, taste


# UX directions for PATHWAY input
    # input for arms
    # input for legs
    # input for privates (G)
    # input for core
    # input for face
    # return all values (they load into array)
def get_path_input():
    print("<-><-><-><-><-><-><-><----------------------------\n")
    print("The following is asked as if being assested\n",
    "from where you feel the stimuli that made you feel emotion.\n",
    "Face is referring to (site, taste, and hearing).\n\n")
    print("<-><-><-><-><-><-><-><----------------------------\n")
    print("Was stimuli from your Arms? \n",
    "1 - Yes\n",
    "2 - No\n\n")
    arms = input()
    print("<-><-><-><-><-><-><-><----------------------------\n")
    print("Was stimuli from your Legs? \n",
    "1 - Yes\n",
    "2 - No\n\n")
    legs = input()
    print("<-><-><-><-><-><-><-><----------------------------\n")
    print("Was stimuli from your Privates? \n",
    "1 - Yes\n",
    "2 - No\n\n")
    pvt = input()
    print("<-><-><-><-><-><-><-><----------------------------\n")
    print("Was arousal from your Core? \n",
    "1 - Yes\n",
    "2 - No\n\n")
    core = input()
    print("<-><-><-><-><-><-><-><----------------------------\n")
    print("Was stimuli from your Face? \n",
    "1 - Yes\n",
    "2 - No\n\n")
    face = input()
    print("<-><-><-><-><-><-><-><----------------------------\n")
    return arms, legs, pvt, core, face


# get users current emotional state
    # UX directions
    # get input convert to lower case
    # variables for loop and emotional int ID
    # while loop (ACTIVE) as long ay they don pick correct word
    # if input is one of these emotions
        # break loop
        # emotion ID = a number
        # else stay in loop an repeat proccess
    # return emotion ID for array
def get_current_state():
    print("<-><-><-><-><-><-><-><----------------------------\n")
    print('Pre-deposition has alot to do with how you feel.\n',
    "This can make you feel a certain way from an\n",
    "empathetic stand-point. Please state the last\n",
    "emotion you felt or an emotion of the last person\n",
    "you were around within the last hour.\n")
    user_input = input().lower()
    emotion_to_int = 0
    loop = True
    while loop:
        if user_input == 'hungery':
            loop = False
            emotion_to_int = 3
        elif user_input == 'happy':
            loop = False
            emotion_to_int = 2
        elif user_input == 'bored':
            loop = False
            emotion_to_int = 1
        elif user_input == 'sleepy':
            loop = False
            emotion_to_int = 1
        elif user_input == 'angry':
            loop = False
            emotion_to_int = 3
        elif user_input == 'hopeless':
            loop = False
            emotion_to_int = 1
        elif user_input == 'joyful':
            loop = False
            emotion_to_int = 2
        elif user_input == 'excited':
            loop = False
            emotion_to_int = 2
        elif user_input == 'confused':
            loop = False
            emotion_to_int = 1
        elif user_input == 'silly':
            loop = False
            emotion_to_int = 2
        elif user_input == 'full':
            loop = False
            emotion_to_int = 2
        elif user_input == 'stressed':
            loop = False
            emotion_to_int = 3
        elif user_input == 'anxious':
            loop = False
            emotion_to_int = 3
        elif user_input == 'loving':
            loop = False
            emotion_to_int = 2
        elif user_input == 'joyful':
            loop = False
            emotion_to_int = 2
        elif user_input == 'gloomy':
            loop = False
            emotion_to_int = 1
        elif user_input == 'hateful':
            loop = False
            emotion_to_int = 3
        elif user_input == 'scared':
            loop = False
            emotion_to_int = 3
        elif user_input == 'fearful':
            loop = False
            emotion_to_int = 3
        elif user_input == 'flustered':
            loop = False
            emotion_to_int = 3
        elif user_input == 'furious':
            loop = False
            emotion_to_int = 3
        elif user_input == 'sad':
            loop = False
            emotion_to_int = 1
        elif user_input == 'malevolent':
            loop = False
            emotion_to_int = 1
        elif user_input == 'heroic':
            loop = False
            emotion_to_int = 2
        elif user_input == 'couragous':
            loop = False
            emotion_to_int = 2
        elif user_input == 'brave':
            loop = False
            emotion_to_int = 2
        elif user_input == 'cowardly':
            loop = False
            emotion_to_int = 1
        elif user_input == 'passionate':
            loop = False
            emotion_to_int = 2
        elif user_input == 'awakened':
            loop = False
            emotion_to_int = 2
        elif user_input == 'cherished':
            loop = False
            emotion_to_int = 2
        elif user_input == 'thoughtful':
            loop = False
            emotion_to_int = 2
        elif user_input == 'accomplished':
            loop = False
            emotion_to_int = 2
        elif user_input == 'comfortable':
            loop = False
            emotion_to_int = 2
        elif user_input == 'mad':
            loop = False
            emotion_to_int = 3
        elif user_input == 'upset':
            loop = False
            emotion_to_int = 1
        elif user_input == 'hurt':
            loop = False
            emotion_to_int = 3
        elif user_input == 'uncomfortable':
            loop = False
            emotion_to_int = 1
        elif user_input == 'comfortable':
            loop = False
            emotion_to_int = 2
        elif user_input == 'nervous':
            loop = False
            emotion_to_int = 3
        elif user_input == 'shy':
            loop = False
            emotion_to_int = 1
        elif user_input == 'afraid':
            loop = False
            emotion_to_int = 3
        elif user_input == 'sick':
            loop = False
            emotion_to_int = 1
        elif user_input == 'calm':
            loop = False
            emotion_to_int = 1
        elif user_input == 'sleepy':
            loop = False
            emotion_to_int = 1
        elif user_input == 'lathargic':
            loop = False
            emotion_to_int = 1
        elif user_input == 'tired':
            loop = False
            emotion_to_int = 1
        elif user_input == 'enraged':
            loop = False
            emotion_to_int = 3
        elif user_input == 'normal':
            loop = False
            emotion_to_int = 2
        else:
            print("<-><-><-><-><-><-><-><----------------------------\n")
            print("The list of emotins is simplified.\n", 
            "Please type another state: \n\n")
            user_input = input().lower()
    return emotion_to_int


#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
# Data Manipulation Functions
#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
# open (PASSED).csv file
    # read .csv data to object
    # retrun data
def open_csv(file_name):
    opened_file = pandas.read_csv(file_name)
    # [ERROR HANDLER] print(opened_file)
    return opened_file


# create an array with all data in csv file
    # call open_csv and load file to object
    # create new list object array
    # for each index, and row in the file iterate through them
        # data object equals the data per listed labls of that row
        # appened(add) to object array new data from each row
    # print to test logic and see array
    # return full object array
def create_full_data_array(string, label_1, label_2, label_3, label_4, label_5, label_6):
    data_frame = open_csv(string)
    updated_data_set = []
    for index, row in data_frame.iterrows():
        data_set = [row[label_1], row[label_2], row[label_3], row[label_4], row[label_5], row[label_6]]
        updated_data_set.append(data_set)
    # [ERROR HANDLER] print(updated_data_set)
    return updated_data_set


# create an array with data_set  in csv file (All but Hormones array)
    # call open_csv and load file to object
    # create new list object array
    # for each index, and row in the file iterate through them
        # data object equals the data per listed labls (all but target data) of that row
        # appened(add) to object array new data from each row
    # print to test logic and see array
    # return full object array
def creat_data_set_array(string, label_1, label_2, label_3, label_4, label_5):
    data_frame = open_csv(string)
    updated_data_set = []
    for index, row in data_frame.iterrows():
        data_set = [row[label_1], row[label_2], row[label_3], row[label_4], row[label_5]]
        updated_data_set.append(data_set)
    # [ERROR HANDLER] print(updated_data_set)
    return updated_data_set   


# create an array with data_set  in csv file (For Hormones array)
    # call open_csv and load file to object
    # create new list object array
    # for each index, and row in the file iterate through them
        # data object equals the data per listed labls (all but target data) of that row
        # appened(add) to object array new data from each row
    # print to test logic and see array
    # return full object array
def creat_beta_data_set_array(string, label_1, label_2, label_3):
    data_frame = open_csv(string)
    updated_data_set = []
    for index, row in data_frame.iterrows():
        data_set = [row[label_1], row[label_2], row[label_3]]
        updated_data_set.append(data_set)
    # [ERROR HANDLER] print(updated_data_set)
    return updated_data_set   


# create an array with target_set  in csv file
    # call open_csv and load file to object
    # create new list object array
    # for each index, and row in the file iterate through them
        # data object equals the data per listed labls (target data ONLY) of that row
        # appened(add) to object array new data from each row
    # print to test logic and see array
    # return full object array
def create_target_array(string, value):
    data_frame = open_csv(string)
    updated_target_set = []
    for index, row in data_frame.iterrows():
        target_set = row[value]
        updated_target_set.append([target_set])
    # [ERROR HANDLER] print(updated_target_set)
    return updated_target_set


# create an array with target set for hormones
    # take (PASSED) values
    # convert bio string to int
    # convert arousal string to int
    # convert path string to int
    # return converted ints (loads into an array)
def create_hormone_target_array(bio, arousal, path):
    int_bio = id_converter(bio)
    int_arousal = id_converter(arousal)
    int_path = id_converter(path)
    # [ERROR HANDLER] print(int_bio, int_arousal, int_path)
    return int_bio, int_arousal, int_path


# create an array with target set for emotions
    # take (PASSED) values
    # get user current emotion notion, state, or environment
    # get primary hormone used
    # convert bio string to int
    # convert arousal string to int
    # convert path string to int
    # return converted ints (loads into an array)
def create_emotion_target_array(bio, arousal, path, state, hormone):
    current_state = state
    primary_hormone = hormone
    int_bio = id_converter(bio)
    int_arousal = id_converter(arousal)
    int_path = id_converter(path)
    # [ERROR HANDLER] print(int_bio, int_arousal, int_path, current_state, primary_hormone)
    return int_bio, int_arousal, int_path, current_state, primary_hormone


# string convert to int value
    # take (PASSED) value
    # int_value object
    # if string is one of these words
        # int_value = a number
        # else print string
    # return int_value for array
def id_converter(string):
    int_value = 0
    if string == 'happy':
        int_value = 2
    elif string == 'sad':
        int_value = 1
    elif string == 'fear':
        int_value = 3
    elif string == 'mad':
        int_value = 1
    elif string == 'disgust':
        int_value = 3
    elif string == 'mild':
        int_value = 1
    elif string == 'strong':
        int_value = 2
    elif string == 'intense':
        int_value = 3
    elif string == 'extreme':
        int_value = 4
    elif string == 'limbic':
        int_value = 1
    elif string == 'hippocampus':
        int_value = 2
    elif string == 'cortex':
        int_value = 3
    elif string == 'amygdala':
        int_value = 4
    elif string == 'cerecbellum':
        int_value = 5
    elif string == 'temporal':
        int_value = 6
    elif string == 'dopamine':
        int_value = 1
    elif string == 'adrenaline':
        int_value = 2
    elif string == 'serotonin':
        int_value = 3
    elif string == 'cortisol':
        int_value = 4
    else:
        # [ERROE HANDLING]
        print(string)
    return int_value

#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
# Training/Prediction Functions
#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
# create classifier tree
    # make classifier tree object
    # return classifier of pairs data and target in tree
def create_classifier_tree(data, target):
    classifier = tree.DecisionTreeClassifier()
    return classifier.fit(data, target)


# make prediction
    # make prediction object comparing classifier to target
    # return prediction
def make_comparison_prediction(classifier, target):
    prediction = classifier.predict(target)
    return prediction


#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
# Main Application
#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
# call UX instructions
welcome_mat()
# loop key
# program repeat loop start state = ACTIVE
loop = True
while loop:
    # create bio full data set
    # create bio training data array - target
    # create bio data array target ONLY
    bio_full_data_set = create_full_data_array('biological_factors.csv', 'pupil', 'breathing', 'heart_rate', 'blood_sugar', 'mouth', 'emotion')
    bio_training_data_set = creat_data_set_array('biological_factors.csv', 'pupil', 'breathing', 'heart_rate', 'blood_sugar', 'mouth')
    bio_target_data_set = create_target_array('biological_factors.csv', 'emotion')
    # [ERROR HANDLING] print(bio_full_data_set)
    # [ERROR HANDLING] print(bio_training_data_set)
    # [ERROR HANDLING] print(bio_target_data_set)
    # create arousal full data set
    # create arousal training data array - target
    # create arousal data array target ONLY
    arousal_type_full_data_set = create_full_data_array('input_type.csv', 'seeing', 'hearing', 'smelling', 'touching', 'tasting', 'level')
    arousal_type_training_data_set = creat_data_set_array('input_type.csv', 'seeing', 'hearing', 'smelling', 'touching', 'tasting')
    arousal_type_target_data_set = create_target_array('input_type.csv', 'level')
    # [ERROR HANDLING] print(arousal_type_full_data_set)
    # [ERROR HANDLING] print(arousal_type_training_data_set)
    # [ERROR HANDLING] print(arousal_type_target_data_set)
    # create path full data set
    # create path training data array - target
    # create path data array target ONLY 
    path_full_data_set = create_full_data_array('path.csv', 'arms', 'legs', 'privates', 'core', 'face', 'brain_location')
    path_training_data_set = creat_data_set_array('path.csv', 'arms', 'legs', 'privates', 'core', 'face')
    path_target_data_set = create_target_array('path.csv', 'brain_location')
    # [ERROR HANDLING] print(path_full_data_set)
    # [ERROR HANDLING] print(path_training_data_set)
    # [ERROR HANDLING] print(path_target_data_set)
    # train bio tree
    # train arousal tree
    # train path tree
    trained_bio = create_classifier_tree(bio_training_data_set, bio_target_data_set)
    trained_arousal = create_classifier_tree(arousal_type_training_data_set, arousal_type_target_data_set)
    trained_path = create_classifier_tree(path_training_data_set, path_target_data_set)
    # [ERROR HANDLING] print(trained_bio)
    # [ERROR HANDLING] print(trained_arousal)
    # [ERROR HANDLING] print(trained_path)
    # get user input for bio target
    # get user input for arousal target
    # get user input for path target
    user_bio = [get_bio_input()]
    user_arousal = [get_arousal_input()]
    user_path = [get_path_input()]
    # [ERROR HANDLING] print(user_bio)
    # [ERROR HANDLING] print(user_arousal)
    # [ERROR HANDLING] print(user_path)
    # make prediction for bio
    # make prediction for arousal
    # make prediction for path
    predict_bio = make_comparison_prediction(trained_bio, user_bio)
    predict_arousal = make_comparison_prediction(trained_arousal, user_arousal)
    predict_path = make_comparison_prediction(trained_path, user_path)
    # [ERROR HANDLING] print(predict_bio)
    # [ERROR HANDLING] print(predict_arousal)
    # [ERROR HANDLING] print(predict_path)
    # create hormone training set array
    # create target data set array
    # train hormone tree
    # create user targets array
    # make prediction for hormones
    hormone_training_data_set =  creat_beta_data_set_array('hormones.csv', 'bio', 'arousal', 'path')
    hormone_target_data_set = create_target_array('hormones.csv', 'hormone')
    trained_hormones = create_classifier_tree(hormone_training_data_set, hormone_target_data_set)
    target_hormones = [create_hormone_target_array(predict_bio, predict_arousal, predict_path)]
    predict_hormones = make_comparison_prediction(trained_hormones, target_hormones)
    # [ERROR HANDLING] print(hormone_training_data_set)
    # [ERROR HANDLING] print(hormone_target_data_set)
    # [ERROR HANDLING] print(predict_hormones)
    # create emotions training set array
    # create target data set array
    # train emotions tree
    # create user targets array
    # make prediction for final emotion
    emotion_training_data_set = creat_data_set_array('emotions.csv', 'bio', 'arousal', 'path', 'hormone', 'state')
    emotion_target_data_set = create_target_array('emotions.csv', 'final_emotion')
    trained_emotion = create_classifier_tree(emotion_training_data_set, emotion_target_data_set)
    target_emotion = [create_emotion_target_array(predict_bio, predict_arousal, predict_path, id_converter(predict_hormones), get_current_state())]
    predict_emotion = make_comparison_prediction(trained_emotion, target_emotion)
    # [ERROR HANDLING] print(predict_emotion) 
    # UX print results
        # main result emotion
        # core emotion
        # emotion intensity
        # brain path
        # primary hormone
    print("\n\nYou are ", predict_emotion, " when performing or emulating this activity.\n")
    print("STATS___________________________________")
    print("Core emotion:     ", predict_bio)
    print("Arousal Intesity: ", predict_arousal)
    print("Signal Path:      ", predict_path)
    print("Primary Hormone:  ", predict_hormones)
    print('\n\n')
    # run application again?
    # get user input to lower case
    # if yes or no
        # loop again or break loop and end
        # else break loop and end
   
    print('Run Program again? ')
    user_input = input().lower()
    if user_input == 'yes':
        loop = True
    elif user_input == 'no':
        loop = False
        print('Thanks for using Emotions, Bye')
    else:
        loop = False
        print('Thanks for using Emotions, Bye')

# <->
# END
# <->

 
