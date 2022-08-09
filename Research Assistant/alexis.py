# Jerard Carney
# AI Assistant Assignment
# alexis.py
# py v3.9


# -----------------------------------------
# IMPORTED LIB
# -----------------------------------------
# import wikipedia libraries as var wiki
# import speech recognition as var sr
# import text wrap as wrap
# import talk to text (pyttsx3) as speak
import wikipedia as wiki
import speech_recognition as sr
import textwrap as wrap
import pyttsx3 as speak

# -----------------------------------------
# VARIABLE
# -----------------------------------------
# User Variables ++++++++++++++++++++++++++
# user first name str
first_name = ''
# user last name str
last_name = ''
# user full name str
full_name = ''
# user search topic
user_search = ''

# AI Variables +++++++++++++++++++++++++++
# ai name
ai_name = 'Alexis'

# Data Variables +++++++++++++++++++++++++
# raw wiki page data object
raw_data = wiki
# speech recognizer object
r = sr
# output to file object
output_to_file = ''


# -----------------------------------------
# DEFINED FUNCTIONS
# -----------------------------------------
# get user first name
def user_first_name():
    # touch global variable
    # get first name from mic
    global first_name
    first_name = use_mic_as_source()


# get user last name
def user_last_name():
    # touch global variable
    # get last name from mic
    global last_name
    last_name = use_mic_as_source()


# get user search topic
def user_topic():
    # touch global variable
    # get search topic from mic
    global user_search
    user_search = use_mic_as_source()


# get page data from wiki
def topic_search_page():
    # touch global variable
    # page data set to variable object
    global raw_data
    raw_data = wiki.page(user_search)


# set acceptable search topic
def actual_topics():
    # touch global variable
    # formatting
    # print searchable pages
    # formatting
    global user_search
    print('+' * 72)
    print(wiki.search(user_search))
    print('+' * 72)
    # call read aloud function (fluff)
    read_to_user(f'Please pick one of the topics I have presented you. ')
    # print (fluff with user topic)
    print(f'Please pick one of the above topics based on {user_search}: ')
    # user topic is new acceptable topic from mic
    user_search = use_mic_as_source()


# speech recognition recognizer
def recognizer():
    # touch global variable
    # set recognizer to object
    global r
    r = sr.Recognizer()


# set output to file to object
def raw_data_to_file():
    # touch global variable
    # assign page data to var object
    global output_to_file
    output_to_file = raw_data.content


# read text to user
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


# user name info
def gather_user_name():
    # touch global variable
    # holder var false for while loop
    # list var for if statement
    # user var as object for if statement
    # fluff text for first name
    # fluff text for last name
    # fluff text to confirm name
    global full_name
    correct = False
    key = {'YES', 'Yes', 'yes'}
    answer = ''
    first_text = f'Please say your first name.'
    last_text = f'And your last?'
    confirm_text = 'Is this your name? '

    # as long as the full name is not correct
    while correct == False:
        # ai ask for first name
        # ai print for first name
        # call function to assign first name
        read_to_user(first_text)
        print(first_text)
        user_first_name()
        # ai ask for last name
        # ai print for last name
        # call function to assign last name
        read_to_user(last_text)
        print('\n' + last_text)
        user_last_name()
        # ai ask confirm full name
        # ai print  confirm full name
        # call user mic to yes/no name
        read_to_user(f'\n {confirm_text} {first_name} {last_name}')
        print(f'\n{confirm_text} {first_name} {last_name}')
        answer = use_mic_as_source()

        # if name is correct (yes)
        if answer in key:
            # correct var is changed true
            # first and last name assign to full name object
            correct = True
            full_name = f'{first_name} {last_name}'
        # anything else
        else:
            # name correct is no, stay in while loop
            correct == False


