import csv
import json
from collections import OrderedDict

csv_filename = 'tcia_labels.csv'
# csv_filename = 'covid(1번)_annotation.csv'
# csv_filename = 'covid(Larxel)_annotations.csv'
# csv_filename = 'covid(MedSeg)_annotations.csv'
# csv_filename = 'nodule_annotations.csv'

f = open(f'{csv_filename}', 'r', encoding='utf-8')

rdr = csv.reader(f)

image_id = -1
filename = ""
group = dict()

for line in rdr:
    if line[0] == filename:
        annotation = dict()
        annotation["bbox"] = [line[1], line[3], line[2], line[4]]
        annotation["bbox_mode"] = 0  # X0,Y0,X1,Y1
        if line[5] == "cancer":
            annotation["category_id"] = 0
        elif line[5] == "covid-19":
            annotation["category_id"] = 1
        elif line[5] == "nodule":
            annotation["category_id"] = 2
        group["annotations"].append(annotation)
        continue
    else:
        print(image_id-1)
        print(filename)
        with open(f'json\\{csv_filename}\\{filename}.json', 'w', encoding='utf-8') as make_file:
            json.dump(group, make_file, indent="\t")

    filename = line[0]
    group["image_id"] = image_id
    group["filename"] = f"{filename}"
    group["height"] = 512
    group["width"] = 512
    annotation = dict()
    annotation["bbox"] = [line[1], line[3], line[2], line[4]]
    annotation["bbox_mode"] = 0  # X0,Y0,X1,Y1
    if line[5] == "cancer":
        annotation["category_id"] = 0
    elif line[5] == "covid":
        annotation["category_id"] = 1
    elif line[5] == "nodule":
        annotation["category_id"] = 2
    group["annotations"] = []  # minX, minY, maxX, maxY
    group["annotations"].append(annotation)
    image_id = image_id + 1

with open(f'json\\{csv_filename}\\{filename}.json', 'w', encoding='utf-8') as make_file:
    json.dump(group, make_file, indent="\t")
print(image_id-1)
print(filename)

f.close()
