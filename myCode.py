import json
import sys
import os

def add_annotation_to_json(json_string):
    json_data = json.loads(json_string)
    json_data['Annotation'] = 'worked'
    output_file = 'output.txt'
    with open(output_file, 'w') as file:
        json.dump(json_data, file, indent=4)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please provide the JSON string as an argument.")
        sys.exit(1)

    json_input = sys.argv[1]
    add_annotation_to_json(json_input)