// Spaceship.java
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
This is the Spaceship class Here is the constructor for the descriptions of the spaceships
(Normandy, Galactica, Falcon, Heart of Gold, and Infinity). They are initialized in the
variable of SpaceshipDescription and then displayed when called on. This Class also has an
overload method. Used in (FILE- AssetDescription.java)
 */
public class Spaceship extends AssetDescription {

    // Spaceship consturtor method, takes in a string variable argument
    public Spaceship(String description) {
        // take variable given and assigns to the SpaceshipDescription private variable
        SpaceshipDescription = description;
    } // End Spaceship method


    // private string variable
    private String SpaceshipDescription;


    // Over Load Method for Spaceship.
    public Spaceship() {
    }


    // SpaceshipDescription method, prints out variable from constructor
    public void SpaceshipDescription() {
        System.out.println(SpaceshipDescription);
    } // End SpaceshipDescription method
} // End Spaceship Class
