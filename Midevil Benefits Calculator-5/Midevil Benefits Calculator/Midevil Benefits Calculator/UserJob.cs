/////////////////////////////////////////////////
// JERARD CARNEY
// 10/4/2020
// MBC Project (Midevil Benefits Calculator)
// Jobs Class (UserJob.cs)
/////////////////////////////////////////////////


// libs used... general setup for class by VS 2017
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


// get set class for Jobs.
// namespace is the main application nameing
namespace Midevil_Benefits_Calculator
{
    // Jobs class
    class UserJob
    {
        // gets set String Job (list).
        public string Job { get; set; }

        // gets set Double Modifier (list)
        public double JobModifier { get; set; }

        /// <summary>
        /// Constructors
        /// </summary>

        /// No overload
        public UserJob()
        {

        }

        // Overloaded
        public UserJob(string job, double mod)
        {
            this.Job = job;
            this.JobModifier = mod;
        }
    }// END
} // END
