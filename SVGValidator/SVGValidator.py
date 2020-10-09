# validate SVG files so they can be converted by MSDF generator
# from pip._vendor.pep517.compat import FileNotFoundError

fileName = 'F1M_ClubIcons-13.svg'
try:
    with open(fileName) as svgFileObj:
        svgContent = svgFileObj.read()
except FileNotFoundError:
    errorMsg = "sorry, the file: " + fileName + "cannot be found"
    print (errorMsg)
else:
    words = svgContent.split()
    numberOfWords = len(words)
    print(numberOfWords)
    