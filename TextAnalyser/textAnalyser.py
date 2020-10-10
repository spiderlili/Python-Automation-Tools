filename = 'frankenstein.txt'
try:
    with open(filename) as fileObj
        fileContent = fileObj.read()
except IOError:
    fileNotFoundMsg = "Sorry, the file: " + filename + "cannot be found"
    print fileNotFoundMsg
else:
    wordsInFile = fileContent.split()
    numberOfWords = len(wordsInFile)
    print("The file: " + filename + " has approximately: " + str(numberOfWords) + " words.")
