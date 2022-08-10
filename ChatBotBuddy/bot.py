'''
# -------------------------------
# IMPORT LIBRARIES
# -------------------------------
'''
# import chatterbot
# import personalities
from chatterbot import ChatBot as Sierra
import personalities as persona


'''
# -------------------------------
# IMPORT LIBRARIES
# -------------------------------
'''
# assign var with AI name
ai_vader = Sierra('Vader')

# set trainers
from chatterbot.trainers import ListTrainer as List
from chatterbot.trainers import ChatterBotCorpusTrainer as Corpus

# load AI training variables basic, empire, rebels, jedi, and prebuilt
trainer_basic = List(ai_vader)
trainer_empire = List(ai_vader)
trainer_rebel = List(ai_vader)
trainer_jedi = List(ai_vader)
trainer = Corpus(ai_vader)

# train ai with personalities basic, empire, rebels, jedi, and prebuilt
trainer.train("chatterbot.corpus.english")
trainer_basic.train(persona.leading_dialog)
trainer_empire.train(persona.empire)
trainer_rebel.train(persona.rebel)
trainer_jedi.train(persona.jedi)


'''
# -------------------------------
# IMPORT LIBRARIES
# -------------------------------
'''
# Chat APP... in CMD
# prompt interaction
print('I am Darth Vader, what is thy bidding?')

# loop in chatbot var
is_exit = False

# does user want to exit?
while is_exit == False:
    # get uer input
    user_input = input()

    # if use says bye
    if user_input.lower().find('bye') != -1:
        # user will exit
        is_exit = True
        print('You can not escape.')
    # if they say vader
    elif user_input.lower().find('vader') != -1:
        print("I am your father.")
    # if they say empire
    elif user_input.lower().find('empire') != -1:
        print('Join the empire.')
    # if they say death star
    elif user_input.lower().find('death star') != -1:
        print("Is nothing compared to the power of the force.")
    # if they say skywalker
    elif user_input.lower().find('skywalker') != -1:
        print('Anakin Skywalker is dead.')
    # if they say no
    elif user_input.lower().find('no') != -1:
        print("Reconsider your words.")
    # if they say yes
    elif user_input.lower().find('yes') != -1:
        print('Very good')
    # else
    else:
        # get perbuilt response from personality
        # print this response
        ai_response = ai_vader.get_response(user_input)
        print(ai_response)
