import os
import re
from keywords import keywords

def main():
    
    inputPath = input("Inserire percorso file: ")
    while not(os.path.exists(inputPath)):
        inputPath = input("Inserire percorso file: ")

    inputFile = open(inputPath, 'r')
    languages = keywords.keys()
    language = ""
    lines = inputFile.readlines()
    maxWords = 0
    for key in languages:
        words =  0
        for line in lines:
            for i in range(0, len(keywords[key])):
                if re.search("^.+ " + keywords[key][i] + " .+$", line) or re.search("^.+ " + keywords[key][i] + " *\(.+$", line) or re.search("^\s*" + keywords[key][i] + " *\(.+$", line) or re.search("^\s*" + keywords[key][i] + " *\(.+$", line):
                    if not (line.startswith(keywords[key][0])):
                        words += 1
        if(words > maxWords):
            language = key
            maxWords = words
            

    inputFile.close()
    print(language)

if __name__ == "__main__" :
    main()
