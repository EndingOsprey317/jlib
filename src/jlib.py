from tkinter import messagebox as mb
import os
import time

class description:
    def __init__(self, *args):
        try:
            if args[0] != "!pass":
                echo("JLIB", "------------", description("!pass"), alert("!pass"), echo("!pass"), fsend("!pass"), error("!pass"))
        except:
            echo("JLIB", "------------", description("!pass"), alert("!pass"), echo("!pass"), fsend("!pass"), error("!pass"))
        
    def __str__(self):
        return "JLIB: description\n--jlib.description(): display a help description of all classes in the JLIB module"

class alert:
    def __init__(self, *args):
        try:
            if args[0] != "!pass":
                try:
                    text = args[0]
                except:
                    text = "JLIB: alert"

                try:
                    title = args[1]
                except:
                    title = "ALERT!"

                mb.showinfo(title, text)
        except Exception as ex:
            error.error("JLIB: jlib.alert" + str(ex), 1, 1, 0)
        
    def __str__(self):
        return "JLIB: alert\n--jlib.alert(): send an alert message box"

class echo:
    def __init__(self, *args):
        try:
            if args[0] != "!pass":
                text = ""

                try:
                    i = 0
                    for x in args:
                        if i == 0:
                            text = str(x)
                        else:
                            text = text + "\n" + str(x)
                        i += 1
                except:
                    text = "JLIB: echo"
                finally:
                    if text == "":
                        text = "JLIB: echo"

                    print(text)
        except Exception as ex:
            error.error("JLIB: jlib.echo" + str(ex), 1, 1, 0)
            
    def __str__(self):
        return "JLIB: echo\n--jlib.echo(): echo multiple lines of text entered back into the terminal"
    
class fsend:
    def __init__(self, file, *args):
        try:
            if file != "!pass":
                if '.' in file:
                    f = open(file, "a")
                    for x in args:
                        f.write(x + "\n")
                    f.close()
                else:
                    f = open(file + ".txt", "a")
                    for x in args:
                        f.write(x + "\n")
                    f.close()
        except Exception as ex:
            error.error("JLIB: jlib.fsend" + str(ex), 1, 1, 0)
        
    def overwrite(file, *args):
        try:
            if '.' in file:
                f = open(file, "w")
                for x in args:
                    f.write(x + "\n")
                f.close()
            else:
                f = open(file + ".txt", "w")
                for x in args:
                    f.write(x + "\n")
                f.close()
        except Exception as ex:
            error.error("JLIB: jlib.fsend.overwrite" + str(ex), 1, 1, 0)
    
    def delete(file, keepFile):
        try:
            if keepFile:
                f = open(file, "w")
                f.write("")
                f.close()
            else:
                os.remove(file)
        except Exception as ex:
            error.error("JLIB: jlib.alert.delete" + str(ex), 1, 1, 0)
    
    def __str__(self):
        return "JLIB: fsend\n--jlib.fsend(): append file\n--jlib.fsend.overwrite(): overwrite file\n--jlib.fsend.delete(): delete file"
    
class error:
    def __init__(self, *args):
        try:
            if args[0] != "!pass":
                echo("JLIB: error\n--jlib.error.log(): send an INFO message to 'terminal', 'error file', and/or 'message box'\n--jlib.error.warn(): send an WARN message to 'terminal', 'error file', and/or 'message box'\n--jlib.error.error(): send an ERROR message to 'terminal', 'error file', and/or 'message box'\n--jlib.error.fatal(): send an FATAL message to 'terminal', 'error file', and/or 'message box'")
        except:
            echo("JLIB: error\n--jlib.error.log(): send an INFO message to 'terminal', 'error file', and/or 'message box'\n--jlib.error.warn(): send an WARN message to 'terminal', 'error file', and/or 'message box'\n--jlib.error.error(): send an ERROR message to 'terminal', 'error file', and/or 'message box'\n--jlib.error.fatal(): send an FATAL message to 'terminal', 'error file', and/or 'message box'")
            
    def log(text, terminal, log, user):
        try:
            if terminal == True:
                echo("(INFO) -- " + text)
            if log == True:
                fsend("error.log", "(INFO) -- " + text)
            if user == True:
                alert(text, "INFO")
        except Exception as ex:
            error.error("JLIB: jlib.error.log" + str(ex), 1, 1, 0)
        
    def warn(text, terminal, log, user):
        try:
            if terminal == True:
                echo("(WARN) -- " + text)
            if log == True:
                fsend("error.log", "(WARN) -- " + text)
            if user == True:
                alert(text, "WARN")
        except Exception as ex:
            error.error("JLIB: jlib.error.warn" + str(ex), 1, 1, 0)
    
    def error(text, terminal, log, user):
        try:
            if terminal == True:
                echo("(ERROR) -- " + text)
            if log == True:
                fsend("error.log", "(ERROR) -- " + text)
            if user == True:
                alert(text, "ERROR")
        except Exception as ex:
            error.error("JLIB: jlib.error.error" + str(ex), 1, 1, 0)
    
    def fatal(text, terminal, log, user):
        try:
            if terminal == True:
                echo("(FATAL) -- " + text)
            if log == True:
                fsend("error.log", "(FATAL) -- " + text)
            if user == True:
                alert(text, "FATAL")
        except Exception as ex:
            error.error("JLIB: jlib.error.fatal" + str(ex), 1, 1, 0)
    
    def __str__(self):
        return "JLIB: error\n--jlib.error.log(): send an INFO message to 'terminal', 'error file', and/or 'message box'\n--jlib.error.warn(): send an WARN message to 'terminal', 'error file', and/or 'message box'\n--jlib.error.error(): send an ERROR message to 'terminal', 'error file', and/or 'message box'\n--jlib.error.fatal(): send an FATAL message to 'terminal', 'error file', and/or 'message box'"

class SaveLog():
    def __init__(self):
        try:
            f = open("error.log")
            try:
                os.mkdir(os.getcwd() + "\\error_logs\\")
                s = open(os.getcwd() + "\\error_logs\\" + str(int(time.time())) + ".log", "w")
                s.write(f.read())
                s.close()
            except FileExistsError:
                s = open(os.getcwd() + "\\error_logs\\" + str(int(time.time())) + ".log", "w")
                s.write(f.read())
                s.close()
            except Exception as ex:
                error.error("JLIB: jlib.SaveLog -- " + str(ex), 1, 1, 0)
            f.close()
        except Exception as ex:
            error.warn("JLIB: jlib.SaveLog -- " + str(ex), 1, 1, 0)
    def __str__(self):
        return "JLIB: saveLog\n--jlib.saveLog(): saves an error log"

if __name__ == "__main__":
    description()
    os.system("pause")
