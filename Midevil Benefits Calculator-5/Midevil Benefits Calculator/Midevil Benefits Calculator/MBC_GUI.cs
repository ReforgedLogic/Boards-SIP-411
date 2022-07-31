/////////////////////////////////////////////////
// JERARD CARNEY
// 10/4/2020
// MBC Project (Midevil Benefits Calculator)
// Main Applicate File (MBC_GUI.cs)
/////////////////////////////////////////////////


/////////////////////////////////////////////////
/// Librarries / Framworks used..  VS 2017
/////////////////////////////////////////////////
using System;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Windows.Forms;
using WMPLib;


/////////////////////////////////////////////////
/// Namespace of Form Main 
/////////////////////////////////////////////////
namespace Midevil_Benefits_Calculator
{
    
    /////////////////////////////////////////////////
    /// Main Class MBC_GUI for form
    /////////////////////////////////////////////////
    public partial class MidevilBenefitsCalculator_GUI : Form
    {
        // Reworked class instances to initialize in form partial class.
        UserInfo user = new UserInfo();
        UserStatus status = new UserStatus();
        UserJob job = new UserJob();
        UserRace race = new UserRace();
        UserDeployment deployment = new UserDeployment();
        UserInjury injury = new UserInjury();
        UserBonus bonus = new UserBonus();

        WindowsMediaPlayer music = new WindowsMediaPlayer();

      

        /////////////////////////////////////////////////
        /// Main Initialize Form Method for MBC_GUI
        /////////////////////////////////////////////////
        public MidevilBenefitsCalculator_GUI()
        {
            /////////////////////////////////////////////////
            /// Initialize MethodS !!!! IMPORTANT
            /////////////////////////////////////////////////
            // Form creation
            // Defult RichText creation
            InitializeComponent();
            InitializeMusic();
            InitializeLists();
            display_Default();


            /////////////////////////////////////////////////
            /// Initializing LISTS/VAR.
            /////////////////////////////////////////////////
            
            //Variables
            //Lotto = NOT USED
            bonus.Rolled = false;
            bonus.LottoModifier = 0;
            user.FirstName = "First";
            user.LastName = "Last";
            user.UserAge = 0;
            user.ExceptTerms = false;
            user.CurrentDate = DateTime.Now.ToString();
            user.BattleID = 0;
        } // END

        
        /////////////////////////////////////////////////
        /// Program Load Method
        /////////////////////////////////////////////////
        private void MidevilBenefitsCalculator_GUI_Load(object sender, EventArgs e)
        {
        //LOADS MBC_GUI
        } //END



        /////////////////////////////////////////////////
        /// Select Job Method
        /////////////////////////////////////////////////
        private void Jobselection_ComboBoxMBC_GUI_SelectedIndexChanged(object sender, EventArgs e)
        {
            // Take set class string and diplay to Label
            job = jobtitle_ComboBox_MBC_GUI.SelectedItem as UserJob;
            jobseletiondisplay_Label_MBC_GUI.Text = job.Job;
        } //END



        /////////////////////////////////////////////////
        /// Select Race Method
        /////////////////////////////////////////////////
        private void Race_ComboBox_MBC_GUI_SelectedIndexChanged(object sender, EventArgs e)
        {
            // Take set class string and diplay to Label
            race = race_ComboBox_MBC_GUI.SelectedItem as UserRace;
            racedisplay_Label_MBC_GUI.Text = race.Race;
        } //END



        /////////////////////////////////////////////////
        /// Select Deployments Method
        /////////////////////////////////////////////////
        private void Deployment_ComboBox_MBC_GUI_SelectedIndexChanged(object sender, EventArgs e)
        {
            // Take set class string and diplay to Label
            deployment = deployment_ComboBox_MBC_GUI.SelectedItem as UserDeployment;
            deploymentdisplay_Label_MBC_GUI.Text = deployment.Deployment;
        } //END



