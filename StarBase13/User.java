// User.java
// SB-13 Final
// Jerard Carney
// 3.10.19


package com.jetbrains;
/*
I honestly have no idea what the package offers to the coding process. I do
know that it is to provide support to the Java coding process.
 */


/*
NOTICE...

I will explain all the code in a summary above each section. If more is needed in
a specific area I will comment above that section as well.
The rest of the commenting will be streamlined for organization and to help me
develop my commenting style.
 */


/*
This is the the file utilized to allow user input via the scanner coding tool.
 */
import java.util.Scanner;

/*
This is the User class I use the Scanner tool for the user input and load it to the variable
userIn. This lets me get the input needed to display back using the getLine method to
display the input exactly back as it is put in. I use the system print out to display
out the items I need. The method user input is for the name of the user. The method userAnswer
is for  the user to describe the Starbase and then have the AI Alexa say it back. The rest is
basically just formatting code. Used in Main Class (FILE- Main.java) and (FILE- Alexa.java
 */
public class User {

    // Scanner assigned the user input when used to userIn variable
    Scanner userIn = new Scanner(System.in);


//**********************************************************************************************************************
    // userInput method (FILE- Main.java)
    public void userInput() {
        // asks user name
        System.out.println("\n\nPlease state your name. ");
        // variable to current user input
        String userName = userIn.nextLine();
        // Alexa name output
        System.out.println("\nI am so happy to meet you " + userName + ".");
    } // End userInput method


//**********************************************************************************************************************
    // userAnswer method (FILE- Alexa.java)
    public void userAnswer() {
            // formatting space
            System.out.println();
            // variable to current user input
            String description = userIn.nextLine();
            // fluff output
            System.out.println("\n\nWhat I heard you say is:\n");
            // takes user description of Starbase and reiterates it back to user
            System.out.println(description);
    } // End userAnswer method
} // End User Class
