from PySide2 import QtCore
from PySide2 import QtGui


def image_file_to_hex_str(file_path):
    hex_str = ""

    qimage = QtGui.QImage(file_path)

    ba = QtCore.QByteArray()
    buffer = QtCore.QBuffer(ba)

    buffer.open(QtCore.QIODevice.WriteOnly)
    # Save the image data to QByteArray
    if qimage.save(buffer, "PNG"):
        hex_str += ba.toHex().data().decode() # Convert ByteArray to a hex encoded copy, decode the data as a string & append it to hex_str

    return hex_str


if __name__ == "__main__":
    # Hex string can be copied into the source code where it's required
    print(image_file_to_hex_str("/Users/jing.tan/Documents/GitHub/Python-Automation-Tools/maya-python-api/watermark_blue.png"))