# search functions called in one main function
def search_mechanic():
    # fluff
    # get user topic
    # show searchable topics based on user topic
    # search wiki page on allowed topic
    print(f'\t{first_name} please say the topic you would like me to search for you.')
    user_topic()
    actual_topics()
    topic_search_page()


# display summary to user
def display_Summary():
    # touch global variable
    # assign summary data to wrapped object
    global raw_data
    wrapped_summary = wrap.wrap(raw_data.summary)

    # for each line in summary object (PARAGRAPH effect)
    for line in wrapped_summary:
        #print full line
        print(line)
    # formatting
    # formatting
    print('+' * 72)
    print('\n')


def display_full_content():
    global raw_data
    # wrapped_content = wrap.wrap(raw_data.content)
    # for line in wrapped_content:
        # print(line)
    print(raw_data.content)
    print('+' * 72)
    print('\n')


# use mic as input source
def use_mic_as_source():
    # speech recognition recognizer
    recognizer()

    # with the mic as audio source
    with sr.Microphone() as source:
        # assign audio from mic to object
        audio = r.listen(source)

        # ERROR HANDLE
        # try block
        try:
            # assign recognized audio to object
            # print what is heard
            voice_data = r.recognize_google(audio)
            print(voice_data)
        # if this fails
        except:
            # print you can't be heard
            print('sorry i could not her you')
            # while not hearing you voice
            while voice_data != r.recognize_google(audio):
                # run function again to hear voice
                use_mic_as_source()
    # return voice data for input
    return voice_data

# create and right page to file
def write_to_file(text_to_file):
    # fluff
    # make a file with desired name, keep character formatting
    # write page data to the file
    # tell user success
    print('Name your file to save you essay to')
    essay_file = open(use_mic_as_source(), 'w', encoding='utf-8')
    essay_file.write(text_to_file)
    read_to_user('Congratulations! Your file has been created. ')


# Formatting/fluff Defined Function
def application_title():
    # opening block fluff
    print('+' * 36)
    print('+' + ' ' * 34 + '+')
    print('+' + ' ' * 34 + '+')
    print('+' + ' ' * 14 + ai_name + ' ' * 14 + '+')
    print('+' + ' ' * 9 + 'AI Search Engine' + ' ' * 9 + '+')
    print('+' + ' ' * 34 + '+')
    print('+' + ' ' * 34 + '+')
    print('+' * 36)
    print('\n')
    # call read aloud to user instruction and welcome
    read_to_user(f'Welcome. I am {ai_name}. Your new AI assistant.')
    read_to_user("I'll be asking you some questions while assisting you today. "
                 "To make sure we don't mis-communicate, please be sure to speak clearly. "
                 "and wait a few seconds after I'm done talking before you respond. "
                 "Thank You. "
                 "Now, lets get this show on the road. ")


# ask if user is ready to start
def alexis_welcomes_user():
    # object var for while loop
    # list var for while loop
    # object var for while loop
    # fluff for welcome
    # fluff for yes ready
    # fluff for no ready
    answer = ''
    key = {'YES', 'Yes', 'yes', 'READY', 'Ready', 'ready', '[Ready]'}
    confirm = False
    text = f'Welcome {full_name}. ' \
           f'I will be assisting you in searching Wikipedia. ' \
           f'Shall we begin? '
    text_no = "Okay, let me know when you're ready by saying, ready. "
    text_yes = 'Great! lets begin. '

    # call read aloud fluff
    read_to_user(text)
    # formatting welcome
    print('\n')
    print('+' * 72)
    print(f'\tWelcome {full_name}. ')
    print(f'\tI will be assisting you in searching Wikipedia')
    print("\tAre you ready to begin? ")
    # answer var object change to mic input
    answer = use_mic_as_source()

    # while not ready
    while confirm == False:
        # if answer is ready
        if answer in key:
            # break out of loop
            # call read aloud fluff
            confirm = True
            read_to_user(text_yes)
        # otherwise
        else:
            # user not ready stay in loop
            # call read aloud fluff
            # print fluff
            # get new input for answer object
            confirm == False
            read_to_user(text_no)
            print('\n\tOk, let me know when your ready by saying [Ready]')
            answer = use_mic_as_source()
    # formatting
    # formatting
    print('+' * 72)
    print('\n')


