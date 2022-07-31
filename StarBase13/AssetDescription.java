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
This is the AssetDescription class. This is to contain all the descriptions for
object constructors and is called from the (FILE- Spaceship.java),
and (FILE- Lifeform.java). I did this souly to make my main look much more streamline. I also
like having all these assets in one file and organized. This class is now the super class for
the spaceships, lifeforms, and locations with that said. The classes of lifeforms and spaceship
get overloaded the arguments. The class using locations is now used with inheritance.
 */
public class AssetDescription {

    // Normandy method
    void Normandy() {
        // Ship description too Normandy (FILE- Spaceship.java)
        Spaceship Normandy = new Spaceship(
                "\n\n///////////////////////////////////" +
                        "\nThe Normandy SR1" +
                        "\n///////////////////////////////////\n" +
                        "The Normandy SR1 is long sleek designed spaceship. It's donning a black \n" +
                        "and white color scheme with blue tinted windows. The four engines \n" +
                        "are attached to the short wing span of to the ship's side. It looks \n" +
                        "Fast and like it's packing the newest tech. The last known commander\n" +
                        "was: Commander Shepard.");
        Normandy.SpaceshipDescription();
    } // End Normandy method


    // Galactica method
    void Galactica() {
        // Ship description too Galactica (FILE- Spaceship.java)
        Spaceship Galactica = new Spaceship(
                "\n\n///////////////////////////////////" +
                        "\nThe Battle Star Galactica" +
                        "\n///////////////////////////////////\n" +
                        "The Battle Star Galactica Is a massive war ship that was used against \n" +
                        "the AI. known as Scylons. It holds star fighters known as Vipers, and \n" +
                        "can be used for long term space voyages in a pinch. The last commander \n" +
                        "was: Admiral Admadala.");
        Galactica.SpaceshipDescription();
    } // End Galactica method


    // Falcon method
    void Falcon() {
        // Ship description too Falcon (FILE- Spaceship.java)
        Spaceship Falcon = new Spaceship(
                "\n\n///////////////////////////////////" +
                        "\nThe Mellenium Falcon" +
                        "\n///////////////////////////////////\n" +
                        "The Mellenium Falcon is technically a Corellian YT-1300 light freighter, \n" +
                        "the Falcon has been converted for the use of smuggling purposes. \n" +
                        "Most notably, the Millennium Falcon was the spaceship that infiltrated the \n" +
                        "heart of the second Death Star and obliterated its fusion core. The current \n" +
                        "commander is: Chewbacca 'Chewy'");
        Falcon.SpaceshipDescription();
    } // End Falcon method


    // Gold method
    void Gold() {
        // Ship description too Gold (FILE- Spaceship.java)
        Spaceship Gold = new Spaceship(
                "\n\n///////////////////////////////////" +
                        "\nThe Heart of Gold" +
                        "\n///////////////////////////////////\n" +
                        "The Heart of Gold already starts off weird. Inside, the walls are contoured \n" +
                        "and shaped at strange angles, making it a rather inefficient use of space.\n" +
                        "Heart of Gold’s signature feature though, is its use of the Infinite Improbability \n" +
                        "Drive. This device is used to cross large, interstellar distances in the tiniest \n" +
                        "unit of time imaginable, and its discovery was in fact by chance.");
        Gold.SpaceshipDescription();
    } // End Gold method


    // Infinity method
    void Infinity() {
        // Ship description too Infinity (FILE- Spaceship.java)
        Spaceship Infinity = new Spaceship(
                "\n\n///////////////////////////////////" +
                        "\nThe UNSC Infinity" +
                        "\n///////////////////////////////////\n" +
                        "The UNSC Infinity is approximately 5.7 kilometers long, the Infinity is a thing to \n" +
                        "behold. Inside is capacity for a crew of just over 17,000, along with training grounds \n" +
                        "for soldiers. Boasting 1,100 missile pods, among various other cannons, the UNSC \n" +
                        "Infinity is well equipped to face any adversary. The current commander is: Commander \n" +
                        "Lanskey.");
        Infinity.SpaceshipDescription();
    } // End Infinity method


//**********************************************************************************************************************
    // Changelings method
    void Changelings() {
            // Life form description too Changelings (FILE- Lifeform.java)
        Lifeform Changelings = new Lifeform(
                "\n\n///////////////////////////////////" +
                            "\nChangelings" +
                            "\n///////////////////////////////////\n" +
                            "Changelings can imitate anything or anyone, do becare with your identity when around one. \n" +
                            "If they manage to impersonate you the process of identifying who is the real you is painful.");
        Changelings.LifeformDescription();
    } // End Changelings method


    // Asari method
    void Asari() {
        // Life form description too Asari (FILE- Lifeform.java)
        Lifeform Asari = new Lifeform(
                "\n\n///////////////////////////////////" +
                        "\nAsari" +
                        "\n///////////////////////////////////\n" +
                        "Asari are naturally calm and educated. The normally have no ill intentions but know they have \n" +
                        "psychic abilities and if one undergoes what they know as the 'Black Calling' they will \n" +
                        "psychicly drain their victims.");
        Asari.LifeformDescription();
    } // End Asari method


    // Kryptonians method
    void Kryptonians() {
        // Life form description too Kryptonians (FILE- Lifeform.java)
        Lifeform Kryptonians = new Lifeform(
                "\n\n///////////////////////////////////" +
                        "\nKryptonians" +
                        "\n///////////////////////////////////\n" +
                        "Another pieceful species that means no harm. They too are also well educated in many topics. \n" +
                        "With Kryptonians you have to beware of their strength and clumsiness as they interact with \n" +
                        "their surroundings.");
        Kryptonians.LifeformDescription();
    } // End Kryptonians method


