# Jerard Carney.AIAPPONE.11/21/21

#---------------------------------------
# Libs
#---------------------------------------
from sklearn import tree    # importing network tree
import json                 # importing json manipulation
import time                 # importing time manipulation


#---------------------------------------
# Defined Functions
#---------------------------------------
# delay program 2 seconds
def delay_2():
    time.sleep(2)


# delay program 5 seconds
def delay_5():
    time.sleep(5)


# rest user value string
    # variable = empty
    # return variable
def reset_user_input():
    var = ' '
    return var


# UI instructions
def instructions_characteristics_UI():
    print('###############################################')
    print('--- USER INSTRUCTION:')
    print('All measurements are metric or are a')
    print('numerical value of its own gauge.')
    print("Each spec will explain how to input.")


# UI instructions
def instructions_span_UI():
    print('###############################################')
    print('--- USER INSTRUCTION:')
    print('The wing span of a plane is the length')
    print('of wings from end to end. This is')
    print("in meters. There are 3.2ft per meter.")


# UI instructions
def instructions_engine_UI():
    print('###############################################')
    print('--- USER INSTRUCTION:')
    print('Enter the amount of visible engines')
    print('on the aircraft.')


# UI instructions
def instructions_engine_type_UI():
    print('###############################################')
    print('--- USER INSTRUCTION:')
    print('Enter the type of engine you can either')
    print('hear or see on the aircraft. The ')
    print("following input option are available.")
    print('0 = Propeller')
    print('1 = Jet Turbine')
    print("2 = Rocket")


# UI instructions
def instructions_length_UI():
    print('###############################################')
    print('--- USER INSTRUCTION:')
    print('The fuselage of a plane is the length')
    print('of the plane from front to end. This is')
    print("in meters. There are 3.2ft per meter.")


# UI instructions
def instructions_arms_UI():
    print('###############################################')
    print('--- USER INSTRUCTION:')
    print('Enter the number of armaments that are')
    print('visible on the plane. Fixed or turret')
    print("machine guns, missiles, and bombs all")
    print("count toward this.")


# UI instructions
def instructions_speed_UI():
    print('###############################################')
    print('--- USER INSTRUCTION:')
    print('This is how fast you perceive the planes')
    print('rate of movement. To help use the ')
    print("following scale. This is in kilometers/Hour.")
    print("You must enter a km/ph value.")
    print('Very Fast - 1000 km/ph')
    print('Fast - 800 km/ph')
    print("Quick - 600 km/ph")
    print('Cruising - 500 km/ph')
    print('Slow - 400 km/ph')
    print("Glide - 300 km/ph")


# UI instructions
def instructions_crew_UI():
    print('###############################################')
    print('--- USER INSTRUCTION:')
    print('Enter the amount of visible crew')
    print('compartments on the aircraft.')


# convert user input to usable list
    # reset user input variables to empty string for loop
    # delay for effect 2sec
    # display instruction for each input needed
    # get input for each variable for list
    # load variables into 2D list
    # return list
def user_inputs_to_list():
    span = reset_user_input()
    engine = reset_user_input()
    eng_type = reset_user_input()
    lgth = reset_user_input()
    arms = reset_user_input()
    spd = reset_user_input()
    crew = reset_user_input()
    delay_2()
    instructions_span_UI()
    span = input("Wingspan Length: ")
    instructions_engine_UI()
    engine = input("Number of Engines: ")
    instructions_engine_type_UI()
    eng_type = input("Type of Engine: ")
    instructions_length_UI()
    lgth = input("Fuselage Length: ")
    instructions_arms_UI()
    arms = input("Number of Visible Armaments: ")
    instructions_speed_UI()
    spd = input("Assumed Speed: ")
    instructions_crew_UI()
    crew = input("Visible Crew Compartments: ")
    user_list = [span, engine, eng_type,
                 lgth, arms, spd, crew]
    return user_list


# open a json file passed in
    # variable take opened file as dictionary
    # return readable data
def open_file(file_name):
    file_data = open(file_name)
    return file_data


# turn readable data into list
    # take dictionary data and load into a list variable
    # return list
def deserialize_data(file_data):
    loaded_data = json.load(file_data)
    return loaded_data


# take aircraft specs and load into 2D list
    # make a list variable
    # for each item in json list for specs
    # add list of specs to new list (2D list)
    # return new 2D List
def load_characteristic_list():
    aircraft_characteristic = []
    for aircraft_data in all_data['aeronautic_vehicle_details']:
        aircraft_characteristic.append(
            [aircraft_data['span'], aircraft_data['engine_count'], aircraft_data['engine_type'],
             aircraft_data['length'],
             aircraft_data['armament_count'], aircraft_data['speed'], aircraft_data['crew_compartments']])
    return aircraft_characteristic


# take aircraft labels and load into 2D list
    # make a list variable
    # for each item in json list for labels
    # add list of labels to new list (2D list)
    # return new 2D List
    # this is done for each type
