import json
from tinydb import TinyDB, Query, where
from string import Formatter
from pick import pick
import os

def databaseinput(txtfilename):
    try:
        hitdb = TinyDB('hitdb.json', indent=4)
        #find all of the lines ***************** New Hit ***************** then read 10 under those lines and add each one to the hitdb
        with open(txtfilename, 'r') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                if line == "***************** New Hit *****************\n":
                    #remove the \n from the end of the line
                    lines[i+1:i+11] = [x.strip() for x in lines[i+1:i+11]]
                    #turn each line into a variable
                    Email = lines[i+1]
                    Password = lines[i+2]
                    Totalspace = lines[i+3]
                    Usedspace = lines[i+4]
                    Foldercount = lines[i+5]
                    Filescount = lines[i+6]
                    Imagecount = lines[i+7]
                    Audiocount = lines[i+8]
                    Videocount = lines[i+9]
                    Compressedcount = lines[i+10]
                    #split each line between the : and the value
                    Email = Email.split(" : ", 1)
                    Password = Password.split(" : ", 1)
                    Totalspace = Totalspace.split(" : ", 1)
                    Usedspace = Usedspace.split(" : ", 1)
                    Foldercount = Foldercount.split(" : ", 1)
                    Filescount = Filescount.split(" : ", 1)
                    Imagecount = Imagecount.split(" : ", 1)
                    Audiocount = Audiocount.split(" : ", 1)
                    Videocount = Videocount.split(" : ", 1)
                    Compressedcount = Compressedcount.split(" : ", 1)
                    #imput the values into the database
                    hitdb.insert({'Email': Email[1], 'Password': Password[1], 'Totalspace': Totalspace[1], 'Usedspace': Usedspace[1], 'Foldercount': Foldercount[1], 'Filescount': Filescount[1], 'Imagecount': Imagecount[1], 'Audiocount': Audiocount[1], 'Videocount': Videocount[1], 'Compressedcount': Compressedcount[1]})
                    #print the hit
                    print(lines[i+1:i+11])
        exit()
    except:
        print("error, contact NullRien#0001 with the steps on how you got this error")


def txtinput(txtfilename, savetotxt):
    try:
        with open(txtfilename, 'r') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                if line == "***************** New Hit *****************\n":
                    lines[i+1:i+11] = [x.strip() for x in lines[i+1:i+11]]
                    #turn each line into a variable
                    Email = lines[i+1]
                    Password = lines[i+2]
                    Totalspace = lines[i+3]
                    Usedspace = lines[i+4]
                    Foldercount = lines[i+5]
                    Filescount = lines[i+6]
                    Imagecount = lines[i+7]
                    Audiocount = lines[i+8]
                    Videocount = lines[i+9]
                    Compressedcount = lines[i+10]
                    #split each line between the : and the value
                    Email = Email.split(" : ", 1)
                    Password = Password.split(" : ", 1)
                    Totalspace = Totalspace.split(" : ", 1)
                    Usedspace = Usedspace.split(" : ", 1)
                    Foldercount = Foldercount.split(" : ", 1)
                    Filescount = Filescount.split(" : ", 1)
                    Imagecount = Imagecount.split(" : ", 1)
                    Audiocount = Audiocount.split(" : ", 1)
                    Videocount = Videocount.split(" : ", 1)
                    Compressedcount = Compressedcount.split(" : ", 1)
                    #save the hit to a txt file
                    with open(savetotxt, 'a') as f:
                        f.write(f"Email:{Email[1]}, Password:{Password[1]}, Totalspace:{Totalspace[1]}, Usedspace:{Usedspace[1]}, Foldercount:{Foldercount[1]}, Filescount:{Filescount[1]}, Imagecount:{Imagecount[1]}, Audiocount:{Audiocount[1]}, Videocount:{Videocount[1]}, Compressedcount:{Compressedcount[1]}\n")
        exit()
    except:
        print("error, contact NullRien#0001 with the steps on how you got this error")


