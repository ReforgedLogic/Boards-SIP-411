/////////////////////////////////////////////////
// JERARD CARNEY
// 9/13/2020
// MBC Project (Midevil Benefits Calculator)
// Designer (MBC_GUI.Designer.cs)
/////////////////////////////////////////////////

namespace Midevil_Benefits_Calculator
{
    partial class MidevilBenefitsCalculator_GUI
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(MidevilBenefitsCalculator_GUI));
            this.jobtitle_ComboBox_MBC_GUI = new System.Windows.Forms.ComboBox();
            this.jobseletiondisplay_Label_MBC_GUI = new System.Windows.Forms.Label();
            this.jobtitleque_Display = new System.Windows.Forms.Label();
            this.race_ComboBox_MBC_GUI = new System.Windows.Forms.ComboBox();
            this.agevalue_TextBox_MBC_GUI = new System.Windows.Forms.TextBox();
            this.race_Display = new System.Windows.Forms.Label();
            this.agevaluedisplay_Label_MBC_GUI = new System.Windows.Forms.Label();
            this.racedisplay_Label_MBC_GUI = new System.Windows.Forms.Label();
            this.benefitsdiplay_LABEL_MBC_GUI = new System.Windows.Forms.Label();
            this.injury_ComboBox_MBC_GUI = new System.Windows.Forms.ComboBox();
            this.injurydisplay_Label_MBC_GUI = new System.Windows.Forms.Label();
            this.age_Display = new System.Windows.Forms.Label();
            this.injury_Display = new System.Windows.Forms.Label();
            this.status_Display = new System.Windows.Forms.Label();
            this.livingstatusdisplay_Label_MBC_GUI = new System.Windows.Forms.Label();
            this.deployment_ComboBox_MBC_GUI = new System.Windows.Forms.ComboBox();
            this.label1 = new System.Windows.Forms.Label();
            this.deploymentdisplay_Label_MBC_GUI = new System.Windows.Forms.Label();
            this.loyalty_Label_MCB_GUI = new System.Windows.Forms.Label();
            this.loyatystatusdisplay_Label_MBC_GUI = new System.Windows.Forms.Label();
            this.hero_radioButton = new System.Windows.Forms.RadioButton();
            this.mia_radioButton = new System.Windows.Forms.RadioButton();
            this.deserter_radioButton = new System.Windows.Forms.RadioButton();
            this.standard_radioButton = new System.Windows.Forms.RadioButton();
            this.alive_radioButton = new System.Windows.Forms.RadioButton();
            this.dead_radioButton = new System.Windows.Forms.RadioButton();
            this.lotterylabel = new System.Windows.Forms.Label();
            this.calculatebenefits_Button_MBC_GUI = new System.Windows.Forms.Button();
            this.lottery_Button_MBC_GUI = new System.Windows.Forms.Button();
            this.lotterydisplay_Label_MBC_GUI = new System.Windows.Forms.Label();
            this.GB_Status = new System.Windows.Forms.GroupBox();
            this.GB_Loyal = new System.Windows.Forms.GroupBox();
            this.saverewardpack_Button_MBC_GUI = new System.Windows.Forms.Button();
            this.rewardsinfo_GB_MBC_GUI = new System.Windows.Forms.GroupBox();
            this.accepttreward_Label_MBC_GUI = new System.Windows.Forms.Label();
            this.reviewdoc_Label_MBC_GUI = new System.Windows.Forms.Label();
            this.reviewdocument_RTB_MBC_GUI = new System.Windows.Forms.RichTextBox();
            this.ID_Textbox_MBC_GUI = new System.Windows.Forms.TextBox();
            this.lastname_Textbox_MBC_GUI = new System.Windows.Forms.TextBox();
            this.firstname_Textbox_MBC_GUI = new System.Windows.Forms.TextBox();
            this.acceptreward_Button_MBC_GUI = new System.Windows.Forms.Button();
            this.firstname_Label_MBC_GUI = new System.Windows.Forms.Label();
            this.lastname_Label_MBC_GUI = new System.Windows.Forms.Label();
            this.ID_Label_MBC_GUI = new System.Windows.Forms.Label();
            this.audiocontrol_Checkbox_MBC_GUI = new System.Windows.Forms.CheckBox();
            this.ambiant_WMP_MBC_GUI = new AxWMPLib.AxWindowsMediaPlayer();
            this.volumebar_Tracker_MBC_GUI = new System.Windows.Forms.TrackBar();
            this.loadreward_Button_MBC_GUI = new System.Windows.Forms.Button();
            this.GB_Status.SuspendLayout();
            this.GB_Loyal.SuspendLayout();
            this.rewardsinfo_GB_MBC_GUI.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.ambiant_WMP_MBC_GUI)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.volumebar_Tracker_MBC_GUI)).BeginInit();
            this.SuspendLayout();
            // 
            // jobtitle_ComboBox_MBC_GUI
            // 
            this.jobtitle_ComboBox_MBC_GUI.BackColor = System.Drawing.Color.Tan;
            this.jobtitle_ComboBox_MBC_GUI.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.jobtitle_ComboBox_MBC_GUI.FormattingEnabled = true;
            resources.ApplyResources(this.jobtitle_ComboBox_MBC_GUI, "jobtitle_ComboBox_MBC_GUI");
            this.jobtitle_ComboBox_MBC_GUI.Name = "jobtitle_ComboBox_MBC_GUI";
            this.jobtitle_ComboBox_MBC_GUI.SelectedIndexChanged += new System.EventHandler(this.Jobselection_ComboBoxMBC_GUI_SelectedIndexChanged);
            // 
            // jobseletiondisplay_Label_MBC_GUI
            // 
            resources.ApplyResources(this.jobseletiondisplay_Label_MBC_GUI, "jobseletiondisplay_Label_MBC_GUI");
            this.jobseletiondisplay_Label_MBC_GUI.BackColor = System.Drawing.SystemColors.ActiveCaption;
            this.jobseletiondisplay_Label_MBC_GUI.ForeColor = System.Drawing.SystemColors.ActiveCaptionText;
            this.jobseletiondisplay_Label_MBC_GUI.Image = global::Midevil_Benefits_Calculator.Properties.Resources.download;
            this.jobseletiondisplay_Label_MBC_GUI.Name = "jobseletiondisplay_Label_MBC_GUI";
            // 
            // jobtitleque_Display
            // 
            resources.ApplyResources(this.jobtitleque_Display, "jobtitleque_Display");
            this.jobtitleque_Display.BackColor = System.Drawing.Color.Black;
            this.jobtitleque_Display.ForeColor = System.Drawing.SystemColors.ButtonFace;
            this.jobtitleque_Display.Name = "jobtitleque_Display";
            // 
            // race_ComboBox_MBC_GUI
            // 
            this.race_ComboBox_MBC_GUI.BackColor = System.Drawing.Color.Tan;
            this.race_ComboBox_MBC_GUI.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.race_ComboBox_MBC_GUI.FormattingEnabled = true;
            this.race_ComboBox_MBC_GUI.Items.AddRange(new object[] {
            resources.GetString("race_ComboBox_MBC_GUI.Items"),
            resources.GetString("race_ComboBox_MBC_GUI.Items1"),
            resources.GetString("race_ComboBox_MBC_GUI.Items2"),
            resources.GetString("race_ComboBox_MBC_GUI.Items3"),
            resources.GetString("race_ComboBox_MBC_GUI.Items4")});
            resources.ApplyResources(this.race_ComboBox_MBC_GUI, "race_ComboBox_MBC_GUI");
            this.race_ComboBox_MBC_GUI.Name = "race_ComboBox_MBC_GUI";
            this.race_ComboBox_MBC_GUI.SelectedIndexChanged += new System.EventHandler(this.Race_ComboBox_MBC_GUI_SelectedIndexChanged);
            // 
            // agevalue_TextBox_MBC_GUI
            // 
            this.agevalue_TextBox_MBC_GUI.BackColor = System.Drawing.Color.Tan;
            resources.ApplyResources(this.agevalue_TextBox_MBC_GUI, "agevalue_TextBox_MBC_GUI");
            this.agevalue_TextBox_MBC_GUI.Name = "agevalue_TextBox_MBC_GUI";
            this.agevalue_TextBox_MBC_GUI.TextChanged += new System.EventHandler(this.agevalue_TextBox_MBC_GUI_TextChanged);
            // 
            // race_Display
            // 
            resources.ApplyResources(this.race_Display, "race_Display");
            this.race_Display.BackColor = System.Drawing.Color.Black;
            this.race_Display.ForeColor = System.Drawing.SystemColors.ButtonFace;
            this.race_Display.Name = "race_Display";
            // 
            // agevaluedisplay_Label_MBC_GUI
            // 
            resources.ApplyResources(this.agevaluedisplay_Label_MBC_GUI, "agevaluedisplay_Label_MBC_GUI");
            this.agevaluedisplay_Label_MBC_GUI.BackColor = System.Drawing.SystemColors.ActiveCaption;
            this.agevaluedisplay_Label_MBC_GUI.ForeColor = System.Drawing.SystemColors.ActiveCaptionText;
            this.agevaluedisplay_Label_MBC_GUI.Image = global::Midevil_Benefits_Calculator.Properties.Resources.download;
            this.agevaluedisplay_Label_MBC_GUI.Name = "agevaluedisplay_Label_MBC_GUI";
            // 
            // racedisplay_Label_MBC_GUI
            // 
            resources.ApplyResources(this.racedisplay_Label_MBC_GUI, "racedisplay_Label_MBC_GUI");
            this.racedisplay_Label_MBC_GUI.BackColor = System.Drawing.SystemColors.ActiveCaption;
            this.racedisplay_Label_MBC_GUI.ForeColor = System.Drawing.SystemColors.ActiveCaptionText;
            this.racedisplay_Label_MBC_GUI.Image = global::Midevil_Benefits_Calculator.Properties.Resources.download;
            this.racedisplay_Label_MBC_GUI.Name = "racedisplay_Label_MBC_GUI";
            // 
            // benefitsdiplay_LABEL_MBC_GUI
            // 
            resources.ApplyResources(this.benefitsdiplay_LABEL_MBC_GUI, "benefitsdiplay_LABEL_MBC_GUI");
            this.benefitsdiplay_LABEL_MBC_GUI.BackColor = System.Drawing.Color.Transparent;
            this.benefitsdiplay_LABEL_MBC_GUI.ForeColor = System.Drawing.SystemColors.ActiveCaptionText;
            this.benefitsdiplay_LABEL_MBC_GUI.Name = "benefitsdiplay_LABEL_MBC_GUI";
            // 
            // injury_ComboBox_MBC_GUI
            // 
            this.injury_ComboBox_MBC_GUI.BackColor = System.Drawing.Color.Tan;
            this.injury_ComboBox_MBC_GUI.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.injury_ComboBox_MBC_GUI.FormattingEnabled = true;
            this.injury_ComboBox_MBC_GUI.Items.AddRange(new object[] {
            resources.GetString("injury_ComboBox_MBC_GUI.Items"),
            resources.GetString("injury_ComboBox_MBC_GUI.Items1"),
            resources.GetString("injury_ComboBox_MBC_GUI.Items2"),
            resources.GetString("injury_ComboBox_MBC_GUI.Items3"),
            resources.GetString("injury_ComboBox_MBC_GUI.Items4")});
            resources.ApplyResources(this.injury_ComboBox_MBC_GUI, "injury_ComboBox_MBC_GUI");
            this.injury_ComboBox_MBC_GUI.Name = "injury_ComboBox_MBC_GUI";
            this.injury_ComboBox_MBC_GUI.SelectedIndexChanged += new System.EventHandler(this.injury_ComboBox_MBC_GUI_SelectedIndexChanged);
            // 
            // injurydisplay_Label_MBC_GUI
            // 
            resources.ApplyResources(this.injurydisplay_Label_MBC_GUI, "injurydisplay_Label_MBC_GUI");
            this.injurydisplay_Label_MBC_GUI.BackColor = System.Drawing.SystemColors.ActiveCaption;
            this.injurydisplay_Label_MBC_GUI.ForeColor = System.Drawing.SystemColors.ActiveCaptionText;
            this.injurydisplay_Label_MBC_GUI.Image = global::Midevil_Benefits_Calculator.Properties.Resources.download;
            this.injurydisplay_Label_MBC_GUI.Name = "injurydisplay_Label_MBC_GUI";
            // 
            // age_Display
            // 
            resources.ApplyResources(this.age_Display, "age_Display");
            this.age_Display.BackColor = System.Drawing.Color.Black;
            this.age_Display.ForeColor = System.Drawing.SystemColors.ButtonFace;
            this.age_Display.Name = "age_Display";
            // 
            // injury_Display
            // 
            resources.ApplyResources(this.injury_Display, "injury_Display");
            this.injury_Display.BackColor = System.Drawing.Color.Black;
            this.injury_Display.ForeColor = System.Drawing.SystemColors.ButtonFace;
            this.injury_Display.Name = "injury_Display";
            // 
            // status_Display
            // 
            resources.ApplyResources(this.status_Display, "status_Display");
            this.status_Display.BackColor = System.Drawing.Color.Black;
            this.status_Display.ForeColor = System.Drawing.SystemColors.ButtonFace;
            this.status_Display.Name = "status_Display";
            // 
            // livingstatusdisplay_Label_MBC_GUI
            // 
            resources.ApplyResources(this.livingstatusdisplay_Label_MBC_GUI, "livingstatusdisplay_Label_MBC_GUI");
            this.livingstatusdisplay_Label_MBC_GUI.BackColor = System.Drawing.SystemColors.ActiveCaption;
            this.livingstatusdisplay_Label_MBC_GUI.ForeColor = System.Drawing.SystemColors.ActiveCaptionText;
            this.livingstatusdisplay_Label_MBC_GUI.Image = global::Midevil_Benefits_Calculator.Properties.Resources.download;
            this.livingstatusdisplay_Label_MBC_GUI.Name = "livingstatusdisplay_Label_MBC_GUI";
            // 
            // deployment_ComboBox_MBC_GUI
            // 
            this.deployment_ComboBox_MBC_GUI.BackColor = System.Drawing.Color.Tan;
            this.deployment_ComboBox_MBC_GUI.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.deployment_ComboBox_MBC_GUI.FormattingEnabled = true;
            this.deployment_ComboBox_MBC_GUI.Items.AddRange(new object[] {
            resources.GetString("deployment_ComboBox_MBC_GUI.Items"),
            resources.GetString("deployment_ComboBox_MBC_GUI.Items1"),
            resources.GetString("deployment_ComboBox_MBC_GUI.Items2"),
            resources.GetString("deployment_ComboBox_MBC_GUI.Items3"),
            resources.GetString("deployment_ComboBox_MBC_GUI.Items4")});
            resources.ApplyResources(this.deployment_ComboBox_MBC_GUI, "deployment_ComboBox_MBC_GUI");
            this.deployment_ComboBox_MBC_GUI.Name = "deployment_ComboBox_MBC_GUI";
            this.deployment_ComboBox_MBC_GUI.SelectedIndexChanged += new System.EventHandler(this.Deployment_ComboBox_MBC_GUI_SelectedIndexChanged);
            // 
            // label1
            // 
            resources.ApplyResources(this.label1, "label1");
            this.label1.BackColor = System.Drawing.Color.Black;
            this.label1.ForeColor = System.Drawing.SystemColors.ButtonFace;
            this.label1.Name = "label1";
            // 
            // deploymentdisplay_Label_MBC_GUI
            // 
            resources.ApplyResources(this.deploymentdisplay_Label_MBC_GUI, "deploymentdisplay_Label_MBC_GUI");
            this.deploymentdisplay_Label_MBC_GUI.BackColor = System.Drawing.SystemColors.ActiveCaption;
            this.deploymentdisplay_Label_MBC_GUI.ForeColor = System.Drawing.SystemColors.ActiveCaptionText;
            this.deploymentdisplay_Label_MBC_GUI.Image = global::Midevil_Benefits_Calculator.Properties.Resources.download;
            this.deploymentdisplay_Label_MBC_GUI.Name = "deploymentdisplay_Label_MBC_GUI";
            // 
            // loyalty_Label_MCB_GUI
            // 
            resources.ApplyResources(this.loyalty_Label_MCB_GUI, "loyalty_Label_MCB_GUI");
            this.loyalty_Label_MCB_GUI.BackColor = System.Drawing.Color.Black;
            this.loyalty_Label_MCB_GUI.ForeColor = System.Drawing.SystemColors.ButtonFace;
            this.loyalty_Label_MCB_GUI.Name = "loyalty_Label_MCB_GUI";
            // 
            // loyatystatusdisplay_Label_MBC_GUI
            // 
            resources.ApplyResources(this.loyatystatusdisplay_Label_MBC_GUI, "loyatystatusdisplay_Label_MBC_GUI");
            this.loyatystatusdisplay_Label_MBC_GUI.BackColor = System.Drawing.SystemColors.ActiveCaption;
            this.loyatystatusdisplay_Label_MBC_GUI.ForeColor = System.Drawing.SystemColors.ActiveCaptionText;
            this.loyatystatusdisplay_Label_MBC_GUI.Image = global::Midevil_Benefits_Calculator.Properties.Resources.download;
            this.loyatystatusdisplay_Label_MBC_GUI.Name = "loyatystatusdisplay_Label_MBC_GUI";
            // 
            // hero_radioButton
            // 
            resources.ApplyResources(this.hero_radioButton, "hero_radioButton");
            this.hero_radioButton.Name = "hero_radioButton";
            this.hero_radioButton.TabStop = true;
            this.hero_radioButton.UseVisualStyleBackColor = true;
            this.hero_radioButton.CheckedChanged += new System.EventHandler(this.hero_radioButton_CheckedChanged);
            // 
            // mia_radioButton
            // 
            resources.ApplyResources(this.mia_radioButton, "mia_radioButton");
            this.mia_radioButton.Name = "mia_radioButton";
            this.mia_radioButton.TabStop = true;
            this.mia_radioButton.UseVisualStyleBackColor = true;
            this.mia_radioButton.CheckedChanged += new System.EventHandler(this.mia_radioButton_CheckedChanged);
            // 
            // deserter_radioButton
            // 
            resources.ApplyResources(this.deserter_radioButton, "deserter_radioButton");
            this.deserter_radioButton.Name = "deserter_radioButton";
            this.deserter_radioButton.TabStop = true;
            this.deserter_radioButton.UseVisualStyleBackColor = true;
            this.deserter_radioButton.CheckedChanged += new System.EventHandler(this.deserter_radioButton_CheckedChanged);
            // 
            // standard_radioButton
            // 
            resources.ApplyResources(this.standard_radioButton, "standard_radioButton");
            this.standard_radioButton.Name = "standard_radioButton";
            this.standard_radioButton.TabStop = true;
            this.standard_radioButton.UseVisualStyleBackColor = true;
            this.standard_radioButton.CheckedChanged += new System.EventHandler(this.standard_radioButton_CheckedChanged);
            // 
            // alive_radioButton
            // 
            resources.ApplyResources(this.alive_radioButton, "alive_radioButton");
            this.alive_radioButton.Name = "alive_radioButton";
            this.alive_radioButton.TabStop = true;
            this.alive_radioButton.UseVisualStyleBackColor = true;
            this.alive_radioButton.CheckedChanged += new System.EventHandler(this.alive_radioButton_CheckedChanged);
            // 
            // dead_radioButton
            // 
            resources.ApplyResources(this.dead_radioButton, "dead_radioButton");
            this.dead_radioButton.Name = "dead_radioButton";
            this.dead_radioButton.TabStop = true;
            this.dead_radioButton.UseVisualStyleBackColor = true;
            this.dead_radioButton.CheckedChanged += new System.EventHandler(this.dead_radioButton_CheckedChanged);
            // 
            // lotterylabel
            // 
            resources.ApplyResources(this.lotterylabel, "lotterylabel");
            this.lotterylabel.BackColor = System.Drawing.Color.Black;
            this.lotterylabel.ForeColor = System.Drawing.SystemColors.ButtonFace;
            this.lotterylabel.Name = "lotterylabel";
            // 
            // calculatebenefits_Button_MBC_GUI
            // 
            resources.ApplyResources(this.calculatebenefits_Button_MBC_GUI, "calculatebenefits_Button_MBC_GUI");
            this.calculatebenefits_Button_MBC_GUI.Image = global::Midevil_Benefits_Calculator.Properties.Resources.download;
            this.calculatebenefits_Button_MBC_GUI.Name = "calculatebenefits_Button_MBC_GUI";
            this.calculatebenefits_Button_MBC_GUI.UseVisualStyleBackColor = true;
            this.calculatebenefits_Button_MBC_GUI.Click += new System.EventHandler(this.Calculatebenefits_Button_MBC_GUI_Click);
            // 
            // lottery_Button_MBC_GUI
            // 
            resources.ApplyResources(this.lottery_Button_MBC_GUI, "lottery_Button_MBC_GUI");
            this.lottery_Button_MBC_GUI.Image = global::Midevil_Benefits_Calculator.Properties.Resources.download;
            this.lottery_Button_MBC_GUI.Name = "lottery_Button_MBC_GUI";
            this.lottery_Button_MBC_GUI.UseVisualStyleBackColor = true;
            this.lottery_Button_MBC_GUI.Click += new System.EventHandler(this.lottery_Button_MBC_GUI_Click);
            // 
            // lotterydisplay_Label_MBC_GUI
            // 
            resources.ApplyResources(this.lotterydisplay_Label_MBC_GUI, "lotterydisplay_Label_MBC_GUI");
            this.lotterydisplay_Label_MBC_GUI.BackColor = System.Drawing.SystemColors.ActiveCaption;
            this.lotterydisplay_Label_MBC_GUI.ForeColor = System.Drawing.SystemColors.ActiveCaptionText;
            this.lotterydisplay_Label_MBC_GUI.Image = global::Midevil_Benefits_Calculator.Properties.Resources.download;
            this.lotterydisplay_Label_MBC_GUI.Name = "lotterydisplay_Label_MBC_GUI";
            // 
            // GB_Status
            // 
            this.GB_Status.Controls.Add(this.status_Display);
            this.GB_Status.Controls.Add(this.alive_radioButton);
            this.GB_Status.Controls.Add(this.dead_radioButton);
            resources.ApplyResources(this.GB_Status, "GB_Status");
            this.GB_Status.Name = "GB_Status";
            this.GB_Status.TabStop = false;
            // 
            // GB_Loyal
            // 
            this.GB_Loyal.Controls.Add(this.loyalty_Label_MCB_GUI);
            this.GB_Loyal.Controls.Add(this.hero_radioButton);
            this.GB_Loyal.Controls.Add(this.standard_radioButton);
            this.GB_Loyal.Controls.Add(this.mia_radioButton);
            this.GB_Loyal.Controls.Add(this.deserter_radioButton);
            resources.ApplyResources(this.GB_Loyal, "GB_Loyal");
            this.GB_Loyal.Name = "GB_Loyal";
            this.GB_Loyal.TabStop = false;
            // 
            // saverewardpack_Button_MBC_GUI
            // 
            resources.ApplyResources(this.saverewardpack_Button_MBC_GUI, "saverewardpack_Button_MBC_GUI");
            this.saverewardpack_Button_MBC_GUI.Image = global::Midevil_Benefits_Calculator.Properties.Resources.download;
            this.saverewardpack_Button_MBC_GUI.Name = "saverewardpack_Button_MBC_GUI";
            this.saverewardpack_Button_MBC_GUI.UseVisualStyleBackColor = true;
            this.saverewardpack_Button_MBC_GUI.Click += new System.EventHandler(this.saverewardpack_Button_MBC_GUI_Click);
            // 
            // rewardsinfo_GB_MBC_GUI
            // 
            this.rewardsinfo_GB_MBC_GUI.BackgroundImage = global::Midevil_Benefits_Calculator.Properties.Resources.another_rough_old_and_worn_parchment_paper;
            resources.ApplyResources(this.rewardsinfo_GB_MBC_GUI, "rewardsinfo_GB_MBC_GUI");
            this.rewardsinfo_GB_MBC_GUI.Controls.Add(this.accepttreward_Label_MBC_GUI);
            this.rewardsinfo_GB_MBC_GUI.Controls.Add(this.reviewdoc_Label_MBC_GUI);
            this.rewardsinfo_GB_MBC_GUI.Controls.Add(this.reviewdocument_RTB_MBC_GUI);
            this.rewardsinfo_GB_MBC_GUI.Controls.Add(this.benefitsdiplay_LABEL_MBC_GUI);
            this.rewardsinfo_GB_MBC_GUI.Name = "rewardsinfo_GB_MBC_GUI";
            this.rewardsinfo_GB_MBC_GUI.TabStop = false;
            // 
            // accepttreward_Label_MBC_GUI
            // 
            resources.ApplyResources(this.accepttreward_Label_MBC_GUI, "accepttreward_Label_MBC_GUI");
            this.accepttreward_Label_MBC_GUI.BackColor = System.Drawing.Color.Transparent;
            this.accepttreward_Label_MBC_GUI.Name = "accepttreward_Label_MBC_GUI";
            // 
            // reviewdoc_Label_MBC_GUI
            // 
            resources.ApplyResources(this.reviewdoc_Label_MBC_GUI, "reviewdoc_Label_MBC_GUI");
            this.reviewdoc_Label_MBC_GUI.BackColor = System.Drawing.Color.Transparent;
            this.reviewdoc_Label_MBC_GUI.Name = "reviewdoc_Label_MBC_GUI";
            // 
            // reviewdocument_RTB_MBC_GUI
            // 
            this.reviewdocument_RTB_MBC_GUI.BackColor = System.Drawing.Color.Tan;
            resources.ApplyResources(this.reviewdocument_RTB_MBC_GUI, "reviewdocument_RTB_MBC_GUI");
            this.reviewdocument_RTB_MBC_GUI.Name = "reviewdocument_RTB_MBC_GUI";
            this.reviewdocument_RTB_MBC_GUI.ReadOnly = true;
            // 
            // ID_Textbox_MBC_GUI
            // 
            this.ID_Textbox_MBC_GUI.BackColor = System.Drawing.Color.Tan;
            resources.ApplyResources(this.ID_Textbox_MBC_GUI, "ID_Textbox_MBC_GUI");
            this.ID_Textbox_MBC_GUI.Name = "ID_Textbox_MBC_GUI";
            // 
            // lastname_Textbox_MBC_GUI
            // 
            this.lastname_Textbox_MBC_GUI.BackColor = System.Drawing.Color.Tan;
            resources.ApplyResources(this.lastname_Textbox_MBC_GUI, "lastname_Textbox_MBC_GUI");
            this.lastname_Textbox_MBC_GUI.Name = "lastname_Textbox_MBC_GUI";
            // 
            // firstname_Textbox_MBC_GUI
            // 
            this.firstname_Textbox_MBC_GUI.BackColor = System.Drawing.Color.Tan;
            resources.ApplyResources(this.firstname_Textbox_MBC_GUI, "firstname_Textbox_MBC_GUI");
            this.firstname_Textbox_MBC_GUI.Name = "firstname_Textbox_MBC_GUI";
            // 
            // acceptreward_Button_MBC_GUI
            // 
            resources.ApplyResources(this.acceptreward_Button_MBC_GUI, "acceptreward_Button_MBC_GUI");
            this.acceptreward_Button_MBC_GUI.Image = global::Midevil_Benefits_Calculator.Properties.Resources.download;
            this.acceptreward_Button_MBC_GUI.Name = "acceptreward_Button_MBC_GUI";
            this.acceptreward_Button_MBC_GUI.UseVisualStyleBackColor = true;
            this.acceptreward_Button_MBC_GUI.Click += new System.EventHandler(this.acceptreward_Button_MBC_GUI_Click);
            // 
            // firstname_Label_MBC_GUI
            // 
            resources.ApplyResources(this.firstname_Label_MBC_GUI, "firstname_Label_MBC_GUI");
            this.firstname_Label_MBC_GUI.BackColor = System.Drawing.SystemColors.ActiveCaption;
            this.firstname_Label_MBC_GUI.ForeColor = System.Drawing.SystemColors.ActiveCaptionText;
            this.firstname_Label_MBC_GUI.Image = global::Midevil_Benefits_Calculator.Properties.Resources.download;
            this.firstname_Label_MBC_GUI.Name = "firstname_Label_MBC_GUI";
            // 
            // lastname_Label_MBC_GUI
            // 
            resources.ApplyResources(this.lastname_Label_MBC_GUI, "lastname_Label_MBC_GUI");
            this.lastname_Label_MBC_GUI.BackColor = System.Drawing.SystemColors.ActiveCaption;
            this.lastname_Label_MBC_GUI.ForeColor = System.Drawing.SystemColors.ActiveCaptionText;
            this.lastname_Label_MBC_GUI.Image = global::Midevil_Benefits_Calculator.Properties.Resources.download;
            this.lastname_Label_MBC_GUI.Name = "lastname_Label_MBC_GUI";
            // 
            // ID_Label_MBC_GUI
            // 
            resources.ApplyResources(this.ID_Label_MBC_GUI, "ID_Label_MBC_GUI");
            this.ID_Label_MBC_GUI.BackColor = System.Drawing.SystemColors.ActiveCaption;
            this.ID_Label_MBC_GUI.ForeColor = System.Drawing.SystemColors.ActiveCaptionText;
            this.ID_Label_MBC_GUI.Image = global::Midevil_Benefits_Calculator.Properties.Resources.download;
            this.ID_Label_MBC_GUI.Name = "ID_Label_MBC_GUI";
            // 
            // audiocontrol_Checkbox_MBC_GUI
            // 
            resources.ApplyResources(this.audiocontrol_Checkbox_MBC_GUI, "audiocontrol_Checkbox_MBC_GUI");
            this.audiocontrol_Checkbox_MBC_GUI.Checked = true;
            this.audiocontrol_Checkbox_MBC_GUI.CheckState = System.Windows.Forms.CheckState.Checked;
            this.audiocontrol_Checkbox_MBC_GUI.Name = "audiocontrol_Checkbox_MBC_GUI";
            this.audiocontrol_Checkbox_MBC_GUI.UseVisualStyleBackColor = true;
            this.audiocontrol_Checkbox_MBC_GUI.CheckedChanged += new System.EventHandler(this.audiocontrol_Checkbox_MBC_GUI_CheckedChanged);
            // 
            // ambiant_WMP_MBC_GUI
            // 
            resources.ApplyResources(this.ambiant_WMP_MBC_GUI, "ambiant_WMP_MBC_GUI");
            this.ambiant_WMP_MBC_GUI.Name = "ambiant_WMP_MBC_GUI";
            this.ambiant_WMP_MBC_GUI.OcxState = ((System.Windows.Forms.AxHost.State)(resources.GetObject("ambiant_WMP_MBC_GUI.OcxState")));
            // 
            // volumebar_Tracker_MBC_GUI
            // 
            this.volumebar_Tracker_MBC_GUI.BackColor = System.Drawing.Color.Black;
            resources.ApplyResources(this.volumebar_Tracker_MBC_GUI, "volumebar_Tracker_MBC_GUI");
            this.volumebar_Tracker_MBC_GUI.Maximum = 50;
            this.volumebar_Tracker_MBC_GUI.Name = "volumebar_Tracker_MBC_GUI";
            this.volumebar_Tracker_MBC_GUI.Scroll += new System.EventHandler(this.volumebar_Tracker_MBC_GUI_Scroll);
            // 
            // loadreward_Button_MBC_GUI
            // 
            resources.ApplyResources(this.loadreward_Button_MBC_GUI, "loadreward_Button_MBC_GUI");
            this.loadreward_Button_MBC_GUI.Image = global::Midevil_Benefits_Calculator.Properties.Resources.download;
            this.loadreward_Button_MBC_GUI.Name = "loadreward_Button_MBC_GUI";
            this.loadreward_Button_MBC_GUI.UseVisualStyleBackColor = true;
            this.loadreward_Button_MBC_GUI.Click += new System.EventHandler(this.loadreward_Button_MBC_GUI_Click);
            // 
            // MidevilBenefitsCalculator_GUI
            // 
            resources.ApplyResources(this, "$this");
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.Tan;
            this.BackgroundImage = global::Midevil_Benefits_Calculator.Properties.Resources._52560e41bf604008451e6dae26edec2a;
            this.Controls.Add(this.loadreward_Button_MBC_GUI);
            this.Controls.Add(this.volumebar_Tracker_MBC_GUI);
            this.Controls.Add(this.ambiant_WMP_MBC_GUI);
            this.Controls.Add(this.audiocontrol_Checkbox_MBC_GUI);
            this.Controls.Add(this.ID_Label_MBC_GUI);
            this.Controls.Add(this.lastname_Label_MBC_GUI);
            this.Controls.Add(this.firstname_Label_MBC_GUI);
            this.Controls.Add(this.acceptreward_Button_MBC_GUI);
            this.Controls.Add(this.firstname_Textbox_MBC_GUI);
            this.Controls.Add(this.lastname_Textbox_MBC_GUI);
            this.Controls.Add(this.ID_Textbox_MBC_GUI);
            this.Controls.Add(this.rewardsinfo_GB_MBC_GUI);
            this.Controls.Add(this.saverewardpack_Button_MBC_GUI);
            this.Controls.Add(this.GB_Loyal);
            this.Controls.Add(this.GB_Status);
            this.Controls.Add(this.lotterydisplay_Label_MBC_GUI);
            this.Controls.Add(this.lottery_Button_MBC_GUI);
            this.Controls.Add(this.lotterylabel);
            this.Controls.Add(this.loyatystatusdisplay_Label_MBC_GUI);
            this.Controls.Add(this.deploymentdisplay_Label_MBC_GUI);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.deployment_ComboBox_MBC_GUI);
            this.Controls.Add(this.livingstatusdisplay_Label_MBC_GUI);
            this.Controls.Add(this.injury_Display);
            this.Controls.Add(this.age_Display);
            this.Controls.Add(this.injurydisplay_Label_MBC_GUI);
            this.Controls.Add(this.injury_ComboBox_MBC_GUI);
            this.Controls.Add(this.calculatebenefits_Button_MBC_GUI);
            this.Controls.Add(this.racedisplay_Label_MBC_GUI);
            this.Controls.Add(this.agevaluedisplay_Label_MBC_GUI);
            this.Controls.Add(this.race_Display);
            this.Controls.Add(this.agevalue_TextBox_MBC_GUI);
            this.Controls.Add(this.race_ComboBox_MBC_GUI);
            this.Controls.Add(this.jobtitleque_Display);
            this.Controls.Add(this.jobseletiondisplay_Label_MBC_GUI);
            this.Controls.Add(this.jobtitle_ComboBox_MBC_GUI);
            this.MinimizeBox = false;
            this.Name = "MidevilBenefitsCalculator_GUI";
            this.ShowIcon = false;
            this.Load += new System.EventHandler(this.MidevilBenefitsCalculator_GUI_Load);
            this.GB_Status.ResumeLayout(false);
            this.GB_Status.PerformLayout();
            this.GB_Loyal.ResumeLayout(false);
            this.GB_Loyal.PerformLayout();
            this.rewardsinfo_GB_MBC_GUI.ResumeLayout(false);
            this.rewardsinfo_GB_MBC_GUI.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.ambiant_WMP_MBC_GUI)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.volumebar_Tracker_MBC_GUI)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.ComboBox jobtitle_ComboBox_MBC_GUI;
        private System.Windows.Forms.Label jobseletiondisplay_Label_MBC_GUI;
        private System.Windows.Forms.Label jobtitleque_Display;
        private System.Windows.Forms.ComboBox race_ComboBox_MBC_GUI;
        private System.Windows.Forms.TextBox agevalue_TextBox_MBC_GUI;
        private System.Windows.Forms.Label race_Display;
        private System.Windows.Forms.Label agevaluedisplay_Label_MBC_GUI;
        private System.Windows.Forms.Label racedisplay_Label_MBC_GUI;
        private System.Windows.Forms.Label benefitsdiplay_LABEL_MBC_GUI;
        private System.Windows.Forms.ComboBox injury_ComboBox_MBC_GUI;
        private System.Windows.Forms.Label injurydisplay_Label_MBC_GUI;
        private System.Windows.Forms.Label age_Display;
        private System.Windows.Forms.Label injury_Display;
        private System.Windows.Forms.Label status_Display;
        private System.Windows.Forms.Label livingstatusdisplay_Label_MBC_GUI;
        private System.Windows.Forms.ComboBox deployment_ComboBox_MBC_GUI;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label deploymentdisplay_Label_MBC_GUI;
        private System.Windows.Forms.Label loyalty_Label_MCB_GUI;
        private System.Windows.Forms.Label loyatystatusdisplay_Label_MBC_GUI;
        private System.Windows.Forms.RadioButton hero_radioButton;
        private System.Windows.Forms.RadioButton mia_radioButton;
        private System.Windows.Forms.RadioButton deserter_radioButton;
        private System.Windows.Forms.RadioButton standard_radioButton;
        private System.Windows.Forms.RadioButton alive_radioButton;
        private System.Windows.Forms.RadioButton dead_radioButton;
        private System.Windows.Forms.Label lotterylabel;
        private System.Windows.Forms.Button calculatebenefits_Button_MBC_GUI;
        private System.Windows.Forms.Button lottery_Button_MBC_GUI;
        private System.Windows.Forms.Label lotterydisplay_Label_MBC_GUI;
        private System.Windows.Forms.GroupBox GB_Status;
        private System.Windows.Forms.GroupBox GB_Loyal;
        private System.Windows.Forms.Button saverewardpack_Button_MBC_GUI;
        private System.Windows.Forms.GroupBox rewardsinfo_GB_MBC_GUI;
        private System.Windows.Forms.Label reviewdoc_Label_MBC_GUI;
        private System.Windows.Forms.RichTextBox reviewdocument_RTB_MBC_GUI;
        private System.Windows.Forms.TextBox ID_Textbox_MBC_GUI;
        private System.Windows.Forms.TextBox lastname_Textbox_MBC_GUI;
        private System.Windows.Forms.TextBox firstname_Textbox_MBC_GUI;
        private System.Windows.Forms.Button acceptreward_Button_MBC_GUI;
        private System.Windows.Forms.Label firstname_Label_MBC_GUI;
        private System.Windows.Forms.Label lastname_Label_MBC_GUI;
        private System.Windows.Forms.Label ID_Label_MBC_GUI;
        private System.Windows.Forms.CheckBox audiocontrol_Checkbox_MBC_GUI;
        private AxWMPLib.AxWindowsMediaPlayer ambiant_WMP_MBC_GUI;
        private System.Windows.Forms.TrackBar volumebar_Tracker_MBC_GUI;
        private System.Windows.Forms.Label accepttreward_Label_MBC_GUI;
        private System.Windows.Forms.Button loadreward_Button_MBC_GUI;
    }
}

