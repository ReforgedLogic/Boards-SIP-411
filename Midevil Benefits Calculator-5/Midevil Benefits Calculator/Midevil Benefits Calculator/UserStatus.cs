/////////////////////////////////////////////////
// JERARD CARNEY
// 10/4/2020
// MBC Project (Midevil Benefits Calculator)
// CBM Class (UserStatus.cs)
/////////////////////////////////////////////////


// libs used... general setup for class by VS 2017
using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;


// get set class for Status.
// namespace is the main application nameing
namespace Midevil_Benefits_Calculator
{
    // Status class
    class UserStatus
    {

        // gets set String Alive, Dead, Hero, MIA, Deserter.
        public string Alive { get; set; }
        public string Dead { get; set; }
        public string Hero { get; set; }
        public string MIA { get; set; }
        public string Deserter { get; set; }

        // gets set Double Modifier
        public double AliveModifier { get; set; }
        public double DeadModifier { get; set; }
        public double HeroModifier { get; set; }
        public double MIAModifier { get; set; }
        public double DeserterModifier { get; set; }
        public double StatusModifier { get; set; }
        public double LoyaltyModifier { get; set; }

        /// <summary>
        /// Constructors
        /// </summary>

        /// No overload
        public UserStatus()
        {

        }

        // Overloaded
        public UserStatus(string alive, string dead, string hero, string mia, string desert)
        {
            this.Alive = alive;
            this.Dead = dead;
            this.Hero = hero;
            this.Deserter = desert;
            this.MIA = mia;
        }

        // Overloaded
        public UserStatus(double alive, double dead, double hero, double mia, double deserter, double status, double loyal)
        {
            this.AliveModifier = alive;
            this.DeadModifier = dead;
            this.HeroModifier = hero;
            this.MIAModifier = mia;
            this.DeserterModifier = deserter;
            this.StatusModifier = status;
            this.LoyaltyModifier = loyal;
        }
    }// END
}// END
