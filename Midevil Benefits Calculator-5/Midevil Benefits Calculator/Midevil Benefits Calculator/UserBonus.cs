/////////////////////////////////////////////////
// JERARD CARNEY
// 10/4/2020
// MBC Project (Midevil Benefits Calculator)
// Age Class (UserBonus.cs)
/////////////////////////////////////////////////

// libs used... general setup for class by VS 2017
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


// get set class for Bonus.
// namespace is the main application nameing
namespace Midevil_Benefits_Calculator
{
    // Bonus class
    class UserBonus
    {
        // gets set Boolean Rolled.
        public bool Rolled { get; set; }

        // gets set Double Modifier
        public int LottoModifier { get; set; }


        /// <summary>
        /// Constructors
        /// </summary>

        /// No overload
        public UserBonus()
        {

        }

        // Overloaded 
        public UserBonus(bool rolled, int lotto)
        {
            this.Rolled = rolled;
            this.LottoModifier = lotto;
        }
    }// END
}// END
