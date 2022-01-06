import os, os.path, time
Word, Words, EncryptedWord, count, Number, sep, Condition, NumberOfNormal, ListNumber, DecryptedWord = [], [], [], 0, 0, ", ", True, 0, 0, []
class IncorrectCommand(Exception):
    pass
def Removal(Check):
    for i in Check:
        if(i == '"'):
            Check.remove(i)

def Encryption():
    ewdfa = input('Enter the entire file directory plus file you wish to encrypt: ')
    Check = list(ewdfa)
    if '"' == Check[0]:
        Removal(Check)
        ewdfa ="".join(Check)
    else:
        return
    eofa = open(ewdfa,"r+").read()
    encrypt = eofa.swapcase()
    efirst = encrypt[2:]+encrypt[:2]
    for i in efirst:
        esecond = chr(ord(i) + 5)
        Words.append(esecond)
        esecond = ''.join(Words)
    for g in range(len(esecond)):
        global EncryptedWord, Number
        efour = ord(Words[Number])
        efour = (efour*20)+59
        efive = '{0:b}'.format(efour)
        EncryptedWord.append(efive)
        Number = Number+1
    ethird = ', '.join(str(x) for x in EncryptedWord)
    print(ethird)
    os.remove(ewdfa)
    NewFile = open(ewdfa, "w")
    NewFile.write(ethird)
    NewFile.close()

def Decryption():

    global Condition, ListNumber, NumberOfNormal
    dwdfa = input('Enter the entire file directory plus file you wish to decrypt:')
    Check = list(dwdfa)
    if '"' == Check[0]:
        Removal(Check)
        print(Check)
        dwdfa = "".join(Check)
    dodf = open(dwdfa,"r+").read()
    while Condition == True:
        try:
            ListString = dodf.split(sep, ListNumber)[ListNumber]
            NumberOfNormal = NumberOfNormal+1
            ListNumber = ListNumber+1
        except IndexError:
            break
    ListNumber = 0
    for v in range(NumberOfNormal):
        Decrypted = dodf.split(sep, NumberOfNormal)[ListNumber]
        ListNumber = ListNumber+1
        Decrypted = int(Decrypted, 2)
        Decrypted  = (Decrypted-59)/20
        Decrypted = int(Decrypted)
        DecryptedWord.append(chr(Decrypted))
    dodf = ''.join(DecryptedWord)
    a = len(DecryptedWord)
    time.sleep(1)
    dfirst = dodf[a-2]+dodf[a-1]+dodf[:a-2]
    for i in dfirst:
        dsecond = (chr(ord(i) - 5))
        Word.append(dsecond)
        dsecond = ''.join(Word)
    dsecond = dsecond.swapcase()
    print(dsecond)
    os.remove(dwdfa)
    new = open(dwdfa, "w")
    new.write(dsecond)
    new.close()
s = input("Do you wish to encrypt(e) or decrypt(d)?").lower()
if s == "e":
    Encryption()
elif s == "d":
    Decryption()
else:
    print("You entered an incorrect command")
    raise IncorrectCommand()
find_packages()
