// Lifeform.java
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
This is the Lifeform class Here is the constructor for the descriptions of the spaceships
(Changeling, Asari, Kryptonians, Predators, and Borg). They are initialized in the
variable of LifeformDescription and then displayed when called on. This Class also has an
overload method. Used in (FILE- AssetDescription.java)
 */
public class Lifeform extends AssetDescription {

    // Lifeform consturtor method, takes in a string variable argument
    public Lifeform(String description){
        // take variable given and assigns to the LifeformDescription private variable
        LifeformDescription = description;
    } // End Lifeform method

    // private string variable
    private String LifeformDescription;


    // Over Load Method for Lifeform
    public Lifeform(){
    }

    // LifeformDescription method, prints out variable from constructor
    public void LifeformDescription(){
        System.out.println(LifeformDescription);
    } // End LifeformDescription method
} // End Lifeform Class
