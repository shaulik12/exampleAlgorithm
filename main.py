from PIL import Image
import pytesseract
import base64
import json
import sys
import io
import os

def getImage(ioPath):
    inputfile = os.path.join(ioPath, "input.txt")
    with open(inputfile, 'r') as file:
        imageData = json.load(file)
    imageData = base64.b64encode(imageData["DATA"])
    imageSteam = io.BytesIO(imageData)
    image = Image.open(imageSteam)
    return image

def OCR(ioPath):
    image = Image.open(ioPath+"/input.png")
    greyscale = image.convert('L')
    text = pytesseract.image_to_string(greyscale)
    print(text.strip()) 
    
def add_annotation_to_json(ioPath):
    inputfile = os.path.join(ioPath, "input.txt")
    input_data = {}
    with open(inputfile, 'r') as file:
        input_data = json.load(file)
    
    outputfile = os.path.join(ioPath, "output.txt")
    output_data = {}
    output_data['Annotation'] = 'worked'
    with open(outputfile, 'w') as file:
        json.dump(output_data, file, indent=4)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please provide the path string as an argument.")
        sys.exit(1)
    ioPath = sys.argv[1]
    OCR(ioPath)