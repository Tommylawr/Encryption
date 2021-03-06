import os
import os.path
import time
import ctypes
import hashlib as h
import tkinter.messagebox as box
from tkinter import *
from tkinter import filedialog
ctypes.windll.shcore.SetProcessDpiAwareness(1)
    
Word, Words, EncryptedWord, count, Number, sep, Condition, NumberOfNormal, ListNumber, DecryptedWord = ([], [], [], 0, 0, ", ", True, 0, 0, [])
class IncorrectPassword(Exception):
    pass


class IncorrectUsername(Exception):
    pass


class IncorrectCommand(Exception):
    pass


def DataCollection(event = None):
    global Entered_username, Entered_password
    Entered_username = Username_entry.get()
    Entered_password = Password_entry.get()
    Details()

    
def Registering():
    global Username_entry, Password_entry, Enter_Username, Enter_Password, Entry_button
    New_or_Old.destroy()
    New.destroy()
    Old.destroy()
    U_and_P = open(r"C:\Users\tommy\Documents\Python\Username and password.txt", "w")
    Enter_Username = Label(window, text = "Enter a username: ")
    Enter_Username.place(x = 0, y = 0)
    Enter_Password = Label(window, text = "Enter a password: ")
    Enter_Password.place(x = 0, y = 27)
    Username_entry = Entry(window)
    Username_entry.place(x = 150, y = 0)
    Password_entry = Entry(window, show = "*")
    Password_entry.place(x = 150, y = 30)
    Entry_button = Button(window, text = "Enter", command = DataCollection)
    Entry_button.place(x = 160, y = 60)
    Password_entry.bind("<Return>", DataCollection)


def Details(event = None):
    global Username_entry, Password_entry, Enter_Username, Enter_Password, Entry_button
    Username = Username_entry.get()
    Password = Password_entry.get()
    Password = h.md5(Password.encode()).hexdigest()
    U_and_P = open(r"C:\Users\tommy\Documents\Python\Username and password.txt", "w")
    U_and_P.write("Username: " + Username + "\n")
    U_and_P.write("Password: " + Password)
    U_and_P.close()
Done()
def Login():
    global Entered_username_entry, Entered_password_entry, Entered_username_label, Entered_password_label, Entered_entry_button, Entered_password, Username, Password
    New_or_Old.destroy()
    New.destroy()
    Old.destroy()
    U_and_P = open(r"C:\Users\tommy\Documents\Python\Username and password.txt", "r")
    Extraction = U_and_P.readlines()
    Username = Extraction[0].strip("??????").strip("\n")
    Password = Extraction[1]
    Username = Username[10: ]
    Password = Password[10: ]
    Entered_username_label = Label(window, text = "Enter your username: ")
    Entered_username_label.place(x = 0, y = 0)
    Entered_password_label = Label(window, text = "Enter your password: ")
    Entered_password_label.place(x = 0, y = 27)
    Entered_username_entry = Entry(window)
    Entered_username_entry.place(x = 150, y = 0)
    Entered_password_entry = Entry(window, show = "*")
    Entered_password_entry.place(x = 150, y = 30)
    Entered_entry_button = Button(window, text = "Enter", command = Check)
    Entered_entry_button.place(x = 160, y = 60)
    Entered_username_entry.bind("<Return>", Check)
    Entered_password_entry.bind("<Return>", Check)

def Check(event = None):
    global Entered_username_entry, Entered_password_entry, Entered_username_label, Entered_password_label, Entered_entry_button, Entered_username, Entered_password, Username, Password
    Entered_username = Entered_username_entry.get()
    Entered_password = Entered_password_entry.get()
    Hashed_password = h.md5(Entered_password.encode()).hexdigest()
    if Username == Entered_username:
        if Password == Hashed_password:
            Done()
        else:
            raise IncorrectPassword
    else:
        raise IncorrectUsername
