import SimpleITK as sitk
import matplotlib.pyplot as plt
import numpy as np
import os, glob
import csv
import matplotlib.image as image

save_path = 'C:\\Users\\hyoj_\\OneDrive\\Desktop\\internship\\C677\\image'

def load_itk_image(filename):
    itkimage = sitk.ReadImage(filename)
    ct_scan = sitk.GetArrayFromImage(itkimage)
    origin = itkimage.GetOrigin()
    spacing = itkimage.GetSpacing()
    return ct_scan, origin, spacing

def read_csv(filename):
    lines = []
    with open(filename, 'r') as f:
        csvreader = csv.reader(f)
        for line in csvreader:
            lines.append(line)

    lines = lines[1:] # remove csv headers
    annotations_dict = {}
    for i in lines:
        series_uid, x, y, z, diameter = i
        value = [float(x),float(y),float(z),float(diameter)]
        if series_uid in annotations_dict.keys():
            annotations_dict[series_uid].append(value)
        else:
            annotations_dict[series_uid] = [value]

    return annotations_dict

def show_nodules(series_uid, num, ct_scan, nodules, Origin, Spacing, radius=20, pad=2): # radius is half of the square side length, pad is the width of the edge, max_show_num maximum number of impressions
    show_index = []
    for idx in range(nodules.shape[0]): # lable is an array of nx4 dimensions, n is the number of lung nodules, 4 is x, y, z, and diameter
        #if idx < max_show_num:
        if abs(nodules[idx, 0]) + abs(nodules[idx, 1]) + abs(nodules[idx, 2]) + abs(nodules[idx, 3]) == 0: continue

        x, y, z = int((nodules[idx, 0]-Origin[0])/SP[0]), int((nodules[idx, 1]-Origin[1])/SP[1]), int((nodules[idx, 2]-Origin[2])/SP[2])
        data = ct_scan[z]
        radius=int(nodules[idx, 3]/SP[0]/2)
        #pad = 2*radius
        # Note y stands for the vertical axis and x stands for the horizontal axis
        """data[max(0, y - radius):min(data.shape[0], y + radius),
            max(0, x - radius - pad):max(0, x - radius)] = 3000 #vertical line
        data[max(0, y - radius):min(data.shape[0], y + radius),
            min(data.shape[1], x + radius):min(data.shape[1], x + radius + pad)] = 1000 #vertical line
        data[max(0, y - radius - pad):max(0, y - radius),
            max(0, x - radius):min(data.shape[1], x + radius)] = 3000 #
        data[min(data.shape[0], y + radius):min(data.shape[0], y + radius + pad),
            max(0, x - radius):min(data.shape[1], x + radius)] = 3000 #"""

        subdata = data.copy()
        subdata = data[max(0, y - radius):min(data.shape[0], y + radius),
            max(0, x - radius):min(data.shape[1], x + radius)]

        if z in show_index: # check if there are nodules in the same slice, if there is, only one
            continue
        show_index.append(z)
        image.imsave(os.path.join(save_path,series_uid+'_'+str(num)+'_'+str(idx)+'.png'), subdata, cmap='gray')

if __name__=="__main__":
    src_root = 'C:\\Users\\hyoj_\\OneDrive\\Desktop\\internship\\C677\\'
    dst_root = 'D:\\image\\'

    annotation_csv = os.path.join(src_root,'annotations.csv')
    annotations = read_csv(annotation_csv)

    for sub_n in range(9) :
        idx = 1
        sub_n_str = 'subset' + str(sub_n)
        image_paths = glob.glob(os.path.join(dst_root,sub_n_str,'*.mhd'))

        for i in image_paths:
            filename = os.path.split(i)[-1]
            series_uid = os.path.splitext(filename)[0]

            subset_num = i.split('\\')[-2]

            numpyImage, OR, SP = load_itk_image(i)
            nodule_coords = []
            if series_uid in annotations.keys():
                nodule_coords = np.array(annotations[series_uid])
                show_nodules(series_uid, idx, numpyImage, nodule_coords,OR,SP)
            idx += 1