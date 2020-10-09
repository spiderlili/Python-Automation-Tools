# validate SVG files so they can be converted by MSDF generator
# from pip._vendor.pep517.compat import FileNotFoundError

fileName = 'F1M_ClubIcons-13.svg'
firstChar = 'M'
midChar = 'L'
lastChar = 'Z'
startStr = ' ' + 'd="'
endStr = '"/>'
polygonStr = 'polygon'
pointsStr = 'points'
pathStr = 'path'
pathDefineStr = 'd'
repeatPathClassStr = '<path class="cls-1" d="'
# tokenizerStart = '<polygon class="cls-1" points="'
tokenizerStart = 'path class="cls-1" d="'
tokenizerEnd = 'Z"/>'

try:
    with open(fileName) as svgFileObj:
        svgContentLines = svgFileObj.readlines()

    for line in svgContentLines:
        print("Before: " + line.strip())

        pathCount = line.count(pathStr)
        polygonCount = line.count(polygonStr)
        endStrCount = line.count(endStr)
        print("path count in the old file: " + str(pathCount))
        print("polygon count in the old file: " + str(polygonCount))
        print("end str count in the old file: " + str(endStrCount))

        if polygonCount > 0:
            line = line.replace(polygonStr, pathStr)
            line = line.replace(pointsStr, pathDefineStr)
            insertMLocation = line.index(startStr) + 4
            line = line[:insertMLocation] + firstChar + line[insertMLocation:]
            line = line.replace(endStr, lastChar)

        if pathCount > 1:
            line = line.replace(endStr, lastChar)

        # add "/> after the last occurrence of ending Z character if there are multiple Zs:
        if line.count(lastChar) > 1:
            insertEndStrLocation = line.rindex(lastChar) + 1
            line = line[:insertEndStrLocation] + endStr + line[insertEndStrLocation:]

        # if there are multiple paths: nest them into 1 path by replacing <path class="cls-1" d=" with M
        while line.count(repeatPathClassStr) > 1:
            lastPathLocation = line.rfind(repeatPathClassStr)
            line = line[:lastPathLocation] + firstChar + line[lastPathLocation+len(repeatPathClassStr):]

        # extract svg coordinate numbers
        svgCoordsStart = line.find(tokenizerStart) + len(tokenizerStart)
        svgCoordsEnd = line.find(endStr)
        svgCoords = line[svgCoordsStart:svgCoordsEnd]

        # split svg coordinates into lists from M to Z
        tempEnd = svgCoords.index(lastChar)
        svgList = svgCoords[:tempEnd]
        print ("svg list: " + svgList)

        print ("Extracted svg coordinates: " + svgCoords)
        print("After: " + line.strip())

    if polygonCount > 0:
        print("There are polygons in the SVG file which needs to be converted to paths")
    if pathCount == 0:
        print("There is no explicit path in the SVG file")
    if pathCount > 1:
        print("There are > 1 path in the SVG file")

    # separate out a different list, divider between errorMsg/successMsg
    print("\n--------------------------------------------\n")

# FileNotFoundError
except IOError:
    errorMsg = "Sorry, the file: " + fileName + "cannot be found"
    print (errorMsg)

else:
    successMsg = "SVG file: " + fileName + " has been successfully validated!"
    print(successMsg)