    // Predators method
    void Predators() {
        // Life form description too Predators (FILE- Lifeform.java)
        Lifeform Predators = new Lifeform(
                "\n\n///////////////////////////////////" +
                        "\nPredators" +
                        "\n///////////////////////////////////\n" +
                        "Predators have a very strict code of honor amongst themselves and if violated can become \n" +
                        "violent. Also if you prove to be an interesting hunt you may be targeted.");
        Predators.LifeformDescription();
    } // End Predators method


    // Borg method
    void Borg() {
        // Life form description too Borg (FILE- Lifeform.java)
        Lifeform Borg = new Lifeform(
                "\n\n///////////////////////////////////" +
                        "\nBorg" +
                        "\n///////////////////////////////////\n" +
                        "Borg used to be a huge threat while assimalating everything they came in contact with. \n" +
                        "Now they are more dosile, still once in a while one will go rogue or corrupt.");
        Borg.LifeformDescription();
    } // End Borg method


//**********************************************************************************************************************
    // GetProminadeDescription method
    String GetProminadeDescription(){
        // String result loaded for GetProminadeDescription (FILE- Location.java)
        String result =
                        "The Prominade:\n" +
                        "Here you see so many beings of all shapes and sizes. You marvel at all the items\n" +
                        "you can purchase. There are wonders you didn't even know exsisted. There are\n" +
                        "recuiters for space travel here, food of all manors, weapons, chapels, and art.\n" +
                        "The space is so large that it almost looks like this place was it's own planet.\n";
        // return output to user
        return result;
    } // End GetProminadeDescription method


    // Lounge method
    String GetLoungeDescription(){
        // String result loaded for GetLoungeDescription (FILE- Location.java)
        String p =
                        "The Star Lounge:\n" +
                        "Nothing to exciting here. It is mostly a fancy eatery that has replicators.\n" +
                        "They say your can ask these machines to make anything and they'll be able \n" +
                        "to make it for you.... Hmmm... Should you put it to the test?\n";
        // return output to user
        return p;
    } // End Lounge method


    // Galaxy method
    String GetGalaxyDescription(){
        // String result loaded for GetGalaxyDescription (FILE- Location.java)
        String g =
                        "The Galaxy:\n" +
                        "This is quit the happening spot. The night club that never sleeps they claim.\n" +
                        "You can't help but walk in but as you do an odd looking creature pulls you to \n" +
                        "the side and introduces himself as Rex. He asks if you know about the races on \n" +
                        "the station and lists a few off. 'Any Questions?' he asks.\n";
        // return output to user
        return g;
    } // End Galaxy method


    // BridgeDoor method
    String GetBridgeDoorDescription(){
        // String result loaded for GetBridgeDoorDescription (FILE- Location.java)
        String bd =
                        "You arrive at the bridge entrance. There is a massive door in your way with a\n" +
                        "data pad glowing of to the side. You walk up to it and Alexa 'says greetings Captain.\n" +
                        "Please enter you last name for entry.'\n";
        // return output to user
        return bd;
    } // End BridgeDoor method


    // BridgeRoom method
    String GetBridgeRoomDescription(){
        // String result loaded for GetBridgeRoomDescription (FILE- Location.java)
        String br =
                        "You enter the bridge. In all your life you have never seen so much state of the art\n" +
                        "tech. There are people running around and screen displays everywhere. The Captains\n" +
                        "is right there in the middle facing away from you. Oh.. And it looks like the Captain\n" +
                        "is sitting in it... better get out of here before I'm noticed and in trouble.";
        // return output to user
        return br;
    } // End BridgeRoom method


    // Security method
    String GetSecurityDescription(){
        // String result loaded for GetSecurityDescription (FILE- Location.java)
        String s =
                        "Security:\n" +
                        "There are Officers everywhere here and they are armed with some heavy gear.\n" +
                        "I wouldn't want to mess with them at all. Still when you talk to one they seem\n" +
                        "friendly enough. They say don't be causing any trouble.\n";
        // return output to user
        return s;
    } // End Security method


    // Sim method
    String GetSimDescription(){
        // String result loaded for GetSimDescription (FILE- Location.java)
        String s1 =
                        "The Sim'1':\n" +
                        "This is the simulation labs. Here you can walk into a room and the room's \n" +
                        "biometrics will read your thoughts and create anything using light and micro\n" +
                        "water droplets. Feel free to imagine anything or anywhere. Here your will is\n" +
                        "reality.\n";
        // return output to user
        return s1;
    } // End Sim method


    // Docks method
    String GetDocksDescription(){
        // String result loaded for GetDocksDescription (FILE- Location.java)
        String d =
                        "The Docks:\n" +
                        "Here you can see out through massive glass windows as ships come and go from the station.\n" +
                        "There are some famous ships currently docked and want to know more about them. You\n" +
                        "notice a AI pad and walk up to it. Alexa materializes and asks You what you if you\n" +
                        "want to learn more about the ships. You say yes, and she displays the menu.\n";
        // return output to user
        return d;
    } // End Docks method


    // Luxury method
    String GetLuxuryDescription(){
        // String result loaded for GetLuxuryDescription (FILE- Location.java)
        String lx =
                        "The Luxury Living Quarters:\n" +
                        "They have some open home here out for display. They make homes on Earth look like\n" +
                        "shabby boxes. You enjoy pretending to feel like your going to buy a home. They each\n" +
                        "come with your own personal Alexa AI unit also... SWEET!!!. Then they drop the price\n" +
                        "tag of the cheapest one... 438 Million Credits... I could work for three lifetimes\n" +
                        "and never make that much\n";
        // return output to user
        return lx;
    } // End Luxury method
} // End AssetDescription Class

