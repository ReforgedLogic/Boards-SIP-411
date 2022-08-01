# Jerard Carney
# 11/28/21
# ML Assignment

###--------------------------------------
# LIBRARIES
###--------------------------------------
# import numpy for number manipulation in lists
# import sikit iris toy data
# import classifier tree for ML
#
#
import numpy as python_numbers
from sklearn.datasets import load_iris
from sklearn import tree
import time as time
import random as rand

# load iris data into object
iris_data_set = load_iris()


###--------------------------------------
# DEFINE FUNCTIONS
###--------------------------------------
# program title UX
def welcome_text():
    print(
        "###########################\n"
        "#     Welcome to IRIS     #\n"
        "###########################"
    )


# summary of program
def explanation_text():
    print(
        "This is a program designed to\n"
        "to help you identify variants\n"
        "of the Iris flower. \n"
        "Yes = Begin\n"
        "No = Quit\n\n"
        "Would you like to START? "
    )


# UX loading learning AI EXP
def status_text(status):
    print(
        "**************************\n"
        "* STATUS: ", status, "\n"
    )


# ask user if they want to test AI learning
def test_text():
    print(
        "**************************\n\n"
        "IRIS is ready to test. this\n"
        "is advised to ensure the AI\n"
        "network has learned correctly.\n"
        "If you choose not to test IRIS\n"
        "will shut down.\n"
        "Would you like to test IRIS? "
    )


# ready title UX
def actual_run_introduction_text():
    print(
        "\n\n"
        "###########################\n"
        "#      IRIS is Ready      #\n"
        "###########################\n"
    )


# instruction on input for prediction UX
def begin_instructions_text():
    print(
        "Welcome to the full version\n"
        "of IRIS. Now that IRIS has\n"
        "completed her learning portion\n"
        "she can identify your variant\n"
        "of iris flower. Please follow\n"
        "the prompts and note all \n"
        "measurements are in (cm).\n"
        "\n"
        "-----ENJOY!\n"
        "***************************\n\n"
    )


# focal point result for UX result
def display_result_text(string):
    print(
        "\n"
        "<><><><><><><><><><><><><><><><><>\n"
        "<> Your flower is a: ", string.upper(), "\n"
        "<><><><><><><><><><><><><><><><><>\n"
    )


# ask user if they want to go again
def play_again_text():
    print(
        "\n"
        "Would you like to ID another flower? "
    )


# all and only UX text above
#######################################################################################################################
# all data manipulation below


# program delay for UX
    # array 1-7 rep. seconds
    # delay program for rand seconds from array
def delay():
    seconds = [1,2,3,4,5,6,7]
    time.sleep(rand.choice(seconds))


# filter class results into UX result
    # set flower name to blank
    # if class is 0 its setosa
    # if class is 1 its versicolor
    # if class is 3 its virginica
    # else its and unknown flower
    # return flower name
def filter_flower_label(class_number):
    flower_name = ""
    if class_number == 0:
        flower_name = "Setosa"
    elif class_number == 1:
        flower_name = "Versicolor"
    elif class_number == 2:
        flower_name = "Virginica"
    else:
        flower_name = "Unknown Variant"
    return flower_name


# separate array class for test data
    # take list of class results
    # go through each item of list
    # filter the class name into UX result name (flower name)
    # print the target flower name
def separate_list(result_list):
    for each in range(len(result_list)):
        class_name = filter_flower_label(result_list[each])
        print("Test Target: ", class_name)


# gets user yes no response
    # variable used it ID if user wants to proceed
    # variable to ID while loop active
    # while loop starts active
        # get user input, input to lowercase for all
        # if input is yes: break loop and proceed
        # if input is no: break loop and not proceed
        # else: loop and try correct answer
    # return proceed
def get_user_answer():
    proceed = None
    active_loop = True
    while active_loop:
        user_answer = input()
        # print(user_answer)
        if user_answer.lower() == "yes":
            # print("y")
            active_loop = False
            proceed = True
        elif user_answer.lower() == "no":
            # print("n")
            active_loop = False
            proceed = False
        else:
            print("Please answer with a yes or no: ")
    return proceed


# get user start or exit response
    # variable to ID while loop active
    # while loop starts active
        # get user input, input to lowercase for all
        # if input is yes: break loop and proceed
        # if input is no: break loop and close program
        # else: loop and try correct answer
def user_start_or_exit():
    active_loop = True
    while active_loop:
        user_answer = input()
        # print(user_answer)
        if user_answer.lower() == "yes":
            # print("y")
            active_loop = False
        elif user_answer.lower() == "no":
            # print("n")
            exit()
        else:
            print("Please answer with a yes or no: ")


# display and take user input for text list creation
    # passed in: string=range of numbers, lower=minimum number, upper=maximum number
    # display UX directions
    # get user input, change to int, align with list -1 offset
    # while input is less then min and more then max
        # inform user to re input correct number
        # get user new input, change to int, align with list -1 offset
    # return variable with user input
