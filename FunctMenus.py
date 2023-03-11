import Art
from sites import Dirb
art = Art.Art()
dirb = Dirb.Dirb()

class FunctMenus:
    def siteIndivScans(self):
        art.drawWebEx();
        print("1. Directory Buster")
        print("2. Web Fuzzer")
        print("3. Nikto")
        print("4. Scraps")
        print("5. WPScan")
        print("6. Back to home")
        menChoice = input("Please make a selection: ")
        while menChoice < "1" or menChoice > "6":
            menChoice = input("Please enter a valid selection: ")
        #ifelif blocks
        if (menChoice == "1"):
            URL = input("Please enter the desired URL (form: https://abcdefg.xyz/): ")
            wlChoice = input("Would you like to use a custom wordlist?\n1: Yes\n2: No\n")
            while (wlChoice < "1" or wlChoice > "2"):
                wlChoice = input("Please make a valid selection: ")
            if (wlChoice == "1"):
                wlName = input("Enter the name of the wordlist: ")
                printChoice = input("Would you like the results recorded in a text file?\n1. Yes\n2. No\n")
                while (printChoice < "1" or printChoice > "2"):
                    printChoice = input("Please make a valid selection: ")
                if (printChoice == "1"):
                    printName = input("Please enter the name of your output file: ")
                    print("Dirb starting:\nURL: " + URL + "\nWordlist: " + wlName + "\nOutput: " + printName)
                    dirb.start(URL,wlName,printName)
                else:
                    print("Dirb starting:\nURL: " + URL + "\nWordlist: " + wlName)
                    dirb.start(URL, wlName)
            else:
                printChoice = input("Would you like the results recorded in a text file?\n1. Yes\n2. No\n")
                while (printChoice < "1" or printChoice > "2"):
                    printChoice = input("Please make a valid selection: ")
                if (printChoice == 1):
                    printName = input("Please enter the name of your output file: ")
                    print("Dirb starting:\nURL: " + URL + "\nOutput: " + printChoice)
                    dirb.start(URL, None, printName)
                else:
                    print("Dirb starting:\nURL: " + URL)
                    dirb.start(URL)
#        elif (menChoice == 2):
            #
#        elif (menChoice == 3):
            #
#        elif (menChoice == 4):
            #
#        elif (menChoice == 5):
            #


    def siteCustomProf(self):
        art.drawWebEx()
        print("Custom configurations appear here.")
        menChoice = input("Please make a selection: ")
        while menChoice < "1" or menChoice > "6":
            menChoice = input("Please enter a valid selection: ")
        #design and implement a loader and parser

    def servIndivScans(self):
        art.drawServer()
        print("1. Port/network scanning")
        print("2. Shodan")
        print("3. Scraps")
        print("4. Back to home")
        menChoice = input("Please make a selection: ")
        while menChoice < "1" or menChoice > "4":
            menChoice = input("Please enter a valid selection: ")
        #ifelif blocks
#        if (menChoice == 1):
            #
#        elif (menChoice == 2):
            #
#        elif (menChoice == 3):
            #

    def servCustomProf(self):
        art.drawServer()
        print("Custom configurations appear here.")
        menChoice = input("Please make a selection: ")
        while menChoice < "1" or menChoice > "6":
            menChoice = input("Please enter a valid selection: ")
        #design and implement a loader and parser

    def intIndivScans(self):
        art.drawOSINT()
        print("1. Social media accounts")
        print("2. Email")
        print("3. License Plate")
        print("4. Phone Number")
        print("5. Address")
        print("6. Back to home")
        menChoice = input("Please make a selection: ")
        while menChoice < "1" or menChoice > "6":
            menChoice = input("Please enter a valid selection: ")
        #ifelif blocks
#        if (menChoice == 1):
            #
#        elif (menChoice == 2):
            #
#        elif (menChoice == 3):
            #
#        elif (menChoice == 4):
            #
#        elif (menChoice == 5):
            #

    def intCustomProf(self):
        art.drawOSINT()
        print("Custom configurations appear here.")
        menChoice = input("Please make a selection: ")
        while menChoice < "1" or menChoice > "6":
            menChoice = input("Please enter a valid selection: ")
        #design and implement a loader and parser

#me, creating the worst code known to man because i don't think before I write
