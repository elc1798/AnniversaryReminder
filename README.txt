To install, "cd" into the folder containing this file and type in "sh install.sh" in Terminal.

On your first use, open a terminal and type in:

python ~/anniversary/main.py

Type in y and enter the number of your month and the day:

1 for January, 2 for February, 3 for March, etc.

To run the program, type in "sh ~/anniversary/src/run.sh" into Terminal.

To append this program to Startup Applications, Go to System > Startup Applications > Add...
-For the name, enter "AnniversaryReminder"
-For the command, enter "sh ~/anniversary/src/run.sh"

You can also go into your home directory and create a .bash_aliases if you do not have one already, and add the line:

alias anniversaryReminder="sh ~/anniversary/src/run.sh"

If you do this, you can run the program simply by typing in "anniversaryReminder" in Terminal.
