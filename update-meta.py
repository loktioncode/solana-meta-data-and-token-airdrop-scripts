import glob
import json


def write_json(new_data, filename):
    with open(filename, 'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside attributes
        file_data["attributes"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent=4)
        print("DONE 1")

newLayer = {
    "trait_type": "Rank",
    "value": "Commander"
}

for file in glob.glob("assets/*.json"):
    write_json(newLayer, file)

