// Alexa.java
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
This is the Alexa CLass. This is made up of strictly fluff based narrative using the System.out.println.
The  methods in here are designed to just be called at a certain time. They all have dialog and
utilize heavy formatting code. The one method Interaction calls another method for user input. Also the
the bridge password hint is in CaptainHint method. Methods used in (FILE- Main.java), (FILE- Menu.java),
and (FILE- Password.java).
 */
public class Alexa {

    // Introduction method (FILE- Main.java)
    public void Introduction() {
        // fluff dialog for user start
        System.out.println("\n///////////////////////////////////");
        System.out.println("//// Welcome to Starbase Corp. ////");
        System.out.println("///////////////////////////////////");
        System.out.println("\nYou are currently approaching installation SB-13.");
        System.out.println("My Name is Alexa Amazon and I will be your AI assistant");
        System.out.println("today.");
    } // End Introduction method


//**********************************************************************************************************************
    // Interaction method (FILE- Main.java)
    public void Interaction() {

        // fluff dialog asking for a five sentence description from the user
        System.out.println("Today you have the luxury of riding on a 'T-34 QUAD Wing', ");
        System.out.println("one of the fastest ships in the Starbase fleet.");
        System.out.println("As part of a unique survey experience plz describe your");
        System.out.println("emotions and what you are seeing to help further learn what");
        System.out.println("we here at Starbase can improve. Please keep your response");
        System.out.println("to a maximum of '1-2' sentences please. \n");


        // I call the User Class here (FILE- User.java)
        User answerObject2 = new User();
        // I call the userInput Method here (FILE- User.java
        answerObject2.userAnswer();

        // fluff output
        System.out.println(
                "*************************" +
                "\nThank you for your input.\n" +
                "*************************");
    } // End Interaction method


//**********************************************************************************************************************
    // ExploreInteraction method (FILE- Main.java)
    public void ExploreInteraction() {
        // fluff dialog about docked ships
        System.out.println(
                "\nAs you finish docking you notice all the wonderful ships docked.\n" +
                "You want to explore this massive station and all of its splendid\n" +
                "wonders. As you get off the T-34 Alexa directs you to the nearest\n" +
                "'Tele-Transportaion Unit' and asks you where too first.");
    } // End ExploreInteraction method


//**********************************************************************************************************************
    // CaptainHint method (FILE- Menu.java)
    public void CaptainHint() {
        // fluff dialog about lifeforms at starbase.
        System.out.println(
                "\nWhile exploring the prominade you here Alexa stating information \n" +
                "about the station. You learn the station has been in operation for \n" +
                "117 years and 32 of those years have been under the command of Captain\n" +
                "Jean-Luc Picard who is still currently the Captain.");
    } // End LifeInteraction method


//**********************************************************************************************************************
    // Welcome method (FILE- Main.java)
    public void Welcome() {
        // fluff dialog for welcome user.
        System.out.println("\n\n//////////////////////////////////////");
        System.out.println("/////// Once again Welcome to ////////");
        System.out.println("///////////// Starbase 13 ////////////");
        System.out.println("//////////////////////////////////////");
    } // End Welcome method


//**********************************************************************************************************************
    // Denied method (FILE- Password.java)
    public void Denied(){
        // just lets user know password attempt is wrong
        System.out.println("ACCESS DENIED");
    }// End Denied method
} // End Alexa Class
