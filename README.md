# simple-keylogger-python
This is a simple keylogger written in python 3.

There are 3 files one is keylogger.pyw, this contains python code for keylogging, when a key is pressed in keyboard, this will be saved in the log.txt file. 

<h2><i>PYW files are used in Windows to indicate a script needs to be run using PYTHONW. EXE instead of PYTHON. EXE in order to prevent a DOS console from popping up to display the output.</i></h2>

There is a launch.bat file, when this file is opened it will start both the keylogger.pyw file and any target application (<i>here chrome app is used to trigger the keylogging</i>). 

You can place the path of any target application or file there as you wish. Keep in mind to change the target path of the application to the path of launch.bat file. Target path is one of the properties find in the properties section of app when the app is reigt clicked.

<h3><b>Warning! After the app icon is clicked the keylogger.pyw starts logging all the keys to the log.txt file until the system is turned off. If you want to disable the keylogger.pyw manually, you can search and delete all the running python processes in te task manager.</b></h3>