        /////////////////////////////////////////////////
        /// Select Injuries Method
        /////////////////////////////////////////////////
        private void injury_ComboBox_MBC_GUI_SelectedIndexChanged(object sender, EventArgs e)
        {
            // Take set class string and diplay to Label
            injury = injury_ComboBox_MBC_GUI.SelectedItem as UserInjury;
            injurydisplay_Label_MBC_GUI.Text = injury.Injury;
        } //END



        /////////////////////////////////////////////////
        /// Age Method
        /////////////////////////////////////////////////
        private void agevalue_TextBox_MBC_GUI_TextChanged(object sender, EventArgs e)
        {
            // CALLS - to set age Double
            setage();
        }//END



        /////////////////////////////////////////////////
        /// Radio Method Group (!notes)
        /////////////////////////////////////////////////
        /// THE FOLLOWING ARE METHODS FOR grouped 
        /// radio buttons THAT PREFORM THE SAME TASK BY
        /// CALLING THE SAME METHOD. THESE METHODS ARE FOR
        /// THE radio buttons: Alive, Dead, Hero, MIA, 
        /// and Deserter.
        /////////////////////////////////////////////////
        ///
        private void alive_radioButton_CheckedChanged(object sender, EventArgs e)
        {
            living_Status(alive_radioButton, 1, "Alive");
        }// END
        private void dead_radioButton_CheckedChanged(object sender, EventArgs e)
        {
            living_Status(dead_radioButton, 4, "Dead");
        }// END
        private void hero_radioButton_CheckedChanged(object sender, EventArgs e)
        {
            loyalty_Status(hero_radioButton, 2.7);
        }// END
        private void standard_radioButton_CheckedChanged(object sender, EventArgs e)
        {
            loyalty_Status(standard_radioButton, 1);
        }// END
        private void mia_radioButton_CheckedChanged(object sender, EventArgs e)
        {
            loyalty_Status(mia_radioButton, 1.2);
        }// END
        private void deserter_radioButton_CheckedChanged(object sender, EventArgs e)
        {
            loyalty_Status(deserter_radioButton, -1);
        }// END

        /////////////////////////////////////////////////
        /// Audio ON OFF 
        /////////////////////////////////////////////////
        private void audiocontrol_Checkbox_MBC_GUI_CheckedChanged(object sender, EventArgs e)
        {
            // Variables
            // bool is t/f for on and off
            bool On = audiocontrol_Checkbox_MBC_GUI.Checked;

            // if checkbox is true
            if (On == true)
            {
                // turn on music
                music.controls.play();
            }
            // if checkbox is false
            else if (On == false)
            {
                // turn off music
                music.controls.stop();
            }
            // else = unknown reason
            else
            {
                // display to user
                MessageBox.Show("Music = NOT FUNCTIONING");
            }
        }// END

        /////////////////////////////////////////////////
        /// Volume Slider 
        /////////////////////////////////////////////////
        private void volumebar_Tracker_MBC_GUI_Scroll(object sender, EventArgs e)
        {
            // ties tracker (SLIDER) to music volume.
            music.settings.volume = volumebar_Tracker_MBC_GUI.Value;
        }// END

        /////////////////////////////////////////////////
        /// Lottery 
        /////////////////////////////////////////////////
        private void lottery_Button_MBC_GUI_Click(object sender, EventArgs e)
        {
            // ERR HAND. using if then (MANUAL FIND)... variable (bonus) SET
            if (bonus.Rolled == true)
            {
                MessageBox.Show("You may only roll for bonus once.");
            }
            else
            {
                // CALL lottery roll
                // diplay roll result
                // set bonus as rolled
                bonus_Lottery_Value_Generator();
                lotterydisplay_Label_MBC_GUI.Text = bonus.LottoModifier.ToString("");
                bonus.Rolled = true;
            }
        }// END

        /////////////////////////////////////////////////
        /// Save File 
        /////////////////////////////////////////////////
        private void saverewardpack_Button_MBC_GUI_Click(object sender, EventArgs e)
        {
            // Error Handling... if else
            // if the reward is accepted
            if (accepttreward_Label_MBC_GUI.Text == "Accepted")
            {
                //call save file
                writefilename();
            }
            // if the reward isn't accepted
            else
            {
                // display issue to user
                MessageBox.Show("You must finish and ACCEPT your rewards before saving.");
            }
        }// END

