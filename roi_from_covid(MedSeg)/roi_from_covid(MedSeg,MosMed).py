import os
import cv2
import numpy as np
import csv

src_root_ct = 'C:\\Users\\hyoj_\\OneDrive\\Desktop\\CT_COVID\\other\\all\\'
src_root_lung = 'C:\\Users\\hyoj_\\OneDrive\\Desktop\\CT_COVID\\other\\mask\\'

def read_filename():
    ctscans = []
    masks = []
    for file in os.listdir(src_root_ct):
        if (file.find('.png') is not -1):
            ctscans.append(file)
            names = file.split('_')
            masks.append(src_root_lung+names[0]+'_'+names[1]+'_mask_'+names[2])
    return ctscans, masks

def write_csv(rois) :
    f = open('covid_annotations.csv', 'w', encoding='utf-8', newline='')
    wr = csv.writer(f)
    wr.writerow(['filename', 'minX', 'maxX', 'minY', 'maxY', 'classname'])
    for roi in rois :
        wr.writerow([roi[0], roi[1], roi[2], roi[3], roi[4], 'covid-19'])
    f.close()

def get_roi(lung_mask, idx, filename) :
    mask = cv2.imread(lung_mask)

    imgray = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    ret, thr = cv2.threshold(imgray, 70, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(thr, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    roi = []

    for i in range(len(contours)) :
        c0 = contours[i]
        x, y, w, h = cv2.boundingRect(c0)
        roi.append([filename, str(x), str(x+w), str(y), str(y+h)])

    return roi

ctscans, masks = read_filename()
rois = []

for idx in range(len(masks)) : 
    rois.extend(get_roi(masks[idx], idx, ctscans[idx]))
write_csv(rois)