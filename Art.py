import os as os
ast = "*********************************************************"
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

class Art:

    def drawReason(self):
        clearConsole();
        print("    ____                            ")
        print("   / __ \___  ____ __________  ____ ")
        print("  / /_/ / _ \/ __ `/ ___/ __ \/ __ \"")
        print(" / _, _/  __/ /_/ (__  ) /_/ / / / /")
        print("/_/ |_|\___/\__,_/____/\____/_/ /_/ ")
        print(ast)

    def drawWebEx(self):
        clearConsole();
        print(" _       __     __    ______    ")
        print("| |     / /__  / /_  / ____/  __")
        print("| | /| / / _ \/ __ \/ __/ | |/_/")
        print("| |/ |/ /  __/ /_/ / /____>  <  ")
        print("|__/|__/\___/_.___/_____/_/|_|  ")
        print(ast)

    def drawServer(self):
        clearConsole();
        print("   _____                          ")
        print("  / ___/___  ______   _____  _____")
        print("  \__ \/ _ \/ ___/ | / / _ \/ ___/")
        print(" ___/ /  __/ /   | |/ /  __/ /    ")
        print("/____/\___/_/    |___/\___/_/     ")
        print(ast)

    def drawOSINT(self):
        clearConsole();
        print("   ____  _____ _____   ________")
        print("  / __ \/ ___//  _/ | / /_  __/")
        print(" / / / /\__ \ / //  |/ / / /   ")
        print("/ /_/ /___/ // // /|  / / /    ")
        print("\____//____/___/_/ |_/ /_/     ")
        print(ast)

    def drawCustom(self):
        clearConsole();
        print("   ______           __                ")
        print("  / ____/_  _______/ /_____  ____ ___ ")
        print(" / /   / / / / ___/ __/ __ \/ __ `__ \"")
        print("/ /___/ /_/ (__  ) /_/ /_/ / / / / / /")
        print("\____/\__,_/____/\__/\____/_/ /_/ /_/ ")
        print(ast)

    def drawHelp(self):
        clearConsole();
        print("    __  __     __    ")
        print("   / / / /__  / /___ ")
        print("  / /_/ / _ \/ / __ \"")
        print(" / __  /  __/ / /_/ /")
        print("/_/ /_/\___/_/ .___/ ")
        print("            /_/      ")
        print(ast)
