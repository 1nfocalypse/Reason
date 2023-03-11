#     ____  _      __
#    / __ \(_)____/ /_
#   / / / / / ___/ __ \
#  / /_/ / / /  / /_/ /
# /_____/_/_/  /_.___/
# **************************************
# Requirements:
# requests: to connect to the desired webserver
# time: in the case of 429 responses, used for retry-after header
# os: to verify that the wordlist selected is, in fact, a file
#
# Parameters:
# url -> The desired url to scan in the form https://abcdefg.com/
# wordlist -> a string of the name of the desired wordlist in the ./Wordlists/ directory
# write -> a string of the name of the desired output file in the ./outputs/ directory
# initializer -> an undefined parameter that will be utilized for output control in the case of
# custom scripting or multiple tests being queued.
#
# Usage Description:
# This is a Directory Buster rewrite in Python. It is utilized to find unlisted or otherwise unreachable
# directories via fuzzing. It operates in O(n) time, and given the nature of python, is likely a bit
# slower than other implementations, however, is capable of being easily interfaced with by the
# overarching Reason framework/library.
#
# Potential additions:
# List of possible wordlists - not sure if it's too messy
# proxies - might not be necessary, only more testing will tell


import requests
import time
import os


class Dirb:

    def start(self, url, wordlist=None, write=None, initializer=None):
        total = 0
        if wordlist is None:
            wordlist = "common.txt"
        fileName = "./sites/Wordlists/" + wordlist
        while os.path.isfile(fileName) is False:
            wordlist = input("Please enter a valid file name: ")
            fileName = "./sites/Wordlists/" + wordlist
        wl = open(fileName, "r+")
        lineArr = wl.read().split("\n")
        lineArrSize = len(lineArr)
        if (write):
            outFileName = "./outputs/" + write
            outFile = open(outFileName, "w+")
        for i in range(int(lineArrSize)):
            try:
                newURL = url + lineArr[i]
                ua = "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)"
                response = requests.get(newURL, headers={"User-agent": ua})
                if (response.status_code != 404 and response.status_code != 429):
                    print(newURL + " : " + str(response.status_code) + " found.")
                    if write:
                        outFile.write(newURL + " : " + str(response.status_code))
                    total = total + 1
                if (response.status_code == 429):
                    retryTime = int(response.headers['retry-after'])
                    print("Ratelimited: Delay of " + str(retryTime) + " now in place.")
                    time.sleep(retryTime)
                    response = requests.get(newURL)
                    if (response.status_code != 404 and response.status_code != 429):
                        print(newURL + " : " + str(response.status_code) + " found.")
                        total = total + 1
                    if (response.status_code == 429):
                        print("Ratelimited again: see header blocks.")
                        print("Consider alternative user agent or proxies.")
            except:
                pass
        print("-------------------------------------------------------------")
        print("Total directories found: " + str(total))
        wl.close()
        outFile.close()
        hold = input("Press enter to return...\n")
        print(hold)