def Done():
    global TotalChar
    UserList, PassList, TotalUser, TotalPass = [], [], 1, 1
    for i in range(len(Entered_username)):
        User = ord(Entered_username[i])
    UserList.append(User)
    for i in range(len(Entered_password)):
        Pass = ord(Entered_password[i])
    PassList.append(Pass)
    for i in range(len(Entered_username)):
        TotalUser = int(UserList[i] * TotalUser)
    for i in range(len(Entered_password)):
        TotalPass = int(PassList[i] * TotalPass)
    TotalChar = int(TotalUser * TotalPass)
    EncryptOrDecrypt()

    
def Encryption():
    EncryptOrDecryptWin.destroy()
    ewdfa = filedialog.askopenfilename()
    Check = list(ewdfa)
    eodf = open(ewdfa, "r+").read()
    encrypt = eodf.swapcase()
    eone = encrypt[2: ] + encrypt[: 2]
    for i in eone:
        etwo = chr(ord(i) + 5)
    Words.append(etwo)
    etwo = "".join(Words)
    for g in range(len(etwo)):
        global EncryptedWord, Number
    ethree = ord(Words[Number])
    ethree = (ethree * 20) + 59
    efour = int(ethree * TotalChar)
    efive = "{0:b}".format(efour)
    EncryptedWord.append(efive)
    Number = Number + 1
    esix = ", ".join(str(x) for x in EncryptedWord)
    os.remove(ewdfa)
    NewFile = open(ewdfa, "w")
    NewFile.write(esix)
    NewFile.close()
    window.destroy()
    quit()

    
def Decryption():
    EncryptOrDecryptWin.destroy()
    dwdfa = filedialog.askopenfilename()
    global Condition, ListNumber, NumberOfNormal
    Check = list(dwdfa)
    dodf = open(dwdfa, "r+").read()
    while Condition:
        try:
            ListString = dodf.split(sep, ListNumber)[ListNumber]
            NumberOfNormal = NumberOfNormal + 1
            ListNumber = ListNumber + 1
        except IndexError:
            break
    ListNumber = 0
    for v in range(NumberOfNormal):
        Decrypted = dodf.split(sep, NumberOfNormal)[ListNumber]
    ListNumber = ListNumber + 1
    Decrypted = int(Decrypted, 2)
    Decrypted = int(Decrypted / TotalChar)
    Decrypted = (Decrypted - 59) / 20
    Decrypted = int(Decrypted)
    DecryptedWord.append(chr(Decrypted))
    dodf = "".join(DecryptedWord)
    a = len(DecryptedWord)
    time.sleep(1)
    dfirst = dodf[a - 2] + dodf[a - 1] + dodf[: a - 2]
    for i in dfirst:
        dsecond = chr(ord(i) - 5)
    Word.append(dsecond)
    dsecond = "".join(Word)
    dsecond = dsecond.swapcase()
    os.remove(dwdfa)
    new = open(dwdfa, "w")
    new.write(dsecond)
    new.close()
    window.destroy()
    os.exit()

    
def EncryptOrDecrypt():
    global EncryptOrDecryptWin
    EncryptOrDecryptWin = Toplevel(window)
    window.withdraw()
    EncryptOrDecryptWin.title("Encryption or Decryption.")
    EncryptOrDecryptWin.geometry("360x150")
    EncryptOrDecryptFrame = Frame()
    EncryptOrDecryptFrame.place()
    EncryptOrDecryptLabel = Label(
    EncryptOrDecryptWin, text = "Do you wish to encrypt or decrypt?")
    EncryptOrDecryptLabel.place(x = 65, y = 0)
    Encrypt = Button(EncryptOrDecryptWin, text = "Encrypt", command = Encryption)
    Decrypt = Button(EncryptOrDecryptWin, text = "Decrypt", command = Decryption)
    Encrypt.place(x = 100, y = 30)
    Decrypt.place(x = 200, y = 30)


window = Tk()
window.title("Login frame")
window.geometry("350x150")
Loginframe = Frame()
Loginframe.place()
New_or_Old = Label(window, text = "Are you registering or are you loging in?")
New_or_Old.place(x = 43, y = 0)
New = Button(window, text = "Registering", command = Registering)
New.place(x = 100, y = 30)
Old = Button(window, text = "Login", command = Login)
Old.place(x = 195, y = 30)
mainloop()
