# Jerard Carney
# 12/5/21
# DATA SET USED: Star

# Data Key
# Temperature -- K
# L -- L/Lo -- Relative Luminosity
# R -- R/Ro -- Relative Radius
# A_M -- Mv -- Absolute Magnitude
# Color -- General Color of Spectrum
# Spectral_Class -- O,B,A,F,G,K,M / SMASS - https://en.wikipedia.org/wiki/Asteroid_spectral_types
# Type -- Red Dwarf, Brown Dwarf, White Dwarf, Main Sequence , Super Giants, Hyper Giants

#TARGET:
# Type

#f rom 0 to 5

# Red Dwarf - 0
# Brown Dwarf - 1
# White Dwarf - 2
# Main Sequence - 3
# Super Giants - 4
# Hyper Giants - 5

# MATH:

# Lo = 3.828 x 10^26 Watts
# (Avg Luminosity of Sun)
# Ro = 6.9551 x 10^8 m
# (Avg Radius of Sun)

import numpy as numpy
from sklearn import tree
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score as score
from matplotlib import pyplot as visual_plot
import pandas as pandas


#<><><><><><><><><><><><><><>
# File Opening/Array Construction
#<><><><><><><><><><><><><><>

# identify color string and convert to int
# though a long function... simply
    # take a passed string and convert to all lower case
    # converted_string base starts as 0 value
    # if string matches one of the colors listed
    # converted_string is a number value
    # else display Error
    # return converted_string
def transform_color_to_int(string):
    string = string.lower()
    converted_string = 0
    if string == "red":
        converted_string = 1
    elif string == "blue white":
        converted_string = 2
    elif string == "white":
        converted_string = 3
    elif string == "yellowish white":
        converted_string = 4
    elif string == "pale yellow orange":
        converted_string = 5
    elif string == "blue":
        converted_string = 6
    elif string == "whitish":
        converted_string = 7
    elif string == "yellow white":
        converted_string = 8
    elif string == "orange":
        converted_string = 9
    elif string == "white yellow":
        converted_string = 10
    elif string == "yellowish":
        converted_string = 11
    elif string == "orange red":
        converted_string = 12
    else:
        print("Star Color Anomaly", string)
    return converted_string


# identify class string and convert to int
# though a long function... simply
    # take a passed string and convert to all lower case
    # converted_string base starts as 0 value
    # if string matches one of the classes listed
    # converted_string is a number value
    # else display Error
    # return converted_string
def transform_class_to_int(string):
    string = string.upper()
    converted_string = 0
    if string == "M":
        converted_string = 1
    elif string == "B":
        converted_string = 2
    elif string == "A":
        converted_string = 3
    elif string == "F":
        converted_string = 4
    elif string == "O":
        converted_string = 5
    elif string == "K":
        converted_string = 6
    elif string == "G":
        converted_string = 7
    else:
        print("Star Class Anomaly", converted_string)
    return converted_string


# open csv file
    # take passed csv file, read it
    # load read file to object
    # return the read file object
def open_csv(file_name):
    opened_file = pandas.read_csv(file_name)
    return opened_file


# create an array with all data in csv file
    # call open_csv and load file to object
    # create new list object array
    # for each index, and row in the file iterate through them
        # data object equals the data per listed labls of that row
        # appened(add) to object array new data from each row
    # print to test logic and see array
    # return full object array
def create_full_file_array():
    data_frame = open_csv('Stars.csv')
    updated_data_set = []
    for index, row in data_frame.iterrows():
        data_set = [row['Temperature'], row['L'], row['R'], row['A_M'],
                    transform_color_to_int(row['Color']), transform_class_to_int(row['Spectral_Class']), row['Type']]
        updated_data_set.append(data_set)
    # print(updated_data_set)
    return updated_data_set


# create an array with data_set  in csv file
    # call open_csv and load file to object
    # create new list object array
    # for each index, and row in the file iterate through them
        # data object equals the data per listed labels (all but 'Type') of that row
        # append(add) to object array new data from each row
    # print to test logic and see array
    # return full object array
