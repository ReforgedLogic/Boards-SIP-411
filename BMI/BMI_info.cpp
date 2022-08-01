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


// GREETING FUNCTION, USES PLAYER NAME FROM BMI CLASS AND DISPLAYS GREETING TO PLAYER WITH NAME
void greet(string name)
{
	// BMI CLASS ACCESS
	BMI patient;
	patient.setName(name);
	// cout >> DISPLAY TO USER
	cout << "\n*******************************************" << endl
		<< "Welcome " << patient.getName() << endl;
}


// PLAYER STAT DISPLAY FUNCTION, USES BMI CLASS STATS AND DIPLAYS TO USER
void statDisplay(string name, int height, double weight)
{
	// BMI CLASS ACCESS
	BMI patient;
	patient.setName(name);
	patient.setHeight(height);
	patient.setWeight(weight);
	// cout >> DISPLAY TO USER WITH GET FUNCTIONS FROM BMI CLASS
	cout << "\n\n***************************************" << endl
		<< "Is your information correct?" << endl
		<< "Name: " << patient.getName() << endl
		<< "Height: " << patient.getHeight() << endl
		<< "Weight: " << patient.getWeight() << endl
		<< "***************************************" << endl;
}


// FRIEND STAT DISPLAY FUNCTION, USES BMI CLASS STATS AND DIPLAYS TO USER
void statFriend(string& name, int& height, double& weight)
{
	// BMI CLASS ACCESS
	BMI friendResults;
	friendResults.setName(name);
	friendResults.setHeight(height);
	friendResults.setWeight(weight);
	// cout >> DISPLAY TO USER WITH GET FUNCTIONS FROM BMI CLASS
	cout << "\n\n***************************************" << endl
		<< "This is your friend's information." << endl
		<< "Name: " << friendResults.getName() << endl
		<< "Height: " << friendResults.getHeight() << endl
		<< "Weight: " << friendResults.getWeight() << endl
		<< "***************************************" << endl;
}