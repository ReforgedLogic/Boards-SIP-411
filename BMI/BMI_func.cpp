/*
FINAL FRONTIER (SOURCE)
source.cpp
JERARD CARNEY
NOVEMBER.23.2018
*/


// LIBRARIES
#include <iostream>
#include <string>
#include <ctime>
#include <cstdlib>
	// HEADER IS DEVELOPER (JERARD CARNEY) CREATED
#include "BMI_header.h"

// std:: NAMESPACE
using namespace std;

// BASIC FUNCTION OF BMI >> SETS THE INITIAL (ZEROED) VARIABLES AND VALUES
BMI::BMI()
{
	newHeight = 0;
	newWeight = 0.0;
}

// OVERLOAD FUNTION OF BMI >> TAKES IN string USER NAME, int HIEGHT, double WEIGHT
BMI::BMI(string name, int height, double weight)
{
	newName = name;
	newHeight = height;
	newWeight = weight;
}

// DESTRUCTOR FUNCTION OF BMI >> CLEARS FOR MEMORY PORPUSE 
BMI::~BMI()
{

}

// ACCESSOR FUNCTION TO BMI >> GET USER INPUT AND PLACES VALUE IN BMI OVERLOAD STRING newName, RETURNS VALUE
string BMI::getName() const
{
	return newName;
}

// ACCESSOR FUNCTION TO BMI >> GET USER INPUT AND PLACES VALUE IN BMI OVERLOAD INT newHeight, RETURNS VALUE
int BMI::getHeight() const
{
	return newHeight;
}

// ACCESSOR FUNCTION TO BMI >> GET USER INPUT AND PLACES VALUE IN BMI OVERLOAD DOUBLE newWeight, RETURNS VALUE
double BMI::getWeight() const
{
	return newWeight;
}

// MUTATOR FUNCTION TO BMI >> GET USER INPUT AND PLACES VALUE IN BMI OVERLOAD STRING newName
void BMI::setName(string name)
{
	newName = name;
}

// MUTATOR FUNCTION TO BMI >> GET USER INPUT AND PLACES VALUE IN BMI OVERLOAD INT newHeight
void BMI::setHeight(int height)
{
	newHeight = height;
}

// MUTATOR FUNCTION TO BMI >> GET USER INPUT AND PLACES VALUE IN BMI OVERLOAD DOUBLE newWeight
void BMI::setWeight(double weight)
{
	newWeight = weight;
}

// MUTATOR FUNCTION TO BMI >> CALULATES ACTUAL BMI >> USING newWeight, newHeight
double BMI::calcBMI()
{
	return ((newWeight * 703) / (newHeight * newHeight));
}