# JLIB
# About

This is the **JLIB** project.
It is a key module for python.
It contains many ease-of-use features that I believe are commonly used when writing python files.
The **JLIB** module file can also be run by itself, displaying a description of the classes contained within the **JLIB** module from [jlib.description()](https://github.com/EndingOsprey317/jlib#jlibdescription-1).
All functions within this project, if you write "!pass" as its first argument, will pass all code contained within the function.

# jlib.description
## jlib.description()

This function writes out a list of all functions into the terminal.

## jlib.description.\_\_str\_\_()

_JLIB: description  
--jlib.description(): display a help description of all classes in the JLIB module_

# jlib.alert
## jlib.alert()

This function will create a message box containing the data given to the function.  
  
Argument 1: this is the text that will be displayed within the message box  
Argument 2: this is the title of the message box

## jlib.alert.\_\_str\_\_()

_JLIB: alert  
--jlib.alert(): send an alert message box_

# jlib.echo
## jlib.echo()

This function will echo back into the terminal any text given into the arguments of the function  
  
Arguments 1+: all arguments will print a string of text seperated by a line break for each argument

## jlib.\_\_str\_\_()

_JLIB: echo  
--jlib.echo(): echo multiple lines of text entered back into the terminal_

# jlib.fsend
## jlib.fsend()

This function will append a file with any text given as arguments  
  
Argument 1: name of the file to be written into  
Argument 2+: text to be written into the file, seperated by a line break

## jlib.fsend.overwrite()

This function will overwrite a file with any text given as arguments  
  
Argument 1: name of the file to be overwritten  
Argument 2+: text to be written into the file, seperated by a line break

## jlib.fsend.delete()

This function will delete a file.
The function will allow only the contents of the file to be deleted, not the file itself.  
  
Argument 1: name of the file to be deleted  
Argument 2: boolean - true will keep the file but still delete the contents whereas false will delete the entire file

## jlib.fsend.\_\_str\_\_()

_JLIB: fsend  
--jlib.fsend(): append file  
--jlib.fsend.overwrite(): overwrite file  
--jlib.fsend.delete(): delete file_
