/*
FINAL FRONTIER (MAIN)
source.cpp
JERARD CARNEY
NOVEMBER.23.2018
*/


// LIBRARIES
#include <iostream>
#include <string>
#include <ctime>
#include <cstdlib>
#include "BMI_header.h"

// std:: NAMESPACE
using namespace std;

// INITIALIZE MAIN CODE
int main()
{
// REPLAY THIS SECTION (CODITION IN LOOP)
replay:

	// INITIALIZE VARIABLES FOR LOOP (do)
	bool goodInfo = false;
	string information;
	string correct;

	// HARD CODE ANSWER TO EXIT LOOP (do), MUST BE "YES" LOWER CASE
	correct = "yes";

	// INITIALIZE VARIABLES FOR USER BMI INPUT
	string name;
	int height;
	double weight;

	// INITIALIZE VARIABLES FOR HARD CODE FRIEND BMI VALUE INPUT
	string friendName;
	int friendHeight;
	double friendWeight;

	// ACTUAL HARD CODE VALUES FOR FRIEND BMI
	friendName = "G.I. Joe";
	friendHeight = 73;
	friendWeight = 215.4;

	// POINTER ADDRESS FOR FRIEND VARIABLES, HERE ASSIGNS THE MEMORY ADDRESS
	string* ptrFriendName = &friendName;
	int* ptrFriendHeight = &friendHeight;
	double* ptrFriendWeight = &friendWeight;

	

	// cout >> ASKS FOR USER NAME, GETLINE GETS FULL USER NAME AND ASSIGNS TO VARIABLE
	cout << "Please enter your  full name: " << endl;
	getline(cin, name);

	// GREET FUNCTION, GREETS USER WITH THERE NAME TO PROGRAM
	greet(name);

	// cout >> ASKS USER FOR THE HEIGHT AND WEIGHT INPUT, CIN GETS VALUES AND ASSIGNS THEM TO VARIABLES
	cout << "\n\nEnter your height (in inches): " << endl;
	cin >> height;
	cout << "Enter your weight (in pounds): " << endl;
	cin >> weight;

	
	// ASSOCIATES CLASS BMI WITH PATIENT KEY WORD
	BMI patient; 


	// DISPLAY STATS FO USER FUNCTION, CIN GET ANSWER OF CORRECT INFO FROM FUNCTION DISPLAYED AND ASSIGNS TO VARIABLE
	statDisplay(name, height, weight);
	cin >> information;

	// LOOP (do), IF USER INFORMATION IS CORRECT THEN MOVE ON, IF NOT THEN START FROM REPLAY MARKER AND RE-ENTER INFO
	do
		if (information != correct)
		{	
			// REPLAY FEATURE GOTO
			goto replay;
		}
		else if (information == correct)
		{
			goodInfo = true;
		}
		else
		{
			cout << "Error" << endl;
		}
	while (goodInfo == false);
	// END LOOP(do)

	// CALL FUNCTIONS TO ASSIGN USER VALUES TO VALUES IN CLASS BMI_func.cpp
	patient.setName(name);
	patient.setHeight(height);
	patient.setWeight(weight);


	// cout >> DISPLAYS USER RESULTS
	cout << "\n\nAwesome!!! Here is your BMI: " << patient.calcBMI() << endl;


	// ASSOCIATE BMI CLASS WITH FRIEND HARD CODE INPUT VALUES
	BMI friendResults;


	// iNPUT FRIND STATS TO FUNCTION FOR DISPLAY
	statFriend(friendName, friendHeight, friendWeight);


	// CALL FUNCTIONS TO ASSIGN FRIEND VALUES TO VALUES IN CLASS BMI_func.cpp
	friendResults.setName(*ptrFriendName);
	friendResults.setHeight(*ptrFriendHeight);
	friendResults.setWeight(*ptrFriendWeight);


	// cout >> DISPLAYS USER AND HARD CODE FRIEND RESULTS
	cout << "\n\nHere is you friends BMI to compare yourself to." << endl
		<< "Your Results: " << patient.calcBMI() << endl
		<< "Friend Results" << friendResults.calcBMI() << endl
		<< "\nThank you for using BMI CALC, have a great day." << endl;


	// SYSTEM PAUSE
	system("pause");

	// CODE CHECK GOOD RETURN 0
	return 0;
}