        /////////////////////////////////////////////////
        /// Calulation Method (!notes)
        /////////////////////////////////////////////////
        private void Calculatebenefits_Button_MBC_GUI_Click(object sender, EventArgs e)
        {
            // Declaring Variables

            // Result is the value of the trasitioning equation for user benefits
            double result = 0;
            double taxrate = .07;

            // initializing intances of classes
            // Jobs jobtitleincome = jobtitle_ComboBox_MBC_GUI.SelectedItem as Jobs;
            // Races racemodifiers = race_ComboBox_MBC_GUI.SelectedItem as Races;
            // Deployments deploymentadjustments = deployment_ComboBox_MBC_GUI.SelectedItem as Deployments;
            // Injuries injuryadjustments = injury_ComboBox_MBC_GUI.SelectedItem as Injuries;


            /////////////////////////////////////////////////
            /// ERROR HANDLES
            /////////////////////////////////////////////////

            // ERR HAND. using if then (MANUAL FIND)... variable (result) RESET
            if (result != 0)
            {
                // Inform use of last result.. Tells dev. that number is reset.
                // result new value is 0
                MessageBox.Show("Benefits = NOT RESET... NOW RESET");
                result = 0;
            }
            else
            {
                // Allow user to continue.
                // MessageBox.Show("Benefits = RESET");  ...(FOR FUTURE USE)
            }


            // ERR HAND. using if then (MANUAL FIND)... variable (age) SET
            if (user.UserAge == double.NaN)
            {
                MessageBox.Show("Age = NOT A DOUBLE");
            }
            else
            {
                setage();
                //MessageBox.Show(ageinput.UserAge.ToString("Age = DOUBLE"));
            }


            // ERR HAND. using Try/catch (MANUAL FIND)...
            try
            {
                // ERR HAND. using if then (MANUAL FIND)... variable (lotto) SET
                if (bonus.LottoModifier == 0)
                {
                    bonus.LottoModifier = Convert.ToInt32(lotterydisplay_Label_MBC_GUI.Text);
                    //MessageBox.Show("Lotto = FAIL");
                }
                else
                {
                    //MessageBox.Show("Lotto = SUCCESS");
                }
            }
            catch
            {
                MessageBox.Show("Roll your Lotto Bonus.");
            }


            // ERR HAND. using if then (MANUAL FIND)... variable (loyalty) SET
            if (status.LoyaltyModifier == 0)
            {
                MessageBox.Show("Loyalty = NOT SELECTED");
            }
            else
            {
                //MessageBox.Show("Loyalty = SUCCES");
            }


            /////////////////////////////////////////////////
            /// METHOD CALLS - Equation !!!! IMPOTANT
            /////////////////////////////////////////////////
            //Call Equation
            result = benefits_Calculator(user.UserAge, job.JobModifier, bonus.LottoModifier,
                injury.InjuryModifier, status.LoyaltyModifier, status.StatusModifier,
                race.RaceModifier, deployment.DeploymentModifier, taxrate);
            //Call Set User Data
            set_User_Data();
            //Call Display All Information
            display_Review(user.UserAge, job.JobModifier, bonus.LottoModifier,
                injury.InjuryModifier, status.LoyaltyModifier, status.StatusModifier,
                race.RaceModifier, deployment.DeploymentModifier, taxrate, result);
            //Call Lotto Reset
            bonus.Rolled = reset_Roll_Bool(bonus.Rolled);
            // Diplay Main Result
            benefitsdiplay_LABEL_MBC_GUI.Text = result.ToString("{0.##}") + " gold pieces";
            // Removes text from accept if user redoes results.
            accepttreward_Label_MBC_GUI.Text = "";
        }// END

        /////////////////////////////////////////////////
        /// Accept Rewards Button
        /////////////////////////////////////////////////
        private void acceptreward_Button_MBC_GUI_Click(object sender, EventArgs e)
        {
            // set label to show accept
            string accept = "Accepted";
            accepttreward_Label_MBC_GUI.Text = accept;
        }// END