# explain search topic process
def alexis_explains_process():
    # fluff
    text = f'Before I ask for your topic, know that Wikipedia does not have a ' \
           f'page for everything. They come close, but not every topic is searchable ' \
           f'in exact wordage. To help you with this I will present a list of pages ' \
           f'you can search based on your topic. An example is car. There is no page specifically for the word car,' \
           f'but there is a page for electric car, model T, and so on. I will display these alternate pages  ' \
           f'for you to choose. When you are ready and chosen one, just say the topic you want. '
    # call read aloud for fluff
    read_to_user(text)


# display function for page data
def alexis_displays_data():
    # summary var object
    # content var object
    # readable var object
    # fluff text summary
    # fluff text content
    summary = ''
    content = ''
    read_content = ''
    text_confirm_summary = 'Results found. Would you like to see and here a summary? '
    text_confirm_content = 'Would you also like to see the full content? '

    # call read aloud fluff summary
    # mic input assigned to summary object
    read_to_user(text_confirm_summary)
    summary = use_mic_as_source()

    # if user wants to see and here summary
    if summary == 'yes':
        # call read aloud fluff
        # formatting
        read_to_user(f'{first_name}, here is a summary of what I found for {user_search}')
        print('+' * 72)
        print('\n')
        print(f'\t- SUMMARY\n')
        # call to display summary
        display_Summary()
        # call to read out summary
        read_to_user(raw_data.summary)

    # does user want be read/see content?
    # assign mic input to confirm object
    read_to_user(text_confirm_content)
    content = use_mic_as_source()

    # if they want to see content
    if content == 'yes':
        # call read aloud fluff
        # formatting
        # formatting
        # call to display full content
        read_to_user(f'And here is the full content of my search')
        print('+' * 72)
        print(f'\t- FULL CONTENT \n')
        display_full_content()

        # ask if user wants to be read content
        # assign mic input to confirm object
        read_to_user(f'Would you like me to read the full content? this could be long, '
                     f'and I cannot stop once I begin.')
        read_content = use_mic_as_source()

        # if want to here content
        if read_content == 'yes':
            # call read aloud to be read all content
            read_to_user(raw_data.content)


# ai explains write file process
def alexis_explains_file():
    # fluff
    text = f"Awesome! Now that we have information that you're looking for we should save it for later. " \
           f'{first_name}, please think of a file name and when prompted say your desired name. '
    # call read aloud fluff
    read_to_user(text)


# ai explain how to find new file and says by
def alexis_direct_user_to_file():
    # fluff
    text = f'Now that you have saved your file, you can find it in the File Explore ' \
           f'in the same folder that you have your python alexis file. ' \
           f'It will have the name that you created a second ago, and it will have ' \
           f'all the information we found together. ' \
           f"Thank you again for allowing me to help you today. Don't be a stranger and " \
           f"come back anytime you need help with research. Bye"
    # call read aloud fluff
    read_to_user(text)


# -----------------------------------------
# -----------------------------------------
# MAIN PROGRAM
# -----------------------------------------
# -----------------------------------------
# greets user
application_title()
# gets users name
gather_user_name()
# Welcomes user if ready
alexis_welcomes_user()
# AI tells user how to search
alexis_explains_process()
# user topic is search on Wikipedia
search_mechanic()
# AI displays/reads page data
alexis_displays_data()
# AI prepares to write page data to file
raw_data_to_file()
# AI explains to user how to make file
alexis_explains_file()
# AI creates file and writes data to it
write_to_file(output_to_file)
# AI finishes closing remarks and file location to user
alexis_direct_user_to_file()

