// Locations.java
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
This is the Locations class. This is for object constructor and is called from the Menu class.
This assigns to the variable on compilation and is for the many locations in the game. This is used
in the list/menu for the location. Used in (FILE- AssetDescription.java)
 */
public class Locations extends AssetDescription {


    // Locations constructor method, takes in a string variable argument
    public Locations(String description){
        // take variable given and assigns to the Locations private variable
        LocationsDescription = description;
    } // End Locations method

    // private string variable
    public String LocationsDescription;

} // End Locations Class
