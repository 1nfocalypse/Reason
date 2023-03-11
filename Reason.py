#     ____
#    / __ \___  ____ __________  ____
#   / /_/ / _ \/ __ `/ ___/ __ \/ __ \
#  / _, _/  __/ /_/ (__  ) /_/ / / / /
# /_/ |_|\___/\__,_/____/\____/_/ /_/
#         Ultima Ratio Regum
#**************************************
# Reason is a preexploitation framework primarily built over preexisting tools.
# Please ensure compliance with these tools before use.
# If you intend on contributing or have questions about licensing, please
# check out the project on GitHub, where you will be able to find
# licensing information and contributing guidelines. The repo for this project
# can be found here: https://github.com/1nfocalypse/Reason
# Use responsibly, and happy hunting!

# Alert before use: until they can be recreated in python, some functionality is
# dependent on other software, some of which is limited to *nix. Those functions
# are as follows:
# Web: wpscan, nikto
# Servers: shodan (requires unique API key)
# OSINT: N/A
# Custom: See ReScript
import sys
import Art
import Menu

def main():
    loop = 0;
    art = Art.Art()
    men = Menu.Menu()
    if len(sys.argv) > 1:
        #parse, process, call once you've figured out what you're including (Create a function)
        if sys.argv[1] == "-h":
            men.makeHelp()

    else:
        while loop != 1:
            art.drawReason()
            print("1. Website Utilities") # Spider, Fuzzer (Fuzzbox?), Proxy, Repeater, see burp suite, pull info about webserver from nmap, dirb, fields, nikto, wpscan
            print("2. Webserver and Networking Utilities") #portscanning, network mapping, service and OS scanning, pull exploits from exploitdb
            print("3. OSINT Utilities") # GET from Shodan, cross reference social media sites, pull from records, etc.
            print("4. Customize") #allow for custom profiles and selection of results, essentially aliasing
            print("5. Help")
            print("6. Quit")
            menu = input("Please enter a choice: ")
            while menu < "0" or menu > "6":
                menu = input("Please enter a valid choice: ")
            if menu == "1":
                men.makeSite();
            elif menu == "2":
                men.makeWeb();
            elif menu == "3":
                men.makeInt();
            elif menu == "4":
                men.makeCustom();
            elif menu == "5":
                men.makeHelp();
            elif menu == "6":
                print("Quitting...")
                loop = 1;
                quit(0);


if __name__ == "__main__":
    main();
