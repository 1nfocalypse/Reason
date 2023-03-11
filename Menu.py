import Art
import FunctMenus
art = Art.Art()
functs = FunctMenus.FunctMenus()

class Menu:
    def makeSite(self):
        art.drawWebEx();
        print("1. Run individual scans")
        print("2. Execute custom website profile")
        print("3. Webserver and Networking Utilities")
        print("4. OSINT Utilities")
        print("5. Customize")
        print("6. Help")
        print("7. Main Menu")
        print("8. Quit")
        menChoice = input("Please make a selection: ")
        while menChoice < "1" or menChoice > "8":
            menChoice = input("Please enter a valid selection: ")
        if menChoice == "1":
            functs.siteIndivScans()
        if menChoice == "2":
            functs.siteCustomProf()
        if menChoice == "3":
            self.makeWeb()
        if menChoice == "4":
            self.makeInt()
        #if menChoice == "5":
#
        if menChoice == "6":
            self.makeHelp()
        elif menChoice == "8":
            print("Quitting...")
            quit(0)

    def makeWeb(self):
        art.drawServer();
        print("1. Run individual scans")
        print("2. Execute custom server/networking profile")
        print("3. Website Utilities")
        print("4. OSINT Utilities")
        print("5. Customize")
        print("6. Help")
        print("7. Main Menu")
        print("8. Quit")
        menChoice = input("Please make a selection: ")
        while menChoice < "1" or menChoice > "8":
            menChoice = input("Please enter a valid selection: ")
        if menChoice == "1":
            functs.servIndivScans()
        if menChoice == "2":
            functs.servCustomProf()
        if menChoice == "3":
            self.makeWeb()
        if menChoice == "4":
            self.makeInt()
        #if menChoice == "5":

        if menChoice == "6":
            self.makeHelp()
        if menChoice == "8":
            print("Quitting...")
            quit(0)

    def makeInt(self):
        art.drawOSINT();
        print("1. Run individual scans")
        print("2. Execute custom OSINT profile")
        print("3. Website Utilities")
        print("4. Webserver and Networking Utilities")
        print("5. Customize")
        print("6. Help")
        print("7. Main Menu")
        print("8. Quit")
        menChoice = input("Please make a selection: ")
        while menChoice < "1" or menChoice > "8":
            menChoice = input("Please enter a valid selection: ")
        if menChoice == "1":
            functs.intIndivScans()
        if menChoice == "2":
            functs.intCustomProf()
        if menChoice == "3":
            self.makeSite()
        if menChoice == "4":
            self.makeWeb()
        #if menChoice == "5":

        if menChoice == "6":
            self.makeHelp()
        if menChoice == "8":
            print("Quitting...")
            quit(0)

    def makeCustom(self):
        art.drawCustom();
        print("1. Build custom profile")
        print("2. Execute custom profile")
        print("3. Website Utilities")
        print("4. Webserver and Networking Utilities")
        print("5. OSINT Utilities")
        print("6. Help")
        print("7. Main Menu")
        print("8. Quit")
        menChoice = input("Please make a selection: ")
        while menChoice < "1" or menChoice > "8":
            menChoice = input("Please enter a valid selection: ")
        if menChoice == "6":
            self.makeHelp()
        if menChoice == "8":
            print("Quitting...")
            quit(0)

    def makeHelp(self):
        art.drawHelp();
        print("Documentation for Reason and ReScript is available in their")
        print("respective GitHub repositories. Please view them here:")
        print("Reason: https://github.com/1nfocalypse/Reason/")
        print("ReScipt: https://github.com/1nfocalypse/ReScript")
        print("To report issues, please submit an issue in the repositories")
        print("listed above. Thank you for using Reason!")
        menChoice = input("Press enter to acknowledge...")