def totalspace(txtfilename):
    try:
        with open(txtfilename, 'r') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                if line == "***************** New Hit *****************\n":
                    lines[i+1:i+11] = [x.strip() for x in lines[i+1:i+11]]
                    #turn each line into a variable
                    Email = lines[i+1]
                    Password = lines[i+2]
                    Totalspace = lines[i+3]
                    Usedspace = lines[i+4]
                    Foldercount = lines[i+5]
                    Filescount = lines[i+6]
                    Imagecount = lines[i+7]
                    Audiocount = lines[i+8]
                    Videocount = lines[i+9]
                    Compressedcount = lines[i+10]
                    #split each line between the : and the value
                    Email = Email.split(" : ", 1)
                    Password = Password.split(" : ", 1)
                    Totalspace = Totalspace.split(" : ", 1)
                    Usedspace = Usedspace.split(" : ", 1)
                    Foldercount = Foldercount.split(" : ", 1)
                    Filescount = Filescount.split(" : ", 1)
                    Imagecount = Imagecount.split(" : ", 1)
                    Audiocount = Audiocount.split(" : ", 1)
                    Videocount = Videocount.split(" : ", 1)
                    Compressedcount = Compressedcount.split(" : ", 1)
                    #save the hit to a txt file
                    if Totalspace[1] == "20":
                        with open("20GB.txt", 'a') as f:
                            f.write(f"Email:{Email[1]}, Password:{Password[1]}, Totalspace:{Totalspace[1]}, Usedspace:{Usedspace[1]}, Foldercount:{Foldercount[1]}, Filescount:{Filescount[1]}, Imagecount:{Imagecount[1]}, Audiocount:{Audiocount[1]}, Videocount:{Videocount[1]}, Compressedcount:{Compressedcount[1]}\n")

                    if Totalspace[1] == "25":
                        with open("25GB.txt", 'a') as f:
                            f.write(f"Email:{Email[1]}, Password:{Password[1]}, Totalspace:{Totalspace[1]}, Usedspace:{Usedspace[1]}, Foldercount:{Foldercount[1]}, Filescount:{Filescount[1]}, Imagecount:{Imagecount[1]}, Audiocount:{Audiocount[1]}, Videocount:{Videocount[1]}, Compressedcount:{Compressedcount[1]}\n")

                    if Totalspace[1] == "50":
                        with open("50GB.txt", 'a') as f:
                            f.write(f"Email:{Email[1]}, Password:{Password[1]}, Totalspace:{Totalspace[1]}, Usedspace:{Usedspace[1]}, Foldercount:{Foldercount[1]}, Filescount:{Filescount[1]}, Imagecount:{Imagecount[1]}, Audiocount:{Audiocount[1]}, Videocount:{Videocount[1]}, Compressedcount:{Compressedcount[1]}\n")

                    if Totalspace[1] == "400":
                        with open("400GB.txt", 'a') as f:
                            f.write(f"Email:{Email[1]}, Password:{Password[1]}, Totalspace:{Totalspace[1]}, Usedspace:{Usedspace[1]}, Foldercount:{Foldercount[1]}, Filescount:{Filescount[1]}, Imagecount:{Imagecount[1]}, Audiocount:{Audiocount[1]}, Videocount:{Videocount[1]}, Compressedcount:{Compressedcount[1]}\n")

                    if Totalspace[1] == "2048":
                        with open("2TB.txt", 'a') as f:
                            f.write(f"Email:{Email[1]}, Password:{Password[1]}, Totalspace:{Totalspace[1]}, Usedspace:{Usedspace[1]}, Foldercount:{Foldercount[1]}, Filescount:{Filescount[1]}, Imagecount:{Imagecount[1]}, Audiocount:{Audiocount[1]}, Videocount:{Videocount[1]}, Compressedcount:{Compressedcount[1]}\n")

                    if Totalspace[1] == "8192":
                        with open("8TB.txt", 'a') as f:
                            f.write(f"Email:{Email[1]}, Password:{Password[1]}, Totalspace:{Totalspace[1]}, Usedspace:{Usedspace[1]}, Foldercount:{Foldercount[1]}, Filescount:{Filescount[1]}, Imagecount:{Imagecount[1]}, Audiocount:{Audiocount[1]}, Videocount:{Videocount[1]}, Compressedcount:{Compressedcount[1]}\n")

                    if Totalspace[1] == "16384":
                        with open("16TB.txt", 'a') as f:
                            f.write(f"Email:{Email[1]}, Password:{Password[1]}, Totalspace:{Totalspace[1]}, Usedspace:{Usedspace[1]}, Foldercount:{Foldercount[1]}, Filescount:{Filescount[1]}, Imagecount:{Imagecount[1]}, Audiocount:{Audiocount[1]}, Videocount:{Videocount[1]}, Compressedcount:{Compressedcount[1]}\n")
        exit()
    except:
        print("error, contact NullRien#0001 with the steps on how you got this error")


def exit():
    os.system('cls')
    print("Done!")
    input("Press any key to exit...")


if __name__ == '__main__':
    print("Welcome please put the txt file in the same folder as this program")
    txtfilename = input("What is the name of the txt file?\n--> ")
    title = 'Made by NullRien#0001 for Mega Foxy V2\nPlease choose a setting: '
    options = ['Save to database', 'Save to txt', 'Sort by Total Space']
    option, index = pick(options, title)

    if option == "Save to database":
        os.system('cls')
        databaseinput(txtfilename)

    if option == "Save all to txt":
        os.system('cls')
        savetotxt = input("What do you want to save the new txt file as?\n-->")
        txtinput(txtfilename, savetotxt)

    if option == "Sort by Total Space":
        os.system('cls')
        input("This will save text files named 20GB, 25GB, 50GB and so on so make shure you do not\nhave any files with those names in the folder before you continue\nPress any key to continue...")
        totalspace(txtfilename)