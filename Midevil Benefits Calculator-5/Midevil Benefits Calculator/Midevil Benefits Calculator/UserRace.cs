/////////////////////////////////////////////////
// JERARD CARNEY
// 10/4/2020
// MBC Project (Midevil Benefits Calculator)
// Rasce Class (UserRace.cs)
/////////////////////////////////////////////////


// libs used... general setup for class by VS 2017
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;



// get set class for Race.
// namespace is the main application nameing
namespace Midevil_Benefits_Calculator
{
    //Race Class
    class UserRace
    {
        // gets set String Race (list).
        public string Race { get; set; }

        // gets set Double Modifier (list)
        public double RaceModifier { get; set; }

        /// <summary>
        /// Constructors
        /// </summary>

        /// No overload
        public UserRace()
        {

        }

        // Overloaded
        public UserRace(string race, double mod)
        {
            this.Race = race;
            this.RaceModifier = mod;
        }
    }// END
}// END