def load_label_list():
    aircraft_label = []
    for aircraft_data in all_data['biplane']:
        aircraft_label.append([aircraft_data['bf']])
        # print(aircraft_label)
    for aircraft_data in all_data['fighter']:
        aircraft_label.append([aircraft_data['f']])
        # print(aircraft_label)
    for aircraft_data in all_data['heavy_fighter']:
        aircraft_label.append([aircraft_data['hvy']])
        # print(aircraft_label)
    for aircraft_data in all_data['jet']:
        aircraft_label.append([aircraft_data['jet']])
        # print(aircraft_label)
    for aircraft_data in all_data['night_fighter']:
        aircraft_label.append([aircraft_data['ngt']])
        # print(aircraft_label)
    for aircraft_data in all_data['dive_bomber']:
        aircraft_label.append([aircraft_data['db']])
        # print(aircraft_label)
    for aircraft_data in all_data['ground_attack_aircraft']:
        aircraft_label.append([aircraft_data['gaa']])
        # print(aircraft_label)
    for aircraft_data in all_data['heavy_bomber']:
        aircraft_label.append([aircraft_data['hvy']])
        # print(aircraft_label)
    for aircraft_data in all_data['light_bomber']:
        aircraft_label.append([aircraft_data['lgt']])
        # print(aircraft_label)
    for aircraft_data in all_data['medium_bomber']:
        aircraft_label.append([aircraft_data['med']])
        # print(aircraft_label)
    return aircraft_label


# action ML training
    # make network tree
    # align specs and labels to predict from tree correctly
    # return network tree
def classification_process(specs, label):
    classifier = tree.DecisionTreeClassifier()
    classifier = classifier.fit(specs, label)
    return classifier


# use user input to compare to ML tree
    # create a weighted result to return prediction
    # return number prediction result
def prediction_process(classifier):
    prediction = classifier.predict([user_inputs_to_list()])
    return prediction


# UI instructions w/ delay
def stage_one_UI():
    print('###############################################')
    print('###- Aircraft Identifying Detection System -###')
    print('###---------------"AIR IDS"-----------------###')
    print('###############################################')
    delay_2()


# UI instructions w/ delays
def stage_two_UI():
    print('STATUS UPDATE >>> Initialisation')
    delay_2()
    print('STATUS UPDATE >>> Structuring Data')
    delay_5()
    print('STATUS UPDATE >>> Training AI  ')


# UI instructions w/ delays
def stage_three_UI():
    delay_5()
    print('STATUS UPDATE >>> Training Complete')


# UI instructions w/ delays
def stage_four_UI():
    print('Thank for using "AIDS"')
    print('###############################################')
    print('###---------- Program Terminated -----------###')
    print('###############################################')
    delay_5()


# discern prediction numerical result
    # if statement
    # based on result determine string result
    # this is for user EXP
    # return readable string
def deliberate_results_UI(prediction):
    result = ' '
    if prediction == 0:
        result = 'Biplane'
    elif prediction == 1:
        result = 'Fighter'
    elif prediction == 2:
        result = 'Heavy Fighter'
    elif prediction == 3:
        result = 'Jet'
    elif prediction == 4:
        result = 'Night Fighter'
    elif prediction == 5:
        result = 'Dive Bomber'
    elif prediction == 6:
        result = 'Ground Attack Aircraft'
    elif prediction == 7:
        result = 'Heavy Bomber'
    elif prediction == 8:
        result = 'Light Bomber'
    elif prediction == 9:
        result = 'Medium Bomber'
    else:
        result = 'Unidentified Flying Object'
    return result


# ask user input to continue
    # input into string variable
    # if a form of yes result variable true = continue program
    # if anything else result variable false = discontinue program
    # return result
def play_again():
    answer = input('Would you like to identify another plane? ')
    print(' ')
    if answer == ("yes" or "Yes" or "YES" or "y" or "Y"):
        result = True
    else:
        result = False
    return result

#---------------------------------------
# PROGRAM
#---------------------------------------
# call stage one UI
stage_one_UI()
# open and deserialize the json file data into lists
json_file_data = open_file('characteristics.json')
all_data = deserialize_data(json_file_data)
# parse data lists into proper lists specs and labels
aircraft_specs = load_characteristic_list()
aircraft_label = load_label_list()
# call stage two UI
stage_two_UI()
# create the corrilation and structure of ML tree with lists
classifier = classification_process(aircraft_specs, aircraft_label)
# call stage three UI
stage_three_UI()
# call instructions UI
instructions_characteristics_UI()

# above is one time run
# ********************************
# below is looped program

# variable to keep loop active
loop_program = True
# while loop = continue program while true
    # run priction process user input and tree comparision
    # identify numerical result
    # call to play again input
while loop_program == True:
    prediction = prediction_process(classifier)
    print(" ")
    print("You likely saw a", deliberate_results_UI(prediction))
    print(" ")
    loop_program = play_again()
# call stage four UI
stage_four_UI()

# END PROGRAM