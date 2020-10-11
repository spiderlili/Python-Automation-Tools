def SVGToMSDFAnalyser(filename):
    """
    Count the number of words in a file
    """
    polygonStr = 'polygon'
    pointsStr = 'points'
    pathStr = 'path'

    try:
        with open(filename) as fileObj:
            fileContent = fileObj.readlines()
        for line in fileContent:
            pathCount = line.count(pathStr)
            polygonCount = line.count(polygonStr)
            print("The file: " + filename + " has: " + str(pathCount) + " paths.")
    except IOError:
        fileNotFoundMsg = "Sorry, the file: " + filename + "cannot be found"
        print fileNotFoundMsg
    else:
        print "analysis finished!"
        # wordsInFile = fileContent.split()
        # numberOfWords = len(wordsInFile)

filenames = ['F1M_ClubIcons-13.svg', 'F1M_ClubIcons-14.svg']
for filename in filenames:
    SVGToMSDFAnalyser(filename)