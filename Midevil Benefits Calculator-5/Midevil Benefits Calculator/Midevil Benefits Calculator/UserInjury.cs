/////////////////////////////////////////////////
// JERARD CARNEY
// 10/4/2020
// MBC Project (Midevil Benefits Calculator)
// Injuries Class (UserInjury.cs)
/////////////////////////////////////////////////


// libs used... general setup for class by VS 2017
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


// get set class for Injury.
// namespace is the main application nameing
namespace Midevil_Benefits_Calculator
{
    //Injury class
    class UserInjury
    {
        // gets set String Injury (list).
        public string Injury { get; set; }

        // gets set Double Modifier (list)
        public double InjuryModifier { get; set; }

        /// <summary>
        /// Constructors
        /// </summary>

        /// No overload
        public UserInjury()
        {

        }
        
        // Overloaded
        public UserInjury(string injury, double mod)
        {
            this.Injury = injury;
            this.InjuryModifier = mod;
        }
    }// END
}// END
