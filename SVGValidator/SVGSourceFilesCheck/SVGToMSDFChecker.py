import os

polygonStr = 'polygon'
pointsStr = 'points'
pathStr = 'path'
rootDir = "svgFiles"
fileSet = set()

def SVGToMSDFAnalyser(filename):
    """
    Count the number of words in a file
    """
    try:
        with open(filename) as svgFileObj:
            fileContentLines = svgFileObj.readlines()

    except IOError:
        fileNotFoundMsg = "Sorry, the file: " + filename + " cannot be found"
        print fileNotFoundMsg

    else:
        for line in fileContentLines:
            pathCount = line.count(pathStr)
            polygonCount = line.count(polygonStr)
            if pathCount == 0:
                print("The file: " + filename + " cannot be converted to MSDF because it has " + str(pathCount) + " path. There are " + str(polygonCount) + " polygons which needs to be converted to 1 single path.")
            if pathCount > 1:
                if polygonCount == 0:
                    print("The file: " + filename + " cannot be converted to MSDF because it has " + str(pathCount) + " paths which all need to be converted to 1 single path.")
                if polygonCount > 0:
                    print("The file: " + filename + " cannot be converted to MSDF because it has " + str(pathCount) + " paths and " + str(polygonCount) + " polygons which all need to be converted to 1 single path.")
            # print("The file: " + filename + " has: " + str(pathCount) + " paths " + "and " + str(polygonCount) + " polygons.")

filenames = ['F1M_ClubIcons-13.svg', 'F1M_ClubIcons-14.svg']

# add svg files with relative path to svgFileNames
svgFileNames = []
for root,dirs,files in os.walk(rootDir):
    for svgFile in files:
        fileSet.add(os.path.join(root[len(rootDir):], svgFile))
        svgFileNames.append(rootDir + "/" + svgFile)

for filename in svgFileNames:
    SVGToMSDFAnalyser(filename)

print "MSDF Conversion Validation finished!"