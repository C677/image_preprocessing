import glob
import pandas  as pd
import numpy   as np
import nibabel as nib
import os, glob
import matplotlib.pyplot as plt
import matplotlib.image as image

src_root = 'C:\\Users\\hyoj_\\OneDrive\\Desktop\\internship\\C677\\covid\\'
save_path_ct = 'C:\\Users\\hyoj_\\OneDrive\\Desktop\\internship\\C677\\covid\\ct_scans\\'
save_path_lung = 'C:\\Users\\hyoj_\\OneDrive\\Desktop\\internship\\C677\\covid\\lung_mask\\'

def read_nii(filepath):
    '''
    Reads .nii file and returns pixel array
    '''
    path = filepath.split('/')[-2] + "\\" + filepath.split('/')[-1]
    ct_scan = nib.load(src_root+path)
    array   = ct_scan.get_fdata()
    array   = np.rot90(np.array(array))
    return(array)

def plot_sample(array_list, idx, color_map = 'nipy_spectral'):
    '''
    Plots and a slice with all available annotations
    '''
    image.imsave(os.path.join(save_path_ct, 'ct_scan'+'_'+str(idx)+'.png'), array_list[0], cmap='gray')
    image.imsave(os.path.join(save_path_lung, 'lung_mask'+'_'+str(idx)+'.png'), array_list[1], cmap=color_map)

# Read and examine metadata
raw_data = pd.read_csv(src_root+"metadata.csv")

# Read sample
sample_ct   = read_nii(raw_data.loc[0,'ct_scan'])
sample_lung = read_nii(raw_data.loc[0,'lung_mask'])
sample_infe = read_nii(raw_data.loc[0,'infection_mask'])
sample_all  = read_nii(raw_data.loc[0,'lung_and_infection_mask'])

for idx in range(len(sample_ct)) :
    plot_sample([sample_ct[idx], sample_lung[idx], sample_infe[idx], sample_all[idx]], idx)