AnniversaryReminder by Ethan "SubliminalMau5" Cheng
---------------------------------------------------------------------------------------------------------------------------------------------------
This is a very simple program, mainly to remind forgetful boyfriends when their anniversary is, and how many days left there are until it comes up.
It uses simple .sh scripts and a main .py file to operate, and is intended to be run at startup. It will open a window in GEdit, displaying the
reminder for the user.
---------------------------------------------------------------------------------------------------------------------------------------------------

To install, "cd" into the folder containing this file and type in "sh install.sh" in Terminal.

On your first use, open a terminal and type in:

python ~/anniversary/main.py

Type in y and enter the number of your month and the day:

1 for January, 2 for February, 3 for March, etc.

To run the program, type in "sh ~/anniversary/run.sh" into Terminal.

To append this program to Startup Applications, Go to System > Startup Applications > Add...
-For the name, enter "AnniversaryReminder"
-For the command, enter "sh ~/anniversary/run.sh"

You can also go into your home directory and create a .bash_aliases if you do not have one already, and add the line:

alias anniversaryReminder="sh ~/anniversary/run.sh"

If you do this, you can run the program simply by typing in "anniversaryReminder" in Terminal.
