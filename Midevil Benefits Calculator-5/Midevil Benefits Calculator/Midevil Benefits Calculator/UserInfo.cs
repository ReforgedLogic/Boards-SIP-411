/////////////////////////////////////////////////
// JERARD CARNEY
// 10/4/2020
// MBC Project (Midevil Benefits Calculator)
// Age Class (UserInfo.cs)
/////////////////////////////////////////////////


// libs used... general setup for class by VS 2017
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


// get set class for UserInfo.
// namespace is the main application nameing
namespace Midevil_Benefits_Calculator
{
    //UserInfo Class
    class UserInfo
    {
        // gets set String FirstName, LastName, BattleID, CurrentDate.
        public string FirstName { get; set; }
        public string LastName { get; set; }
        public string CurrentDate { get; set; }

        // gets set Boolean ExceptTerms.
        public bool ExceptTerms { get; set; }


        // get set Double UserAge.
        public double UserAge { get; set; }

        // get set Int BattleID
        public int BattleID { get; set; }


        /// <summary>
        /// Constructors
        /// </summary>
       
        /// No overload
        public UserInfo()
        {

        }

        // Overloaded
        public UserInfo(string first, string last, string date, bool terms, double age, int id)
        {
            this.FirstName = first;
            this.LastName = last;
            this.CurrentDate = date;
            this.ExceptTerms = terms;
            this.UserAge = age;
            this.BattleID = id;
        }
    }// END
}//END
