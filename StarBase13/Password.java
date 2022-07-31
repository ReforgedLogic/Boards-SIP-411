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
This is the Password class for The is used for access to the description of the bridge.
A user will have three tries before they get spat back to the menu of locations. I
used a while loop for this attempt limit. The actual password is "Picard" and "742273"this
is used in (FILE- Menu.java ~ case 4). I also added the Array and FOR loop here atr the bottom
to go through the set password 742273 in each index and compare to array of 0-9 and
display the result of the index when the number of the code match 0-9. I also added the
choice for the player to either use the decryption option or use the knowledge of the captains name
as the entry password. Either way they get you into the room and back to the location menu.
 */
public class Password {
    // DecryptionType Method (FILE- Menu.java)
    public void DecryptionType(){
        // declare boolean variable as false for do loop
        boolean returnToLocations = false;

        // start do loop... runs once + conditions.
        do {
            // fluff dialog for options
            System.out.println("1 - Type in the password.");
            System.out.println("2 - Hack the password.");
            System.out.println("3 - Return to locations menu.");

            // Scanner for user input of and int, then assigns this to variable userSelection for switch
            Scanner getmethod = new Scanner(System.in);
            int userSelection = 0;
            userSelection = getmethod.nextInt();

            /*
            SWITCH for userSelection... This is basically
            so that the user can switch to different methods
            and have them display the description of the object.
            The BREAK is to prevent the code from continuing pass
            the selected option. The DEFAULT is the go to for
            user input that is not existent.
            */
            switch (userSelection) {
                // option 1
                case 1:
                    // Call BridgePassword
                    BridgePassword();
                    break;

                // option 2
                case 2:
                    // call Hack method
                    Hack();
                    // prompt user to enter numeric password
                    System.out.println("Enter Password: ");
                    // call BridgePassword method
                    BridgePassword();
                    break;

                // option 3
                case 3:
                    // I call the Menu Class here (FILE- Menu.java)
                    Menu activateMenu = new Menu();
                    // I call the LocationMenu Method here (FILE- Menu.java)
                    activateMenu.LocationMenu();
                    break;
            } // End of switch
        } while(!returnToLocations); // End of for loop
    } // End DecryptionType method

//**********************************************************************************************************************
    // BridgePassword method
    public void BridgePassword(){
        // declared string variable for password input
        String passwordInput;

        // declared int variable for attempts = 0
        int attempts = 0;

        // Begining of while loop for attempt count, limit is 3
        while(attempts <= 3){

        // Scanner to get user input and assign it to passwordInput variable
        Scanner getPassword = new Scanner(System.in);
        passwordInput = getPassword.nextLine();

            // Beginning of if then statements
            // if password is right then show bridge description.
            if (passwordInput.equals("Picard") || passwordInput.equals("742273")){
                // I call the AssetDescription Class here (FILE- AssetDescription.java)
                AssetDescription bridge = new AssetDescription();
                // I call the BridgeRoom Method here (FILE- AssetDescription.java)
                bridge.GetBridgeRoomDescription();

                // I call the Location Class here (FILE- Location.java)
                Menu activateMenu = new Menu();
                // I call the LocationMenu Method here (FILE- Location.java)
                activateMenu.LocationMenu();
            }
            // if password is not right and attempts is less then or equal to 3 try again.
            else if((passwordInput != ("Picard")) && (attempts <= 3)){
                Alexa denied = new Alexa();
                denied.Denied();
                ++attempts;
            }
            // else access is not granted and you get pushed to location menu again.
            else {
                // I call the Alexa Class here (FILE- Alexa.java)
                Alexa denied = new Alexa();
                // I call the Denied Method here (FILE- Alexa.java)
                denied.Denied();


                // I call the Location Class here (FILE- Location.java)
                Menu activateMenu = new Menu();
                // I call the LocationMenu Method here (FILE- Location.java)
                activateMenu.LocationMenu();
            } // End if statements
        } // End while loop
    } // End BridgePassword method


//**********************************************************************************************************************
    // Hack method - The password is Picard In numeric form
    public void  Hack(){
        // array for correct password
        int access[] = {7,4,2,2,7,3};

        //Begin FOR loop - starting at 0 if index of access array is not the length of array +1 repeat.
        for(int indexAccess = 0; indexAccess < access.length; indexAccess++){

            // array for access code to be compared to, if access element is equal to hackTool element
            int [] hackTool;
            // initialize array to have 10 elements
            hackTool = new int[10];

            // hackTool elements #s 0-9
            hackTool[0] = 0;
            hackTool[1] = 1;
            hackTool[2] = 2;
            hackTool[3] = 3;
            hackTool[4] = 4;
            hackTool[5] = 5;
            hackTool[6] = 6;
            hackTool[7] = 7;
            hackTool[8] = 8;
            hackTool[9] = 9;

            /*
            Begin FOR loop. For each element in access array compare to each element in
            hackTool array. add + to count(indexHackTool) as long as the count is less
            then the length of hackTool array.
             */
            for(int indexHackTool = 0; indexHackTool < hackTool.length; indexHackTool++){
                // if statement - if element at same index for access and hackTool array are ==
                // print  out the element/ index for hackTool
                if(access[indexAccess] == hackTool[indexHackTool]){
                    access[indexAccess] = hackTool[indexHackTool];
                    System.out.print(hackTool[indexHackTool]);
                } // End IF statement compare arrays
            } // End FOR loop hackTool
        } // End FOR loop access
        // Formatting line break
        System.out.println(" ");
    } // End Hack method
} // End Password Class
