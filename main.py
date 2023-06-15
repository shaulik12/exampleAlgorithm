from PIL import Image
import pytesseract
import json
import math
import sys
import os

def OCR(ioPath):
    image = Image.open(ioPath+"/input.png")
    greyscale = image.convert('L')
    text = pytesseract.image_to_string(greyscale)
    return text

def getDimentions(ioPath):
    image = Image.open(ioPath+"/input.png")
    [width, height] = image.size
    return [width, height]

def createOutput(text, imageWidth, imageHeight):
    output = {"data": []}
    paragraphs = text.split("\n\n")
    heightAcc = 0
    for paragraph in paragraphs:
        width, height = annotationSize(paragraph, imageWidth, imageHeight)
        if width != 0:
            annotation = {}
            annotation["content"] = paragraph
            annotation["startX"] = 0
            annotation["startY"] = heightAcc
            heightAcc += height
            annotation["endX"] = heightAcc
            annotation["endY"] = width
            output["data"].append(annotation)
    return output

def annotationSize(content : str, imageWidth, imageHeight):
    length = len(content)
    if length == 0:
        return 0, 0
    textSquareBLockLength = round(math.sqrt(length))
    width = min(textSquareBLockLength, imageWidth)
    height = round(length / width)
    return width, height
    

def writeOutput(output, ioPath):
    outputfile = os.path.join(ioPath, "output.txt")
    with open(outputfile, 'w') as file:
        json.dump(output, file, indent=4)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please provide the path string as an argument.")
        sys.exit(1)
        
    ioPath = sys.argv[1]
    text = OCR(ioPath)
    [imageWidth, imageHeight] = getDimentions(ioPath)
    output = createOutput(text, imageWidth, imageHeight)
    writeOutput(output, ioPath)