        // DEV TEST... button
        private void benefitsdiplay_LABEL_MBC_GUI_Click(object sender, EventArgs e)
        {
            // Hidden Button For DEV TESTING!!!
        }// END

        /////////////////////////////////////////////////
        /// Load Rewards Button
        /////////////////////////////////////////////////
        private void loadreward_Button_MBC_GUI_Click(object sender, EventArgs e)
        {
            // Call to load text file.
            loadFile();
        }// END




        /////////////////////////////////////////////////
        /// Custom Methods
        /////////////////////////////////////////////////
        // Radio Button Status checker
        void living_Status(RadioButton radbut, double selectedvalue, string selecetedwords)
        {
            // take passed in radio button.check it
            if (radbut.Checked)
            {
                //if checked.set words to label.set value to status
                livingstatusdisplay_Label_MBC_GUI.Text = selecetedwords;
                status.StatusModifier = selectedvalue;
            }
        }// END

        // Radio Button Loyalty checker
        void loyalty_Status(RadioButton radbut, double selectedvalue)
        {
            // take passed in radio button.check it
            if (radbut.Checked)
            {
                //if checked.set words to label.set value to status
                loyatystatusdisplay_Label_MBC_GUI.Text = radbut.Text;
                status.LoyaltyModifier = selectedvalue;
            }
        }// END

        // Convert double to int... currently not used... saved for future
        //  int double_to_int(double incomingvalue)
        //  {
        //      // take passed double and covert to int
        //     int outgoingvalue = Convert.ToInt32(incomingvalue);
        //      return outgoingvalue;
        //  }

        // Random Number Generator
        void bonus_Lottery_Value_Generator()
        {
            // Variable Temp
            int bonusvalue;

            // uses random and make new instance
            // sets temp var to random value 1-3000
            // set class lotto value = random number
            Random numvalue = new Random();
            bonusvalue = numvalue.Next(1,3001);
            bonus.LottoModifier = bonusvalue;
        }// END

        // Reset Lotto Roll
        bool reset_Roll_Bool(bool reset)
        {
            // take boolean passed.set to false
            // return boolean value
            reset = false;
            return reset;
        }// END

        // Set User Age 
        void setage()
        {
            // Declare Variables
            string stringage = agevalue_TextBox_MBC_GUI.Text;

            // Error Containment... Do While...
            // If user does not put a value in that can be converted to a double
            // then put in a new value.
            

            // Set instnace of age to value of user textbox age
            // diplay age to form label
            user.UserAge = str_TO_dbl(stringage);
            agevaluedisplay_Label_MBC_GUI.Text = user.UserAge.ToString();
        } //END

        // Create Save File
        void writefilename()
        {
            // new instance of file
            SaveFileDialog filesavedname = new SaveFileDialog();
            // If file is a legal file name
            if (filesavedname.ShowDialog() == DialogResult.OK)
            {
                // Open file explorer and allow User to make name and type
                using (Stream save = File.Open(filesavedname.FileName, FileMode.CreateNew))

                // Using Streamer as IO to write new save
                using (StreamWriter savewrite = new StreamWriter(save))
                {
                    // the actual save of the RICHTEXTBOX text
                    savewrite.Write(reviewdocument_RTB_MBC_GUI.Text);
                }
            }
        }// END

        // Benefits Equation (PASSED 9 DOUBLES)
        double benefits_Calculator(double age, double job, double lotto, double injury, double loyalty, 
            double status, double race, double deployment, double tax)
        {
            // Variable Temp
            double rewardtotal = 0;
            // EQUATION = ((((( job + Injury + bonus + (age * 100)) /deployment) *status) *((race *loyalty) *tax)= retirment package
            rewardtotal = (((((age * 100) + job + injury + lotto) / deployment) * status) * ((race * loyalty) * tax));
            // Return temp variable value
            return rewardtotal;
        }// END