def user_selection(string, lower_limit, upper_limit):
    print("Choose an Index number between ", string, ": ")
    selection = int(input()) - 1
    while selection < lower_limit or selection > upper_limit:
        print("Sorry the number you chose wasn't correct. \n"
              "Choose a Index number between ", string, ": ")
        selection = int(input()) - 1
    return selection


# get user input and place into array
    # object list set to blank
    # call for user input with parameters 1-50
    # call for user input with parameters 51-100
    # call for user input with parameters 101-149
    # assemble list with variables
    # return user made list
def user_chosen_test_data():
    user_selected_list = []
    selection_one = user_selection("1-50", 0, 49)
    selection_two = user_selection("51-100", 50, 99)
    selection_three = user_selection("101-150", 100, 149)
    user_selected_list = [selection_one, selection_two, selection_three]
    return user_selected_list


# make classifier data sets
    # object to hold network tree
    # fit data and labels aligned in network tree
def classify_data(data, target):
    classifier = tree.DecisionTreeClassifier()
    return classifier.fit(data, target)


# activate ML test
    # call for user test list UX
    # confirm user would like to test ML
    # while user says yes
def testing():
    test_text()
    answer = get_user_answer()
    while answer == True:
        # new array for user test data selection
        # remove user selected labels from iris toy data
        # remove user selected data from iris toy data start at index (0)
        # object to hold user selected data from toy data
        # call tree creation with altered data and train AI
        # call predict of test data, separate it, and label it as flower for UX
        # break loop
        test_index = user_chosen_test_data()
        training_target = python_numbers.delete(iris_data_set.target, test_index)
        training_data = python_numbers.delete(iris_data_set.data, test_index, axis=0)
        # (NOT NEEDED part of class demo) test_target = iris_data_set.target[test_index]
        test_data = iris_data_set.data[test_index]
        classifier = classify_data(training_data, training_target)
        separate_list(classifier.predict(test_data))
        answer = False


# get user input for sepal length
    # UX instructions
    # object for user input
    # return object
def get_sepal_length():
    print("What is the sepal length?\n"
          "This is the part of the\n"
          "flower that is the leaves\n"
          "just below the petals.\n"
          "Sepal Length: ")
    sepal_length = input()
    return sepal_length


# get user input for sepal width
    # UX instructions
    # object for user input
    # return object
def get_sepal_width():
    print("What is the sepal width?\n"
          "This is the part of the\n"
          "flower that is the leaves\n"
          "just below the petals.\n"
          "Sepal width: ")
    sepal_width = input()
    return sepal_width


# get user input for petal length
    # UX instructions
    # object for user input
    # return object
def get_petal_length():
    print("What is the petal length?\n"
          "Petal Length: ")
    petal_length = input()
    return petal_length


# get user input for petal width
    # UX instructions
    # object for user input
    # return object
def get_petal_width():
    print("What is the petal width?\n"
          "Petal width: ")
    petal_width = input()
    return petal_width


# get user flower specs loaded to list
    # call in list each spec need for flower list
    # return user spec list
def get_user_target():
    user_target_list = [get_sepal_length(), get_sepal_width(), get_petal_length(), get_petal_width()]
    return user_target_list


# retrain AI with full unaltered iris data set
    # object for iris labels full set
    # object for iris data full set
    # call classifier creation to make network tree
    # return the network tree
def true_learning():
    live_target = iris_data_set.target
    live_data = iris_data_set.data
    classifier = classify_data(live_data, live_target)
    return classifier


# take user input and classifier and make prediction
    # classifier uses user list and predict to iris data set as 2D array
    # return prediction
def predict_result(classifier, target):
    prediction = classifier.predict([target])
    return prediction


# sudo main
    # object for repeating loop
    # while player wants to repeat
def repeat_program(classifier):
    repeat = True
    while repeat:
        # call for user input flower specs array
        # call for raw prediction class results with full data set and user specs
        # filter the raw result into UX flower name
        # call UX display results
        # call UX text for play again
        # call user input for play again
        # if user not repeat exit program
        # if user repeats stay in loop
        # else error note
        user_target = get_user_target()
        raw_result = predict_result(classifier, user_target)
        filtered_result = filter_flower_label(raw_result)
        display_result_text(filtered_result)
        play_again_text()
        repeat = get_user_answer()
        if repeat == False:
            exit()
        elif repeat == True:
            repeat == repeat
        else:
            print("End Timing Error")
            repeat = True


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
###--------------------------------------
# MAIN PROGRAM
###--------------------------------------
# TEST #
# UX title
welcome_text()
# UX directions for test
explanation_text()
# does user want to run or exit program
user_start_or_exit()
# UX start
status_text("Initializing")
# UX delay random
delay()
# UX load
status_text("Structuring Data")
# UX delay random
delay()
# UX load
status_text("Learning Data")
# UX delay random
delay()
# UX ready
status_text("Learning Complete")
# call to actual testing process
testing()


# ACTUAL #
# call for AI ML full iris data set
full_data_list = true_learning()
# UX welcome for actual program
actual_run_introduction_text()
# UX directions for actual program
begin_instructions_text()
# call to program sudo main to ID flower specs
repeat_program(full_data_list)


# END PROGRAM#