// Main.java
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
This is the Menu class. This is the work horse for the user menus in the game. This has
the locations menu for the user to pick a location and then get a description of it.
Also this is where the menus for the ships and lifeforms are now located. I took the bulky
text from just displaying and made it so that the user can choose to look at ships/aliens
if they want. Now the theme is do you want to know this... press 1... ok here is the info.
These lists use a boolean or the repeat functionality and do loops to utilize the boolean.
They will only exit if the user selects the ext option. All three menus function the same way
and use the switch tool to select/ emulate moving through locations.
 */
public class Menu {

    // LocationMenu method
    public void LocationMenu(){

        // declared boolean variable = false
        boolean exitStarBase = false;

        AssetDescription assetDescription = new AssetDescription();

        // start do loop... displays options to user
        do {
            System.out.println("\n\nSB-13 Tele-Transportaion Unit");
            System.out.println("-----------------------------");
            System.out.println();
            System.out.println("1 - Prominade.");
            System.out.println("2 - Star Lounge.");
            System.out.println("3 - The Galaxy.");
            System.out.println("4 - Bridge.");
            System.out.println("5 - Security.");
            System.out.println("6 - Sim'1'.");
            System.out.println("7 - Docks.");
            System.out.println("8 - Luxury Living Quarters");
            System.out.println("9 - Departure SB-13");
            System.out.println();
            System.out.println("Please select a location by entering a number.\n");

            // Scanner for user input of and int, then assigns this to variable userSelection for switch
            Scanner getLocation = new Scanner(System.in);
            int userSelection = 0;
            userSelection = getLocation.nextInt();



            /*
            SWITCH for userSelection... This is basically
            so that the user can switch to different methods
            and have them display the description of the object.
            The BREAK is to prevent the code from continuing pass
            the selected option. The DEFAULT is the go to for
            user input that is not existent.
            */
            switch (userSelection){
                // option 1
                case 1:
                    String prminadeDescription = assetDescription.GetProminadeDescription();
                    // I call the AssetDescription Class here (FILE- Locations.java)
                    Locations prominade = new Locations(prminadeDescription);
                    // I call the GetProminadeDescription Method here (FILE- Locations.java)
                    prominade.GetProminadeDescription();

                    // I call the Alexa Class here (FILE- Alexa.java)
                    Alexa hint = new Alexa();
                    // I call the CaptainHint Method here (FILE- Alexa.java)
                    hint.CaptainHint();
                    break;

                // option 2
                case 2:
                    String loungeDescription = assetDescription.GetLoungeDescription();
                    // I call the AssetDescription Class here (FILE- Locations.java)
                    Locations lounge = new Locations(loungeDescription);
                    // I call the Lounge Method here (FILE- Locations.java)
                    lounge.GetLoungeDescription();
                    break;

                // option 3
                case 3:
                    String galaxyDescription = assetDescription.GetGalaxyDescription();
                    // I call the AssetDescription Class here (FILE- Locations.java)
                    Locations galaxy = new Locations(galaxyDescription);
                    // I call the Galaxy Method here (FILE- Locations.java)
                    galaxy.GetGalaxyDescription();
                    // I call the LifeformMenu Method
                    LifeformMenu();
                    break;

                // option 4
                case 4:
                    String bridgeDescription = assetDescription.GetBridgeDoorDescription();
                    // I call the AssetDescription Class here (FILE- Locations.java)
                    Locations bridge = new Locations(bridgeDescription);
                    // I call the BridgeDoor Method here (FILE- Locations.java)
                    bridge.GetBridgeDoorDescription();

                    // I call the AssetDescription Class here (FILE- Locations.java)
                    Password access = new Password();
                    // I call the BridgeDoor Method here (FILE- Locations.java)
                    access.DecryptionType();
                    break;

                // option 5
                case 5:
                    String securityDescription = assetDescription.GetSecurityDescription();
                    // I call the AssetDescription Class here (FILE- Locations.java)
                    Locations security = new Locations(securityDescription);
                    // I call the Security Method here (FILE- Locations.java)
                    security.GetSecurityDescription();
                    break;

                // option 6
                case 6:
                    String simDescription = assetDescription.GetSimDescription();
                    // I call the AssetDescription Class here (FILE- Locations.java)
                    Locations sim = new Locations(simDescription);
                    // I call the Sim Method here (FILE- Locations.java)
                    sim.GetSimDescription();
                    break;

                // option 7
                case 7:
                    String docksDescription = assetDescription.GetDocksDescription();
                    // I call the AssetDescription Class here (FILE- Locations.java)
                    Locations docks = new Locations(docksDescription);
                    // I call the Docks Method here (FILE- Locations.java)
                    docks.GetDocksDescription();
                    // I call the DockMenu Method
                    DockMenu();
                    break;

                // option 8
                case 8:
                    String luxuryDescription = assetDescription.GetLuxuryDescription();
                    // I call the Asset DGetLuxuryDescriptionescription Class here (FILE- Locations.java)
                    Locations luxury = new Locations(luxuryDescription);
                    // I call the Luxury Method here (FILE- Locations.java)
                    luxury.GetLuxuryDescription();
                    break;

                // option 9
                case 9:
                    // set true value to boolean variable
                    exitStarBase = true;
                    // fluff dialog
                    System.out.println("Ok. It has been a pleasure serving you. Come back again sometime!");
                    break;

                // default
                default:
                    // fluff dialog
                    System.out.println("Sorry, please try again and pick a destination.");
            } // End Switch
        } while(!exitStarBase); // End do loop
    } // End LocationMenu method


//**********************************************************************************************************************
    public void DockMenu(){

        // declared boolean variable = false
        boolean exitDock = false;

        // start do loop... displays options to user
        do {
            System.out.println("\n\nView A Spacecraft");
            System.out.println("-----------------------------");
            System.out.println();
            System.out.println("1 - Normandy SR-1.");
            System.out.println("2 - Galactica.");
            System.out.println("3 - Millennium Falcon");
            System.out.println("4 - Heart of Gold.");
            System.out.println("5 - Infinity.");
            System.out.println("6 - Exit Docks.");
            System.out.println();
            System.out.println("Please select a ship by entering a number.\n");

            // Scanner for user input of and int, then assigns this to variable userSelection for switch
            Scanner getShip = new Scanner(System.in);
            int userSelection = 0;
            userSelection = getShip.nextInt();

            /*
            SWITCH for userSelection... This is basically
            so that the user can switch to different methods
            and have them display the description of the object.
            The BREAK is to prevent the code from continuing pass
            the selected option. The DEFAULT is the go to for
            user input that is not existent.
            */
            switch (userSelection){
                // option 1
                case 1:
                    // I call the AssetDescription Class here (FILE- Spaceship.java)
                    Spaceship normandyObject = new Spaceship();
                    // I call the Normandy method... Normandy Description (FILE- Spaceship.java)
                    normandyObject.Normandy();
                    break;

                // option 2
                case 2:
                    // I call the AssetDescription Class here (FILE- Spaceship.java)
                    Spaceship galacticaObject = new Spaceship();
                    // I call the Galactica method... Galactica Description (FILE- Spaceship.java)
                    galacticaObject.Galactica();
                    break;

                // option 3
                case 3:
                    // I call the AssetDescription Class here (FILE- Spaceship.java)
                    Spaceship falconObject = new Spaceship();
                    // I call the Falcon method... Falcon Description (FILE- Spaceship.java)
                    falconObject.Falcon();
                    break;

                // option 4
                case 4:
                    // I call the AssetDescription Class here (FILE- Spaceship.java)
                    Spaceship goldObject = new Spaceship();
                    // I call the Gold method... Gold Description (FILE- Spaceship.java)
                    goldObject.Gold();
                    break;

                // option 5
                case 5:
                    // I call the AssetDescription Class here (FILE- Spaceship.java)
                    Spaceship infinityObject = new Spaceship();
                    // I call the Infinity method... Infinity Description (FILE- Spaceship.java)
                    infinityObject.Infinity();
                    break;

                // option 6
                case 6:
                    // set true value to boolean variable
                    exitDock = true;
                    // fluff dialog
                    System.out.println("Ok. It has been a pleasure serving you.");
                    break;

                // default
                default:
                    // fluff dialog
                    System.out.println("Sorry, please try again and pick a ship listed.");
            } // End Switch
        } while(!exitDock); // End do loop
    } // End DockMenu method


//**********************************************************************************************************************
    public void LifeformMenu(){

        // declared boolean variable = false
        boolean exitLifeform = false;

        // start do loop... displays options to user
        do {
            System.out.println("\n\nAsk about...");
            System.out.println("-----------------------------");
            System.out.println();
            System.out.println("1 - Changelings SR-1.");
            System.out.println("2 - Asari.");
            System.out.println("3 - Kryptonians");
            System.out.println("4 - Predators");
            System.out.println("5 - Borg");
            System.out.println("6 - 'Thanks for the heads up.'");
            System.out.println();
            System.out.println("'Numbered from one to six, which do ya want to know about?'\n");

            // Scanner for user input of and int, then assigns this to variable userSelection for switch
            Scanner getLifeform = new Scanner(System.in);
            int userSelection = 0;
            userSelection = getLifeform.nextInt();

            /*
            SWITCH for userSelection... This is basically
            so that the user can switch to different methods
            and have them display the description of the object.
            The BREAK is to prevent the code from continuing pass
            the selected option. The DEFAULT is the go to for
            user input that is not existent.
            */
            switch (userSelection){
                // option 1
                case 1:
                    // I call the AssetDescription Class here (FILE- Lifeform.java)
                    Lifeform changelingsObject = new Lifeform();
                    // I call the Changelings method... Changelings Description (FILE- Lifeform.java)
                    changelingsObject.Changelings();
                    break;

                // option 2
                case 2:
                    // I call the AssetDescription Class here (FILE- Lifeform.java)
                    Lifeform asariObject = new Lifeform();
                    // I call the Asari method... Asari Description (FILE- Lifeform.java)
                    asariObject.Asari();
                    break;

                // option 3
                case 3:
                    // I call the AssetDescription Class here (FILE- Lifeform.java)
                    Lifeform kryptoniansObject = new Lifeform();
                    // I call the Kryptonians method... Kryptonians Description (FILE- Lifeform.java)
                    kryptoniansObject.Kryptonians();
                    break;

                // option 4
                case 4:
                    // I call the AssetDescription Class here (FILE- Lifeform.java)
                    Lifeform predatorsObject = new Lifeform();
                    // I call the Predators method... Predators Description (FILE- Lifeform.java)
                    predatorsObject.Predators();
                    break;

                // option 5
                case 5:
                    // I call the AssetDescription Class here (FILE- Lifeform.java)
                    Lifeform borgObject = new Lifeform();
                    // I call the Borg method... Borg Description (FILE- Lifeform.java)
                    borgObject.Borg();
                    break;

                // option 6
                case 6:
                    // set true value to boolean variable
                    exitLifeform = true;
                    // fluff dialog
                    System.out.println("'No problem friend.'");
                    break;

                // default
                default:
                    // fluff dialog
                    System.out.println("'Speak up... I can't here you.'");
            } // End Switch
        } while(!exitLifeform); // End do loop
    } // End LifeformMenu method
} // End Menu Class