        // Defualt Display on Initalization
        void display_Default()
        {
            // String Formatting using data from classes
            // Diplays to RichTextBox
            reviewdocument_RTB_MBC_GUI.Text =
               "Date: " + user.CurrentDate + "\n\n\n" +


               "First: " + user.FirstName + "\n" +
               "Last: " + user.LastName + "\n" +
               "Battle ID: " + user.BattleID + "\n\n\n" +


               "Reward Package for " + user.FirstName + " " + user.LastName + ". Review the " +
               "following reward package and accept. If you have any issues contact your races' " +
               "resources scribe in the RH department. IMPORTANT!! - save this document after " +
               "you have accepted terms. By choosing accepted terms you are premorming a magical " +
               "signature (M-signature) that is legally and lethally binding. \n\n";
        }// END

        // Display Review Final (PASSED 10 DOUBLES)
        void display_Review(double agemod, double jobmod, double lottomod, double injurymod, double loyaltymod, 
            double statusmod, double racemod, double deploymentmod, double tax, double result)
        {
            // String Formatting using data from classes
            // Diplays to RichTextBox
            reviewdocument_RTB_MBC_GUI.Text =
                "Date: " + user.CurrentDate + "\n\n\n" +


                "First: " + user.FirstName + "\n" +
                "Last: " + user.LastName + "\n" +
                "Battle ID: " + user.BattleID + "\n\n\n" +


                "Reward Package for " + user.FirstName + " " + user.LastName + ". Review the " +
                "following reward package and accept. If you have any issues contact your races' " +
                "resources scribe in the RH department. IMPORTANT!! - save this document after " +
                "you have accepted terms. By choosing accepted terms you are premorming a magical " +
                "signature (M-signature) that is legally and lethally binding. \n\n" +

                "The Following Modifiers Apply: \n" +
                "\t" + job.Job + " = " + jobmod + " gp" + "\n" +
                "\t" + user.UserAge + " = " + (agemod * 100) + " gp" + "\n" +
                "\t" + race.Race + " = " + racemod + "\n" +
                "\t" + deployment.Deployment + " = " + deploymentmod + "\n" +
                "\t" + injury.Injury + " = " + injurymod + " gp" + "\n" +
                "\t" + livingstatusdisplay_Label_MBC_GUI.Text + " = " + statusmod + "\n" +
                "\t" + loyatystatusdisplay_Label_MBC_GUI.Text + " = " + loyaltymod + "\n" +
                "\t" + "Bonus = " + bonus.LottoModifier + " gp" + "\n\n" +

                "The above is calculated as follows: \n" +
                "(((((" + agemod + " * 100) + " + jobmod + " + " + injurymod + " + " + lottomod + ") / " +
                deploymentmod + ") * " + statusmod + ") * ((" + racemod + " * " + loyaltymod + ") * " + tax + "))\n\n" +

                "Total = " + result.ToString("0.##") + "\n\n\n\n" +


                "To accept this package click accept and save."
                ;
        }// END

        // Set User Data Values
        void set_User_Data()
        {
            // Variable Temps
            // gets current date and time.make date as stringB
            string current = DateTime.Now.ToShortDateString();
            string battleID = "";
            int dividedID = 0;
            int digitCount = 0;


            // sets strings value to firs, last, id, date
            user.FirstName = firstname_Textbox_MBC_GUI.Text;
            user.LastName = lastname_Textbox_MBC_GUI.Text;
            user.CurrentDate = current;
            battleID = ID_Textbox_MBC_GUI.Text;

            // Error Handling... try catch 
            try
            {
                // try to convert string ID to Int...
                user.BattleID = Convert.ToInt32(battleID);
            }
            catch
            {
                // Prompt user to put in numbers
                MessageBox.Show("Enter numbers only please.");
            }

            // set user battle id to int
            dividedID = user.BattleID;

            // Error Handling... try catch (NOTES!)
            /// this err hand. is designed to find if the number put in by
            /// the user is actually 5 digits. the thoery is take the input
            /// number and divide by 10 until it devides to 0. then count this
            /// each time to get the digit count.
            try
            {
                // while the input number is not 0 AND 
                // the digit of the number is less then 5
                while(dividedID > 0)
                {
                    // take the input # and /10
                    // digit count increase by 1
                    dividedID = dividedID / 10;
                    digitCount++;
                    //MessageBox.Show(digitCount.ToString());
                }

                // Error Handling... if else
                // if input number = 5 digits
                if(digitCount == 5) 
                {
                    //MessageBox.Show("ID = CORRECT LENGTH");
                }
                // if input number is more then 5 digits
                else if(digitCount > 5)
                {
                    
                    MessageBox.Show("ID = MORE THEN 5 DIGITS");
                }
                // if input number is less then 5 digits
                else if (digitCount < 5)
                {
                    MessageBox.Show("ID = LESS THEN 5 DIGITS");
                }
                // else something is very wrong
                else
                {
                    MessageBox.Show("ID = NOT =/>/<");
                }
            }
            // if all thee above doesn't work then digit count is a FAIL
            catch
            {
                MessageBox.Show("DIGIT COUNT = FAILED");
            }
        }// END

