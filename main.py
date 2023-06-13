import json
import sys
import os

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
    add_annotation_to_json(ioPath)