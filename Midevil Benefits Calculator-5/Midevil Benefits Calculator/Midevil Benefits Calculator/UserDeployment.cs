/////////////////////////////////////////////////
// JERARD CARNEY
// 10/4/2020
// MBC Project (Midevil Benefits Calculator)
// Deployments Class (UserDeployment.cs)
/////////////////////////////////////////////////


// libs used... general setup for class by VS 2017
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;


// get set class for Deployment.
// namespace is the main application nameing
namespace Midevil_Benefits_Calculator
{

    //Deployment class
    class UserDeployment
    {
        // gets set String Deployment (list).
        public string Deployment { get; set; }

        // gets set Double Modifier (list)
        public double DeploymentModifier { get; set; }

        /// <summary>
        /// Constructors
        /// </summary>

        /// No overload
        public UserDeployment()
        {

        }

        // Overloaded
        public UserDeployment(string deploy, double mod)
        {
            this.Deployment = deploy;
            this.DeploymentModifier = mod;
        }
    }// END
}// END
