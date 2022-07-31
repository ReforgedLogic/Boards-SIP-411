// Main.java
// SB-13 Final
// Jerard Carney
// 3.10.19


package com.jetbrains;
/*
provide support to the Java coding process.
 */


/*
NOTICE...

I will explain all the code in a summary above each section. If more is needed in
a specific area I will comment above that section as well.
The rest of the commenting will be streamlined for organization and to help me
develop my commenting style.
 */


/*
This is the Main class for the hub of my coding for Starbase 13. This is where I
call Methods from the class (Alexa, Menu, and User). I cleaned this up a bunch.
now only methods are called from here and the pre-loads for the constructors have
been moved to the AssetDescription Class. The bulk text has been removed and
presented as an option to view via new menus in the Menu Class. This feels more RPG.
The Menu Class call at the end is where everything gets fun and can be accessed.
 */
public class Main {

    /*
    This is my Main Method for the Main Class. I have all the Method calls in here.
    The class is public meaning it can be change/ accessed from other code calls.
     */
    public static void main(String[] args) {
        // I call the Alexa Class here (FILE- Alexa.java)
        Alexa narrativeObject1 = new Alexa();
        // I call the Introduction Method here (FILE- Alexa.java)
        narrativeObject1.Introduction();


//**********************************************************************************************************************
        // I call the User Class here (FILE- User.java)
        User userObject1 = new User();
        // I call the userInput Method here (FILE- User.java
        userObject1.userInput();


//**********************************************************************************************************************
        // I call the Alexa Class here (FILE- Alexa.java)
        Alexa narrativeObject2 = new Alexa();
        // I call the Interaction Method here (FILE- Alexa.java)
        narrativeObject2.Introduction();


//**********************************************************************************************************************
        // I call the Alexa Class here (FILE- Alexa.java)
        Alexa narrativeObject3 = new Alexa();
        // I call the Welcome Method here (FILE- Alexa.java)
        narrativeObject3.Welcome();


//**********************************************************************************************************************
        // I call the Alexa Class here (FILE- Alexa.java)
        Alexa narrativeObject4 = new Alexa();
        // I call the ExploreInteraction Method here (FILE- Alexa.java)
        narrativeObject4.ExploreInteraction();


//**********************************************************************************************************************
        // I call the Menu Class here (FILE- Menu.java)
        Menu activateMenu = new Menu();
        // I call the LocationMenu Method here (FILE- Menu.java)
        activateMenu.LocationMenu();
    } // End Main method
} // End Main Class


