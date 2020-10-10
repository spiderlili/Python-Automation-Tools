def textAnalyser(filename):
    """
    Count the number of words in a file
    """
    try:
        with open(filename) as fileObj:
            fileContent = fileObj.read()
    except IOError:
        fileNotFoundMsg = "Sorry, the file: " + filename + "cannot be found"
        print fileNotFoundMsg
    else:
        wordsInFile = fileContent.split()
        numberOfWords = len(wordsInFile)
        print("The file: " + filename + " has approximately: " + str(numberOfWords) + " words.")

filenames = ['frankenstein.txt', 'aliceInWonderland.txt']
for filename in filenames:
    textAnalyser(filename)