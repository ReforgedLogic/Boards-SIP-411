'''
# -------------------------------
# IMPORTS LIBRARIES
# -------------------------------
'''
# import personalities.py
# import bot_setup_function.py
import personalities as persona
import bot_setup_functions as func
from chatbot_gui import ChatbotGUI


'''
# -------------------------------
# CHAT ENGINE
# -------------------------------
'''
# call name function and load chatbot name to variable
vader = func.get_chatbot_name()

# Packages used to Train your chatbot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# Setting trainers for personalities basic, empire, rebel, jedi, and prebuilt
trainer_basic = ListTrainer(vader)
trainer_empire = ListTrainer(vader)
trainer_rebel = ListTrainer(vader)
trainer_jedi = ListTrainer(vader)
trainer = ChatterBotCorpusTrainer(vader)

# Standard personality chatterbot comes with and added basic,empire, rebel, jedi
trainer.train('chatterbot.corpus.english')
trainer_basic.train(persona.leading_dialog)
trainer_empire.train(persona.vader)
trainer_rebel.train(persona.rebels)
trainer_jedi.train(persona.jedi)


'''
# -------------------------------
# CHAT ENGINE
# -------------------------------
'''
# chatbot GUI settings and initialization
app = ChatbotGUI(
    # GUI title
    # gif used for talking
    # time stamp of chatbot response
    # default voice options
    title="Bow before the Empire!!",
    gif_path="vader.gif",
    show_timestamps=True,
    default_voice_options={
        # rate of speech
        # sound volume
        # voice is male
        "rate": 100,
        "volume": 0.8,
        "voice": "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
    }
)


'''
# -------------------------------
# DEFINE INCOMING MESSAGE HANDLING
# -------------------------------
'''
@app.event
def on_message(chat: ChatbotGUI, text: str):
    # print the text the user entered to console
    print("User Entered Message: " + text)

    # Intercept messages
    # if the user send the "clear" message clear the chats
    if text.lower().find("erase chat") != -1:
        # clear chat GUI
        chat.clear()
    # user can say any form of bye to close the chat.
    elif text.lower().find("bye" or "goodbye") != -1:
        # define a callback which will close the application
        def close():
            # exit chat GUI
            chat.exit()
        # send the goodbye message and provide the close function as a callback
        chat.send_ai_message("The Empire will reign for a millennia to come. Now, get out of my site.", callback=close)
    elif text.lower().find("hello" or "hi") != -1:
        # send the hi message and provide the close function as a callback
        chat.send_ai_message("Where are the rebels and there hidden base?")
    elif text.lower().find('no') != -1:
        # send the no message and provide the close function as a callback
        chat.send_ai_message("Reconsider your choice.")
    elif text.lower().find('yes') != -1:
        # send the yes message and provide the close function as a callback
        chat.send_ai_message('Very good')
    else:
        # offload chat bot processing to a worker thread and also send the result as an ai message
        chat.process_and_send_ai_message(vader.get_response, text)


'''
# -------------------------------
# RUN APP
# -------------------------------
'''
# run the chat bot application
app.run()
