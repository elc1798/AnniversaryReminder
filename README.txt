AnniversaryReminder by Ethan "SubliminalMau5" Cheng
---------------------------------------------------------------------------
This is a very simple program, mainly to remind forgetful boyfriends when their anniversary is, and how many days left there are until it comes up.
It uses simple .sh scripts and a main .py file to operate, and is intended to be run at startup. It will open a message box, displaying the
reminder for the user.
---------------------------------------------------------------------------

To install, "cd" into the folder containing this file and type in "sh install.sh" in Terminal.

On your first use, open a terminal and type in:

python ~/anniversary/main.py

EDIT: In the latest update, dependency on Gedit was removed, allowing the first use to be run simply by run.sh (See below)

Type in y and enter the number of your month and the day:

1 for January, 2 for February, 3 for March, etc.

To run the program, type in "sh ~/anniversary/run.sh" into Terminal.

To append this program to Startup Applications, Go to System > Startup Applications > Add...
-For the name, enter "AnniversaryReminder"
-For the command, enter "sh ~/anniversary/run.sh"

You can also go into your home directory and create a .bash_aliases if you do not have one already, and add the line:

alias anniversaryReminder="sh ~/anniversary/run.sh"

If you do this, you can run the program simply by typing in "anniversaryReminder" in Terminal.
Note that 'anniversaryReminder' can be changed to any command you wish, such as anniRem or anniCheck

IF you are not using this in a *nix system, then you need a Python Interpreter, such as IDLE to run the code.
To run the code in IDLE, simply open "src/main.py" in IDLE and hit F5 to run.
