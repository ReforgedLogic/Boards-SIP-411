/*
FINAL FRONTIER (HEADER)
source.cpp
JERARD CARNEY
NOVEMBER.23.2018
*/

#pragma once

// LIBRARIES
#include <iostream>
#include <string>


//std:: NAMESPACE
using namespace std;


// IF NOT DEFINED
#ifndef Header_H
// DEFINED
#define Header_H


// CONTAINER FOR BMI CLASS
class BMI
{
// PUBLIC ACCESS ELEMENTS
public:

//FUNCTION FOR NAVIGATING CLASS
	// Default Constructor
	BMI();

	// Overload Constructor
	BMI(string, int, double);

	// Destuctor
	~BMI();

	//Accessors Functions
	string getName() const;
	int getHeight() const;
	double getWeight() const;

	//Mutator Functions
	void setName(string);
	void setHeight(int);
	void setWeight(double);
	double calcBMI();


// LIMITED ACCESS ELEMENTS (CAN ONLY CHANGE VIA ACCESSOR FUNCTIONS)
private:

	// Member Variables
	string newName;
	int newHeight;
	double newWeight;
};
// END CLASS BMI


// DECLARATIONS FOR FUNCTIONS
	//GREETING FUNCTION FOR USER
void greet(string name);
	// USER STAT DISPLAY FUNCTION
void statDisplay(string name, int height, double weight);
	// FRIEND HARD CODE STAT DISPLAY FUNCTION
void statFriend(string& name, int& height, double& weight);

// END
#endif