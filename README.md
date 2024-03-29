# JLIB

# About

This is the **JLIB** project.
It is a key module for python.
It contains many ease-of-use features that I believe are commonly used when writing python files.
The **JLIB** module file can also be run by itself, displaying a description of the classes contained within the **JLIB** module.
All functions within this module will pass all code contained within the function if you write pass as its first argument.

## Install

### PIP

`pip install -i https://test.pypi.org/simple/ jlib==0.1.0`

### Manual

Download [latest stable release](https://github.com/EndingOsprey317/jlib/releases/latest).  
Put jlib.py in your python libs folder.

**Do not download a release marked \*NP since it could be an unstable build**

# Contents

* [About](#about)  
  * [Install](#install)
    * [PIP](#pip)
    * [Manual](#manual)
* [Contents](#contents)  
* [jlib.description](#jlibdescription)
  * [jlib.description()](#jlibdescription-1)
  * [jlib.decription.\_\_str\_\_()](#jlibdescription__str__)
* [jlib.alert](#jlibalert)
  * [jlib.alert()](#jlibalert-1)
    * [Arguments](#arguments)
  * [jlib.alert.\_\_str\_\_()](#jlibalert__str__)
* [jlib.echo](#jlibecho)
  * [jlib.echo()](#jlibecho-1)
    * [Arguments](#arguments-1)
  * [jlib.echo.\_\_str\_\_()](#jlibecho__str__)
* [jlib.fsend](#jlibfsend)
  * [jlib.fsend()](#jlibfsend-1)
    * [Arguments](#arguments-2)
  * [jlib.fsend.overwrite()](#jlibfsendoverwrite)
    * [Arguments](#arguments-3)
  * [jlib.fsend.delete()](#jlibfsenddelete)
    * [Arguments](#arguments-4)
  * [jlib.fsend.\_\_str\_\_()](#jlibfsend__str__)
* [jlib.error](#jliberror)
  * [jlib.error.log()](#jliberrorlog)
    * [Arguments](#arguments-5)
  * [jlib.error.warn()](#jliberrorwarn)
    * [Arguments](#arguments-6)
  * [jlib.error.error()](#jliberrorerror)
    * [Arguments](#arguments-7)
  * [jlib.error.fatal()](#jliberrorfatal)
    * [Arguments](#arguments-8)
  * [jlib.error.\_\_str\_\_()](#jliberror__str__)
* [jlib.SaveLog](#jlibsavelog)
  * [jlib.Savelog()](#jlibsavelog-1)
  * [jlib.SaveLog.\_\_str\_\_()](#jlibsavelog__str__)
* [jlib.FizzBuzz](#jlibfizzbuzz)
  * [jlib.FizzBuzz()](#jlibfizzbuzz-1)
    * [Arguments](#arguments-9)
  * [jlib.FizzBuzz.\_\_str\_\_()](#jlibfizzbuzz__str__)

# jlib.description

## jlib.description()

This function writes out a list of all functions into the terminal.

## jlib.description.\_\_str\_\_()

_JLIB: description  
--jlib.description(): display a help description of all classes in the JLIB module_

# jlib.alert

## jlib.alert()

This function will create a message box containing the data given to the function.  

### Arguments

Argument 1: this is the text that will be displayed within the message box  
Argument 2: this is the title of the message box

## jlib.alert.\_\_str\_\_()

_JLIB: alert  
--jlib.alert(): send an alert message box_

# jlib.echo

## jlib.echo()

This function will echo back into the terminal any text given into the arguments of the function  

### Arguments

Arguments 1+: all arguments will print a string of text seperated by a line break for each argument

## jlib.echo.\_\_str\_\_()

_JLIB: echo  
--jlib.echo(): echo multiple lines of text entered back into the terminal_

# jlib.fsend

## jlib.fsend()

This function will append a file with any text given as arguments  

### Arguments

Argument 1: name of the file to be written into  
Argument 2+: text to be written into the file, seperated by a line break

## jlib.fsend.overwrite()

This function will overwrite a file with any text given as arguments

### Arguments

Argument 1: name of the file to be overwritten  
Argument 2+: text to be written into the file, seperated by a line break

## jlib.fsend.delete()

This function will delete a file.
The function will allow only the contents of the file to be deleted, not the file itself.

### Arguments

Argument 1: name of the file to be deleted  
Argument 2: boolean - true will keep the file but still delete the contents whereas false will delete the entire file

## jlib.fsend.\_\_str\_\_()

_JLIB: fsend  
--jlib.fsend(): append file  
--jlib.fsend.overwrite(): overwrite file  
--jlib.fsend.delete(): delete file_

# jlib.error

## jlib.error.log()

This function will create a LOG entry in 'terminal' (argument 2), 'the error.log file' (argument 3), and/or 'a user displayed message box' (argument 4).

### Arguments

Argument 1: info to log and/or description of text  
Argument 2: boolean - whether to display in terminal  
Argument 3: boolean - whether to write to error file  
Argument 4: boolean - whether to display a message box to user

## jlib.error.warn()

This function will create a WARN entry in 'terminal' (argument 2), 'the error.log file' (argument 3), and/or 'a user displayed message box' (argument 4).

### Arguments

Argument 1: warning to log and/or description of error  
Argument 2: boolean - whether to display in terminal  
Argument 3: boolean - whether to write to error file  
Argument 4: boolean - whether to display a message box to user

## jlib.error.error()

This function will create an ERROR entry in 'terminal' (argument 2), 'the error.log file' (argument 3), and/or 'a user displayed message box' (argument 4).

### Arguments

Argument 1: error to log and/or description of error  
Argument 2: boolean - whether to display in terminal  
Argument 3: boolean - whether to write to error file  
Argument 4: boolean - whether to display a message box to user

## jlib.error.fatal()

This function will create a FATAL entry in 'terminal' (argument 2), 'the error.log file' (argument 3), and/or 'a user displayed message box' (argument 4).

### Arguments

Argument 1: fatality to log and/or description of error  
Argument 2: boolean - whether to display in terminal  
Argument 3: boolean - whether to write to error file  
Argument 4: boolean - whether to display a message box to user

## jlib.error.\_\_str\_\_()

_JLIB: error  
--jlib.error.log(): send an INFO message to 'terminal', 'error file', and/or 'message box'  
--jlib.error.warn(): send an WARN message to 'terminal', 'error file', and/or 'message box'  
--jlib.error.error(): send an ERROR message to 'terminal', 'error file', and/or 'message box'  
--jlib.error.fatal(): send an FATAL message to 'terminal', 'error file', and/or 'message box'_

# jlib.SaveLog

## jlib.SaveLog()

Saves error.log to timestamped text file.

## jlib.SaveLog.\_\_str\_\_()

_JLIB: SaveLog  
--jlib.SaveLog(): saves an error log_

# jlib.FizzBuzz

## jlib.FizzBuzz()

Lists out FizzBuzz numbers.
Multiples of 3 are replaced by fizz.
Multiples of 4 are replaced by buzz.
Multiples of both 3 and 4 are replaced with fizzbuzz.

### Arguments

Argument 1: how many fizzbuzz numbers to list

## jlib.FizzBuzz.\_\_str\_\_()

_JLIB: FizzBuzz  
--jlib.FizzBuzz(): play fizzbuzz_
