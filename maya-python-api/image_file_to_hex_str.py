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
        hex_str += ba.toHex().data().decode()

    return hex_str


if __name__ == "__main__":

    print(image_file_to_hex_str("C:/Users/czurbrigg/Documents/maya/projects/default/sourceimages/watermark_blue.png"))
