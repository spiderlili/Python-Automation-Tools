polygonStr = 'polygon'
pointsStr = 'points'
pathStr = 'path'

def SVGToMSDFAnalyser(filename):
    """
    Count the number of words in a file
    """
    try:
        with open(filename) as svgFileObj:
            fileContentLines = svgFileObj.readlines()

    except IOError:
        fileNotFoundMsg = "Sorry, the file: " + filename + "cannot be found"
        print fileNotFoundMsg

    else:
        for line in fileContentLines:
            pathCount = line.count(pathStr)
            polygonCount = line.count(polygonStr)
            print("The file: " + filename + " has: " + str(pathCount) + " paths.")
            print("The file: " + filename + " has: " + str(polygonCount) + " polygons.")
        # wordsInFile = fileContent.split()
        # numberOfWords = len(wordsInFile)

filenames = ['F1M_ClubIcons-13.svg', 'F1M_ClubIcons-14.svg']
for filename in filenames:
    SVGToMSDFAnalyser(filename)
print "analysis finished!"