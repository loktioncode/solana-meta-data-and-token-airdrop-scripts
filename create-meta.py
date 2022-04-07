import glob
import json

ranks = [
    {
        "Name": "420Boi",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Abbot the Astro Boy",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Albus the Astro Boy",
        "trait": "Uncommon",
        "rank": 1
    },
    
]


def write_json(rank_info, rank_data, new_image_name, filename):
    with open(filename, 'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside attributes
        file_data['name'] = rank_info["Name"]
        file_data["image"] = new_image_name
        file_data["attributes"].append({
            "trait_type": "Rank",
            "value": rank_info["trait"]
        })
        file_data["properties"]["files"].append(rank_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent=4)
        print("DONE 1>>", file_data["attributes"])


for i in range(len(ranks)):
    print('START AT {n}'.format(n=i))
    write_json(ranks[i], {
        "uri": "{n}.png".format(n=i),
        "type": "image/png"
    }, "{n}.png".format(n=i), "fixed-json/{n}.json".format(n=i))
    # break
