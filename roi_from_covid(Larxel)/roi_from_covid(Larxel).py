import os
import cv2
import numpy as np
import csv

src_root_ct = 'C:\\Users\\hyoj_\\OneDrive\\Desktop\\internship\\C677\\covid\\ct_scans\\'
src_root_lung = 'C:\\Users\\hyoj_\\OneDrive\\Desktop\\internship\\C677\\covid\\infection_mask\\'
save_path = 'C:\\Users\\hyoj_\\OneDrive\\Desktop\\internship\\C677\\covid\\roi_lung\\'

def read_png(filepath):
    scans = []
    for file in os.listdir(filepath):
        if (file.find('.png') is not -1):
            scans.append(filepath + file)
    return scans

def read_filename(filepath) :
    filenames = []
    for file in os.listdir(filepath):
        if (file.find('.png') is not -1):
            filenames.append(file)
    return filenames

def write_csv(rois) :
    f = open('covid(Larxel)_annotations.csv', 'w', encoding='utf-8', newline='')
    wr = csv.writer(f)
    wr.writerow(['filename', 'minX', 'maxX', 'minY', 'maxY', 'classname'])
    for roi in rois :
        wr.writerow([roi[0], roi[1], roi[2], roi[3], roi[4], 'covid-19'])
    f.close()

def get_roi(lung_mask, idx, filename) :
    mask = cv2.imread(lung_mask)

    height, width, channel = mask.shape
    matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 1)
    mask = cv2.warpAffine(mask, matrix, (width, height))

    imgray = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    ret, thr = cv2.threshold(imgray, 70, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(thr, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    """original = cv2.imread(ct_scan)

    height, width, channel = original.shape
    matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 1)
    original = cv2.warpAffine(original, matrix, (width, height))

    kernel = np.ones((9,9), np.uint8)
    thr = cv2.morphologyEx(thr, cv2.MORPH_CLOSE, kernel)
    thr = cv2.morphologyEx(thr, cv2.MORPH_OPEN, kernel)

    result = original.copy()
    result = cv2.cvtColor(result, cv2.COLOR_BGR2BGRA)
    result[:, :, 3] = thr"""

    roi = []

    for i in range(len(contours)) :
        c0 = contours[i]
        x, y, w, h = cv2.boundingRect(c0)
        roi.append([filename, str(x), str(x+w), str(y), str(y+h)])

        """crop_left = result[y:y+h, x:x+w]
        cv2.imwrite(os.path.join(save_path, str(idx)+'_'+str(i)+'.png'), crop_left)"""

    return roi

filenames = read_filename(src_root_ct)
lung_masks = read_png(src_root_lung)
rois = []

for idx in range(len(lung_masks)) : 
    rois.extend(get_roi(lung_masks[idx], idx, filenames[idx]))

write_csv(rois)