def create_data_set_array():
    data_frame = open_csv('Stars.csv')
    updated_data_set = []
    for index, row in data_frame.iterrows():
        data_set = [row['Temperature'], row['L'], row['R'], row['A_M'],
                    transform_color_to_int(row['Color']), transform_class_to_int(row['Spectral_Class'])]
        updated_data_set.append(data_set)
    # print(updated_data_set)
    return updated_data_set


# create a single data type by label array
def create_data_single_array(csv_file, label):
    data_frame = open_csv(csv_file)
    updated_data_set = []
    for index, row in data_frame.iterrows():
        data_set = [row[label]]
        updated_data_set.append(data_set)
    # print(updated_data_set)
    return updated_data_set


# create an array with target_set  in csv file
    # call open_csv and load file to object
    # create new list object array
    # for each index, and row in the file iterate through them
        # data object equals the data per listed labls ('Type' ONLY) of that row
        # appened(add) to object array new data from each row
    # print to test logic and see array
    # return full object array
def create_target_array():
    data_frame = open_csv('Stars.csv')
    updated_target_set = []
    for index, row in data_frame.iterrows():
        target_set = row['Type']
        updated_target_set.append([target_set])
    # print(updated_target_set)
    return updated_target_set


#<><><><><><><><><><><><><><>
# Comparison Prediction Functions
#<><><><><><><><><><><><><><>

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


#<><><><><><><><><><><><><><>
# Linear Prediction Functions
#<><><><><><><><><><><><><><>

# split data set 50/50
def split_data_set():
    x_train, x_test, y_train, y_test = train_test_split(
        create_data_set_array(), create_target_array(),
        test_size=0.5, random_state=0)
    split_array =[x_train, x_test, y_train, y_test]
    # print(split_array)
    return split_array


# create linear regression learning
def create_linear_regression(x_train, y_train):
    machine_learning = LinearRegression()
    machine_learning.fit(x_train, y_train)
    return machine_learning


# linear regression prediction
def make_linear_prediction(linear_data, target):
    prediction = linear_data.predict(target)
    return prediction


# weight accuracy
def identify_weight_accuracy(prediction, training_set):
    weight_score = score(training_set, prediction)
    return weight_score


def get_feature_input(feature):
    print("Stars ", feature, " ?")
    value = input()
    return value


def string_to_int(string):
    new_value = int(string)
    # print(type(new_value))
    return new_value


def string_to_float(string):
    new_value = float(string)
    # print(type(new_value))
    return new_value


def get_user_target_array():
    user_target = [[string_to_int(get_feature_input("Temp")), string_to_float(get_feature_input("Luminosity")),
                         string_to_float(get_feature_input("Radius")), string_to_float(get_feature_input("Absolute Magnitude")),
                         transform_color_to_int(get_feature_input("Color")), transform_class_to_int(get_feature_input("Class"))]]
    return user_target


#<><><><><><><><><><><><><><>
# MAIN
#<><><><><><><><><><><><><><>

test = [[3068, 0.0024, 0.17, 16.12, transform_color_to_int("Red"), transform_class_to_int("M")]]
# print(test)
test = get_user_target_array()
# comparison data set
prediction_comp = make_comparison_prediction(create_classifier_tree(create_data_set_array(), create_target_array()), test)
print('Prediction Comparison', prediction_comp)


# linear data set
machine_learning = create_linear_regression(split_data_set()[0], split_data_set()[2])
prediction_line = make_linear_prediction(machine_learning, split_data_set()[1])
print('Prediction Linear', prediction_line)

# test linear
print('Prediction with test input', machine_learning.predict(test))
print('Prediction Accuracy', identify_weight_accuracy(split_data_set()[3], prediction_line) * 100)


# Visual Chart
visual_plot.figure(figsize=(15, 10))
visual_plot.scatter(split_data_set()[3], prediction_line)
visual_plot.xlabel('Star Prediction Stats in Linear Regression to Actual Star Stats')
visual_plot.ylabel('Actual Star Data Stats')
visual_plot.title('Predicted Star Data Stats')
visual_plot.show()


# test = open_csv('Stars.csv')
# print(test.columns)
# print(test["Temperature"][0:3])
# print(test.Temperature[1:5+1])
# print("!!!")
# print(test.head(1)[test.columns[0:6]])