import csv
import json
from collections import OrderedDict

csv_filename = 'train.csv'
# csv_filename = 'val.csv'
# csv_filename = 'test.csv'


f = open(f'{csv_filename}', 'r', encoding='utf-8')

rdr = csv.reader(f)

image_id = 0
filename = ""
upper_group = dict()
group = dict()
line_count = 0
for line in rdr:

    if line_count == 0:
        line_count = line_count +1
        continue
    if line[0] == filename:
        annotation = dict()
        print(line[1])
        print(type(line[1]))

        annotation["bbox"] = [int(float(line[1])), int(float(line[3])), int(float(line[2])), int(float(line[4]))]
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
        upper_group[f'{filename}'] = group
        group = dict()

    filename = line[0]
    group["image_id"] = image_id
    group["filename"] = f"{filename}"
    group["height"] = 512
    group["width"] = 512
    annotation = dict()
    annotation["bbox"] = [int(float(line[1])), int(float(line[3])), int(float(line[2])), int(float(line[4]))]
    annotation["bbox_mode"] = 0  # X0,Y0,X1,Y1
    if line[5] == "cancer":
        annotation["category_id"] = 0
    elif line[5] == "covid-19":
        annotation["category_id"] = 1
    elif line[5] == "nodule":
        annotation["category_id"] = 2
    group["annotations"] = []  # minX, minY, maxX, maxY
    group["annotations"].append(annotation)
    image_id = image_id + 1

upper_group[f'{filename}'] = group

with open(f'json\\{csv_filename}.json', 'w', encoding='utf-8') as make_file:
    json.dump(upper_group, make_file, indent="\t")
print(image_id-1)
print(filename)

f.close()
