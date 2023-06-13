import json
import sys
import os

def add_annotation_to_json(outputPath):
    inputfile = os.path.join(outputPath, "input.txt")
    input_data = json()
    with open(inputfile, 'r') as file:
        input_data = json.load(file)
    
    outputfile = os.path.join(outputPath, "output.txt")
    output_data = json()
    output_data['Annotation'] = 'worked'
    with open(outputfile, 'w') as file:
        json.dump(output_data, file, indent=4)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please provide the path string as an argument.")
        sys.exit(1)

    outputPath = sys.argv[1]
    add_annotation_to_json(outputPath)