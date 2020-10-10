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
        # svgCoords = svgCoords.split(' ')

        # split svg coordinates into lists from M to Z, for all pairs found from M to Z
        # if svgCoords.find(endStr) > 1:
        tempStart = svgCoords.index(firstChar)
        tempEnd = svgCoords.index(lastChar)
        svgList = svgCoords[tempStart:tempEnd]
        svgList = svgList.split(' ')

        # list of index at which the first character M occurs
        svgFirstCharIndex = [svg for svg, coord in enumerate(svgCoords) if coord[0] == firstChar]
        svgLastCharIndex = [svg for svg, coord in enumerate(svgCoords) if coord[0] == lastChar]
        print ("number of SVG Paths: " + str(len(svgFirstCharIndex)))
        print ("svg list comprehension debug: " + str(svgFirstCharIndex))
        numberOfPaths = len(svgFirstCharIndex)

        # create empty paths lists depending on number of Ms
        paths = [[] for path in range(0, numberOfPaths)]
        # print paths

        # slice according to number of times character M occurs
        for x in paths:
            num = numberOfPaths
            x = svgCoords[svgFirstCharIndex[numberOfPaths-num]: svgFirstCharIndex[numberOfPaths-1]]
            num += 1
            # print x
        paths[0] = svgCoords[svgFirstCharIndex[0]:svgFirstCharIndex[len(svgFirstCharIndex)-1]]
        paths[1] = svgCoords[len(svgFirstCharIndex)-1:svgLastCharIndex[len(svgLastCharIndex)-1]]
        print paths

        # add midChar L to each odd coordinate, skip the 1st coordinate which starts with M
        for i in range(2, len(svgList), 2):
            svgList[i] = midChar + svgList[i]
            # print(svgList[i])
        svgList = ' '.join(svgList)
        print ("svg list after appending L: " + str(svgList))

        print ("Extracted svg coordinates: " + svgCoords)
        print("After: " + line.strip())

    if polygonCount > 0:
        print("There are polygons in the SVG file, all of them need to be converted to paths")
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