        // Turns strings into doubles if able
        double str_TO_dbl(string str)
        {
            double dbl;
            // Error Containment... Do While...
            // If user does not put a value in that can be converted to a double
            // then put in a new value.
            do
            {
                //ERR HAND. using if then messages (MANUAL FIND)
                if (double.TryParse(str, out dbl))
                {
                    // Just continue and don't disturb user
                    // MessageBox.Show("Valid Double"); ...(HERE FOR FUTURE USE)
                }
                else
                {
                    // Notify user invalid... 
                    // Set double to "NOT A NUMBER"... end result will be NaN and retry.
                    MessageBox.Show("Age = NOT A DOUBLE");
                    dbl = double.NaN;
                }
                // Is number equal to not a number
            } while (dbl == double.NaN);
            return dbl;
        }

        // Starts Music for Program
        void InitializeMusic()
        {
            music.URL = "ScottH_Epic.mp3";
        }

        // Lists put inot classes
        void InitializeLists() {
            // Lists
            // Job list.. populates class, which populates dropdown in form.
            List<UserJob> joblist = new List<UserJob>
            {
                new UserJob() { JobModifier = 1000, Job = "Commander" },
                new UserJob() { JobModifier = 650, Job = "Warrior" },
                new UserJob() { JobModifier = 725, Job = "Healer" },
                new UserJob() { JobModifier = 675, Job = "Mage" },
                new UserJob() { JobModifier = 300, Job = "Trebuchet Engineer" },
                new UserJob() { JobModifier = 150, Job = "Squire" },
                new UserJob() { JobModifier = 1450, Job = "Messanger" },
                new UserJob() { JobModifier = 500, Job = "Archer" },
                new UserJob() { JobModifier = 525, Job = "Rogue" },
                new UserJob() { JobModifier = 10, Job = "Conscript" },
            };
            // ComboBox uses data from class instance as data
            // ComboBox uses only string data to diplay in dropdown
            jobtitle_ComboBox_MBC_GUI.DataSource = joblist;
            jobtitle_ComboBox_MBC_GUI.DisplayMember = "Job";


            // Race list.. populates class, which populates dropdown in form.
            List<UserRace> racelist = new List<UserRace>
            {
                new UserRace() { RaceModifier = .73, Race = "Human"},
                new UserRace() { RaceModifier = .69, Race = "Elf"},
                new UserRace() { RaceModifier = .089, Race = "Orc"},
                new UserRace() { RaceModifier = .2, Race = "Gnome"},
                new UserRace() { RaceModifier = .065, Race = "Fiarie"},
                new UserRace() { RaceModifier = .4, Race = "Halfling"},
                new UserRace() { RaceModifier = .577, Race = "Dwarf"},
                new UserRace() { RaceModifier = .3, Race = "Teifling"},
                new UserRace() { RaceModifier = .099, Race = "Minotaur"},
            };
            // ComboBox uses data from class instance as data
            // ComboBox uses only string data to diplay in dropdown
            race_ComboBox_MBC_GUI.DataSource = racelist;
            race_ComboBox_MBC_GUI.DisplayMember = "Race";


            // Deployment list.. populates class, which populates dropdown in form.
            List<UserDeployment> deploymentlist = new List<UserDeployment>
            {
                new UserDeployment() {DeploymentModifier = .1, Deployment = "ONE"},
                new UserDeployment() {DeploymentModifier = .2, Deployment = "TWO"},
                new UserDeployment() {DeploymentModifier = .3, Deployment = "THREE"},
                new UserDeployment() {DeploymentModifier = .4, Deployment = "FOUR"},
                new UserDeployment() {DeploymentModifier = .5, Deployment = "FIVE"},
                new UserDeployment() {DeploymentModifier = .6, Deployment = "SIX"},
                new UserDeployment() {DeploymentModifier = .7, Deployment = "SEVEN"},
                new UserDeployment() {DeploymentModifier = .8, Deployment = "EIGHT"},
                new UserDeployment() {DeploymentModifier = .9, Deployment = "NINE"},
                new UserDeployment() {DeploymentModifier = .91, Deployment = "TEN"},
                new UserDeployment() {DeploymentModifier = .92, Deployment = "ELEVEN"},
                new UserDeployment() {DeploymentModifier = .93, Deployment = "TWELVE"},
                new UserDeployment() {DeploymentModifier = .94, Deployment = "THIRTEEN"},
                new UserDeployment() {DeploymentModifier = .95, Deployment = "FOURTEEN"},
                new UserDeployment() {DeploymentModifier = .96, Deployment = "FIFTEEN"},
                new UserDeployment() {DeploymentModifier = .97, Deployment = "SIXTEEN"},
                new UserDeployment() {DeploymentModifier = .98, Deployment = "SEVENTEEN"},
                new UserDeployment() {DeploymentModifier = .99, Deployment = "EIGHTEEN"},
                new UserDeployment() {DeploymentModifier = 1, Deployment = "NINETEEN"},
                new UserDeployment() {DeploymentModifier = 1.1, Deployment = "TWENTY or MORE"},
            };
            // ComboBox uses data from class instance as data
            // ComboBox uses only string data to diplay in dropdown
            deployment_ComboBox_MBC_GUI.DataSource = deploymentlist;
            deployment_ComboBox_MBC_GUI.DisplayMember = "Deployment";


            // Injuries list.. populates class, which populates dropdown in form.
            List<UserInjury> injurylist = new List<UserInjury>
            {
                new UserInjury() { InjuryModifier = 200, Injury = "0-2 Light Injuries"},
                new UserInjury() { InjuryModifier = 500, Injury = "3-5 Light Injuries"},
                new UserInjury() { InjuryModifier = 700, Injury = "6+ Light Injuries"},
                new UserInjury() { InjuryModifier = 600, Injury = "0-3 Heavy Injuries"},
                new UserInjury() { InjuryModifier = 1000, Injury = "4+ Heavy Injuries"},
                new UserInjury() { InjuryModifier = 1050, Injury = "0-2 Amputations"},
                new UserInjury() { InjuryModifier = 2100, Injury = "3-4 Amputations"},
            };
            // ComboBox uses data from class instance as data
            // ComboBox uses only string data to diplay in dropdown
            injury_ComboBox_MBC_GUI.DataSource = injurylist;
            injury_ComboBox_MBC_GUI.DisplayMember = "Injury";
        }

        // Loads a TEXT FILE 
        async void loadFile()
        {
            // new instance of open file class
            OpenFileDialog loadfile = new OpenFileDialog();

            // load fiel selection will only show .txt in selection
            loadfile.Filter = "text|*.txt";

            // If the load is correct
            if (loadfile.ShowDialog() == DialogResult.OK)
            {
                // take file name and data
                using(StreamReader readfile = new StreamReader(loadfile.FileName))
                {
                    // diaplay data to rich text box
                    reviewdocument_RTB_MBC_GUI.Text = await readfile.ReadToEndAsync();
                }

                // chcnge the labe to accepted to re-save.
                string accept = "Accepted";
                accepttreward_Label_MBC_GUI.Text = accept;
            }
            else
            {
                // else there is and error for loading the file
                MessageBox.Show("Error loading your file.");
            };
        }// END
    }// END
}// END
